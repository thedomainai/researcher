"""
全分野並列論文取得スクリプト
sources.yaml の research_domains から Semantic Scholar API で
システマティックレビュー / メタアナリシス / 高被引用論文を取得し
raw/papers/ に分野別サブディレクトリで格納する
"""
import json
import os
import re
import time
import hashlib
import yaml

try:
    import httpx
except ImportError:
    print("httpx が必要です: pip3 install --user httpx")
    exit(1)

BASE = "/Users/yuta/workspace/projects/researcher"
RAW_PAPERS = os.path.join(BASE, "raw", "papers")
CONFIG_PATH = os.path.join(BASE, "config", "sources.yaml")

# Semantic Scholar API
S2_BASE = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,abstract,year,citationCount,influentialCitationCount,authors,url,externalIds,publicationTypes"

# レート制限
S2_INTERVAL = 1.2  # Semantic Scholar: ~1 req/sec

def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[\s]+', '-', text).strip('-')[:80]

def detect_paper_type(title, abstract):
    """論文タイプを検出"""
    title_lower = (title or "").lower()
    abstract_lower = (abstract or "").lower()

    sr_title = ["systematic review", "scoping review", "literature review", "survey"]
    sr_abstract = ["prisma", "systematic search", "inclusion criteria", "excluded studies"]
    ma_title = ["meta-analysis", "meta analysis", "quantitative synthesis"]
    ma_abstract = ["effect size", "pooled estimate", "heterogeneity", "forest plot", "random effects"]

    if any(k in title_lower for k in ma_title) or any(k in abstract_lower for k in ma_abstract):
        return "meta_analysis"
    if any(k in title_lower for k in sr_title) or any(k in abstract_lower for k in sr_abstract):
        return "systematic_review"
    return "primary"

def search_s2(query, limit=5):
    """Semantic Scholar 検索"""
    try:
        resp = httpx.get(
            f"{S2_BASE}/paper/search",
            params={"query": query, "limit": limit, "fields": S2_FIELDS},
            timeout=30,
        )
        if resp.status_code == 200:
            data = resp.json()
            return data.get("data", [])
        else:
            print(f"      S2 API {resp.status_code}: {query[:50]}")
            return []
    except Exception as e:
        print(f"      S2 エラー: {e}")
        return []

def tier_estimate(paper, min_citations):
    """簡易Tier推定（LLMなしのヒューリスティック）"""
    citations = paper.get("citationCount", 0) or 0
    influential = paper.get("influentialCitationCount", 0) or 0
    paper_type = detect_paper_type(paper.get("title", ""), paper.get("abstract", ""))

    # メタアナリシス・システマティックレビューは高優先
    if paper_type in ("meta_analysis", "systematic_review"):
        return 1
    # 高被引用 + 理論的（influential比率が高い）
    if citations >= min_citations and influential >= 10:
        return 1
    if citations >= min_citations * 0.5:
        return 2
    return 3

def save_paper(paper, domain_slug, domain_label):
    """論文をMarkdownとして保存"""
    title = (paper.get("title") or "untitled").replace("\n", " ")
    abstract = paper.get("abstract", "") or ""
    authors_list = paper.get("authors", []) or []
    authors = ", ".join(a.get("name", "") for a in authors_list[:5])
    if len(authors_list) > 5:
        authors += f" (+{len(authors_list)-5}名)"
    year = paper.get("year", "")
    citations = paper.get("citationCount", 0) or 0
    influential = paper.get("influentialCitationCount", 0) or 0
    url = paper.get("url", "")
    paper_id = paper.get("paperId", "")
    ext_ids = paper.get("externalIds", {}) or {}
    arxiv_id = ext_ids.get("ArXiv", "")
    doi = ext_ids.get("DOI", "")
    paper_type = detect_paper_type(title, abstract)
    tier = tier_estimate(paper, 100)

    slug = slugify(title)
    domain_dir = os.path.join(RAW_PAPERS, domain_slug)
    os.makedirs(domain_dir, exist_ok=True)
    filepath = os.path.join(domain_dir, f"{slug}.md")

    md = f"""---
title: "{title}"
authors: "{authors}"
year: {year}
citations: {citations}
influential_citations: {influential}
paper_type: "{paper_type}"
tier: {tier}
domain: "{domain_slug}"
domain_label: "{domain_label}"
semantic_scholar_id: "{paper_id}"
arxiv_id: "{arxiv_id}"
doi: "{doi}"
url: "{url}"
---

# {title}

**著者**: {authors}
**年**: {year} | **被引用数**: {citations} | **影響力のある引用**: {influential}
**タイプ**: {paper_type} | **Tier**: {tier}
**分野**: {domain_label}

## Abstract

{abstract}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    return {
        "id": hashlib.md5(paper_id.encode()).hexdigest()[:12] if paper_id else slug[:12],
        "type": "paper",
        "paper_type": paper_type,
        "tier": tier,
        "title": title,
        "authors": authors,
        "year": year,
        "citations": citations,
        "domain": domain_slug,
        "file": f"papers/{domain_slug}/{slug}.md",
        "url": url,
    }


# ==========================================================================
# メイン処理
# ==========================================================================
def main():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    domains = config.get("research_domains", {})
    cross_cutting = config.get("cross_cutting_themes", {})

    # 全分野 + 横断テーマを統合
    all_sources = {}
    for key, val in domains.items():
        all_sources[key] = val
    for key, val in cross_cutting.items():
        all_sources[key] = val

    all_index = []
    stats = {"total": 0, "tier1": 0, "tier2": 0, "tier3": 0,
             "systematic_review": 0, "meta_analysis": 0, "primary": 0}

    print("=" * 70)
    print("全分野並列論文取得")
    print(f"対象分野数: {len(all_sources)}")
    print("=" * 70)

    for domain_key, domain_conf in all_sources.items():
        label = domain_conf.get("label", domain_key)
        queries = domain_conf.get("semantic_scholar_queries", {})
        min_cit = domain_conf.get("min_citations", 100)
        priority = domain_conf.get("priority", "medium")

        print(f"\n{'─' * 50}")
        print(f"[{label}] (priority: {priority})")
        print(f"{'─' * 50}")

        domain_papers = set()  # 重複排除

        # システマティックレビュー / メタアナリシス
        for q in queries.get("systematic_reviews", []):
            time.sleep(S2_INTERVAL)
            papers = search_s2(q, limit=3)
            for p in papers:
                pid = p.get("paperId", "")
                if pid in domain_papers:
                    continue
                domain_papers.add(pid)
                entry = save_paper(p, domain_key, label)
                all_index.append(entry)
                stats["total"] += 1
                stats[f"tier{entry['tier']}"] += 1
                stats[entry["paper_type"]] += 1
                tier_mark = "★" if entry["tier"] == 1 else "◇" if entry["tier"] == 2 else "·"
                type_mark = {"systematic_review": "SR", "meta_analysis": "MA", "primary": "P"}
                print(f"  {tier_mark} [{type_mark.get(entry['paper_type'], '?')}] {entry['title'][:60]}... (cited:{entry['citations']})")

        # Seminal papers
        for q in queries.get("seminal", []):
            time.sleep(S2_INTERVAL)
            papers = search_s2(q, limit=2)
            for p in papers:
                pid = p.get("paperId", "")
                if pid in domain_papers:
                    continue
                citations = p.get("citationCount", 0) or 0
                if citations < min_cit * 0.3:
                    continue
                domain_papers.add(pid)
                entry = save_paper(p, domain_key, label)
                all_index.append(entry)
                stats["total"] += 1
                stats[f"tier{entry['tier']}"] += 1
                stats[entry["paper_type"]] += 1
                tier_mark = "★" if entry["tier"] == 1 else "◇" if entry["tier"] == 2 else "·"
                print(f"  {tier_mark} [Seminal] {entry['title'][:60]}... (cited:{entry['citations']})")

        print(f"  → {len(domain_papers)}件取得")

    # インデックス保存（既存に追記）
    index_path = os.path.join(BASE, "raw", "index.jsonl")
    with open(index_path, "a", encoding="utf-8") as f:
        for entry in all_index:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    # サマリー
    print("\n" + "=" * 70)
    print("取得完了サマリー")
    print("=" * 70)
    print(f"  総論文数:              {stats['total']}")
    print(f"  Tier 1（不変原理）:     {stats['tier1']}")
    print(f"  Tier 2（消滅制約分析）: {stats['tier2']}")
    print(f"  Tier 3（スキップ候補）: {stats['tier3']}")
    print(f"  ─────────────────────")
    print(f"  システマティックレビュー: {stats['systematic_review']}")
    print(f"  メタアナリシス:           {stats['meta_analysis']}")
    print(f"  プライマリ研究:           {stats['primary']}")

if __name__ == "__main__":
    main()
