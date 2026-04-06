#!/usr/bin/env python3
"""
compile_wiki.py — raw/ のデータを wiki/ にコンパイルするパイプライン

Phase 1: 全論文のアブストラクトを読み、分野横断コンセプトマップを生成
Phase 2: 各コンセプトのwiki記事を生成
Phase 3: wikiインデックスとメタデータを更新

使い方:
  source .env && python3 tools/compile_wiki.py
  source .env && python3 tools/compile_wiki.py --phase 1   # コンセプト抽出のみ
  source .env && python3 tools/compile_wiki.py --phase 2   # 記事生成のみ
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime

import httpx

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "raw")
WIKI = os.path.join(BASE, "wiki")
WIKI_CONCEPTS = os.path.join(WIKI, "concepts")
WIKI_META = os.path.join(WIKI, "_meta")

os.makedirs(WIKI_CONCEPTS, exist_ok=True)
os.makedirs(WIKI_META, exist_ok=True)

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
if not API_KEY:
    print("ANTHROPIC_API_KEY not set. Run: source .env")
    sys.exit(1)

MODEL = "claude-sonnet-4-20250514"


def call_claude(system, user, max_tokens=4096):
    r = httpx.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": MODEL,
            "max_tokens": max_tokens,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        },
        timeout=120,
    )
    r.raise_for_status()
    return "".join(b.get("text", "") for b in r.json()["content"] if b["type"] == "text")


def load_all_papers():
    """全論文のメタデータとアブストラクト冒頭を読み込む"""
    papers = []
    papers_dir = os.path.join(RAW, "papers")
    for domain in sorted(os.listdir(papers_dir)):
        dd = os.path.join(papers_dir, domain)
        if not os.path.isdir(dd):
            continue
        for fn in sorted(os.listdir(dd)):
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(dd, fn)
            with open(fp) as f:
                content = f.read()
            # メタデータ抽出
            t_m = re.search(r'title:\s*"?([^"\n]+)', content)
            title = t_m.group(1).strip('"') if t_m else ""
            if not title:
                h = re.search(r'^# (.+)', content, re.MULTILINE)
                title = h.group(1) if h else fn
            ci_m = re.search(r'citations:\s*(\d+)', content)
            citations = int(ci_m.group(1)) if ci_m else 0
            yr_m = re.search(r'year:\s*(\d+)', content)
            year = yr_m.group(1) if yr_m else ""
            au_m = re.search(r'authors:\s*"?([^"\n]+)', content)
            authors = au_m.group(1).strip('"') if au_m else ""
            # アブストラクト抽出（冒頭500文字）
            ab_m = re.search(r'## Abstract\s*\n+(.+)', content, re.DOTALL)
            abstract = ab_m.group(1)[:500].strip() if ab_m else ""
            papers.append({
                "title": title, "domain": domain, "citations": citations,
                "year": year, "authors": authors, "abstract": abstract,
                "file": f"papers/{domain}/{fn}",
            })
    return papers


def load_articles():
    articles = []
    articles_dir = os.path.join(RAW, "articles")
    if not os.path.isdir(articles_dir):
        return articles
    for fn in sorted(os.listdir(articles_dir)):
        if not fn.endswith(".md"):
            continue
        fp = os.path.join(articles_dir, fn)
        with open(fp) as f:
            content = f.read()
        t_m = re.search(r'title:\s*"?([^"\n]+)', content)
        title = t_m.group(1).strip('"') if t_m else fn
        au_m = re.search(r'author:\s*"?([^"\n]+)', content)
        author = au_m.group(1).strip('"') if au_m else ""
        # 本文冒頭
        parts = content.split("---", 2)
        body = parts[2][:800] if len(parts) >= 3 else content[:800]
        articles.append({
            "title": title, "author": author, "body_excerpt": body.strip(),
            "file": f"articles/{fn}",
        })
    return articles


# ============================================================
# Phase 1: コンセプト抽出
# ============================================================
def phase1_extract_concepts(papers, articles):
    print("=" * 60)
    print("Phase 1: コンセプト抽出")
    print(f"  論文: {len(papers)} | 記事: {len(articles)}")
    print("=" * 60)

    # 分野ごとのサマリーを作成（トークン節約）
    domain_summaries = {}
    for p in papers:
        d = p["domain"]
        if d not in domain_summaries:
            domain_summaries[d] = []
        domain_summaries[d].append(
            f"- {p['title']} ({p['year']}, cited:{p['citations']}): {p['abstract'][:150]}"
        )

    # ドメインサマリーテキスト
    summary_text = ""
    for domain, items in sorted(domain_summaries.items()):
        summary_text += f"\n### [{domain}] ({len(items)}件)\n"
        # 被引用数トップ10を選択
        sorted_items = sorted(items, key=lambda x: int(re.search(r'cited:(\d+)', x).group(1)) if re.search(r'cited:(\d+)', x) else 0, reverse=True)
        for item in sorted_items[:10]:
            summary_text += item + "\n"

    # 記事サマリー
    article_text = "\n### [技術記事]\n"
    for a in articles:
        article_text += f"- {a['title']} by {a['author']}: {a['body_excerpt'][:150]}\n"

    prompt = f"""以下は「AI Nativeな社会・組織・システム設計」というテーマで収集した17分野の論文と記事のサマリーです。

{summary_text}
{article_text}

---

これらの知見を統合し、AI Nativeな社会・組織・システム設計に必要なコンセプトを抽出してください。

要件:
1. 分野横断的なコンセプトを15〜20個抽出
2. 各コンセプトは複数の分野の知見を統合するもの
3. 以下の3つのTierに分類:
   - Tier 1（不変原理）: AGI時代でも成立する構造的原理
   - Tier 2（設計原理）: AI Nativeなシステムの設計に直接使える原理
   - Tier 3（分析枠組み）: 変化を理解するための分析フレームワーク

JSON配列のみで回答（他のテキスト不要）:
[
  {{
    "slug": "concept-slug",
    "title_ja": "日本語タイトル",
    "title_en": "English Title",
    "tier": 1,
    "description": "1行の説明",
    "related_domains": ["domain1", "domain2"],
    "key_sources": ["著者名 or 論文タイトルの一部"]
  }}
]
"""

    print("  Claude APIでコンセプト抽出中...")
    response = call_claude(
        "あなたはAI Nativeな社会設計の研究者です。17の学問分野の知見を統合し、分野横断的なコンセプトを抽出してください。回答はJSON配列のみ。",
        prompt,
        max_tokens=4000,
    )

    # JSONパース
    cleaned = response.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1]
    if cleaned.endswith("```"):
        cleaned = cleaned.rsplit("```", 1)[0]
    concepts = json.loads(cleaned.strip())

    # 保存
    meta_path = os.path.join(WIKI_META, "concepts.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(concepts, f, ensure_ascii=False, indent=2)

    print(f"  {len(concepts)}個のコンセプトを抽出:")
    for c in concepts:
        tier_mark = {1: "★", 2: "◇", 3: "△"}.get(c["tier"], "?")
        print(f"    {tier_mark} [{c['slug']}] {c['title_ja']}")
        print(f"      → {', '.join(c['related_domains'])}")

    return concepts


# ============================================================
# Phase 2: wiki記事生成
# ============================================================
def phase2_generate_articles(concepts, papers, articles):
    print("\n" + "=" * 60)
    print("Phase 2: wiki記事生成")
    print("=" * 60)

    # 分野→論文のマッピング
    domain_papers = {}
    for p in papers:
        d = p["domain"]
        if d not in domain_papers:
            domain_papers[d] = []
        domain_papers[d].append(p)

    for i, concept in enumerate(concepts):
        slug = concept["slug"]
        title_ja = concept["title_ja"]
        title_en = concept["title_en"]
        tier = concept["tier"]
        related_domains = concept["related_domains"]
        key_sources = concept.get("key_sources", [])

        print(f"\n  [{i+1}/{len(concepts)}] {title_ja} ({slug})")

        # 関連する論文を収集（被引用数上位）
        related_papers = []
        for domain in related_domains:
            if domain in domain_papers:
                sorted_p = sorted(domain_papers[domain],
                                  key=lambda x: x["citations"], reverse=True)
                related_papers.extend(sorted_p[:5])

        # ソーステキスト
        sources_text = ""
        for p in related_papers[:15]:  # 最大15件
            sources_text += f"\n### {p['title']} ({p['domain']}, {p['year']}, cited:{p['citations']})\n"
            sources_text += f"Authors: {p['authors']}\n"
            sources_text += f"Abstract: {p['abstract']}\n"

        # 記事の関連部分
        for a in articles:
            sources_text += f"\n### {a['title']} by {a['author']}\n"
            sources_text += f"{a['body_excerpt'][:300]}\n"

        prompt = f"""以下のソースに基づいて、「{title_ja} ({title_en})」についてのwiki記事を作成してください。

コンセプト情報:
- Tier: {tier}（{"不変原理" if tier==1 else "設計原理" if tier==2 else "分析枠組み"}）
- 説明: {concept['description']}
- 関連分野: {', '.join(related_domains)}

ソース:
{sources_text}

---

以下の形式でMarkdown記事を書いてください:
1. 「# {title_ja}」で始める
2. 概要（この概念が何か、なぜAI Native設計に重要か）
3. 理論的背景（主要な理論・モデル・実証知見）
4. AI Nativeな設計への示唆（具体的な設計原理や指針）
5. 分野横断的な接続（他のコンセプトとの関係を [[slug]] 形式で）
6. 参考ソース（主要論文のタイトルとraw/内パス）

日本語で、技術的に正確だが読みやすく書いてください。2000-3000字程度。
"""

        time.sleep(1)  # API rate limit
        try:
            article = call_claude(
                "あなたはAI Nativeな社会設計のテクニカルライターです。複数の学問分野の知見を統合し、設計指針につながるwiki記事を書いてください。",
                prompt,
                max_tokens=4000,
            )
            filepath = os.path.join(WIKI_CONCEPTS, f"{slug}.md")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(article)
            print(f"    ✅ 保存: concepts/{slug}.md ({len(article)}文字)")
        except Exception as e:
            print(f"    ❌ エラー: {e}")


# ============================================================
# Phase 3: wikiインデックス生成
# ============================================================
def phase3_generate_index(concepts, papers, articles):
    print("\n" + "=" * 60)
    print("Phase 3: wikiインデックス生成")
    print("=" * 60)

    # 分野統計
    domain_stats = {}
    for p in papers:
        d = p["domain"]
        domain_stats[d] = domain_stats.get(d, 0) + 1

    # Tier別にコンセプトを整理
    tiers = {1: [], 2: [], 3: []}
    for c in concepts:
        tiers[c["tier"]].append(c)

    index_md = "# Wiki インデックス — AI Native 社会・組織・システム設計\n\n"
    index_md += "このwikiは17の学問分野から収集した論文・記事をLLMによってコンセプト別に構造化したナレッジベースです。\n"
    index_md += "`fetch_latest.py`により毎日自動で最新論文が追加され、`compile_wiki.py`でwikiが更新されます。\n\n"

    tier_labels = {1: "Tier 1: 不変原理", 2: "Tier 2: 設計原理", 3: "Tier 3: 分析枠組み"}
    tier_descs = {
        1: "AGI時代でも成立する構造的原理。対象（人間/AI/組織）を入れ替えても成立する。",
        2: "AI Nativeなシステムの設計に直接使える原理。",
        3: "AI時代の変化を理解するための分析フレームワーク。",
    }
    for tier_num in [1, 2, 3]:
        if not tiers[tier_num]:
            continue
        index_md += f"## {tier_labels[tier_num]}\n\n"
        index_md += f"_{tier_descs[tier_num]}_\n\n"
        for c in tiers[tier_num]:
            domains_str = ", ".join(c["related_domains"][:3])
            index_md += f"- [[{c['slug']}|{c['title_ja']}]] — {c['description']} ({domains_str})\n"
        index_md += "\n"

    # 統計
    index_md += "## 統計\n\n"
    index_md += f"- 論文数: {len(papers)}\n"
    index_md += f"- 記事数: {len(articles)}\n"
    index_md += f"- コンセプト数: {len(concepts)} (Tier1: {len(tiers[1])}, Tier2: {len(tiers[2])}, Tier3: {len(tiers[3])})\n"
    index_md += f"- 対象分野: {len(domain_stats)}\n"
    index_md += f"- 最終コンパイル: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"

    index_md += "## 分野別ソース数\n\n"
    for d, c in sorted(domain_stats.items(), key=lambda x: -x[1]):
        index_md += f"- {d}: {c}\n"

    with open(os.path.join(WIKI, "index.md"), "w", encoding="utf-8") as f:
        f.write(index_md)
    print(f"  ✅ wiki/index.md 更新")


# ============================================================
# メイン
# ============================================================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", type=int, help="実行するフェーズ (1, 2, or 3)")
    args = parser.parse_args()

    papers = load_all_papers()
    articles = load_articles()
    print(f"ロード完了: 論文 {len(papers)} | 記事 {len(articles)}")

    if args.phase is None or args.phase == 1:
        concepts = phase1_extract_concepts(papers, articles)
    else:
        with open(os.path.join(WIKI_META, "concepts.json")) as f:
            concepts = json.load(f)

    if args.phase is None or args.phase == 2:
        phase2_generate_articles(concepts, papers, articles)

    if args.phase is None or args.phase == 3:
        phase3_generate_index(concepts, papers, articles)

    print("\n" + "=" * 60)
    print("コンパイル完了!")
    print("=" * 60)


if __name__ == "__main__":
    main()
