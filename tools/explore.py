#!/usr/bin/env python3
"""
explore.py — 新分野の深探索モジュール

seed論文からBFS引用展開で分野の知識地図を構築する。

使い方:
  python3 tools/fetch.py explore --domain neuroscience
  python3 tools/fetch.py explore --domain neuroscience --depth 2 --limit 300
  python3 tools/fetch.py explore --domain neuroscience --seeds W1234,W5678
  python3 tools/fetch.py explore --domain neuroscience --resume
  python3 tools/fetch.py explore --domain neuroscience --tier
  python3 tools/fetch.py explore --domain neuroscience --dry-run

アルゴリズム:
  1. seed論文を決定（--seeds or sources.yaml のクエリ）
  2. BFS引用展開: seed → 被引用論文 + 参照文献を幅優先でたどる
  3. 各depthでmin_citationsフィルタを適用して発散を防ぐ
  4. (--tier) LLM Tier分類を実行
  5. カバレッジレポートを出力
"""

import json
import os
import sys
from collections import deque
from datetime import datetime
from typing import Dict, List, Optional, Set

import yaml

from lib.rate_limiter import RateLimiter
from lib.openalex import OpenAlexClient
from lib.storage import PaperStore
from lib.schema import build_index_entry
from lib.utils import normalize_openalex_id, tier_estimate

# ============================================================
# パス設定
# ============================================================
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE, "config", "sources.yaml")
EXPLORE_STATE_DIR = os.path.join(BASE, "config")


def load_sources_yaml():
    # type: () -> Dict
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_domain_config(config, domain):
    # type: (Dict, str) -> Optional[Dict]
    """Get domain config from sources.yaml (research_domains or cross_cutting_themes)."""
    domains = config.get("research_domains", {})
    cross = config.get("cross_cutting_themes", {})
    return domains.get(domain) or cross.get(domain)


# ============================================================
# 探索状態の永続化
# ============================================================
def explore_state_path(domain):
    # type: (str) -> str
    return os.path.join(EXPLORE_STATE_DIR, "explore_state_%s.json" % domain)


def load_explore_state(domain):
    # type: (str) -> Dict
    path = explore_state_path(domain)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {"domain": domain, "visited_ids": [], "saved_count": 0}


def save_explore_state(domain, state):
    # type: (str, Dict) -> None
    state["last_explore"] = datetime.now().isoformat()
    with open(explore_state_path(domain), "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


# ============================================================
# seed論文の取得
# ============================================================
def resolve_seeds_from_ids(oa, seed_str):
    # type: (OpenAlexClient, str) -> List[Dict]
    """Resolve seed paper IDs to OpenAlex Work objects."""
    seeds = []
    for sid in seed_str.split(","):
        sid = sid.strip()
        if not sid:
            continue
        work = oa.get_work(sid)
        if work:
            seeds.append(work)
            print("  seed: %s (c:%d)" % (
                (work.get("title") or "?")[:60],
                work.get("cited_by_count", 0)))
        else:
            print("  seed not found: %s" % sid)
    return seeds


def resolve_seeds_from_queries(oa, domain_config):
    # type: (OpenAlexClient, Dict) -> List[Dict]
    """Search for seed papers using sources.yaml queries."""
    seeds = []
    seen_ids = set()  # type: Set[str]
    queries = domain_config.get("semantic_scholar_queries", {})

    # Seminal papers first (most important)
    for q in queries.get("seminal", []):
        results = oa.search(q, per_page=3, sort="cited_by_count:desc")
        for work in results:
            oa_id = normalize_openalex_id(work.get("id", ""))
            if oa_id in seen_ids:
                continue
            seen_ids.add(oa_id)
            seeds.append(work)
            print("  seed [seminal]: %s (c:%d)" % (
                (work.get("title") or "?")[:55],
                work.get("cited_by_count", 0)))

    # Systematic reviews (high-quality evidence)
    for q in queries.get("systematic_reviews", []):
        results = oa.search(q, per_page=2, sort="cited_by_count:desc")
        for work in results:
            oa_id = normalize_openalex_id(work.get("id", ""))
            if oa_id in seen_ids:
                continue
            seen_ids.add(oa_id)
            seeds.append(work)
            print("  seed [SR]: %s (c:%d)" % (
                (work.get("title") or "?")[:55],
                work.get("cited_by_count", 0)))

    return seeds


# ============================================================
# BFS引用展開
# ============================================================
def run_bfs_expansion(oa, store, seeds, domain, domain_label, min_cit,
                      max_depth, limit, dry_run):
    # type: (OpenAlexClient, PaperStore, List[Dict], str, str, int, int, int, bool) -> tuple
    """BFS citation expansion from seed papers.

    Returns (saved_papers, visited_ids, stats).
    """
    queue = deque()  # type: deque
    visited = set()  # type: Set[str]
    saved = []  # type: List[Dict]
    stats = {
        "total_visited": 0,
        "saved": 0,
        "skipped_dup": 0,
        "skipped_low_cit": 0,
        "by_depth": {},
        "by_type": {},
    }  # type: Dict

    # Enqueue seeds at depth 0
    for work in seeds:
        oa_id = normalize_openalex_id(work.get("id", ""))
        if oa_id:
            queue.append((oa_id, 0, work))  # (id, depth, pre-fetched work or None)

    print("\n" + "-" * 50)
    print("BFS 引用展開開始")
    print("  seeds: %d | max_depth: %d | limit: %d | min_cit: %d" % (
        len(seeds), max_depth, limit, min_cit))
    print("-" * 50)

    while queue and len(saved) < limit:
        work_id, depth, prefetched = queue.popleft()

        if work_id in visited:
            continue
        visited.add(work_id)
        stats["total_visited"] += 1

        # Fetch work details (use prefetched if available)
        if prefetched is not None:
            work = prefetched
        else:
            work = oa.get_work(work_id)
            if not work:
                continue

        title = (work.get("title") or "").replace("\n", " ")
        citations = work.get("cited_by_count", 0) or 0

        # Citation threshold by depth
        if depth > 0:
            depth_threshold = min_cit * (0.3 if depth == 1 else 0.5)
            if citations < depth_threshold:
                stats["skipped_low_cit"] += 1
                continue

        # Extract and save
        paper_data = oa.extract_paper_data(work, domain, domain_label)
        abstract = paper_data.pop("abstract", "")
        paper_data["explore_depth"] = depth

        # Heuristic tier
        paper_data["tier"] = tier_estimate(
            citations, 0, paper_data["paper_type"], min_cit)

        fpath = store.save_paper(paper_data, abstract, dry_run)
        if fpath is None:
            stats["skipped_dup"] += 1
        else:
            saved.append({"data": paper_data, "file": fpath})
            stats["saved"] += 1
            depth_key = "depth_%d" % depth
            stats["by_depth"][depth_key] = stats["by_depth"].get(depth_key, 0) + 1
            pt = paper_data["paper_type"]
            stats["by_type"][pt] = stats["by_type"].get(pt, 0) + 1

            tier_mark = {1: "★", 2: "◇", 3: "·"}.get(paper_data.get("tier", 3), "?")
            type_mark = {"systematic_review": "SR", "meta_analysis": "MA"}.get(pt, "P")
            print("  %s [d%d][%s] %s (c:%d)" % (
                tier_mark, depth, type_mark, title[:50], citations))

        # Citation expansion (only if within depth limit)
        if depth < max_depth:
            # Cited-by: papers citing this work (high-citation first)
            cited_by_threshold = int(min_cit * 0.3)
            cited_by_works = oa.get_cited_by(
                work_id, min_citations=cited_by_threshold, per_page=20)
            for cb_work in cited_by_works:
                cb_id = normalize_openalex_id(cb_work.get("id", ""))
                if cb_id and cb_id not in visited:
                    queue.append((cb_id, depth + 1, cb_work))

            # References: papers this work cites
            ref_ids = oa.get_references(work_id)
            for ref_id in ref_ids[:10]:
                if ref_id and ref_id not in visited:
                    queue.append((ref_id, depth + 1, None))

    return saved, visited, stats


# ============================================================
# LLM Tier 分類
# ============================================================
def run_llm_tier_classification(saved_papers, config):
    # type: (List[Dict], Dict) -> None
    """Apply LLM-based tier classification using Claude API."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("\n  ANTHROPIC_API_KEY が未設定のため LLM Tier 分類をスキップ")
        return

    prompt_template = config.get("quality", {}).get("tier_classification_prompt", "")
    if not prompt_template:
        print("\n  tier_classification_prompt が sources.yaml に未定義のためスキップ")
        return

    import httpx
    import time

    print("\n" + "-" * 50)
    print("LLM Tier 分類 (%d 件)" % len(saved_papers))
    print("-" * 50)

    classified = 0
    for item in saved_papers:
        paper_data = item["data"]
        fpath = item["file"]

        title = paper_data.get("title", "")
        # Read abstract from saved file
        full_path = os.path.join(BASE, "raw", fpath)
        abstract = ""
        if os.path.exists(full_path):
            with open(full_path, encoding="utf-8") as f:
                content = f.read()
            # Extract abstract section
            if "## Abstract" in content:
                abstract = content.split("## Abstract\n\n", 1)[-1].strip()[:1000]

        if not abstract:
            continue

        prompt = prompt_template.replace("{title}", title).replace("{abstract}", abstract)

        try:
            time.sleep(0.5)
            resp = httpx.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": api_key,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json",
                },
                json={
                    "model": "claude-haiku-4-5-20251001",
                    "max_tokens": 300,
                    "messages": [{"role": "user", "content": prompt}],
                },
                timeout=30,
            )
            resp.raise_for_status()
            result_text = resp.json()["content"][0]["text"]

            # Parse JSON response
            import re
            json_match = re.search(r'\{[^}]+\}', result_text)
            if json_match:
                result = json.loads(json_match.group())
                new_tier = result.get("tier", paper_data.get("tier", 3))

                # Update frontmatter in file
                if os.path.exists(full_path):
                    with open(full_path, encoding="utf-8") as f:
                        content = f.read()
                    old_tier_line = "tier: %s" % paper_data.get("tier", 3)
                    new_tier_line = "tier: %s" % new_tier
                    content = content.replace(old_tier_line, new_tier_line, 1)
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(content)

                tier_mark = {1: "★", 2: "◇", 3: "·"}.get(new_tier, "?")
                print("  %s T%d %s" % (tier_mark, new_tier, title[:55]))
                classified += 1
        except Exception as e:
            print("  LLM error [%s]: %s" % (title[:30], e))

    print("  → %d 件を分類" % classified)


# ============================================================
# メイン
# ============================================================
def run_explore(args):
    """Entry point called from fetch.py CLI."""
    config = load_sources_yaml()
    domain_config = get_domain_config(config, args.domain)

    if not domain_config:
        print("不明な分野: %s" % args.domain)
        all_domains = list(config.get("research_domains", {}).keys())
        all_domains += list(config.get("cross_cutting_themes", {}).keys())
        print("利用可能: %s" % ", ".join(sorted(all_domains)))
        return

    domain = args.domain
    label = domain_config.get("label", domain)
    min_cit = domain_config.get("min_citations", 100)

    store = PaperStore(BASE)
    rl = RateLimiter(
        domain_intervals={"api.openalex.org": 0.15},
        default_interval=1.5,
    )
    oa = OpenAlexClient(rl)

    print("=" * 60)
    print("explore — %s (%s)" % (label, domain))
    print("  depth: %d | limit: %d | min_cit: %d | dry_run: %s" % (
        args.depth, args.limit, min_cit, args.dry_run))
    print("  既存: %d 件" % len(store.load_existing_hashes()))
    print("=" * 60)

    # Resume support
    explore_state = {}  # type: Dict
    visited_from_state = set()  # type: Set[str]
    if args.resume:
        explore_state = load_explore_state(domain)
        visited_from_state = set(explore_state.get("visited_ids", []))
        print("  resume: %d 件の探索済み ID を復元" % len(visited_from_state))

    # Step 1: Resolve seeds
    print("\n" + "-" * 50)
    print("Step 1: seed 論文の決定")
    print("-" * 50)

    if args.seeds:
        seeds = resolve_seeds_from_ids(oa, args.seeds)
    else:
        seeds = resolve_seeds_from_queries(oa, domain_config)

    if not seeds:
        print("  seed 論文が見つかりません。--seeds で直接指定してください。")
        return

    print("  → %d 件の seed を取得" % len(seeds))

    # Step 2: BFS expansion
    saved, visited, stats = run_bfs_expansion(
        oa, store, seeds, domain, label, min_cit,
        args.depth, args.limit, args.dry_run,
    )

    # Merge with previous state
    all_visited = visited | visited_from_state

    # Step 3: LLM tier classification (optional)
    if args.tier and saved and not args.dry_run:
        run_llm_tier_classification(saved, config)

    # Step 4: Index update
    if not args.dry_run and saved:
        index_entries = []
        for item in saved:
            idx = build_index_entry(item["data"], item["file"])
            index_entries.append(idx)
        store.append_to_index(index_entries)

    # Save explore state
    if not args.dry_run:
        save_explore_state(domain, {
            "domain": domain,
            "visited_ids": list(all_visited),
            "saved_count": explore_state.get("saved_count", 0) + len(saved),
        })

    # Summary report
    print("\n" + "=" * 60)
    print("探索完了レポート — %s" % label)
    print("=" * 60)
    print("  探索済み:    %d 件" % stats["total_visited"])
    print("  新規保存:    %d 件" % stats["saved"])
    print("  重複スキップ: %d 件" % stats["skipped_dup"])
    print("  低引用スキップ: %d 件" % stats["skipped_low_cit"])
    if stats["by_depth"]:
        print("  depth 別:")
        for k, v in sorted(stats["by_depth"].items()):
            print("    %s: %d 件" % (k, v))
    if stats["by_type"]:
        print("  タイプ別:")
        for k, v in sorted(stats["by_type"].items()):
            print("    %s: %d 件" % (k, v))
    print("=" * 60)
