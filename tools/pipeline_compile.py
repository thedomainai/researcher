"""
Step 4: raw/ → wiki/ コンパイル
raw/のインデックスと記事内容を読み、コンセプト別のwiki記事を生成する
Gemini APIを使用

Usage:
    python tools/pipeline_compile.py [--domain DOMAIN] [--limit N] [--tier-only]

    --domain    : 特定の分野のみ処理（例: neuroscience, ai_governance）
    --limit     : 1回の実行で処理する論文数上限（デフォルト: 30）
    --tier-only : Tier分類のみ実行しコンパイルはスキップ
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import httpx

BASE = "/Users/yuta/workspace/projects/researcher"
RAW = os.path.join(BASE, "raw")
WIKI = os.path.join(BASE, "wiki")
WIKI_CONCEPTS = os.path.join(WIKI, "concepts")
WIKI_META = os.path.join(WIKI, "_meta")

os.makedirs(WIKI_CONCEPTS, exist_ok=True)
os.makedirs(WIKI_META, exist_ok=True)

parser = argparse.ArgumentParser(description="Compile raw papers into wiki articles")
parser.add_argument("--domain", default=None, help="Filter by domain (e.g. neuroscience)")
parser.add_argument("--limit", type=int, default=30, help="Max papers to process per run (default: 30)")
parser.add_argument("--tier-only", action="store_true", help="Run tier classification only, skip compilation")
args = parser.parse_args()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
if not GEMINI_API_KEY:
    for op_ref in [
        "op://orchestration/Gemini API/credential",
        "op://orchestration/Gemini/credential",
    ]:
        try:
            GEMINI_API_KEY = subprocess.check_output(
                ["op", "read", op_ref],
                stderr=subprocess.DEVNULL,
            ).decode().strip()
            if GEMINI_API_KEY:
                break
        except Exception:
            pass
if not GEMINI_API_KEY:
    print("GEMINI_API_KEY が設定されていません（環境変数または 1Password）")
    sys.exit(1)

GEMINI_MODEL = "gemini-3.5-flash"

MAX_RETRIES = 5
RETRY_BASE_DELAY = 10  # seconds

def call_llm(system_prompt, user_prompt, max_tokens=4096):
    """Gemini APIを呼び出す（429 リトライ付き）"""
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        + GEMINI_MODEL
        + ":generateContent"
    )
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
        "generationConfig": {
            "maxOutputTokens": max_tokens,
            "thinkingConfig": {"thinkingBudget": 0},
        },
    }
    for attempt in range(1, MAX_RETRIES + 1):
        resp = httpx.post(
            url,
            params={"key": GEMINI_API_KEY},
            headers={"content-type": "application/json"},
            json=payload,
            timeout=120,
        )
        if resp.status_code == 429:
            delay = RETRY_BASE_DELAY * attempt
            print(f"    429 rate-limited, retrying in {delay}s (attempt {attempt}/{MAX_RETRIES})")
            time.sleep(delay)
            continue
        if resp.status_code >= 400:
            raise RuntimeError("Gemini API error %d: %s" % (resp.status_code, resp.text[:300]))
        data = resp.json()
        candidates = data.get("candidates", [])
        if not candidates:
            raise RuntimeError("Gemini API returned no candidates: %s" % json.dumps(data)[:500])
        parts = candidates[0].get("content", {}).get("parts", [])
        return "".join(p.get("text", "") for p in parts)
    raise RuntimeError("Gemini API: max retries exceeded (429)")

# ============================================================
# Tier分類
# ============================================================

TIER_SYSTEM_PROMPT = (
    "あなたは研究論文の品質評価者です。与えられた論文を3つのテストで評価し、"
    "Tier分類をJSON形式で返してください。JSON以外は出力しないでください。"
)

TIER_USER_PROMPT = """以下の論文について、AI nativeな社会・組織・システム設計への有用性を評価してください。

タイトル: {title}
アブストラクト: {abstract}

以下の3つのテストを適用してください:

1. 抽象度テスト: この知見から具体的な対象（人間、現在の技術、現在の制度）を除去しても成立するか？
2. 制約不変テスト: この知見が依拠している制約条件は、AGI時代にも存続するか？
3. メカニズムテスト: この研究は「なぜ」を説明しているか、それとも「何が起きたか」を記述しているだけか？

分類:
- Tier 1（不変原理）: 3テスト全てを満たす
- Tier 2（消滅制約の分析）: テスト2で「消滅する制約」に依拠するが、その制約の構造的分析として価値がある
- Tier 3（スキップ）: 条件依存的な現象記述または手法レベルの最適化

JSON形式で回答（JSON以外は出力しないでください）:
{{"tier": 1, "reasoning": "判定理由", "key_insight": "核心的知見の1行要約"}}"""


def classify_tier(title, abstract):
    """論文のTier分類を実行し、結果dictを返す。失敗時はNone。"""
    prompt = TIER_USER_PROMPT.format(title=title, abstract=abstract)
    try:
        raw_response = call_llm(TIER_SYSTEM_PROMPT, prompt, max_tokens=512)
        cleaned = raw_response.strip()
        # ```json ... ``` フェンスを除去
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[1]
        if cleaned.endswith("```"):
            cleaned = cleaned.rsplit("```", 1)[0]
        cleaned = cleaned.strip()
        # JSONオブジェクトを抽出（前後にテキストがある場合に対応）
        match = re.search(r'\{[^{}]*\}', cleaned)
        if match:
            cleaned = match.group(0)
        result = json.loads(cleaned)
        tier = result.get("tier")
        if tier not in (1, 2, 3):
            return None
        return {
            "tier": tier,
            "tier_reasoning": result.get("reasoning", ""),
            "key_insight": result.get("key_insight", ""),
        }
    except Exception as e:
        print(f"    ⚠ Tier分類エラー: {e}")
        return None


def read_excerpt(entry):
    """rawファイルから評価用のexcerptを読む。"""
    filepath = os.path.join(RAW, entry["file"])
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if entry["type"] == "article":
        parts = content.split("---", 2)
        body = parts[2] if len(parts) >= 3 else content
        return body[:2000].strip()
    return content[:1500].strip()


# ============================================================
# rawデータの読み込み
# ============================================================
print("=" * 60)
print("Step 4: raw → wiki コンパイル")
print("=" * 60)

# インデックス読み込み
index_path = os.path.join(RAW, "index.jsonl")
with open(index_path, "r", encoding="utf-8") as f:
    index = [json.loads(line) for line in f if line.strip()]

# ============================================================
# Phase 0: Tier分類（未分類エントリのみ）
# ============================================================
needs_tier = [e for e in index if "tier" not in e]
if args.domain:
    needs_tier = [e for e in needs_tier if e.get("domain") == args.domain]

if needs_tier:
    print(f"\n  Tier未分類: {len(needs_tier)}件")
    tier_limit = args.limit
    if len(needs_tier) > tier_limit:
        print(f"  ℹ️  上限 {tier_limit} 件に絞ってTier分類します")
        needs_tier = needs_tier[:tier_limit]

    print("\n" + "-" * 40)
    print("Phase 0: Tier分類")
    print("-" * 40)

    tier_counts = {1: 0, 2: 0, 3: 0}
    tier_errors = 0

    for i, entry in enumerate(needs_tier):
        excerpt = read_excerpt(entry)
        if not excerpt:
            print(f"  [{i+1}/{len(needs_tier)}] SKIP (ファイルなし): {entry['title'][:50]}")
            continue

        result = classify_tier(entry["title"], excerpt)
        if result:
            # index内の該当エントリを更新
            for e in index:
                if e["title"] == entry["title"] and e["file"] == entry["file"]:
                    e["tier"] = result["tier"]
                    e["tier_reasoning"] = result["tier_reasoning"]
                    e["key_insight"] = result["key_insight"]
                    break
            tier_counts[result["tier"]] += 1
            label = {1: "不変原理", 2: "設計原理", 3: "スキップ"}[result["tier"]]
            print(f"  [{i+1}/{len(needs_tier)}] Tier {result['tier']} ({label}): {entry['title'][:50]}")
        else:
            tier_errors += 1
            print(f"  [{i+1}/{len(needs_tier)}] ERROR: {entry['title'][:50]}")

        time.sleep(0.5)  # API レート制限

    # index.jsonl に書き戻し
    with open(index_path, "w", encoding="utf-8") as f:
        for e in index:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    print(f"\n  Tier分類結果: T1={tier_counts[1]}, T2={tier_counts[2]}, T3={tier_counts[3]}, エラー={tier_errors}")
    print(f"  ✅ raw/index.jsonl 更新済み")
else:
    print(f"\n  Tier分類: 全件分類済み")

if args.tier_only:
    total_with_tier = sum(1 for e in index if "tier" in e)
    print(f"\n  --tier-only: Tier分類のみ完了（{total_with_tier}/{len(index)}件分類済み）")
    sys.exit(0)

# ============================================================
# コンパイル対象のフィルタリング（Tier 3はスキップ）
# ============================================================
pending = [e for e in index if not e.get("wiki_compiled") and e.get("tier", 2) != 3]
if args.domain:
    pending = [e for e in pending if e.get("domain") == args.domain]
    print(f"\n  インデックス: {len(index)}件（コンパイル対象: {len(pending)}件, domain={args.domain}）")
else:
    print(f"\n  インデックス: {len(index)}件（コンパイル対象: {len(pending)}件）")

tier3_skip = sum(1 for e in index if e.get("tier") == 3 and not e.get("wiki_compiled"))
if tier3_skip:
    print(f"  ℹ️  Tier 3 スキップ: {tier3_skip}件")

if not pending:
    print("  ✅ 全件コンパイル済み（またはTier 3でスキップ）。終了します。")
    sys.exit(0)

# 1回あたりの処理上限
if len(pending) > args.limit:
    print(f"  ℹ️  上限 {args.limit} 件に絞って処理します（残り {len(pending) - args.limit} 件は次回以降）")
    pending = pending[: args.limit]

# 各rawファイルの要約を作成（全文はトークン過多なので冒頭を使う）
raw_summaries = []
for entry in pending:
    excerpt = read_excerpt(entry)
    if excerpt:
        raw_summaries.append({
            "title": entry["title"],
            "type": entry["type"],
            "author": entry.get("author", entry.get("authors", "")),
            "excerpt": excerpt,
        })

print(f"  読み込み完了: {len(raw_summaries)}件\n")

# ============================================================
# Phase 1: コンセプト抽出
# ============================================================
print("-" * 40)
print("Phase 1: コンセプト抽出")
print("-" * 40)

summaries_text = ""
for i, s in enumerate(raw_summaries):
    summaries_text += f"\n### [{i+1}] {s['title']} ({s['type']}, {s['author']})\n{s['excerpt']}\n"

concept_prompt = f"""以下は最近取得したAI/ML関連の記事・論文です。

{summaries_text}

---

これらの内容から、wikiに整理すべき主要コンセプトを5つ抽出してください。
各コンセプトについて以下のJSON配列で返してください（JSON以外は出力しないでください）:

[
  {{
    "slug": "concept-slug-in-english",
    "title_ja": "日本語タイトル",
    "title_en": "English Title",
    "description": "1行の説明（日本語）",
    "mechanisms": ["中核的メカニズム名（日本語、2-4個）"],
    "related_sources": [1, 2]  // 上の番号
  }}
]

mechanismsの抽出基準:
- 対象（人間/AI/組織/技術）を入れ替えても成立する構造的原理・メカニズムの名前を記述する
- 例: "情報の非対称性", "有限合理性", "プリンシパル＝エージェント問題", "予測誤差による学習", "フィードバックループ", "経路依存性"
- 具体的なツール名・手法名ではなく、背後にある抽象的メカニズムを抽出する
"""

print("  Gemini APIでコンセプト抽出中...")
concept_response = call_llm(
    "あなたはAI/ML研究のナレッジエンジニアです。与えられたソース群から主要コンセプトを抽出し、構造化してください。回答はJSON配列のみで、他のテキストは含めないでください。",
    concept_prompt,
    max_tokens=4096,
)

# JSONパース
try:
    # ```json ... ``` のフェンスを除去
    cleaned = concept_response.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1]
    if cleaned.endswith("```"):
        cleaned = cleaned.rsplit("```", 1)[0]
    concepts = json.loads(cleaned.strip())
    print(f"  ✅ {len(concepts)}個のコンセプトを抽出:")
    for c in concepts:
        print(f"     - {c['title_ja']} ({c['slug']})")
        print(f"       関連ソース: {c['related_sources']}")
except Exception as e:
    print(f"  ❌ JSONパースエラー: {e}")
    print(f"  レスポンス: {concept_response[:500]}")
    sys.exit(1)

# ============================================================
# Phase 2: 各コンセプトのwiki記事生成
# ============================================================
print("\n" + "-" * 40)
print("Phase 2: wiki記事生成")
print("-" * 40)

for concept in concepts:
    slug = concept["slug"]
    title_ja = concept["title_ja"]
    title_en = concept["title_en"]
    related_indices = concept["related_sources"]

    # 関連ソースの本文を収集
    related_content = ""
    for idx in related_indices:
        if 1 <= idx <= len(raw_summaries):
            s = raw_summaries[idx - 1]
            related_content += f"\n### {s['title']} ({s['author']})\n{s['excerpt']}\n"

    article_prompt = f"""以下のソースに基づいて、「{title_ja} ({title_en})」についてのwiki記事を作成してください。

{related_content}

---

以下の形式でMarkdown記事を書いてください:
- フロントマターは不要
- 見出し1は「# {title_ja}」
- 概要セクション（この概念が何か、なぜ重要か）
- 詳細セクション（ソースから得られた知見を整理）
- 関連概念セクション（他の概念へのリンクを [[概念名]] 形式で）
- 参考ソースセクション（ソースのタイトルとraw/内のファイルパス）

日本語で、技術的に正確に、しかし読みやすく書いてください。
"""

    print(f"\n  [{slug}] 記事生成中...")
    time.sleep(1)  # API レート制限
    
    try:
        article = call_llm(
            "あなたはAI/ML分野のテクニカルライターです。与えられたソースから正確で読みやすいwiki記事を日本語で作成してください。",
            article_prompt,
            max_tokens=3000,
        )

        filepath = os.path.join(WIKI_CONCEPTS, f"{slug}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(article)

        print(f"  ✅ 保存: concepts/{slug}.md ({len(article)}文字)")

        # コンパイル済みフラグをindex.jsonlに反映（1-based index を 0-based に変換）
        compiled_titles = {raw_summaries[i]["title"] for i in range(len(raw_summaries)) if (i + 1) in related_indices}
        updated_index = []
        for e in index:
            if e["title"] in compiled_titles:
                e = {**e, "wiki_compiled": True, "wiki_slug": slug}
            updated_index.append(e)
        index = updated_index

    except Exception as e:
        print(f"  ❌ エラー [{slug}]: {e}")

# ============================================================
# Phase 3: メタデータ更新 + index.jsonl 書き戻し
# ============================================================
print("\n" + "-" * 40)
print("Phase 3: メタデータ更新")
print("-" * 40)

# _meta/concepts.json に今回のコンセプトをマージ（既存を保持）
meta_path = os.path.join(WIKI_META, "concepts.json")
existing_concepts = []
if os.path.exists(meta_path):
    with open(meta_path, "r", encoding="utf-8") as f:
        existing_concepts = json.load(f)

existing_slugs = {c["slug"] for c in existing_concepts}
merged_concepts = existing_concepts + [c for c in concepts if c["slug"] not in existing_slugs]

with open(meta_path, "w", encoding="utf-8") as f:
    json.dump(merged_concepts, f, ensure_ascii=False, indent=2)

print(f"  ✅ wiki/_meta/concepts.json 更新（{len(merged_concepts)}件）")

# index.jsonl に wiki_compiled フラグを書き戻し
with open(index_path, "w", encoding="utf-8") as f:
    for e in index:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")

compiled_count = sum(1 for e in index if e.get("wiki_compiled"))
print(f"  ✅ raw/index.jsonl 更新（コンパイル済み: {compiled_count}/{len(index)}件）")
print("  ℹ️  wiki/index.md は手動管理のため上書きしません")

print("\n" + "=" * 60)
print("パイプライン完了!")
print("=" * 60)
print(f"  wiki/concepts/*.md  — コンセプト別記事 {len(concepts)}件")
print(f"  wiki/_meta/         — メタデータ")
