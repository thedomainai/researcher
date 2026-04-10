#!/usr/bin/env python3
"""Utilities for building explicit knowledge graph artifacts from the wiki."""

from __future__ import annotations

import hashlib
import json
import os
import re
import unicodedata
from collections import defaultdict
from datetime import datetime
from typing import Dict, Iterable, List, Optional, Tuple

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
PAREN_RE = re.compile(r"[\(\（]([^\)\）]+)[\)\）]")
SOURCE_PATH_RE = re.compile(r"(raw/[^\s\)`\]]+\.(?:md|pdf))")


def extract_h1(text: str, fallback: str = "") -> str:
    match = H1_RE.search(text)
    return match.group(1).strip() if match else fallback


def extract_wikilinks(text: str) -> List[dict]:
    return scan_wikilink_mentions(text)


def scan_wikilink_mentions(text: str) -> List[dict]:
    mentions = []
    current_section = "本文"
    for line_number, line in enumerate(text.splitlines(), start=1):
        heading = re.match(r"^(#{2,6})\s+(.+)$", line)
        if heading:
            current_section = heading.group(2).strip()

        for match in WIKILINK_RE.finditer(line):
            inner = match.group(1).strip()
            if not inner:
                continue
            if "|" in inner:
                target, label = inner.split("|", 1)
            else:
                target, label = inner, inner
            mentions.append(
                {
                    "raw": inner,
                    "target": target.strip(),
                    "label": label.strip(),
                    "line": line_number,
                    "section": current_section,
                }
            )
    return mentions


def normalize_text(value: str) -> str:
    text = unicodedata.normalize("NFKC", value or "").strip().lower()
    text = re.sub(r"\s+", " ", text)
    return text


def compact_text(value: str) -> str:
    return re.sub(r"[\W_]+", "", normalize_text(value), flags=re.UNICODE)


def strip_parenthetical(value: str) -> str:
    stripped = re.sub(r"\s*[\(\（][^\)\）]*[\)\）]\s*", " ", value or "")
    stripped = re.sub(r"\s+", " ", stripped)
    return stripped.strip()


def build_alias_variants(value: str) -> List[str]:
    text = unicodedata.normalize("NFKC", value or "").strip()
    if not text:
        return []

    variants = {text}

    stripped = strip_parenthetical(text)
    if stripped and stripped != text:
        variants.add(stripped)

    for inner in PAREN_RE.findall(text):
        inner = inner.strip()
        if inner:
            variants.add(inner)

    if ":" in text or "：" in text:
        for part in re.split(r"[:：]", text):
            part = part.strip()
            if part:
                variants.add(part)

    return sorted(variants)


def candidate_keys(value: str, compact_penalty: int = 5) -> Dict[str, int]:
    keys: Dict[str, int] = {}
    for variant in build_alias_variants(value):
        normalized = normalize_text(variant)
        if normalized:
            keys[normalized] = max(keys.get(normalized, -999), 0)
        compact = compact_text(variant)
        if compact:
            keys[compact] = max(keys.get(compact, -999), -compact_penalty)
    return keys


def read_json(path: str, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def register_alias(
    alias_index: Dict[str, Dict[str, int]],
    alias: str,
    slug: str,
    priority: int,
) -> None:
    for key, bonus in candidate_keys(alias, compact_penalty=4).items():
        score = priority + bonus
        alias_index[key][slug] = max(alias_index[key].get(slug, -999), score)


def load_concept_graph_inputs(
    wiki_concepts_dir: str,
    concepts_meta_path: str,
) -> Tuple[Dict[str, dict], Dict[str, Dict[str, int]]]:
    meta_list = read_json(concepts_meta_path, [])
    meta_by_slug = {item["slug"]: item for item in meta_list if item.get("slug")}

    concept_nodes: Dict[str, dict] = {}
    alias_index: Dict[str, Dict[str, int]] = defaultdict(dict)

    for filename in sorted(os.listdir(wiki_concepts_dir)):
        if not filename.endswith(".md"):
            continue

        slug = filename[:-3]
        full_path = os.path.join(wiki_concepts_dir, filename)
        with open(full_path, encoding="utf-8") as handle:
            article = handle.read()

        meta = meta_by_slug.get(slug, {})
        h1 = extract_h1(article, meta.get("title_ja") or slug)
        title_ja = meta.get("title_ja") or h1
        title_en = meta.get("title_en", "")

        aliases = {
            slug,
            h1,
            title_ja,
            title_en,
        }
        if title_ja and title_en:
            aliases.add(f"{title_ja} ({title_en})")
            aliases.add(f"{title_ja}（{title_en}）")

        for alias in list(aliases):
            aliases.update(build_alias_variants(alias))

        node = {
            "id": slug,
            "slug": slug,
            "label": title_ja,
            "title": title_ja,
            "title_ja": title_ja,
            "title_en": title_en,
            "tier": meta.get("tier"),
            "description": meta.get("description", ""),
            "related_domains": meta.get("related_domains", []),
            "key_sources": meta.get("key_sources", []),
            "file": f"concepts/{filename}",
            "kind": "concept",
            "resolved": True,
            "aliases": sorted(a for a in aliases if a),
            "article_exists": True,
            "metadata_source": "concepts.json" if slug in meta_by_slug else "article",
        }
        concept_nodes[slug] = node

        register_alias(alias_index, slug, slug, 120)
        register_alias(alias_index, h1, slug, 100)
        if title_ja:
            register_alias(alias_index, title_ja, slug, 95)
        if title_en:
            register_alias(alias_index, title_en, slug, 90)
        for alias in node["aliases"]:
            register_alias(alias_index, alias, slug, 70)

    return concept_nodes, alias_index


def resolve_target(
    target: str,
    concept_nodes: Dict[str, dict],
    alias_index: Dict[str, Dict[str, int]],
) -> Tuple[Optional[str], bool, bool, List[str], Optional[str]]:
    if target in concept_nodes:
        return target, True, False, [target], "slug"

    scores: Dict[str, int] = {}
    for key, bonus in candidate_keys(target).items():
        for slug, base_score in alias_index.get(key, {}).items():
            scores[slug] = max(scores.get(slug, -999), base_score + bonus)

    if not scores:
        return None, False, False, [], None

    best_score = max(scores.values())
    best = sorted(slug for slug, score in scores.items() if score == best_score)
    ranked = [slug for slug, _ in sorted(scores.items(), key=lambda item: (-item[1], item[0]))]
    if len(best) != 1:
        return None, False, True, ranked, None

    return best[0], True, False, ranked, "alias"


def unresolved_node_id(target: str) -> str:
    digest = hashlib.sha1(normalize_text(target).encode("utf-8")).hexdigest()[:12]
    return f"dangling:{digest}"


def scan_source_references(text: str) -> List[str]:
    return SOURCE_PATH_RE.findall(text)


def build_knowledge_graph(
    base_dir: str,
    wiki_dir: Optional[str] = None,
    meta_dir: Optional[str] = None,
) -> Tuple[dict, dict]:
    wiki_root = wiki_dir or os.path.join(base_dir, "wiki")
    wiki_concepts_dir = os.path.join(wiki_root, "concepts")
    meta_root = meta_dir or os.path.join(wiki_root, "_meta")
    concepts_meta_path = os.path.join(meta_root, "concepts.json")

    concept_nodes, alias_index = load_concept_graph_inputs(
        wiki_concepts_dir=wiki_concepts_dir,
        concepts_meta_path=concepts_meta_path,
    )

    nodes = {slug: dict(node) for slug, node in concept_nodes.items()}
    edge_buckets: Dict[Tuple[str, str], dict] = {}
    total_mentions = 0
    valid_source_refs = 0
    invalid_source_refs = 0
    unresolved_mentions = []

    for source_slug in sorted(concept_nodes):
        source_file = os.path.join(wiki_concepts_dir, f"{source_slug}.md")
        with open(source_file, encoding="utf-8") as handle:
            article = handle.read()

        for raw_path in scan_source_references(article):
            if os.path.exists(os.path.join(base_dir, raw_path)):
                valid_source_refs += 1
            else:
                invalid_source_refs += 1

        for link in scan_wikilink_mentions(article):
            total_mentions += 1
            raw_target = link["target"]
            target_slug, resolved, ambiguous, candidates, resolved_via = resolve_target(
                raw_target,
                concept_nodes=concept_nodes,
                alias_index=alias_index,
            )

            if resolved and target_slug:
                target_id = target_slug
                target_label = nodes[target_slug]["label"]
                target_file = nodes[target_slug]["file"]
            else:
                target_id = unresolved_node_id(raw_target)
                target_label = raw_target
                target_file = None
                if target_id not in nodes:
                    nodes[target_id] = {
                        "id": target_id,
                        "slug": None,
                        "label": raw_target,
                        "title": raw_target,
                        "title_ja": raw_target,
                        "title_en": "",
                        "tier": None,
                        "description": "",
                        "related_domains": [],
                        "key_sources": [],
                        "file": None,
                        "kind": "placeholder",
                        "resolved": False,
                        "aliases": [raw_target],
                        "article_exists": False,
                        "ambiguous": ambiguous,
                        "candidates": candidates,
                    }
                elif ambiguous and candidates:
                    existing = nodes[target_id].setdefault("candidates", [])
                    merged = sorted(set(existing) | set(candidates))
                    nodes[target_id]["candidates"] = merged
                    nodes[target_id]["ambiguous"] = True

                unresolved_mentions.append(
                    {
                        "source_slug": source_slug,
                        "source_title": nodes[source_slug]["label"],
                        "source_file": nodes[source_slug]["file"],
                        "target": target_id,
                        "raw_target": raw_target,
                        "label": link["label"],
                        "section": link["section"],
                        "line": link["line"],
                        "ambiguous": ambiguous,
                        "candidates": candidates,
                    }
                )

            bucket = edge_buckets.setdefault(
                (source_slug, target_id),
                {
                    "id": f"{source_slug}->{target_id}",
                    "source": source_slug,
                    "target": target_id,
                    "source_label": nodes[source_slug]["label"],
                    "target_label": target_label,
                    "source_file": nodes[source_slug]["file"],
                    "target_file": target_file,
                    "relation": "wikilink",
                    "resolved": resolved,
                    "weight": 0,
                    "raw_targets": set(),
                    "display_labels": set(),
                    "mentions": [],
                    "ambiguous": False,
                    "candidates": set(),
                },
            )
            bucket["weight"] += 1
            bucket["raw_targets"].add(raw_target)
            if link["label"]:
                bucket["display_labels"].add(link["label"])
            bucket["mentions"].append(
                {
                    "raw_target": raw_target,
                    "label": link["label"],
                    "section": link["section"],
                    "line": link["line"],
                    "resolved_via": resolved_via,
                }
            )
            if ambiguous:
                bucket["ambiguous"] = True
            bucket["candidates"].update(candidates)

    edges = []
    for key in sorted(edge_buckets):
        edge = edge_buckets[key]
        edge["raw_targets"] = sorted(edge["raw_targets"])
        edge["display_labels"] = sorted(edge["display_labels"])
        edge["candidates"] = sorted(edge["candidates"])
        edge["mentions"] = sorted(edge["mentions"], key=lambda item: (item["section"], item["line"], item["raw_target"]))
        edges.append(edge)

    inbound_map: Dict[str, List[dict]] = defaultdict(list)
    outbound_map: Dict[str, List[dict]] = defaultdict(list)

    for edge in edges:
        outbound_map[edge["source"]].append(
            {
                "id": edge["target"],
                "label": edge["target_label"],
                "resolved": edge["resolved"],
                "weight": edge["weight"],
                "target_file": edge["target_file"],
                "raw_targets": edge["raw_targets"],
                "display_labels": edge["display_labels"],
                "mentions": edge["mentions"],
                "ambiguous": edge["ambiguous"],
                "candidates": edge["candidates"],
            }
        )
        inbound_map[edge["target"]].append(
            {
                "id": edge["source"],
                "label": edge["source_label"],
                "resolved": True,
                "weight": edge["weight"],
                "source_file": edge["source_file"],
                "mentions": edge["mentions"],
            }
        )

    resolved_nodes = 0
    unresolved_nodes = 0
    isolated_nodes = 0
    for node_id, node in nodes.items():
        inbound = sorted(inbound_map.get(node_id, []), key=lambda item: item["label"])
        outbound = sorted(outbound_map.get(node_id, []), key=lambda item: item["label"])
        node["inbound_count"] = len(inbound)
        node["outbound_count"] = len(outbound)
        node["degree"] = node["inbound_count"] + node["outbound_count"]
        if node["resolved"]:
            resolved_nodes += 1
        else:
            unresolved_nodes += 1
        if node["degree"] == 0 and node["resolved"]:
            isolated_nodes += 1

    graph = {
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "articles_scanned": len(concept_nodes),
            "nodes": len(nodes),
            "resolved_nodes": resolved_nodes,
            "unresolved_nodes": unresolved_nodes,
            "edges": len(edges),
            "resolved_edges": sum(1 for edge in edges if edge["resolved"]),
            "unresolved_edges": sum(1 for edge in edges if not edge["resolved"]),
            "link_mentions": total_mentions,
            "valid_source_refs": valid_source_refs,
            "invalid_source_refs": invalid_source_refs,
            "isolated_concepts": isolated_nodes,
        },
        "nodes": sorted(nodes.values(), key=lambda item: (not item["resolved"], item["label"])),
        "edges": edges,
        "unresolved_mentions": sorted(
            unresolved_mentions,
            key=lambda item: (item["raw_target"], item["source_slug"], item["line"]),
        ),
    }

    backlinks = {
        "generated_at": graph["generated_at"],
        "summary": graph["summary"],
        "nodes": {},
        "by_target": {},
        "unresolved": {},
    }

    for node_id, node in sorted(nodes.items(), key=lambda item: item[0]):
        backlinks["nodes"][node_id] = {
            "id": node["id"],
            "slug": node["slug"],
            "label": node["label"],
            "resolved": node["resolved"],
            "kind": node["kind"],
            "file": node["file"],
            "inbound": sorted(inbound_map.get(node_id, []), key=lambda item: item["label"]),
            "outbound": sorted(outbound_map.get(node_id, []), key=lambda item: item["label"]),
        }
        backlinks["by_target"][node_id] = backlinks["nodes"][node_id]["inbound"]
        if not node["resolved"]:
            backlinks["unresolved"][node["label"]] = backlinks["nodes"][node_id]["inbound"]

    return graph, backlinks


def write_graph_artifacts(
    base_dir: str,
    wiki_dir: Optional[str] = None,
    meta_dir: Optional[str] = None,
) -> Tuple[dict, dict]:
    wiki_root = wiki_dir or os.path.join(base_dir, "wiki")
    meta_root = meta_dir or os.path.join(wiki_root, "_meta")
    os.makedirs(meta_root, exist_ok=True)

    graph, backlinks = build_knowledge_graph(
        base_dir=base_dir,
        wiki_dir=wiki_root,
        meta_dir=meta_root,
    )

    graph_path = os.path.join(meta_root, "concepts-graph.json")
    backlinks_path = os.path.join(meta_root, "backlinks.json")

    with open(graph_path, "w", encoding="utf-8") as handle:
        json.dump(graph, handle, ensure_ascii=False, indent=2)
    with open(backlinks_path, "w", encoding="utf-8") as handle:
        json.dump(backlinks, handle, ensure_ascii=False, indent=2)

    return graph, backlinks


def validate_graph(graph: dict, backlinks: dict) -> List[str]:
    issues = []
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    node_ids = [node["id"] for node in nodes]
    unique_node_ids = set(node_ids)

    if len(node_ids) != len(unique_node_ids):
        issues.append("duplicate node ids detected")

    seen_edges = set()
    for edge in edges:
        if edge["source"] not in unique_node_ids:
            issues.append(f"missing source node: {edge['source']}")
        if edge["target"] not in unique_node_ids:
            issues.append(f"missing target node: {edge['target']}")

        edge_key = (edge["source"], edge["target"])
        if edge_key in seen_edges:
            issues.append(f"duplicate edge detected: {edge['source']} -> {edge['target']}")
        seen_edges.add(edge_key)

    backlink_nodes = backlinks.get("nodes", {})
    for node_id in unique_node_ids:
        if node_id not in backlink_nodes:
            issues.append(f"missing backlinks entry for node: {node_id}")

    expected_backlinks = defaultdict(set)
    for edge in edges:
        expected_backlinks[edge["target"]].add(edge["source"])

    for node_id, sources in expected_backlinks.items():
        actual = {
            item["id"]
            for item in backlinks.get("nodes", {}).get(node_id, {}).get("inbound", [])
        }
        if actual != sources:
            issues.append(f"backlinks mismatch for node: {node_id}")

    return sorted(set(issues))
