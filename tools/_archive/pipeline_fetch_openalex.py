"""
OpenAlex APIを使った全分野網羅取得スクリプト
Semantic Scholar のレート制限を回避し、不足分野を補完する
また既存分野で取得が不十分なものも補強する
"""
import json
import os
import re
import time
import hashlib
import httpx

BASE = "/Users/yuta/workspace/projects/researcher"
RAW_PAPERS = os.path.join(BASE, "raw", "papers")
OA_BASE = "https://api.openalex.org/works"
POLITE_EMAIL = "researcher-bot@example.com"  # polite pool

def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[\s]+', '-', text).strip('-')[:80]

def detect_paper_type(title, abstract):
    tl = (title or "").lower()
    al = (abstract or "").lower()
    ma_kw = ["meta-analysis", "meta analysis", "quantitative synthesis", "effect size",
             "pooled estimate", "heterogeneity", "forest plot", "random effects"]
    sr_kw = ["systematic review", "scoping review", "prisma", "systematic search",
             "inclusion criteria", "literature review"]
    if any(k in tl for k in ma_kw[:3]) or sum(1 for k in ma_kw if k in al) >= 2:
        return "meta_analysis"
    if any(k in tl for k in sr_kw[:3]) or sum(1 for k in sr_kw if k in al) >= 2:
        return "systematic_review"
    return "primary"

def tier_estimate(citations, paper_type, min_cit):
    if paper_type in ("meta_analysis", "systematic_review"):
        return 1
    if citations >= min_cit:
        return 1
    if citations >= min_cit * 0.3:
        return 2
    return 3

def search_openalex(query, per_page=5, sort="cited_by_count:desc"):
    """OpenAlex検索（polite pool使用）"""
    try:
        params = {
            "search": query,
            "per_page": per_page,
            "sort": sort,
            "mailto": POLITE_EMAIL,
        }
        r = httpx.get(OA_BASE, params=params, timeout=30)
        if r.status_code == 200:
            return r.json().get("results", [])
        else:
            print(f"      OpenAlex {r.status_code}: {query[:50]}")
            return []
    except Exception as e:
        print(f"      Error: {e}")
        return []

def extract_abstract(work):
    """OpenAlexのinverted_indexからアブストラクトを復元"""
    inv = work.get("abstract_inverted_index")
    if not inv:
        return ""
    # {word: [positions]} -> テキスト復元
    word_positions = []
    for word, positions in inv.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(w for _, w in word_positions)

def save_paper(work, domain_slug, domain_label, min_cit):
    """論文をMarkdownとして保存"""
    title = (work.get("title") or "untitled").replace("\n", " ")
    abstract = extract_abstract(work)
    year = work.get("publication_year", "")
    citations = work.get("cited_by_count", 0)
    doi = work.get("doi", "")
    oa_id = work.get("id", "")
    url = work.get("doi") or oa_id

    authorships = work.get("authorships", [])
    authors = ", ".join(
        a.get("author", {}).get("display_name", "")
        for a in authorships[:5]
    )
    if len(authorships) > 5:
        authors += f" (+{len(authorships)-5})"

    paper_type = detect_paper_type(title, abstract)
    tier = tier_estimate(citations, paper_type, min_cit)

    slug = slugify(title)
    domain_dir = os.path.join(RAW_PAPERS, domain_slug)
    os.makedirs(domain_dir, exist_ok=True)
    filepath = os.path.join(domain_dir, f"{slug}.md")

    # 重複チェック
    if os.path.exists(filepath):
        return None

    md = f"""---
title: "{title}"
authors: "{authors}"
year: {year}
citations: {citations}
paper_type: "{paper_type}"
tier: {tier}
domain: "{domain_slug}"
domain_label: "{domain_label}"
doi: "{doi or ''}"
openalex_id: "{oa_id}"
---

# {title}

**著者**: {authors}
**年**: {year} | **被引用数**: {citations}
**タイプ**: {paper_type} | **Tier**: {tier}
**分野**: {domain_label}

## Abstract

{abstract}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    return {
        "title": title,
        "paper_type": paper_type,
        "tier": tier,
        "citations": citations,
        "domain": domain_slug,
        "file": f"papers/{domain_slug}/{slug}.md",
    }

# ====================================================================
# 全分野クエリ定義
# ====================================================================
# 不足分野（5つ）+ 既存分野の補強
ALL_QUERIES = {
    # === 不足分野（完全に未取得）===
    "philosophy": {
        "label": "哲学",
        "min_cit": 100,
        "queries": [
            ("philosophy of mind artificial intelligence consciousness", 5),
            ("value alignment AI ethics framework", 5),
            ("artificial moral agency responsibility review", 3),
            ("epistemology artificial intelligence knowledge", 3),
            ("political philosophy artificial intelligence justice", 3),
        ],
    },
    "behavioral_economics": {
        "label": "行動経済学",
        "min_cit": 200,
        "queries": [
            ("prospect theory meta-analysis", 3),
            ("nudge theory choice architecture systematic review", 3),
            ("algorithm aversion trust automation", 5),
            ("bounded rationality decision making", 3),
            ("default effect opt-in opt-out meta-analysis", 3),
            ("information cascade herding behavior review", 3),
        ],
    },
    "organization_science": {
        "label": "組織科学",
        "min_cit": 200,
        "queries": [
            ("dynamic capabilities meta-analysis", 5),
            ("organizational routines systematic review", 3),
            ("ambidexterity exploration exploitation", 5),
            ("team cognition shared mental models systematic review", 3),
            ("knowledge management artificial intelligence", 3),
        ],
    },
    "ai_governance": {
        "label": "AIガバナンス",
        "min_cit": 50,
        "queries": [
            ("AI governance framework systematic review", 5),
            ("algorithmic fairness bias meta-analysis", 5),
            ("responsible AI principles systematic review", 3),
            ("AI safety alignment review", 3),
            ("AI regulation policy review", 3),
        ],
    },
    # === 既存分野の補強 ===
    "complexity_science": {
        "label": "複雑系科学",
        "min_cit": 150,
        "queries": [
            ("complex adaptive systems review", 5),
            ("emergence self-organization systematic review", 3),
            ("cybernetics requisite variety", 3),
            ("systems thinking leverage points Meadows", 3),
        ],
    },
    "economics": {
        "label": "経済学",
        "min_cit": 200,
        "queries": [
            ("task-based framework automation labor Autor", 3),
            ("general purpose technology economic growth", 3),
            ("AI labor market impact review", 5),
            ("platform economics two-sided markets review", 3),
        ],
    },
    "sociology": {
        "label": "社会学",
        "min_cit": 200,
        "queries": [
            ("institutional theory systematic review", 3),
            ("actor-network theory technology review", 3),
            ("trust social systems Luhmann", 3),
            ("network society information technology Castells", 3),
        ],
    },
    "law": {
        "label": "法学",
        "min_cit": 50,
        "queries": [
            ("AI legal personhood artificial intelligence law", 5),
            ("algorithmic accountability transparency law review", 5),
            ("AI liability tort law autonomous systems", 3),
            ("intellectual property AI generated content", 3),
        ],
    },
    "cognitive_science": {
        "label": "認知科学",
        "min_cit": 200,
        "queries": [
            ("dual process theory systematic review", 3),
            ("distributed cognition review", 3),
            ("metacognition calibration systematic review", 3),
            ("cognitive bias decision making meta-analysis", 5),
        ],
    },
    "psychology": {
        "label": "心理学",
        "min_cit": 200,
        "queries": [
            ("flow theory optimal experience meta-analysis", 3),
            ("trust in automation meta-analysis", 5),
            ("automation complacency systematic review", 3),
            ("creativity AI collaboration", 3),
        ],
    },
    "evolutionary_biology": {
        "label": "進化生物学・文化進化",
        "min_cit": 100,
        "queries": [
            ("cultural evolution systematic review", 3),
            ("gene-culture coevolution review", 3),
            ("niche construction evolution review", 3),
        ],
    },
    "human_ai_collaboration": {
        "label": "人間-AI協働",
        "min_cit": 50,
        "queries": [
            ("human-AI collaboration productivity systematic review", 5),
            ("centaur model AI augmentation", 3),
            ("AI augmented decision making review", 5),
        ],
    },
}

# ====================================================================
# メイン処理
# ====================================================================
def main():
    stats = {"total": 0, "new": 0, "dup": 0, "by_domain": {}, "by_type": {},
             "tier1": 0, "tier2": 0, "tier3": 0}
    all_entries = []

    print("=" * 70)
    print("OpenAlex 全分野論文取得")
    print(f"対象分野数: {len(ALL_QUERIES)}")
    print("=" * 70)

    for domain_key, domain_conf in ALL_QUERIES.items():
        label = domain_conf["label"]
        min_cit = domain_conf["min_cit"]
        queries = domain_conf["queries"]

        print(f"\n{'─' * 50}")
        print(f"[{label}] (min_citations: {min_cit})")
        print(f"{'─' * 50}")

        domain_count = 0
        for query, limit in queries:
            time.sleep(0.3)  # OpenAlex polite pool: 10 req/sec
            results = search_openalex(query, per_page=limit)

            for work in results:
                stats["total"] += 1
                entry = save_paper(work, domain_key, label, min_cit)
                if entry is None:
                    stats["dup"] += 1
                    continue

                stats["new"] += 1
                stats[f"tier{entry['tier']}"] += 1
                stats["by_type"][entry["paper_type"]] = stats["by_type"].get(entry["paper_type"], 0) + 1
                all_entries.append(entry)
                domain_count += 1

                tier_mark = {"1": "★", "2": "◇", "3": "·"}.get(str(entry["tier"]), "?")
                type_mark = {"systematic_review": "SR", "meta_analysis": "MA", "primary": "P"}.get(entry["paper_type"], "?")
                print(f"  {tier_mark} [{type_mark}] {entry['title'][:55]}... (c:{entry['citations']})")

        stats["by_domain"][domain_key] = domain_count
        print(f"  → {domain_count}件 新規保存")

    # インデックスに追記
    index_path = os.path.join(BASE, "raw", "index.jsonl")
    with open(index_path, "a", encoding="utf-8") as f:
        for entry in all_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    # サマリー
    print("\n" + "=" * 70)
    print("取得完了サマリー")
    print("=" * 70)
    print(f"  API応答総数:            {stats['total']}")
    print(f"  新規保存:               {stats['new']}")
    print(f"  重複スキップ:           {stats['dup']}")
    print(f"  ─────────────────────")
    print(f"  Tier 1（不変原理）:      {stats['tier1']}")
    print(f"  Tier 2（消滅制約分析）:  {stats['tier2']}")
    print(f"  Tier 3（候補）:          {stats['tier3']}")
    print(f"  ─────────────────────")
    for pt, c in sorted(stats["by_type"].items()):
        print(f"  {pt}: {c}")
    print(f"  ─────────────────────")
    print(f"  分野別:")
    for dk, c in sorted(stats["by_domain"].items()):
        print(f"    {dk}: {c}")

if __name__ == "__main__":
    main()
