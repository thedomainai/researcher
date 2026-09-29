#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""未コンパイルの Tier 1/2 論文から wiki 記事を増分生成する(claude -p 経由・サブスクリプション課金)。

pipeline_compile.py(Gemini 版)の Phase 1〜3 を、tier_classify_cli.py と同じ型で
`claude -p` に載せ替えたもの。既存記事は上書きしない(増分専用)。

処理(1 ラウンド = 同一分野の論文 BATCH 件):
  Phase 1  概念抽出   : 論文の抜粋と既存 slug 一覧を渡し、最大 5 概念を JSON で受け取る(既定 sonnet)
  Phase 2  記事生成   : 新規概念ごとに日本語の記事を書く(既定 sonnet)。既存 slug に該当した論文は
                        既存記事の末尾に「追加ソース」節を追記するだけで LLM は呼ばない
  Phase 3  書き戻し   : raw/index.jsonl(wiki_compiled / wiki_slug)と wiki/_meta/concepts.json に追記
  仕上げ   再ビルド   : 新規記事があれば知識グラフと HTML 3 本(reader / graph / index)を再生成

取り決め:
  - 従量課金の API キーは子プロセスから外す(lib/claude_cli.py)
  - 認証切れは何も書き換えず終了コード 3。`claude auth login` で復旧する
  - 概念に採用されなかった論文は wiki_compile_attempts を +1 し、MAX_ATTEMPTS 回で対象から外す
    (旧実装は先頭に居座って以降の論文が処理されなかった)
  - 新規記事の [[リンク]] は既存 slug に解決できるものだけ残し、raw/ のパスは実在確認する。
    既存記事には触れない(compile_wiki.py の Phase 4 は全記事のリンクを潰すので使わない)

モデルの既定(2026-09-29 の同一 20 件での比較):
  - 概念抽出は sonnet。haiku は既存 slug 一覧を無視して論文 1 本ごとに新 slug を作り(採用 5/20)、
    sonnet は 13/20 を既存 5 概念へ合流させた。966 記事の wiki では重複回避が抽出の主目的なので
    1 ラウンド 1 回の呼び出し(API 換算 $0.27 vs $0.09)に見合う
  - 記事生成も sonnet。haiku の記事は構成は保つが誤字・不自然な語が混じり、出力トークンは
    sonnet の 2〜3 倍(思考分を含む)。1 記事の API 換算は sonnet $0.15 / haiku $0.05

使い方:
    python3 tools/compile_articles_cli.py --limit 60 [--domain neuroscience] [--dry-run]
    python3 tools/compile_articles_cli.py --pilot-dir /tmp/pilot --limit 20 --model-write haiku
        (--pilot-dir: 記事をそのディレクトリに書き、index / concepts.json / HTML には触れない)
"""

import argparse
import datetime
import fcntl
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # tools/
from lib.claude_cli import AuthError, UsageTally, call_claude, strip_code_fence  # noqa: E402
from lib.knowledge_graph import load_concept_graph_inputs, resolve_target  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "raw")
WIKI = os.path.join(BASE, "wiki")
WIKI_CONCEPTS = os.path.join(WIKI, "concepts")
WIKI_META = os.path.join(WIKI, "_meta")
INDEX_PATH = os.path.join(RAW, "index.jsonl")
META_PATH = os.path.join(WIKI_META, "concepts.json")
LOCK_PATH = os.path.join(BASE, "logs", "compile_articles.lock")

BATCH = 20                 # 1 ラウンドで概念抽出にかける論文数
CONCEPTS_PER_BATCH = 5
MAX_ATTEMPTS = 3           # 採用されなかった論文を諦めるまでのラウンド数
MAX_CONSECUTIVE_FAILURES = 3
EXCERPT_CHARS = 1200
MIN_ARTICLE_CHARS = 600
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{2,79}$")

DOMAIN_LABELS = {
    "ai_governance": "AIガバナンス", "behavioral_economics": "行動経済学", "cognitive_science": "認知科学",
    "complexity_science": "複雑系科学", "evolutionary_biology": "進化生物学", "human_ai_collaboration": "人間-AI協調",
    "neuroscience": "脳科学", "operations_research": "オペレーションズ・リサーチ", "organization_science": "組織科学",
    "law": "法学", "philosophy": "哲学", "religious_studies": "宗教学", "economics": "経済学",
    "political_science": "政治学", "sociology": "社会学", "education": "教育学", "history": "歴史学",
}

EXTRACT_SYSTEM = (
    "あなたはAI Nativeな社会・組織・システム設計の研究知識ベースを編集するナレッジエンジニアです。"
    "与えられた論文群から、wiki の 1 記事 = 1 コンセプトとして整理すべき概念を抽出します。"
    "回答は JSON 配列のみで、他のテキストは含めないでください。"
)

EXTRACT_PROMPT = """以下は「{domain_label}」分野で新たに取得した論文です(番号付き)。

{sources}

---

既存 wiki の slug 一覧(この中に該当する概念があれば新規に作らず、その slug を使う):
{existing_slugs}

---

これらの論文から、wiki に整理すべき主要コンセプトを最大 {max_concepts} 個抽出してください。

抽出の規則:
- 1 コンセプトは、対象(人間/AI/組織/技術)を入れ替えても成立する構造的原理・メカニズムを中心に立てる
- 各論文は最大 1 つのコンセプトにだけ割り当てる。どのコンセプトも支えない論文は割り当てない
- 内容が上の既存 slug 一覧の概念と同じなら、その slug をそのまま使い "existing": true とする
  (新しい概念なら英語ケバブケースの新しい slug を作り "existing": false)
- mechanisms は具体的なツール名・手法名ではなく、背後にある抽象的メカニズムの名前(日本語、2〜4 個)
  例: "情報の非対称性", "有限合理性", "予測誤差による学習", "フィードバックループ", "経路依存性"

JSON 配列だけを返してください:
[
  {{
    "slug": "concept-slug-in-english",
    "existing": false,
    "title_ja": "日本語タイトル",
    "title_en": "English Title",
    "description": "1 行の説明(日本語)",
    "mechanisms": ["メカニズム名"],
    "related_sources": [1, 2]
  }}
]"""

WRITE_SYSTEM = """あなたはAI Nativeな社会・組織・システム設計を扱う研究 wiki のテクニカルライターです。
与えられたソースだけを根拠に、正確で読みやすい日本語の wiki 記事を書きます。

絶対に守る規則:
- 他の概念へのリンクは [[slug]] 形式で、下の「既存 slug 一覧」にあるものだけを使う。
  一覧に無い概念はリンクにせず、プレーンテキストで書く
- 参考ソースのファイルパスは、ソースに書かれた File: の値をそのままコピーする。推測・変換しない
- ソースに無い主張・数値・著者名を作らない。ソースが述べていないことは書かない
- Markdown 本文のみを出力する。フロントマターや前置き・後書きは付けない

既存 slug 一覧:
{existing_slugs}"""

WRITE_PROMPT = """以下のソースに基づいて、「{title_ja} ({title_en})」についての wiki 記事を書いてください。

コンセプト情報:
- 説明: {description}
- 中核メカニズム: {mechanisms}
- 分野: {domain_label}

ソース:
{sources}

---

構成(見出しは次のとおり):
# {title_ja}
(冒頭に 2〜4 文で、この概念が何か・なぜ AI Native な設計に重要かを述べる)
## 概要
## 理論的背景と知見
(ソースから得られた主要な理論・モデル・実証知見を整理する。誰の研究かを明示する)
## AI Native な設計への示唆
(具体的な設計原理・指針として 3〜5 点)
## 関連概念
(既存 slug 一覧にある概念だけ [[slug]] で列挙。無ければ「(該当なし)」)
## 参考ソース
(各ソースについて次の 2 行:
* **タイトル**: <タイトル> (<年>)
  **ファイルパス**: `<File: の値>`)

日本語で、技術的に正確だが読みやすく、1500〜2500 字程度で書いてください。"""


# ============================================================
# 入出力
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


def existing_slugs():
    return sorted(fn[:-3] for fn in os.listdir(WIKI_CONCEPTS) if fn.endswith(".md"))


def read_excerpt(entry, limit=EXCERPT_CHARS):
    """フロントマターと見出しを除いた本文(論文なら Abstract 以降)の冒頭を返す。"""
    path = os.path.join(RAW, entry["file"])
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    parts = content.split("---", 2)
    body = parts[2] if content.startswith("---") and len(parts) >= 3 else content
    m = re.search(r"^## Abstract\s*\n", body, re.M)
    if m:
        body = body[m.end():]
    else:
        body = re.sub(r"^# .*\n(\*\*.*\n)*", "", body, count=1)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return body[:limit] if body else None


def pending_entries(index, domain=None):
    out = []
    for e in index:
        if e.get("wiki_compiled") or e.get("tier") not in (1, 2):
            continue
        if int(e.get("wiki_compile_attempts", 0) or 0) >= MAX_ATTEMPTS:
            continue
        if domain and e.get("domain") != domain:
            continue
        if not os.path.exists(os.path.join(RAW, e["file"])):
            continue
        out.append(e)
    # 採用されやすい順: 試行回数が少ない → 同じ分野をまとめる → Tier 1 優先 → 被引用数
    out.sort(key=lambda e: (int(e.get("wiki_compile_attempts", 0) or 0), e.get("domain") or "",
                            e.get("tier", 2), -int(e.get("citations", 0) or 0)))
    return out


def format_sources(items, with_domain=True):
    lines = []
    for n, e, excerpt in items:
        head = "### [%d] %s" % (n, e["title"])
        meta = []
        author = e.get("author") or e.get("authors") or ""
        if author:
            meta.append("Authors: %s" % author)
        if e.get("year"):
            meta.append("Year: %s" % e["year"])
        if e.get("citations") is not None:
            meta.append("Cited: %s" % e.get("citations"))
        if with_domain and e.get("domain"):
            meta.append("Domain: %s" % e["domain"])
        lines.append(head)
        if meta:
            lines.append("  " + " | ".join(meta))
        lines.append("  File: raw/%s" % e["file"])
        if e.get("key_insight"):
            lines.append("  Key insight: %s" % e["key_insight"])
        lines.append("  Abstract: %s" % excerpt.replace("\n", " "))
        lines.append("")
    return "\n".join(lines)


# ============================================================
# Phase 1: 概念抽出
# ============================================================
def parse_concepts(text, n_sources, known_slugs):
    cleaned = strip_code_fence(text)
    m = re.search(r"\[.*\]", cleaned, re.S)
    arr = json.loads(m.group(0) if m else cleaned)
    concepts = []
    used = set()
    for item in arr:
        if not isinstance(item, dict):
            continue
        slug = str(item.get("slug", "")).strip().lower()
        if not SLUG_RE.match(slug):
            continue
        srcs = []
        for v in item.get("related_sources") or []:
            try:
                k = int(v)
            except (TypeError, ValueError):
                continue
            if 1 <= k <= n_sources and k not in used:
                srcs.append(k)
                used.add(k)
        if not srcs:
            continue
        mech = [str(x).strip() for x in (item.get("mechanisms") or []) if str(x).strip()]
        concepts.append({
            "slug": slug,
            "existing": bool(item.get("existing")) or slug in known_slugs,
            "title_ja": str(item.get("title_ja") or slug).strip(),
            "title_en": str(item.get("title_en") or slug).strip(),
            "description": str(item.get("description") or "").strip(),
            "mechanisms": mech[:4],
            "related_sources": srcs,
        })
    return concepts[:CONCEPTS_PER_BATCH]


def extract_concepts(items, domain, slugs, model, tally):
    prompt = EXTRACT_PROMPT.format(
        domain_label=DOMAIN_LABELS.get(domain, domain or "未分類"),
        sources=format_sources(items, with_domain=False),
        existing_slugs=", ".join(slugs),
        max_concepts=CONCEPTS_PER_BATCH,
    )
    text, usage = call_claude(prompt, EXTRACT_SYSTEM, model=model)
    tally.add(usage)
    return parse_concepts(text, len(items), set(slugs)), usage


# ============================================================
# Phase 2: 記事生成と検証
# ============================================================
def write_article(concept, items, domain, slugs, model, tally):
    prompt = WRITE_PROMPT.format(
        title_ja=concept["title_ja"], title_en=concept["title_en"],
        description=concept["description"] or "(説明なし)",
        mechanisms=", ".join(concept["mechanisms"]) or "(未抽出)",
        domain_label=DOMAIN_LABELS.get(domain, domain or "未分類"),
        sources=format_sources(items, with_domain=False),
    )
    system = WRITE_SYSTEM.format(existing_slugs=", ".join(slugs))
    text, usage = call_claude(prompt, system, model=model)
    tally.add(usage)
    return strip_code_fence(text) if text.strip().startswith("```") else text.strip(), usage


def validate_article(text, concept, concept_nodes, alias_index, valid_slugs, existing_raw):
    """新規記事だけに当てる検証。戻り値は (本文, 統計)。"""
    stats = {"broken_links": 0, "normalized_links": 0, "bad_paths": 0}
    if not text.lstrip().startswith("# "):
        text = "# %s\n\n%s" % (concept["title_ja"], text)

    def fix_link(m):
        target = m.group(1).strip()
        label = (m.group(2) or target).strip()
        if target in valid_slugs:
            return "[[%s|%s]]" % (target, label) if m.group(2) else "[[%s]]" % target
        slug, resolved, _, _, _ = resolve_target(target, concept_nodes=concept_nodes, alias_index=alias_index)
        if resolved and slug:
            stats["normalized_links"] += 1
            return "[[%s]]" % slug if label == slug else "[[%s|%s]]" % (slug, label)
        stats["broken_links"] += 1
        return label

    text = re.sub(r"\[\[([^\]|]+?)(?:\|([^\]]+?))?\]\]", fix_link, text)

    def fix_path(m):
        path = m.group(1)
        if path in existing_raw:
            return m.group(0)
        stats["bad_paths"] += 1
        return "（パス未確認）"

    text = re.sub(r"`?(raw/[^\s`\)\]]+\.md)`?", fix_path, text)
    return text.rstrip() + "\n", stats


def append_sources_to_existing(slug, items, today):
    path = os.path.join(WIKI_CONCEPTS, slug + ".md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    lines = ["", "", "## 追加ソース（%s）" % today, ""]
    for _, e, _ in items:
        year = " (%s)" % e["year"] if e.get("year") else ""
        lines.append("* **タイトル**: %s%s" % (e["title"], year))
        lines.append("  **ファイルパス**: `raw/%s`" % e["file"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.rstrip("\n") + "\n".join(lines) + "\n")


# ============================================================
# 仕上げ: 知識グラフと HTML の再生成
# ============================================================
def rebuild_site():
    from lib.knowledge_graph import write_graph_artifacts
    from build_reader import build_reader
    from build_graph_ui import build_graph_ui
    from build_index_ui import build_index_ui

    graph, _ = write_graph_artifacts(base_dir=BASE)
    s = graph["summary"]
    print("  グラフ: concepts=%d edges=%d unresolved=%d" % (s["resolved_nodes"], s["edges"], s["unresolved_nodes"]), flush=True)
    r = build_reader()
    print("  wiki/reader.html: %d 記事 (%d bytes)" % (r["articles"], r["size"]), flush=True)
    g = build_graph_ui()
    print("  %s (%d bytes)" % (os.path.relpath(g["path"], BASE), g["size"]), flush=True)
    i = build_index_ui()
    print("  wiki/index.html: %d 記事 (%d bytes)" % (i["articles"], i["size"]), flush=True)


# ============================================================
# メイン
# ============================================================
def main():
    ap = argparse.ArgumentParser(description="claude -p による wiki 記事の増分生成")
    ap.add_argument("--limit", type=int, default=60, help="1 回の実行で概念抽出にかける論文数の上限(既定 60)")
    ap.add_argument("--batch", type=int, default=BATCH, help="1 ラウンドの論文数(既定 %d)" % BATCH)
    ap.add_argument("--domain", help="分野を 1 つに限定")
    ap.add_argument("--model-extract", default="sonnet", help="Phase 1(概念抽出)のモデル(既定 sonnet)")
    ap.add_argument("--model-write", default="sonnet", help="Phase 2(記事生成)のモデル(既定 sonnet)")
    ap.add_argument("--dry-run", action="store_true", help="対象を数えるだけ")
    ap.add_argument("--pilot-dir", help="記事をこのディレクトリに書き、index / concepts.json / HTML には触れない")
    ap.add_argument("--no-rebuild", action="store_true", help="HTML の再生成をしない")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(LOCK_PATH), exist_ok=True)
    lock = open(LOCK_PATH, "a+")
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("別の compile_articles_cli.py が実行中のためスキップします。", flush=True)
        return 0

    index = load_index()
    pending = pending_entries(index, args.domain)
    print("未コンパイル(Tier 1/2, 試行 %d 回未満): %d 件(今回 %d 件まで, 抽出=%s / 記事=%s)"
          % (MAX_ATTEMPTS, len(pending), args.limit, args.model_extract, args.model_write), flush=True)
    if args.dry_run or not pending:
        return 0
    pending = pending[: args.limit]

    pilot = bool(args.pilot_dir)
    out_dir = args.pilot_dir or WIKI_CONCEPTS
    os.makedirs(out_dir, exist_ok=True)
    today = datetime.date.today().isoformat()
    slugs = existing_slugs()
    meta = load_meta()
    known_meta_slugs = {c.get("slug") for c in meta}
    concept_nodes, alias_index = load_concept_graph_inputs(wiki_concepts_dir=WIKI_CONCEPTS, concepts_meta_path=META_PATH)
    existing_raw = set()
    for dirpath, _, filenames in os.walk(RAW):
        for fn in filenames:
            if fn.endswith(".md"):
                existing_raw.add(os.path.relpath(os.path.join(dirpath, fn), BASE))

    tally = UsageTally()
    new_articles = 0
    appended = 0
    compiled = 0
    failures = 0
    consecutive_failures = 0
    by_key = {(e["title"], e["file"]): e for e in index}

    for start in range(0, len(pending), args.batch):
        batch = pending[start:start + args.batch]
        domain = batch[0].get("domain")
        # 分野がまたがる端数は、先頭の分野に合わせて切る(抽出の質を保つ)
        batch = [e for e in batch if e.get("domain") == domain] or batch
        items = []
        for e in batch:
            ex = read_excerpt(e)
            if ex:
                items.append((len(items) + 1, e, ex))
        if not items:
            continue
        print("\n--- ラウンド %d: %s %d 件" % (start // args.batch + 1, domain, len(items)), flush=True)

        try:
            concepts, usage = extract_concepts(items, domain, slugs, args.model_extract, tally)
        except AuthError as e:
            print("認証エラー: %s\n`claude auth login` を実行してから再実行してください。" % str(e)[:200], flush=True)
            if not pilot:
                write_index(index)
            return 3
        except Exception as e:
            print("  ! 概念抽出に失敗: %s" % str(e)[:200], flush=True)
            failures += 1
            consecutive_failures += 1
            if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                print("連続 %d 回失敗したため中断します(利用枠の上限か障害の可能性)。" % consecutive_failures, flush=True)
                break
            continue
        consecutive_failures = 0
        print("  概念 %d 件 (入力 %d / 出力 %d トークン)" % (
            len(concepts), usage["input_tokens"] + usage["cache_creation_input_tokens"] + usage["cache_read_input_tokens"],
            usage["output_tokens"]), flush=True)

        assigned = set()
        for c in concepts:
            src_items = [items[k - 1] for k in c["related_sources"]]
            slug = c["slug"]
            is_existing = c["existing"] or slug in slugs or os.path.exists(os.path.join(out_dir, slug + ".md"))
            if is_existing and slug in slugs:
                if pilot:
                    print("  [%s] 既存記事に追加ソース %d 件(pilot のため書き込まない)" % (slug, len(src_items)), flush=True)
                else:
                    append_sources_to_existing(slug, src_items, today)
                    appended += 1
                    print("  [%s] 既存記事に追加ソース %d 件" % (slug, len(src_items)), flush=True)
            elif is_existing:
                # 既存と申告されたが記事が無い(pilot の重複等)。今回は採用しない
                print("  [%s] 既存扱いだが記事が無いためスキップ" % slug, flush=True)
                continue
            else:
                try:
                    text, usage = write_article(c, src_items, domain, slugs, args.model_write, tally)
                except AuthError as e:
                    print("認証エラー: %s" % str(e)[:200], flush=True)
                    if not pilot:
                        write_index(index)
                        write_meta(meta)
                    return 3
                except Exception as e:
                    print("  ! [%s] 記事生成に失敗: %s" % (slug, str(e)[:200]), flush=True)
                    failures += 1
                    continue
                if len(text) < MIN_ARTICLE_CHARS:
                    print("  ! [%s] 記事が短すぎるため破棄 (%d 文字)" % (slug, len(text)), flush=True)
                    failures += 1
                    continue
                text, stats = validate_article(text, c, concept_nodes, alias_index, set(slugs), existing_raw)
                with open(os.path.join(out_dir, slug + ".md"), "w", encoding="utf-8") as f:
                    f.write(text)
                new_articles += 1
                slugs.append(slug)
                print("  [%s] 新規記事 %d 文字 (出力 %d トークン; リンク解決 %d / 除去 %d, パス除去 %d)" % (
                    slug, len(text), usage["output_tokens"], stats["normalized_links"], stats["broken_links"], stats["bad_paths"]), flush=True)
                if not pilot and slug not in known_meta_slugs:
                    meta.append({
                        "slug": slug, "title_ja": c["title_ja"], "title_en": c["title_en"],
                        "description": c["description"], "mechanisms": c["mechanisms"],
                        "related_sources": c["related_sources"],
                        "source_files": ["raw/%s" % e["file"] for _, e, _ in src_items],
                        "domain": domain, "compiled_at": today,
                    })
                    known_meta_slugs.add(slug)
            for _, e, _ in src_items:
                assigned.add((e["title"], e["file"]))
                if not pilot:
                    row = by_key[(e["title"], e["file"])]
                    row["wiki_compiled"] = True
                    row["wiki_slug"] = slug
                    row["wiki_compiled_at"] = today
                    compiled += 1

        if not pilot:
            for _, e, _ in items:
                key = (e["title"], e["file"])
                if key not in assigned:
                    row = by_key[key]
                    row["wiki_compile_attempts"] = int(row.get("wiki_compile_attempts", 0) or 0) + 1
            write_index(index)
            write_meta(meta)
        print("  採用されなかった論文: %d 件" % (len(items) - len(assigned)), flush=True)

    print("\n結果: 新規記事 %d / 既存記事への追加 %d / 論文コンパイル %d / 失敗 %d" % (new_articles, appended, compiled, failures), flush=True)
    print("トークン: %s" % tally.summary(), flush=True)

    if not pilot and (new_articles or appended) and not args.no_rebuild:
        print("\n知識グラフと HTML を再生成します", flush=True)
        rebuild_site()

    if failures and not (new_articles or appended):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
