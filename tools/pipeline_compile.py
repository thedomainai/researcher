#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 4: raw/ → wiki/ コンパイル(Claude Code の headless モード経由・サブスクリプション課金)

raw/index.jsonl のうち Tier 1/2 で未コンパイルの論文をバッチにまとめ、次の順で処理する。

  Phase 0: 未分類論文の Tier 分類  … tools/tier_classify_cli.py に委譲(Haiku)
  Phase 1: バッチからコンセプト抽出 … 既定 Sonnet(バッチ 1 回の呼び出しで wiki の構造が決まるため)
  Phase 2: コンセプトごとの記事生成 … 既定 auto(Tier 1 ソースを含むコンセプトは Sonnet、Tier 2 のみなら Haiku)
  Phase 3: raw/index.jsonl / wiki/_meta/concepts.json への追記(wiki/index.md は統計行のみ更新)
  Phase 4: バリデーション・グラフ・HTML(reader / graph / index)の再ビルド … compile_wiki.py の Phase 4-8

LLM の呼び出しは共通ヘルパー lib/claude_cli.py の `claude -p`(Claude Code の非対話モード)。従量課金の
API キーは子プロセスから外し、ログイン済みのサブスクリプションで動かす。ツール定義・設定を読ませないため、
1 呼び出しあたりの固定オーバーヘッドは小さい(既定のままだと数万トークン)。

  - 既存記事は上書きしない(新規スラッグだけを追加する。衝突したら連番を付ける)
  - index.jsonl / concepts.json はバッチごとに書き戻すので、途中で止まっても成果が残る
  - 認証切れ(OAuth session expired)は終了コード 3、利用枠の上限は終了コード 4 で止まる
  - 何度バッチに入れてもどのコンセプトにも割り当てられない論文は MAX_COMPILE_ATTEMPTS 回で諦める

使い方:
    python3 tools/pipeline_compile.py --limit 90 [--domain neuroscience] [--dry-run]
    python3 tools/pipeline_compile.py --tier-only --limit 200      # Tier 分類だけ
    python3 tools/pipeline_compile.py --rebuild-only                # HTML の再ビルドだけ
    python3 tools/pipeline_compile.py --limit 30 --article-model haiku --extract-model sonnet
"""

import argparse
import fcntl
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(BASE, "tools")
RAW = os.path.join(BASE, "raw")
WIKI = os.path.join(BASE, "wiki")
WIKI_CONCEPTS = os.path.join(WIKI, "concepts")
WIKI_META = os.path.join(WIKI, "_meta")
INDEX_PATH = os.path.join(RAW, "index.jsonl")
META_PATH = os.path.join(WIKI_META, "concepts.json")
WIKI_INDEX_MD = os.path.join(WIKI, "index.md")
LOCK_PATH = os.path.join(BASE, "logs", "pipeline_compile.lock")

MAX_CONSECUTIVE_FAILURES = 3   # 連続で失敗したら止める(利用枠の上限・障害を想定)
MAX_COMPILE_ATTEMPTS = 3       # コンセプトに割り当てられなかった論文を再挑戦する回数
EXCERPT_CHARS = 1500           # 1 ソースあたりプロンプトに載せる本文の長さ
LINK_CANDIDATES = 20           # 記事生成時に提示する既存コンセプトの数
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]+?))?\]\]")
RAW_PATH_RE = re.compile(r"raw/[^\s\)`\]]+\.(?:md|pdf)")
TIER_LABEL = {1: "不変原理", 2: "設計原理", 3: "分析枠組み"}

sys.path.insert(0, TOOLS)
from lib.claude_cli import AuthError, call_claude as _cli_call  # noqa: E402

WORK_DIR = None  # claude -p の作業ディレクトリ(プロジェクトの CLAUDE.md / hooks を読ませない)


class UsageLimitError(RuntimeError):
    pass


# ============================================================
# claude -p 呼び出し
# ============================================================
USAGE = {"calls": 0, "cost_usd": 0.0, "models": {}}
USAGE_LOCK = threading.Lock()


def _record_usage(usage):
    with USAGE_LOCK:
        USAGE["calls"] += 1
        USAGE["cost_usd"] += usage["total_cost_usd"]
        slot = USAGE["models"].setdefault(usage["model"], {"calls": 0, "in": 0, "out": 0})
        slot["calls"] += 1
        slot["in"] += usage["input_tokens"] + usage["cache_creation_input_tokens"] + usage["cache_read_input_tokens"]
        slot["out"] += usage["output_tokens"]


def call_claude(system_prompt, prompt, model, timeout=900):
    """共通ヘルパー(lib/claude_cli.py)経由で claude -p を呼び、本文を返す。
    認証切れは AuthError、利用枠の上限は UsageLimitError。"""
    try:
        text, usage = _cli_call(prompt, system_prompt, model=model, timeout=timeout, cwd=WORK_DIR)
    except AuthError:
        raise
    except RuntimeError as e:
        low = str(e).lower()
        if "usage limit" in low or "rate limit" in low or "limit reached" in low:
            raise UsageLimitError(str(e))
        raise
    _record_usage(usage)
    return text


def strip_fences(text):
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1] if "\n" in cleaned else ""
        if cleaned.rstrip().endswith("```"):
            cleaned = cleaned.rstrip()[:-3]
    return cleaned.strip()


def parse_json_object(text):
    cleaned = strip_fences(text)
    start, end = cleaned.find("{"), cleaned.rfind("}")
    if start < 0 or end < 0:
        raise ValueError("JSON オブジェクトが見つからない: %s" % cleaned[:200])
    return json.loads(cleaned[start:end + 1])


# ============================================================
# raw / wiki の読み込み
# ============================================================
def load_index():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_index(index):
    tmp = INDEX_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for e in index:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    os.replace(tmp, INDEX_PATH)


def load_meta():
    if not os.path.exists(META_PATH):
        return []
    with open(META_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def write_meta(meta):
    tmp = META_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    os.replace(tmp, META_PATH)


def read_excerpt(entry):
    """raw ファイルから評価用の抜粋を読む。"""
    path = os.path.join(RAW, entry["file"])
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if entry.get("type") == "article":
        parts = content.split("---", 2)
        body = parts[2] if len(parts) >= 3 else content
        return body[:2000].strip()
    return content[:2000].strip()


def extract_h1(text, fallback):
    m = re.search(r"^# (.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else fallback


def load_concept_catalog(meta):
    """既存コンセプトの一覧(slug → タイトル等)。concepts.json に無い記事は H1 から補う。"""
    catalog = {}
    for c in meta:
        catalog[c["slug"]] = {
            "title_ja": c.get("title_ja") or c["slug"],
            "title_en": c.get("title_en", ""),
            "description": c.get("description", ""),
            "mechanisms": list(c.get("mechanisms") or []),
        }
    for fn in sorted(os.listdir(WIKI_CONCEPTS)):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        if slug in catalog:
            continue
        with open(os.path.join(WIKI_CONCEPTS, fn), "r", encoding="utf-8") as f:
            head = f.read(4000)
        catalog[slug] = {"title_ja": extract_h1(head, slug), "title_en": "", "description": "", "mechanisms": []}
    return catalog


def existing_raw_paths():
    paths = set()
    for dirpath, _, filenames in os.walk(RAW):
        for fn in filenames:
            if fn.endswith(".md"):
                paths.add(os.path.relpath(os.path.join(dirpath, fn), BASE))
    return paths


# ============================================================
# 対象の選択とバッチ化
# ============================================================
def is_pending(entry):
    return (
        not entry.get("wiki_compiled")
        and entry.get("tier") in (1, 2)
        and int(entry.get("wiki_compile_attempts", 0) or 0) < MAX_COMPILE_ATTEMPTS
    )


def make_batches(pending, batch_size):
    """分野ごとにまとめてからバッチに切る(同じ分野の論文が同じバッチに入るとコンセプトがまとまりやすい)。"""
    ordered = sorted(pending, key=lambda e: (e.get("domain") or "zz", e.get("year") or 0))
    return [ordered[i:i + batch_size] for i in range(0, len(ordered), batch_size)]


# ============================================================
# Phase 1: コンセプト抽出
# ============================================================
EXTRACT_SYSTEM = (
    "あなたはAI Nativeな社会・組織・システム設計のナレッジエンジニアです。"
    "与えられたソース群から、対象(人間/AI/組織/技術)を入れ替えても成立する構造的原理・メカニズムを"
    "中心とした主要コンセプトを抽出し、構造化してください。回答はJSONオブジェクトのみで、他のテキストは含めないでください。"
)

EXTRACT_PROMPT = """以下は「AI Nativeな社会・組織・システム設計」のために収集した論文・記事です。
Tier 1 = 不変原理(AGI時代でも成立する構造的原理)、Tier 2 = 消滅制約の構造的分析。

{sources}

---

これらの内容から、wikiに整理すべき主要コンセプトを {k} 個前後(最大 {kmax} 個)抽出してください。

要件:
- 各コンセプトは、対象(人間/AI/組織/技術)を入れ替えても成立する構造的原理・メカニズムを中心に据える
- すべてのソースを少なくとも1つのコンセプトの related_sources に割り当てる。どれにも当てはまらないソースだけ unassigned に番号を列挙する
- slug は英小文字・数字・ハイフンのみ(例: principal-agent-problem)。末尾の既存スラッグ一覧と重複させない。既存コンセプトと同じ主題なら、より具体的な切り口で新しいコンセプトにする
- mechanisms は中核的メカニズム名(日本語、2〜4個)。具体的なツール名・手法名ではなく背後の抽象的メカニズムを書く
  例: "情報の非対称性", "有限合理性", "プリンシパル＝エージェント問題", "予測誤差による学習", "フィードバックループ", "経路依存性"

JSON形式で回答(JSON以外は出力しないでください):
{{
  "concepts": [
    {{
      "slug": "concept-slug-in-english",
      "title_ja": "日本語タイトル",
      "title_en": "English Title",
      "description": "1行の説明(日本語)",
      "mechanisms": ["中核的メカニズム名"],
      "related_sources": [1, 2]
    }}
  ],
  "unassigned": []
}}

既存スラッグ一覧(重複させない):
{existing_slugs}
"""


def format_source_block(n, src, chars=EXCERPT_CHARS):
    e = src["entry"]
    head = "### [%d] %s" % (n, e["title"])
    meta = "  種別: %s | 著者: %s | 年: %s | 分野: %s | Tier %s" % (
        e.get("type", "paper"), src["author"] or "不明", e.get("year") or "不明",
        e.get("domain") or "-", e.get("tier") or "-")
    lines = [head, meta, "  File: %s" % src["file"]]
    if e.get("key_insight"):
        lines.append("  核心的知見: %s" % e["key_insight"])
    lines.append("  抜粋: %s" % src["excerpt"][:chars].replace("\n", " "))
    return "\n".join(lines)


def extract_concepts(sources, existing_slugs, model, k):
    blocks = "\n\n".join(format_source_block(i + 1, s, chars=1000) for i, s in enumerate(sources))
    prompt = EXTRACT_PROMPT.format(
        sources=blocks, k=k, kmax=k + 2,
        existing_slugs=", ".join(sorted(existing_slugs)),
    )
    text = call_claude(EXTRACT_SYSTEM, prompt, model)
    data = parse_json_object(text)
    raw_concepts = data.get("concepts") or []
    if not isinstance(raw_concepts, list) or not raw_concepts:
        raise ValueError("concepts が空")
    concepts = []
    seen = set()
    n = len(sources)
    for c in raw_concepts:
        if not isinstance(c, dict):
            continue
        slug = str(c.get("slug", "")).strip().lower()
        slug = re.sub(r"[^a-z0-9-]+", "-", slug).strip("-")
        if not slug or not SLUG_RE.match(slug):
            continue
        related = []
        for v in c.get("related_sources") or []:
            try:
                iv = int(v)
            except (TypeError, ValueError):
                continue
            if 1 <= iv <= n and iv not in related:
                related.append(iv)
        if not related:
            continue
        base = slug
        suffix = 2
        while slug in existing_slugs or slug in seen:
            slug = "%s-%d" % (base, suffix)
            suffix += 1
        if slug != base:
            print("    ℹ️  スラッグ衝突: %s → %s" % (base, slug), flush=True)
        seen.add(slug)
        concepts.append({
            "slug": slug,
            "title_ja": str(c.get("title_ja") or slug).strip(),
            "title_en": str(c.get("title_en") or "").strip(),
            "description": str(c.get("description") or "").strip(),
            "mechanisms": [str(m).strip() for m in (c.get("mechanisms") or []) if str(m).strip()][:4],
            "related_sources": related,
        })
    if not concepts:
        raise ValueError("有効なコンセプトが 1 つも得られなかった")
    return concepts


# ============================================================
# Phase 2: 記事生成
# ============================================================
ARTICLE_SYSTEM = (
    "あなたはAI Nativeな社会設計のテクニカルライターです。与えられたソースから、正確で読みやすいwiki記事を日本語で作成してください。"
    "★重要: [[リンク]]は提示されたスラッグ一覧に存在するものだけを使ってください。存在しないスラッグへのリンクは作成しないでください。"
    "ソースのファイルパスは提示された値をそのまま使ってください。ソースにない事実を作らないでください。"
    "回答はMarkdown記事本文のみで、前置きや説明は含めないでください。"
)

ARTICLE_PROMPT = """以下のソースに基づいて、「{title_ja} ({title_en})」についてのwiki記事を作成してください。

コンセプト情報:
- Tier: {tier}({tier_label})
- 説明: {description}
- 中核メカニズム: {mechanisms}

ソース:
{sources}

---

以下の構成でMarkdown記事を書いてください(フロントマターは不要):
1. 「# {title_ja}」で始める
2. ## 概要 … この概念が何か、なぜAI Nativeな設計に重要か
3. ## メカニズム … 対象(人間/AI/組織/技術)を入れ替えても成立する構造的原理として整理する
4. ## 理論的背景 … ソースから得られた主要な理論・モデル・実証知見
5. ## AI Nativeな設計への示唆 … 具体的な設計原理や指針
6. ## 関連コンセプト … [[slug]] 形式のリンク(下の「リンク可能なスラッグ」にあるものだけ)
7. ## 参考ソース … ソースごとにタイトル・著者・年と、上記「File:」のパスをそのまま記載する

★★★ 絶対に守るべきルール ★★★
- [[リンク]]は「リンク可能なスラッグ」にあるものだけを使う。それ以外の概念はプレーンテキストで書く
- 参考ソースのファイルパスは上記「File:」の値をそのままコピーする。推測したり形式を変えたりしない
- ソースに書かれていない事実・数値・引用を作らない
- 日本語で、技術的に正確だが読みやすく。2000〜3000字程度

リンク可能なスラッグ(slug — 日本語タイトル):
{link_candidates}
"""

STOPWORDS = {"the", "and", "for", "with", "from", "into", "under", "over", "between", "through",
             "toward", "towards", "based", "using", "via", "of", "in", "on", "to", "a", "an", "as",
             "ai", "native", "system", "systems", "design", "model", "models", "theory", "approach"}


def _tokens(*texts):
    out = set()
    for t in texts:
        for w in re.split(r"[^a-z0-9]+", (t or "").lower()):
            if len(w) > 2 and w not in STOPWORDS:
                out.add(w)
    return out


def pick_link_candidates(concept, batch_concepts, catalog, limit=LINK_CANDIDATES):
    """新コンセプトに近い既存コンセプトを簡単な語彙の重なりで選ぶ(全 900 件超を毎回渡すとトークンが嵩む)。"""
    mine = _tokens(concept["slug"], concept["title_en"])
    my_mech = set(concept.get("mechanisms") or [])
    scored = []
    for slug, info in catalog.items():
        theirs = _tokens(slug, info.get("title_en", ""))
        score = len(mine & theirs) * 2 + len(my_mech & set(info.get("mechanisms") or []))
        if score > 0:
            scored.append((score, slug))
    scored.sort(key=lambda x: (-x[0], x[1]))
    picked = [(s, catalog[s]["title_ja"]) for _, s in scored[:limit]]
    for other in batch_concepts:
        if other["slug"] != concept["slug"]:
            picked.append((other["slug"], other["title_ja"]))
    return picked


def choose_article_model(concept, sources, mode):
    if mode != "auto":
        return mode
    tiers = [sources[i - 1]["entry"].get("tier") for i in concept["related_sources"]]
    return "sonnet" if 1 in tiers else "haiku"


def sanitize_article(text, title_ja, valid_slugs, title_to_slug, raw_paths):
    article = strip_fences(text)
    # 前置きが付いていたら最初の見出しから始める
    m = re.search(r"^# .+$", article, re.MULTILINE)
    if m:
        article = article[m.start():]
    else:
        article = "# %s\n\n%s" % (title_ja, article)

    stats = {"links_fixed": 0, "links_dropped": 0, "paths_unverified": 0}

    def fix_link(match):
        target = match.group(1).strip()
        label = (match.group(2) or target).strip()
        if target in valid_slugs:
            return match.group(0)
        resolved = title_to_slug.get(target)
        if resolved:
            stats["links_fixed"] += 1
            return "[[%s|%s]]" % (resolved, label) if label != resolved else "[[%s]]" % resolved
        stats["links_dropped"] += 1
        return label

    article = LINK_RE.sub(fix_link, article)

    def check_path(match):
        p = match.group(0)
        if p in raw_paths:
            return p
        stats["paths_unverified"] += 1
        return "（パス未確認）"

    article = RAW_PATH_RE.sub(check_path, article)
    return article.rstrip() + "\n", stats


def generate_article(concept, sources, batch_concepts, catalog, valid_slugs, title_to_slug,
                     raw_paths, model):
    related = [sources[i - 1] for i in concept["related_sources"]]
    tiers = [s["entry"].get("tier") for s in related if s["entry"].get("tier") in (1, 2)]
    tier = min(tiers) if tiers else 2
    blocks = "\n\n".join(format_source_block(i + 1, s) for i, s in enumerate(related))
    candidates = pick_link_candidates(concept, batch_concepts, catalog)
    prompt = ARTICLE_PROMPT.format(
        title_ja=concept["title_ja"], title_en=concept["title_en"] or concept["slug"],
        tier=tier, tier_label=TIER_LABEL.get(tier, ""),
        description=concept["description"] or "-",
        mechanisms="、".join(concept["mechanisms"]) or "-",
        sources=blocks,
        link_candidates="\n".join("- %s — %s" % (s, t) for s, t in candidates) or "(なし)",
    )
    text = call_claude(ARTICLE_SYSTEM, prompt, model)
    article, stats = sanitize_article(text, concept["title_ja"], valid_slugs, title_to_slug, raw_paths)
    if len(article) < 400:
        raise RuntimeError("記事が短すぎる(%d 文字): %s" % (len(article), article[:120]))
    return article, tier, stats


# ============================================================
# Phase 3: メタデータ・索引の追記
# ============================================================
def update_wiki_index_stats(meta):
    """wiki/index.md の「## 統計」の件数と日付だけを更新する。

    index.md のコンセプト一覧は手動でキュレーションされたものなので、新コンセプトを機械的に
    追記はしない(全コンセプトは index.html / reader.html 側に載る)。
    """
    if not os.path.exists(WIKI_INDEX_MD):
        return False
    with open(WIKI_INDEX_MD, "r", encoding="utf-8") as f:
        text = f.read()
    articles = len([fn for fn in os.listdir(WIKI_CONCEPTS) if fn.endswith(".md")])
    new = re.sub(r"(?m)^- wiki記事: \d+$", "- wiki記事: %d" % articles, text)
    new = re.sub(r"(?m)^(- コンセプト数: .*?/ 全)\d+(概念)$", r"\g<1>%d\2" % len(meta), new)
    new = re.sub(r"(?m)^- 最終コンパイル: .*$", "- 最終コンパイル: %s" % datetime.now().strftime("%Y-%m-%d"), new)
    if new != text:
        with open(WIKI_INDEX_MD, "w", encoding="utf-8") as f:
            f.write(new)
        return True
    return False


# ============================================================
# Phase 4: サイトの再ビルド(compile_wiki.py の Phase 4-8)
# ============================================================
def rebuild_site():
    """グラフと HTML を再生成する(compile_wiki.py の Phase 5-8。API キーは不要)。

    compile_wiki.py の Phase 4(バリデーション)は既存記事の [[日本語タイトル]] リンクを
    プレーンテキストに書き換えて 700 件近い記事を変更してしまうため、ここでは実行しない。
    新規記事のリンク・パス検証は sanitize_article() で書き込み前に済ませている。
    """
    import compile_wiki  # noqa: WPS433  (tools/ 配下)

    compile_wiki.phase5_build_graph()
    compile_wiki.phase6_build_reader()
    compile_wiki.phase7_build_graph_ui()
    compile_wiki.phase8_build_index_ui()


# ============================================================
# メイン
# ============================================================
def run_tier_classification(limit, domain):
    cmd = [sys.executable, os.path.join(TOOLS, "tier_classify_cli.py"), "--limit", str(limit)]
    if domain:
        cmd += ["--domain", domain]
    print("\n" + "-" * 40)
    print("Phase 0: Tier分類 (tier_classify_cli.py)")
    print("-" * 40, flush=True)
    r = subprocess.run(cmd, cwd=BASE)
    return r.returncode


def print_usage_summary():
    if not USAGE["calls"]:
        return
    print("\n  LLM 呼び出し: %d 回(API 換算の参考額: $%.2f。サブスクリプション認証なら課金なし)"
          % (USAGE["calls"], USAGE["cost_usd"]))
    for model, mu in sorted(USAGE["models"].items()):
        print("    %-32s %3d 回  in=%7d  out=%7d" % (model, mu["calls"], mu["in"], mu["out"]))


def main():
    global WORK_DIR
    ap = argparse.ArgumentParser(description="raw/ → wiki/ コンパイル(claude -p 経由)")
    ap.add_argument("--domain", default=None, help="特定の分野のみ処理(例: neuroscience)")
    ap.add_argument("--limit", type=int, default=30, help="1回の実行で処理する論文数の上限(既定: 30)")
    ap.add_argument("--batch", type=int, default=30, help="コンセプト抽出 1 回あたりの論文数(既定: 30)")
    ap.add_argument("--concepts-per-batch", type=int, default=5, help="1 バッチから抽出するコンセプト数の目安(既定: 5)")
    ap.add_argument("--extract-model", default="sonnet", help="コンセプト抽出のモデル(既定: sonnet)")
    ap.add_argument("--article-model", default="auto",
                    help="記事生成のモデル。auto=Tier 1 を含めば sonnet、それ以外は haiku(既定: auto)")
    ap.add_argument("--workers", type=int, default=3, help="記事生成の並列数(既定: 3)")
    ap.add_argument("--tier-only", action="store_true", help="Tier分類のみ実行しコンパイルはスキップ")
    ap.add_argument("--no-tier", action="store_true", help="Tier分類(Phase 0)をスキップ")
    ap.add_argument("--no-rebuild", action="store_true", help="HTML の再ビルド(Phase 4)をスキップ")
    ap.add_argument("--rebuild-only", action="store_true", help="HTML の再ビルドだけ実行")
    ap.add_argument("--dry-run", action="store_true", help="対象を数えるだけ(LLM は呼ばない)")
    args = ap.parse_args()

    print("=" * 60)
    print("Step 4: raw → wiki コンパイル (claude -p)")
    print("=" * 60, flush=True)

    if args.rebuild_only:
        rebuild_site()
        return 0

    # 同時に 2 本走ると index.jsonl / concepts.json の書き戻しが競合する
    os.makedirs(os.path.dirname(LOCK_PATH), exist_ok=True)
    lock = open(LOCK_PATH, "a+")
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("別の pipeline_compile.py が実行中のためスキップします。")
        return 0

    # ---------- Phase 0 ----------
    if not args.no_tier and not args.dry_run:
        rc = run_tier_classification(args.limit if not args.tier_only else max(args.limit, 200), args.domain)
        if rc == 3:
            print("認証エラーのため中断します(`claude login` を実行してください)。")
            return 3
        if rc not in (0, 1):
            print("Tier分類が終了コード %d で失敗しました。コンパイルは続行します。" % rc)
    if args.tier_only:
        index = load_index()
        print("\n  --tier-only: Tier分類のみ完了(%d/%d 件分類済み)"
              % (sum(1 for e in index if "tier" in e), len(index)))
        return 0

    # ---------- 対象の選択 ----------
    index = load_index()
    pending = [e for e in index if is_pending(e)]
    if args.domain:
        pending = [e for e in pending if e.get("domain") == args.domain]
    tier3 = sum(1 for e in index if e.get("tier") == 3 and not e.get("wiki_compiled"))
    untiered = sum(1 for e in index if "tier" not in e)
    gave_up = sum(1 for e in index if not e.get("wiki_compiled") and e.get("tier") in (1, 2)
                  and int(e.get("wiki_compile_attempts", 0) or 0) >= MAX_COMPILE_ATTEMPTS)
    print("\n  インデックス: %d 件 / コンパイル対象(Tier 1-2 未処理): %d 件%s"
          % (len(index), len(pending), " (domain=%s)" % args.domain if args.domain else ""))
    print("  ℹ️  Tier 3 スキップ: %d 件 / Tier 未分類: %d 件 / 割り当て不能で保留: %d 件" % (tier3, untiered, gave_up))
    if not pending:
        print("  ✅ 全件コンパイル済み。終了します。")
        if not args.no_rebuild and not args.dry_run:
            rebuild_site()
        return 0
    if len(pending) > args.limit:
        print("  ℹ️  上限 %d 件に絞って処理します(残り %d 件は次回以降)" % (args.limit, len(pending) - args.limit))
    batches = make_batches(pending, args.batch)
    # 上限は「論文数」なので、バッチ列の先頭から limit 件ぶんだけ取る
    kept, count = [], 0
    for b in batches:
        if count >= args.limit:
            break
        b = b[: args.limit - count]
        kept.append(b)
        count += len(b)
    batches = kept
    print("  バッチ数: %d(1 バッチ %d 件、抽出 %s / 記事 %s、並列 %d)"
          % (len(batches), args.batch, args.extract_model, args.article_model, args.workers), flush=True)
    if args.dry_run:
        for i, b in enumerate(batches):
            doms = sorted({e.get("domain") or "-" for e in b})
            print("    batch %d: %d 件 [%s]" % (i + 1, len(b), ", ".join(doms)))
        return 0

    meta = load_meta()
    catalog = load_concept_catalog(meta)
    raw_paths = existing_raw_paths()
    WORK_DIR = tempfile.mkdtemp(prefix="pipeline_compile_")

    written_total = 0
    compiled_total = 0
    failures = 0
    consecutive_failures = 0
    exit_code = 0
    try:
        for bi, batch in enumerate(batches):
            print("\n" + "-" * 40)
            print("Batch %d/%d: %d 件" % (bi + 1, len(batches), len(batch)))
            print("-" * 40, flush=True)

            sources = []
            for e in batch:
                ex = read_excerpt(e)
                if not ex:
                    print("  SKIP (ファイルなし): %s" % e["title"][:60])
                    continue
                sources.append({
                    "entry": e,
                    "author": e.get("author") or e.get("authors") or "",
                    "file": "raw/" + e["file"],
                    "excerpt": ex,
                })
            if not sources:
                continue

            # ---------- Phase 1 ----------
            print("  Phase 1: コンセプト抽出中 (%s)..." % args.extract_model, flush=True)
            try:
                concepts = extract_concepts(sources, set(catalog), args.extract_model, args.concepts_per_batch)
            except (AuthError, UsageLimitError):
                raise
            except Exception as e:  # noqa: BLE001
                failures += 1
                consecutive_failures += 1
                print("  ❌ コンセプト抽出に失敗: %s" % str(e)[:200], flush=True)
                if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                    print("連続 %d 回失敗したため中断します。" % consecutive_failures)
                    break
                continue
            for c in concepts:
                print("     - %s (%s) ← %s" % (c["title_ja"], c["slug"], c["related_sources"]))

            # ---------- Phase 2 ----------
            valid_slugs = set(catalog) | {c["slug"] for c in concepts}
            title_to_slug = {info["title_ja"]: s for s, info in catalog.items() if info.get("title_ja")}
            title_to_slug.update({info["title_en"]: s for s, info in catalog.items() if info.get("title_en")})
            title_to_slug.update({c["title_ja"]: c["slug"] for c in concepts})
            title_to_slug.update({c["title_en"]: c["slug"] for c in concepts if c["title_en"]})

            def work(concept):
                model = choose_article_model(concept, sources, args.article_model)
                try:
                    article, tier, stats = generate_article(
                        concept, sources, concepts, catalog, valid_slugs, title_to_slug, raw_paths, model)
                    return concept, model, article, tier, stats, None
                except Exception as e:  # noqa: BLE001
                    return concept, model, None, None, None, e

            print("  Phase 2: 記事生成中 (%d 件)..." % len(concepts), flush=True)
            with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
                results = list(pool.map(work, concepts))

            fatal = next((r[5] for r in results if isinstance(r[5], (AuthError, UsageLimitError))), None)
            if fatal:
                raise fatal

            batch_meta = []
            batch_ok = 0
            covered = set()
            for concept, model, article, tier, stats, err in results:
                if err:
                    failures += 1
                    print("  ❌ [%s] %s" % (concept["slug"], str(err)[:200]), flush=True)
                    continue
                path = os.path.join(WIKI_CONCEPTS, concept["slug"] + ".md")
                if os.path.exists(path):  # 念のため(catalog に無い記事があっても上書きしない)
                    print("  ⚠ 既存記事があるため書き込みをスキップ: %s" % concept["slug"])
                    continue
                with open(path, "w", encoding="utf-8") as f:
                    f.write(article)
                batch_ok += 1
                written_total += 1
                related_entries = [sources[i - 1]["entry"] for i in concept["related_sources"]]
                covered.update(concept["related_sources"])
                for e in related_entries:
                    e["wiki_compiled"] = True
                    e["wiki_slug"] = concept["slug"]
                    e.pop("wiki_compile_attempts", None)
                entry_meta = {
                    "slug": concept["slug"],
                    "title_ja": concept["title_ja"],
                    "title_en": concept["title_en"],
                    "tier": tier,
                    "description": concept["description"],
                    "mechanisms": concept["mechanisms"],
                    "related_domains": sorted({e.get("domain") for e in related_entries if e.get("domain")}),
                    "source_files": [sources[i - 1]["file"] for i in concept["related_sources"]],
                    "compiled_at": datetime.now().strftime("%Y-%m-%d"),
                    "model": model,
                }
                batch_meta.append(entry_meta)
                catalog[concept["slug"]] = {
                    "title_ja": concept["title_ja"], "title_en": concept["title_en"],
                    "description": concept["description"], "mechanisms": concept["mechanisms"],
                }
                note = ""
                if stats["links_dropped"] or stats["links_fixed"] or stats["paths_unverified"]:
                    note = " [link fix=%d drop=%d, path未確認=%d]" % (
                        stats["links_fixed"], stats["links_dropped"], stats["paths_unverified"])
                print("  ✅ concepts/%s.md (%s, Tier %d, %d 文字, %d ソース)%s"
                      % (concept["slug"], model, tier, len(article), len(related_entries), note), flush=True)

            # どのコンセプトにも入らなかった(または記事生成に失敗した)ソースは再挑戦回数を増やす
            for i, s in enumerate(sources, start=1):
                if i not in covered and not s["entry"].get("wiki_compiled"):
                    s["entry"]["wiki_compile_attempts"] = int(s["entry"].get("wiki_compile_attempts", 0) or 0) + 1
            compiled_total += len(covered)

            # ---------- Phase 3(バッチごとに書き戻す) ----------
            if batch_meta:
                meta.extend(batch_meta)
                write_meta(meta)
                update_wiki_index_stats(meta)
            write_index(index)
            if batch_ok == 0:
                failures += 1
                consecutive_failures += 1
                if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                    print("連続 %d バッチで記事を 1 本も書けなかったため中断します。" % consecutive_failures)
                    break
            else:
                consecutive_failures = 0
            print("  💾 index.jsonl / concepts.json 書き戻し(記事 %d 本、ソース %d 件)" % (batch_ok, len(covered)), flush=True)

    except AuthError as e:
        print("\n認証エラー: %s\n`claude login` を実行してから再実行してください。" % str(e)[:200])
        write_index(index)
        exit_code = 3
    except UsageLimitError as e:
        print("\n利用枠の上限に達しました: %s\n枠が回復してから再実行してください。" % str(e)[:200])
        write_index(index)
        exit_code = 4
    finally:
        if WORK_DIR:
            shutil.rmtree(WORK_DIR, ignore_errors=True)

    # ---------- 集計 ----------
    print("\n" + "-" * 40)
    print("Phase 3: メタデータ更新")
    print("-" * 40)
    compiled_count = sum(1 for e in index if e.get("wiki_compiled"))
    remaining = sum(1 for e in index if is_pending(e))
    print("  記事 %d 本を追加(wiki/concepts: %d 件、concepts.json: %d 件)"
          % (written_total, len([f for f in os.listdir(WIKI_CONCEPTS) if f.endswith(".md")]), len(meta)))
    print("  raw/index.jsonl: コンパイル済み %d/%d 件、残り %d 件" % (compiled_count, len(index), remaining))
    if failures:
        print("  ⚠ 失敗: %d 件" % failures)
    print_usage_summary()

    # ---------- Phase 4 ----------
    if written_total and not args.no_rebuild:
        print("\n" + "-" * 40)
        print("Phase 4: サイト再ビルド")
        print("-" * 40, flush=True)
        rebuild_site()

    print("\n" + "=" * 60)
    print("パイプライン完了" + ("(エラーあり)" if exit_code or failures else "!"))
    print("=" * 60)
    if exit_code:
        return exit_code
    return 1 if (failures and not written_total) else 0


if __name__ == "__main__":
    sys.exit(main())
