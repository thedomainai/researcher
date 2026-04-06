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
            "model": "claude-sonnet-4-20250514",
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

# インデックス読み込み
index_path = os.path.join(RAW, "index.jsonl")
with open(index_path, "r", encoding="utf-8") as f:
    index = [json.loads(line) for line in f if line.strip()]

print(f"\n  インデックス: {len(index)}件")

# 各rawファイルの要約を作成（全文はトークン過多なので冒頭を使う）
raw_summaries = []
for entry in index:
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

    except Exception as e:
        print(f"  ❌ エラー [{slug}]: {e}")

# ============================================================
# Phase 3: wikiインデックス生成
# ============================================================
print("\n" + "-" * 40)
print("Phase 3: wikiインデックス生成")
print("-" * 40)

index_md = """# Wiki インデックス

このwikiは、raw/に取り込んだAI/ML関連の記事・論文からLLMによって自動生成されたものです。

## コンセプト一覧

"""
for concept in concepts:
    index_md += f"- [[{concept['slug']}|{concept['title_ja']}]] — {concept['description']}\n"

index_md += f"""
## 統計

- ソース数: {len(index)}件（記事: {sum(1 for e in index if e['type']=='article')}、論文: {sum(1 for e in index if e['type']=='paper')}）
- コンセプト数: {len(concepts)}件
- 最終更新: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}

## rawソース一覧

"""
for entry in index:
    if entry["type"] == "article":
        index_md += f"- 📄 [{entry['title']}]({entry['url']}) by {entry['author']}\n"
    else:
        index_md += f"- 📝 {entry['title']} ({entry.get('categories', '')})\n"

wiki_index_path = os.path.join(WIKI, "index.md")
with open(wiki_index_path, "w", encoding="utf-8") as f:
    f.write(index_md)

# メタデータ保存
meta_path = os.path.join(WIKI_META, "concepts.json")
with open(meta_path, "w", encoding="utf-8") as f:
    json.dump(concepts, f, ensure_ascii=False, indent=2)

print(f"  ✅ wiki/index.md 生成")
print(f"  ✅ wiki/_meta/concepts.json 保存")

print("\n" + "=" * 60)
print("パイプライン完了!")
print("=" * 60)
print(f"  wiki/index.md       — ウィキのインデックス")
print(f"  wiki/concepts/*.md  — コンセプト別記事 {len(concepts)}件")
print(f"  wiki/_meta/         — メタデータ")
