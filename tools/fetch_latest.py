#!/usr/bin/env python3
"""
fetch_latest.py — 17分野の最新論文を継続的に取得するモジュール

設計思想:
  - cronで定期実行される（推奨: 1日1回）
  - 前回取得日以降の新着論文のみを取得
  - OpenAlex API（全分野、レート緩い）+ arXiv API（CS系補完）
  - 取得した論文はraw/papers/{domain}/に保存、index.jsonlに追記
  - 重複排除はタイトルハッシュ

使い方:
  python3 tools/fetch_latest.py                        # 全分野の最新を取得
  python3 tools/fetch_latest.py --domain neuroscience  # 特定分野のみ
  python3 tools/fetch_latest.py --since 2026-04-01     # 日付指定
  python3 tools/fetch_latest.py --dry-run              # 取得せず確認のみ

cronの設定例:
  0 6 * * * cd /Users/yuta/workspace/projects/researcher && /usr/bin/python3 tools/fetch_latest.py >> logs/fetch.log 2>&1
"""

import argparse
import atexit
import fcntl
import json
import os
import re
import time
import hashlib
from datetime import datetime, timedelta

import httpx
import feedparser

# ============================================================
# パス設定
# ============================================================
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PAPERS = os.path.join(BASE, "raw", "papers")
RAW_ARTICLES = os.path.join(BASE, "raw", "articles")
INDEX_PATH = os.path.join(BASE, "raw", "index.jsonl")
STATE_PATH = os.path.join(BASE, "config", "fetch_state.json")
LOG_DIR = os.path.join(BASE, "logs")
LOCK_PATH = os.path.join(LOG_DIR, "fetch_latest.lock")
os.makedirs(LOG_DIR, exist_ok=True)

OA_BASE = "https://api.openalex.org/works"
OA_MAILTO = "researcher-bot@example.com"

# ============================================================
# 分野定義
# ============================================================
# 設計: 各分野のキーワードは「AI×その分野」の交差点を狙う。
# OpenAlexではキーワード自体が検索クエリになるので、
# キーワードにAI/技術の文脈を含めることでノイズを防ぐ。
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
# ユーティリティ
# ============================================================
def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[\s]+', '-', text).strip('-')[:80]


def title_hash(title):
    normalized = re.sub(r'[^a-z0-9]', '', title.lower())
    return hashlib.md5(normalized.encode()).hexdigest()[:16]


def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def load_existing_hashes():
    hashes = set()
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH) as f:
            for line in f:
                if line.strip():
                    entry = json.loads(line)
                    t = entry.get("title", "")
                    if t:
                        hashes.add(title_hash(t))
    return hashes


def inv_index_to_text(inv):
    if not inv:
        return ""
    wp = []
    for word, positions in inv.items():
        for pos in positions:
            wp.append((pos, word))
    wp.sort()
    return " ".join(w for _, w in wp)


def detect_paper_type(title, abstract):
    tl = (title or "").lower()
    al = (abstract or "").lower()
    if any(k in tl for k in ["meta-analysis", "meta analysis"]) or \
       any(k in al for k in ["effect size", "pooled estimate", "heterogeneity"]):
        return "meta_analysis"
    if any(k in tl for k in ["systematic review", "scoping review"]) or \
       any(k in al for k in ["prisma", "systematic search", "inclusion criteria"]):
        return "systematic_review"
    return "primary"


def save_paper_md(title, authors, year, citations, abstract,
                  paper_type, domain, domain_label, extra_meta, dry_run):
    """論文をMarkdownとして保存。成功したらファイルパスを返す。"""
    if dry_run:
        return "dry-run"
    slug = slugify(title)
    domain_dir = os.path.join(RAW_PAPERS, domain)
    os.makedirs(domain_dir, exist_ok=True)
    filepath = os.path.join(domain_dir, f"{slug}.md")
    if os.path.exists(filepath):
        return None  # 重複

    meta_lines = "\n".join(f'{k}: "{v}"' for k, v in extra_meta.items())
    md = f"""---
title: "{title}"
authors: "{authors}"
year: {year}
citations: {citations}
paper_type: "{paper_type}"
domain: "{domain}"
fetched: "{datetime.now().isoformat()}"
{meta_lines}
---

# {title}

**著者**: {authors}
**年**: {year} | **被引用数**: {citations}
**タイプ**: {paper_type} | **分野**: {domain_label}

## Abstract

{abstract}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)
    return f"papers/{domain}/{slug}.md"


# ============================================================
# OpenAlex取得
# ============================================================
def fetch_openalex(domain, config, since, existing_hashes, dry_run=False):
    """OpenAlex APIで最新論文を取得。
    
    キーワード自体に「AI×分野」の文脈を含めているので、
    追加のis_relevantフィルタは不要。
    OpenAlexの検索エンジンが関連性でランキングしてくれる。
    """
    results = []
    queries = config.get("search_queries", [])

    for query in queries:
        try:
            params = {
                "search": query,
                "filter": f"from_publication_date:{since}",
                "sort": "relevance_score:desc",
                "per_page": 3,
                "mailto": OA_MAILTO,
            }
            time.sleep(0.2)
            r = httpx.get(OA_BASE, params=params, timeout=30)
            if r.status_code != 200:
                continue

            for work in r.json().get("results", []):
                title = (work.get("title") or "").replace("\n", " ")
                if not title:
                    continue

                th = title_hash(title)
                if th in existing_hashes:
                    continue

                abstract = inv_index_to_text(work.get("abstract_inverted_index"))
                year = work.get("publication_year", "")
                citations = work.get("cited_by_count", 0)
                doi = work.get("doi", "")
                oa_id = work.get("id", "")
                authorships = work.get("authorships", []) or []
                authors = ", ".join(
                    a.get("author", {}).get("display_name", "")
                    for a in authorships[:5]
                )
                paper_type = detect_paper_type(title, abstract)

                fpath = save_paper_md(
                    title, authors, year, citations, abstract,
                    paper_type, domain, config["label"],
                    {"doi": doi or "", "openalex_id": oa_id, "source_api": "openalex"},
                    dry_run,
                )
                if fpath is None:
                    continue

                existing_hashes.add(th)
                results.append({
                    "title": title, "paper_type": paper_type,
                    "citations": citations, "domain": domain,
                    "file": fpath, "source_api": "openalex",
                })
        except Exception as e:
            print(f"    OA error [{query[:30]}]: {e}")

    return results


# ============================================================
# arXiv取得
# ============================================================
def fetch_arxiv(domain, config, since, existing_hashes, dry_run=False):
    """arXiv APIで最新論文を取得。カテゴリ+キーワードで検索。"""
    arxiv_queries = config.get("arxiv_queries", [])
    if not arxiv_queries:
        return []

    results = []
    try:
        import arxiv as arxiv_lib
        client = arxiv_lib.Client()

        seen_ids = set()
        for category, keyword in arxiv_queries:
            query = f"cat:{category} AND all:{keyword}"
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
                th = title_hash(title)
                if th in existing_hashes:
                    continue

                pub_date = paper.published.strftime("%Y-%m-%d")
                if pub_date < since:
                    continue

                abstract = paper.summary or ""
                authors = ", ".join(a.name for a in paper.authors[:5])
                paper_type = detect_paper_type(title, abstract)

                fpath = save_paper_md(
                    title, authors, paper.published.year, 0, abstract,
                    paper_type, domain, config["label"],
                    {"arxiv_id": paper.entry_id, "source_api": "arxiv",
                     "categories": ", ".join(paper.categories)},
                    dry_run,
                )
                if fpath is None:
                    continue

                existing_hashes.add(th)
                results.append({
                    "title": title, "paper_type": paper_type,
                    "citations": 0, "domain": domain,
                    "file": fpath, "source_api": "arxiv",
                })
    except Exception as e:
        print(f"    arXiv error [{domain}]: {e}")

    return results


# ============================================================
# RSS取得
# ============================================================
def fetch_rss(since, existing_hashes, dry_run=False):
    """RSSフィードから最新記事を取得。"""
    try:
        import trafilatura
    except ImportError:
        print("    trafilatura not installed, skipping RSS")
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

                th = title_hash(title)
                if th in existing_hashes:
                    continue

                if dry_run:
                    existing_hashes.add(th)
                    results.append({"type": "article", "title": title, "author": author})
                    continue

                time.sleep(1)
                downloaded = trafilatura.fetch_url(url)
                if not downloaded:
                    continue
                text = trafilatura.extract(downloaded, output_format="txt",
                                           include_links=True)
                if not text:
                    continue

                slug = slugify(title)
                filepath = os.path.join(RAW_ARTICLES, f"{slug}.md")
                if os.path.exists(filepath):
                    continue

                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f'---\ntitle: "{title}"\nauthor: "{author}"\n'
                            f'url: "{url}"\npublished: "{published}"\n'
                            f'fetched: "{datetime.now().isoformat()}"\n'
                            f'source_type: "rss_article"\n---\n\n# {title}\n\n{text}\n')

                existing_hashes.add(th)
                results.append({
                    "type": "article", "title": title, "author": author,
                    "file": f"articles/{slug}.md",
                })
        except Exception as e:
            print(f"    RSS error [{author}]: {e}")

    return results


# ============================================================
# 実行ロック
# ============================================================
def acquire_run_lock():
    lock_file = open(LOCK_PATH, "a+", encoding="utf-8")
    try:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        lock_file.close()
        return None

    lock_file.seek(0)
    lock_file.truncate()
    lock_file.write(f"{os.getpid()}\n")
    lock_file.flush()

    def _release():
        try:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
        finally:
            lock_file.close()

    atexit.register(_release)
    return lock_file


# ============================================================
# メイン
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="最新論文を継続的に取得")
    parser.add_argument("--domain", help="特定分野のみ取得")
    parser.add_argument("--since", help="取得開始日 (YYYY-MM-DD)")
    parser.add_argument("--dry-run", action="store_true", help="取得せず確認のみ")
    parser.add_argument("--no-rss", action="store_true", help="RSS取得をスキップ")
    args = parser.parse_args()

    lock = acquire_run_lock()
    if lock is None:
        print(f"fetch_latest.py — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("別の fetch_latest.py が実行中のためスキップします。")
        return

    state = load_state()
    since = args.since or state.get(
        "last_fetch_date",
        (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
    )
    existing_hashes = load_existing_hashes()

    print("=" * 60)
    print(f"fetch_latest.py — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"対象: {args.domain or '全分野'} | since: {since}")
    print(f"既存: {len(existing_hashes)} | dry_run: {args.dry_run}")
    print("=" * 60)

    if args.domain:
        if args.domain not in DOMAINS:
            print(f"不明: {args.domain}. 利用可能: {', '.join(DOMAINS.keys())}")
            return
        targets = {args.domain: DOMAINS[args.domain]}
    else:
        targets = DOMAINS

    all_new = []

    for dk, dc in targets.items():
        print(f"\n[{dc['label']}] ({dk})")

        oa = fetch_openalex(dk, dc, since, existing_hashes, args.dry_run)
        for r in oa:
            print(f"  + [OA:{r['paper_type'][:2].upper()}] {r['title'][:55]}...")
        all_new.extend(oa)

        ax = fetch_arxiv(dk, dc, since, existing_hashes, args.dry_run)
        for r in ax:
            print(f"  + [arXiv] {r['title'][:55]}...")
        all_new.extend(ax)

        if not oa and not ax:
            print("  (新着なし)")

    if not args.no_rss:
        print(f"\n[RSS記事]")
        rss = fetch_rss(since, existing_hashes, args.dry_run)
        for r in rss:
            print(f"  + {r['title'][:55]}...")
        all_new.extend(rss)

    if not args.dry_run and all_new:
        with open(INDEX_PATH, "a", encoding="utf-8") as f:
            for entry in all_new:
                idx = {k: v for k, v in entry.items() if k != "abstract"}
                idx["type"] = idx.get("type", "paper")
                f.write(json.dumps(idx, ensure_ascii=False) + "\n")

    if not args.dry_run:
        state["last_fetch_date"] = datetime.now().strftime("%Y-%m-%d")
        state["last_fetch_count"] = len(all_new)
        state["last_fetch_time"] = datetime.now().isoformat()
        save_state(state)

    print("\n" + "=" * 60)
    print(f"新規取得: {len(all_new)}件")
    by_domain = {}
    for e in all_new:
        d = e.get("domain", "rss")
        by_domain[d] = by_domain.get(d, 0) + 1
    for d, c in sorted(by_domain.items()):
        print(f"  {d}: {c}")
    print("=" * 60)


if __name__ == "__main__":
    main()
