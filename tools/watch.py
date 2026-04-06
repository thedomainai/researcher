#!/usr/bin/env python3
"""
watch.py — 17分野の最新論文を継続的に取得するモジュール

設計思想:
  - cronで定期実行される（推奨: 1日1回）
  - 前回取得日以降の新着論文のみを取得
  - OpenAlex API（全分野、レート緩い）+ arXiv API（CS系補完）+ RSS記事
  - 取得した論文はraw/papers/{domain}/に保存、index.jsonlに追記
  - 重複排除はタイトルハッシュ（lib/storage経由）

使い方:
  python3 tools/fetch.py watch                        # 全分野の最新を取得
  python3 tools/fetch.py watch --domain neuroscience  # 特定分野のみ
  python3 tools/fetch.py watch --since 2026-04-01     # 日付指定
  python3 tools/fetch.py watch --dry-run              # 取得せず確認のみ
  python3 tools/fetch.py watch --no-rss               # RSS取得をスキップ
"""

import json
import os
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional

from lib.rate_limiter import RateLimiter
from lib.openalex import OpenAlexClient
from lib.storage import PaperStore
from lib.schema import build_index_entry
from lib.utils import detect_paper_type, title_hash, slugify

# ============================================================
# パス設定
# ============================================================
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_PATH = os.path.join(BASE, "config", "fetch_state.json")
LOG_DIR = os.path.join(BASE, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# ============================================================
# 分野定義（新着取得に最適化されたクエリ）
# ============================================================
DOMAINS = {
    "neuroscience": {
        "label": "脳科学",
        "search_queries": [
            "predictive coding artificial intelligence",
            "neural plasticity human-computer interaction",
            "decision making brain AI",
            "social brain hypothesis AI",
            "embodied cognition robot",
            "working memory cognitive AI",
        ],
        "arxiv_queries": [
            ("q-bio.NC", "artificial intelligence"),
            ("q-bio.NC", "machine learning"),
        ],
    },
    "cognitive_science": {
        "label": "認知科学",
        "search_queries": [
            "cognitive load artificial intelligence",
            "dual process theory AI decision",
            "distributed cognition AI system",
            "metacognition AI calibration",
            "cognitive bias machine learning",
            "mental model AI interaction",
        ],
        "arxiv_queries": [
            ("cs.HC", "cognitive load"),
            ("cs.HC", "cognitive bias"),
        ],
    },
    "complexity_science": {
        "label": "複雑系科学",
        "search_queries": [
            "complex adaptive systems artificial intelligence",
            "emergence multi-agent systems",
            "self-organization AI",
            "cybernetics AI system",
            "systems thinking artificial intelligence",
        ],
        "arxiv_queries": [
            ("cs.MA", "multi-agent"),
            ("cs.MA", "emergence"),
            ("nlin.AO", "complex adaptive"),
        ],
    },
    "psychology": {
        "label": "心理学",
        "search_queries": [
            "self-determination theory AI technology",
            "trust automation AI",
            "self-efficacy artificial intelligence",
            "creativity AI collaboration",
            "flow experience technology AI",
            "automation complacency AI",
        ],
    },
    "behavioral_economics": {
        "label": "行動経済学",
        "search_queries": [
            "algorithm aversion trust",
            "nudge artificial intelligence",
            "bounded rationality AI decision",
            "default effect AI recommendation",
            "decision making AI behavioral",
        ],
    },
    "evolutionary_biology": {
        "label": "進化生物学・文化進化",
        "search_queries": [
            "cultural evolution artificial intelligence",
            "human AI coevolution",
            "niche construction technology AI",
        ],
    },
    "sociology": {
        "label": "社会学",
        "search_queries": [
            "institutional theory artificial intelligence",
            "actor-network theory AI technology",
            "trust social systems AI",
            "digital divide artificial intelligence",
            "network society AI",
        ],
    },
    "economics": {
        "label": "経済学",
        "search_queries": [
            "AI labor market automation",
            "task automation artificial intelligence",
            "general purpose technology AI",
            "AI productivity economic",
            "platform economics artificial intelligence",
        ],
    },
    "organization_science": {
        "label": "組織科学",
        "search_queries": [
            "AI organizational design",
            "dynamic capabilities artificial intelligence",
            "knowledge management AI",
            "organizational ambidexterity AI",
            "team cognition AI",
            "organizational routines automation AI",
        ],
    },
    "anthropology": {
        "label": "人類学",
        "search_queries": [
            "digital anthropology artificial intelligence",
            "technology anthropology AI",
            "organizational ethnography AI",
        ],
    },
    "philosophy": {
        "label": "哲学",
        "search_queries": [
            "philosophy of mind artificial intelligence",
            "epistemology AI knowledge",
            "artificial moral agency",
            "value alignment AI ethics",
            "political philosophy artificial intelligence",
        ],
    },
    "law": {
        "label": "法学",
        "search_queries": [
            "AI legal personhood",
            "algorithmic accountability law",
            "AI liability tort",
            "AI regulation governance",
            "intellectual property AI generated",
        ],
    },
    "hci": {
        "label": "HCI",
        "search_queries": [
            "human-AI interaction design",
            "explainable AI user study",
            "mixed-initiative AI interaction",
            "AI decision support system",
        ],
        "arxiv_queries": [
            ("cs.HC", "human-AI interaction"),
            ("cs.HC", "explainable AI"),
        ],
    },
    "systems_engineering": {
        "label": "システム工学",
        "search_queries": [
            "resilience engineering AI system",
            "sociotechnical systems AI",
            "safety critical AI",
            "human-automation interaction",
        ],
        "arxiv_queries": [
            ("cs.SY", "safety AI"),
            ("cs.SY", "human-automation"),
        ],
    },
    "history_of_technology": {
        "label": "技術史",
        "search_queries": [
            "technological revolution automation history",
            "general purpose technology historical",
            "automation labor history AI",
        ],
    },
    "human_ai_collaboration": {
        "label": "人間-AI協働",
        "search_queries": [
            "human-AI collaboration",
            "AI augmentation knowledge work",
            "AI productivity experiment",
            "human AI team performance",
        ],
        "arxiv_queries": [
            ("cs.AI", "human-AI collaboration"),
            ("cs.HC", "AI augmentation"),
        ],
    },
    "ai_governance": {
        "label": "AIガバナンス",
        "search_queries": [
            "AI governance framework",
            "algorithmic fairness bias",
            "responsible AI principles",
            "AI safety alignment",
            "AI regulation policy",
        ],
        "arxiv_queries": [
            ("cs.CY", "AI governance"),
            ("cs.AI", "AI safety alignment"),
        ],
    },
}


# ============================================================
# 状態管理
# ============================================================
def load_state():
    # type: () -> Dict
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_state(state):
    # type: (Dict) -> None
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


# ============================================================
# arXiv取得
# ============================================================
def fetch_arxiv(domain, config, since, store, dry_run=False):
    # type: (str, Dict, str, PaperStore, bool) -> List[Dict]
    """Fetch latest papers from arXiv API."""
    arxiv_queries = config.get("arxiv_queries", [])
    if not arxiv_queries:
        return []

    try:
        import arxiv as arxiv_lib
    except ImportError:
        print("    arxiv package not installed, skipping")
        return []

    results = []
    try:
        client = arxiv_lib.Client()
        seen_ids = set()  # type: set

        for category, keyword in arxiv_queries:
            query = "cat:%s AND all:%s" % (category, keyword)
            search = arxiv_lib.Search(
                query=query,
                max_results=3,
                sort_by=arxiv_lib.SortCriterion.SubmittedDate,
                sort_order=arxiv_lib.SortOrder.Descending,
            )
            time.sleep(3)

            for paper in client.results(search):
                if paper.entry_id in seen_ids:
                    continue
                seen_ids.add(paper.entry_id)

                title = paper.title.replace("\n", " ")
                if store.is_duplicate(title):
                    continue

                pub_date = paper.published.strftime("%Y-%m-%d")
                if pub_date < since:
                    continue

                abstract = paper.summary or ""
                authors = ", ".join(a.name for a in paper.authors[:5])
                if len(paper.authors) > 5:
                    authors += " (+%d)" % (len(paper.authors) - 5)
                paper_type = detect_paper_type(title, abstract)

                paper_data = {
                    "title": title,
                    "authors": authors,
                    "year": paper.published.year,
                    "citations": 0,
                    "paper_type": paper_type,
                    "domain": domain,
                    "domain_label": config["label"],
                    "source_api": "arxiv",
                    "fetched": datetime.now().isoformat(),
                    "doi": "",
                    "openalex_id": "",
                    "semantic_scholar_id": "",
                    "arxiv_id": paper.entry_id,
                    "url": paper.entry_id,
                    "categories": ", ".join(paper.categories),
                }

                fpath = store.save_paper(paper_data, abstract, dry_run)
                if fpath is None:
                    continue

                results.append({
                    "title": title,
                    "paper_type": paper_type,
                    "citations": 0,
                    "domain": domain,
                    "file": fpath,
                    "source_api": "arxiv",
                })
    except Exception as e:
        print("    arXiv error [%s]: %s" % (domain, e))

    return results


# ============================================================
# RSS取得
# ============================================================
def fetch_rss(since, store, dry_run=False):
    # type: (str, PaperStore, bool) -> List[Dict]
    """Fetch latest articles from RSS feeds."""
    try:
        import feedparser
        import trafilatura
    except ImportError:
        print("    feedparser/trafilatura not installed, skipping RSS")
        return []

    feeds = [
        ("https://lilianweng.github.io/index.xml", "Lilian Weng"),
        ("https://magazine.sebastianraschka.com/feed", "Sebastian Raschka"),
        ("https://huyenchip.com/feed.xml", "Chip Huyen"),
        ("https://eugeneyan.com/feed.xml", "Eugene Yan"),
        ("https://blog.google/technology/ai/rss/", "Google AI Blog"),
        ("https://openai.com/blog/rss.xml", "OpenAI Blog"),
    ]

    results = []
    for feed_url, author in feeds:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:3]:
                title = entry.get("title", "")
                url = entry.get("link", "")
                published = entry.get("published", "")

                if store.is_duplicate(title):
                    continue

                if dry_run:
                    results.append({"type": "article", "title": title, "author": author})
                    continue

                time.sleep(1)
                downloaded = trafilatura.fetch_url(url)
                if not downloaded:
                    continue
                text = trafilatura.extract(
                    downloaded, output_format="txt", include_links=True
                )
                if not text:
                    continue

                slug = slugify(title)
                filepath = os.path.join(store.raw_articles, "%s.md" % slug)
                if os.path.exists(filepath):
                    continue

                os.makedirs(store.raw_articles, exist_ok=True)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(
                        '---\ntitle: "%s"\nauthors: "%s"\n'
                        'url: "%s"\npublished: "%s"\n'
                        'fetched: "%s"\nsource_type: "rss_article"\n---\n\n'
                        "# %s\n\n%s\n"
                        % (title, author, url, published,
                           datetime.now().isoformat(), title, text)
                    )

                results.append({
                    "type": "article",
                    "title": title,
                    "authors": author,
                    "file": "articles/%s.md" % slug,
                })
        except Exception as e:
            print("    RSS error [%s]: %s" % (author, e))

    return results


# ============================================================
# メイン
# ============================================================
def run_watch(args):
    """Entry point called from fetch.py CLI."""
    store = PaperStore(BASE)
    rl = RateLimiter(
        domain_intervals={"api.openalex.org": 0.2},
        default_interval=1.5,
    )
    oa = OpenAlexClient(rl)

    state = load_state()
    since = args.since or state.get(
        "last_fetch_date",
        (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
    )

    print("=" * 60)
    print("watch — %s" % datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("対象: %s | since: %s | dry_run: %s" % (
        args.domain or "全分野", since, args.dry_run))
    print("既存: %d 件" % len(store.load_existing_hashes()))
    print("=" * 60)

    if args.domain:
        if args.domain not in DOMAINS:
            print("不明な分野: %s" % args.domain)
            print("利用可能: %s" % ", ".join(DOMAINS.keys()))
            return
        targets = {args.domain: DOMAINS[args.domain]}
    else:
        targets = DOMAINS

    all_new = []  # type: List[Dict]

    for dk, dc in targets.items():
        print("\n[%s] (%s)" % (dc["label"], dk))

        # OpenAlex
        for query in dc.get("search_queries", []):
            papers = oa.search(query, since=since, per_page=3)
            for work in papers:
                paper_data = oa.extract_paper_data(work, dk, dc["label"])
                abstract = paper_data.pop("abstract", "")
                fpath = store.save_paper(paper_data, abstract, args.dry_run)
                if fpath is None:
                    continue
                idx = build_index_entry(paper_data, fpath)
                all_new.append(idx)
                print("  + [OA:%s] %s..." % (
                    paper_data["paper_type"][:2].upper(),
                    paper_data["title"][:55]))

        # arXiv
        ax = fetch_arxiv(dk, dc, since, store, args.dry_run)
        for r in ax:
            idx = build_index_entry(r, r["file"])
            all_new.append(idx)
            print("  + [arXiv] %s..." % r["title"][:55])

        if not all_new:
            print("  (新着なし)")

    # RSS
    if not getattr(args, "no_rss", False):
        print("\n[RSS記事]")
        rss = fetch_rss(since, store, args.dry_run)
        for r in rss:
            if "file" in r:
                idx = build_index_entry(r, r["file"])
                all_new.append(idx)
            print("  + %s..." % r["title"][:55])

    # Index 追記
    if not args.dry_run and all_new:
        store.append_to_index(all_new)

    # 状態保存
    if not args.dry_run:
        state["last_fetch_date"] = datetime.now().strftime("%Y-%m-%d")
        state["last_fetch_count"] = len(all_new)
        state["last_fetch_time"] = datetime.now().isoformat()
        save_state(state)

    # サマリー
    print("\n" + "=" * 60)
    print("新規取得: %d 件" % len(all_new))
    by_domain = {}  # type: Dict[str, int]
    for e in all_new:
        d = e.get("domain", "rss")
        by_domain[d] = by_domain.get(d, 0) + 1
    for d, c in sorted(by_domain.items()):
        print("  %s: %d" % (d, c))
    print("=" * 60)
