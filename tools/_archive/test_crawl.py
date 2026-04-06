"""各情報源からのテスト取得スクリプト"""
import json
import time
import sys

results = {}

# === 1. RSS フィード取得テスト ===
print("=" * 60)
print("1. RSS フィード取得テスト (Lilian Weng)")
print("=" * 60)
try:
    import feedparser
    feed = feedparser.parse("https://lilianweng.github.io/index.xml")
    print(f"  フィードタイトル: {feed.feed.get('title', 'N/A')}")
    print(f"  記事数: {len(feed.entries)}")
    for entry in feed.entries[:3]:
        print(f"  - {entry.get('title', 'N/A')}")
        print(f"    公開日: {entry.get('published', 'N/A')}")
        print(f"    URL: {entry.get('link', 'N/A')}")
    results["rss"] = {"status": "OK", "count": len(feed.entries)}
except Exception as e:
    print(f"  エラー: {e}")
    results["rss"] = {"status": "ERROR", "error": str(e)}

print()
time.sleep(1)

# === 2. Web 記事の本文抽出テスト ===
print("=" * 60)
print("2. Web 記事の本文抽出テスト (Trafilatura)")
print("=" * 60)
try:
    import trafilatura
    # Lilian Weng の最新記事を取得
    if feed.entries:
        test_url = feed.entries[0].get("link", "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/")
    else:
        test_url = "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
    print(f"  取得URL: {test_url}")
    downloaded = trafilatura.fetch_url(test_url)
    if downloaded:
        text = trafilatura.extract(downloaded, output_format="txt", include_links=True)
        if text:
            preview = text[:300].replace("\n", " ")
            print(f"  抽出文字数: {len(text)}")
            print(f"  プレビュー: {preview}...")
            results["trafilatura"] = {"status": "OK", "chars": len(text)}
        else:
            print("  本文抽出失敗（extractがNone）")
            results["trafilatura"] = {"status": "WARN", "error": "extract returned None"}
    else:
        print("  ページ取得失敗")
        results["trafilatura"] = {"status": "ERROR", "error": "fetch failed"}
except Exception as e:
    print(f"  エラー: {e}")
    results["trafilatura"] = {"status": "ERROR", "error": str(e)}

print()
time.sleep(2)

# === 3. arXiv 論文取得テスト ===
print("=" * 60)
print("3. arXiv 論文取得テスト (cs.AI, 最新5件)")
print("=" * 60)
try:
    import arxiv
    client = arxiv.Client()
    search = arxiv.Search(
        query="cat:cs.AI",
        max_results=5,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    papers = list(client.results(search))
    print(f"  取得論文数: {len(papers)}")
    for p in papers:
        print(f"  - {p.title[:80]}")
        print(f"    著者: {', '.join(a.name for a in p.authors[:3])}{'...' if len(p.authors) > 3 else ''}")
        print(f"    公開日: {p.published.strftime('%Y-%m-%d')}")
    results["arxiv"] = {"status": "OK", "count": len(papers)}
except Exception as e:
    print(f"  エラー: {e}")
    results["arxiv"] = {"status": "ERROR", "error": str(e)}

print()

# === サマリー ===
print("=" * 60)
print("サマリー")
print("=" * 60)
for source, res in results.items():
    status = res["status"]
    emoji = "✅" if status == "OK" else "⚠️" if status == "WARN" else "❌"
    print(f"  {emoji} {source}: {status}")
