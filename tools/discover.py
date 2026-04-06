#!/usr/bin/env python3
"""Discover candidate papers from Semantic Scholar across 15 research domains.

Usage:
    python tools/discover.py [--dry-run] [--domain DOMAIN] [--limit N]

Reads  : config/sources.yaml  (15 domains × query lists)
Writes : raw/papers/<domain>/<slug>.md  (Markdown per paper)
         raw/index.jsonl                (append-only index)
"""

import argparse
import os
import sys
from datetime import datetime

import yaml

# Allow running from repo root or tools/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from lib.rate_limiter import RateLimiter
from lib.semantic_scholar import SemanticScholarClient
from lib.storage import PaperStore
from lib.schema import build_index_entry


def load_config(path):
    # type: (str) -> dict
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def discover(config_path, base_dir, target_domain=None, limit=20, dry_run=False):
    # type: (str, str, object, int, bool) -> None
    config = load_config(config_path)
    domains = config.get("research_domains", {})

    rl = RateLimiter(
        domain_intervals={"api.semanticscholar.org": 1.0},
        default_interval=1.5,
    )
    s2 = SemanticScholarClient(rl)
    store = PaperStore(base_dir)

    os.makedirs(os.path.join(base_dir, "raw", "papers"), exist_ok=True)

    total_saved = 0
    total_skipped = 0

    for domain_key, domain_cfg in domains.items():
        if target_domain and domain_key != target_domain:
            continue

        label = domain_cfg.get("label", domain_key)
        min_citations = domain_cfg.get("min_citations", 50)
        queries_cfg = domain_cfg.get("semantic_scholar_queries", {})

        # Collect all queries for this domain
        all_queries = []  # type: list
        for qtype, qlist in queries_cfg.items():
            if isinstance(qlist, list):
                for q in qlist:
                    all_queries.append((qtype, q))

        print("\n[%s] %s — %d queries, min_citations=%d" % (
            domain_key, label, len(all_queries), min_citations
        ))

        domain_saved = 0
        domain_skipped = 0
        new_entries = []

        for qtype, query in all_queries:
            print("  %-22s | %s" % (qtype, query[:60]))
            papers = s2.search(query, limit=limit, min_citations=min_citations)

            for paper in papers:
                title = paper.get("title", "")
                if not title:
                    continue

                if store.is_duplicate(title):
                    domain_skipped += 1
                    continue

                paper_data = dict(paper)
                paper_data["domain"] = domain_key
                paper_data["domain_label"] = label
                paper_data["source_api"] = "semantic_scholar"
                paper_data["fetched"] = datetime.now().isoformat()
                paper_data["semantic_scholar_id"] = paper.get("s2_id", "")
                # Normalize author list to string
                authors = paper.get("authors", [])
                if isinstance(authors, list):
                    paper_data["authors"] = ", ".join(authors[:5])
                    if len(authors) > 5:
                        paper_data["authors"] += " et al."

                abstract = paper.get("abstract", "")

                rel_path = store.save_paper(paper_data, abstract=abstract, dry_run=dry_run)
                if rel_path:
                    entry = build_index_entry(paper_data, rel_path)
                    new_entries.append(entry)
                    domain_saved += 1
                    print("    + (%4d cit) %s" % (paper.get("citations", 0), title[:70]))
                else:
                    domain_skipped += 1

        if not dry_run and new_entries:
            store.append_to_index(new_entries)

        total_saved += domain_saved
        total_skipped += domain_skipped
        print("  => saved=%d skipped=%d" % (domain_saved, domain_skipped))

    print("\n=== Discovery complete: saved=%d skipped=%d ===" % (total_saved, total_skipped))


def main():
    # type: () -> None
    parser = argparse.ArgumentParser(description="Discover papers from Semantic Scholar")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files")
    parser.add_argument("--domain", default=None, help="Run only this domain key")
    parser.add_argument("--limit", type=int, default=20, help="Max papers per query (default: 20)")
    parser.add_argument(
        "--config", default=os.path.join(os.path.dirname(__file__), "..", "config", "sources.yaml"),
        help="Path to sources.yaml"
    )
    parser.add_argument(
        "--base-dir", default=os.path.join(os.path.dirname(__file__), ".."),
        help="Repository root directory"
    )
    args = parser.parse_args()

    discover(
        config_path=os.path.abspath(args.config),
        base_dir=os.path.abspath(args.base_dir),
        target_domain=args.domain,
        limit=args.limit,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
