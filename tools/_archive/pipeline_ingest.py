"""
researcherパイプライン: raw取得 → wiki コンパイル
Step 1: RSS + Trafilatura で記事を raw/articles/ に保存
Step 2: arXiv で論文を raw/papers/ に保存  
Step 3: インデックス生成
"""
import json
import os
import re
import time
import hashlib
from datetime import datetime

import feedparser
import trafilatura
import arxiv

BASE = "/Users/yuta/workspace/projects/researcher"
RAW_ARTICLES = os.path.join(BASE, "raw", "articles")
RAW_PAPERS = os.path.join(BASE, "raw", "papers")

os.makedirs(RAW_ARTICLES, exist_ok=True)
os.makedirs(RAW_PAPERS, exist_ok=True)

index_entries = []

def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[\s]+', '-', text).strip('-')[:80]

# ============================================================
# Step 1: RSS → Trafilatura → raw/articles/
# ============================================================
print("=" * 60)
print("Step 1: RSS記事の取得と本文抽出")
print("=" * 60)

rss_feeds = [
    ("https://lilianweng.github.io/index.xml", "Lilian Weng"),
    ("https://magazine.sebastianraschka.com/feed", "Sebastian Raschka"),
]

saved_articles = 0
MAX_ARTICLES_PER_FEED = 2  # テスト用に各フィードから2記事

for feed_url, author in rss_feeds:
    print(f"\n  [{author}] フィード取得中...")
    try:
        feed = feedparser.parse(feed_url)
        entries = feed.entries[:MAX_ARTICLES_PER_FEED]
        for entry in entries:
            title = entry.get("title", "untitled")
            url = entry.get("link", "")
            published = entry.get("published", "")
            slug = slugify(title)
            filename = f"{slug}.md"
            filepath = os.path.join(RAW_ARTICLES, filename)

            print(f"    取得中: {title[:60]}...")
            time.sleep(1.5)  # レート制限

            downloaded = trafilatura.fetch_url(url)
            if downloaded:
                text = trafilatura.extract(downloaded, output_format="txt", include_links=True)
                if text:
                    # フロントマター付きMarkdownとして保存
                    md_content = f"""---
title: "{title}"
author: "{author}"
url: "{url}"
published: "{published}"
fetched: "{datetime.now().isoformat()}"
source_type: "rss_article"
---

# {title}

{text}
"""
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(md_content)

                    index_entries.append({
                        "id": hashlib.md5(url.encode()).hexdigest()[:12],
                        "type": "article",
                        "title": title,
                        "author": author,
                        "url": url,
                        "published": published,
                        "file": f"articles/{filename}",
                        "chars": len(text),
                    })
                    saved_articles += 1
                    print(f"    ✅ 保存: {filename} ({len(text)}文字)")
                else:
                    print(f"    ⚠️ 本文抽出失敗: {title[:40]}")
            else:
                print(f"    ❌ ページ取得失敗: {url}")
    except Exception as e:
        print(f"    ❌ フィードエラー [{author}]: {e}")

print(f"\n  → 記事 {saved_articles}件 保存完了")

# ============================================================
# Step 2: arXiv → raw/papers/
# ============================================================
print("\n" + "=" * 60)
print("Step 2: arXiv論文の取得")
print("=" * 60)

saved_papers = 0
MAX_PAPERS = 5

try:
    client = arxiv.Client()
    search = arxiv.Search(
        query="cat:cs.AI OR cat:cs.LG",
        max_results=MAX_PAPERS,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    for paper in client.results(search):
        title = paper.title.replace("\n", " ")
        slug = slugify(title)
        filename = f"{slug}.md"
        filepath = os.path.join(RAW_PAPERS, filename)
        authors = ", ".join(a.name for a in paper.authors[:5])
        if len(paper.authors) > 5:
            authors += f" (+{len(paper.authors)-5}名)"
        categories = ", ".join(paper.categories)

        md_content = f"""---
title: "{title}"
authors: "{authors}"
arxiv_id: "{paper.entry_id}"
published: "{paper.published.isoformat()}"
categories: "{categories}"
fetched: "{datetime.now().isoformat()}"
source_type: "arxiv_paper"
---

# {title}

**著者**: {authors}
**カテゴリ**: {categories}
**公開日**: {paper.published.strftime('%Y-%m-%d')}
**arXiv**: {paper.entry_id}

## Abstract

{paper.summary}
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)

        index_entries.append({
            "id": hashlib.md5(paper.entry_id.encode()).hexdigest()[:12],
            "type": "paper",
            "title": title,
            "authors": authors,
            "arxiv_id": paper.entry_id,
            "published": paper.published.isoformat(),
            "categories": categories,
            "file": f"papers/{filename}",
        })
        saved_papers += 1
        print(f"  ✅ {title[:70]}...")

except Exception as e:
    print(f"  ❌ arXivエラー: {e}")

print(f"\n  → 論文 {saved_papers}件 保存完了")

# ============================================================
# Step 3: インデックス生成
# ============================================================
print("\n" + "=" * 60)
print("Step 3: インデックス生成")
print("=" * 60)

index_path = os.path.join(BASE, "raw", "index.jsonl")
with open(index_path, "w", encoding="utf-8") as f:
    for entry in index_entries:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"  ✅ {len(index_entries)}件のエントリを index.jsonl に保存")

# サマリー
print("\n" + "=" * 60)
print("完了サマリー")
print("=" * 60)
print(f"  記事: {saved_articles}件")
print(f"  論文: {saved_papers}件")
print(f"  インデックス: {len(index_entries)}件")
