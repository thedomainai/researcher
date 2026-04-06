"""
Step 4: raw/ → wiki/ コンパイル
raw/のインデックスと記事内容を読み、コンセプト別のwiki記事を生成する
Claude APIを使用
"""
import json
import os
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

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
if not ANTHROPIC_API_KEY:
    print("❌ ANTHROPIC_API_KEY が設定されていません")
    sys.exit(1)

def call_claude(system_prompt, user_prompt, max_tokens=4096):
    """Claude APIを呼び出す"""
    resp = httpx.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": "claude-sonnet-4-6",
            "max_tokens": max_tokens,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return "".join(b.get("text", "") for b in data["content"] if b["type"] == "text")

# ============================================================
# rawデータの読み込み
# ============================================================
print("=" * 60)
print("Step 4: raw → wiki コンパイル")
print("=" * 60)

# インデックス読み込み（未コンパイルのみ対象）
index_path = os.path.join(RAW, "index.jsonl")
with open(index_path, "r", encoding="utf-8") as f:
    index = [json.loads(line) for line in f if line.strip()]

pending = [e for e in index if not e.get("wiki_compiled")]
print(f"\n  インデックス: {len(index)}件（未コンパイル: {len(pending)}件）")

if not pending:
    print("  ✅ 全件コンパイル済み。終了します。")
    sys.exit(0)

# 各rawファイルの要約を作成（全文はトークン過多なので冒頭を使う）
raw_summaries = []
for entry in pending:
    filepath = os.path.join(RAW, entry["file"])
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # 記事は冒頭2000文字、論文はAbstract全文
        if entry["type"] == "article":
            # フロントマター後の本文冒頭
            parts = content.split("---", 2)
            body = parts[2] if len(parts) >= 3 else content
            excerpt = body[:2000]
        else:
            excerpt = content[:1500]
        
        raw_summaries.append({
            "title": entry["title"],
            "type": entry["type"],
            "author": entry.get("author", entry.get("authors", "")),
            "excerpt": excerpt.strip(),
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
    "related_sources": [1, 2]  // 上の番号
  }}
]
"""

print("  Claude APIでコンセプト抽出中...")
concept_response = call_claude(
    "あなたはAI/ML研究のナレッジエンジニアです。与えられたソース群から主要コンセプトを抽出し、構造化してください。回答はJSON配列のみで、他のテキストは含めないでください。",
    concept_prompt,
    max_tokens=2000,
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
        article = call_claude(
            "あなたはAI/ML分野のテクニカルライターです。与えられたソースから正確で読みやすいwiki記事を日本語で作成してください。",
            article_prompt,
            max_tokens=3000,
        )

        filepath = os.path.join(WIKI_CONCEPTS, f"{slug}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(article)

        print(f"  ✅ 保存: concepts/{slug}.md ({len(article)}文字)")

        # コンパイル済みフラグをindex.jsonlに反映
        compiled_titles = {s["title"] for s in raw_summaries if raw_summaries.index(s) + 1 in related_indices}
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
