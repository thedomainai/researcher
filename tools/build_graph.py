#!/usr/bin/env python3
"""Generate explicit knowledge graph artifacts for the wiki."""

import argparse
import os
import sys

from lib.knowledge_graph import build_knowledge_graph, validate_graph, write_graph_artifacts


def main():
    parser = argparse.ArgumentParser(description="wiki の知識グラフを生成")
    parser.add_argument(
        "--base-dir",
        default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        help="プロジェクトのルートディレクトリ",
    )
    parser.add_argument("--check", action="store_true", help="ファイルを書かずに整合性チェックだけ行う")
    parser.add_argument("--strict", action="store_true", help="未解決参照や不正ソース参照もエラー扱いにする")
    args = parser.parse_args()

    if args.check:
        graph, backlinks = build_knowledge_graph(base_dir=args.base_dir)
    else:
        graph, backlinks = write_graph_artifacts(base_dir=args.base_dir)
    summary = graph["summary"]
    issues = validate_graph(graph, backlinks)
    if args.strict:
        if summary["unresolved_nodes"]:
            issues.append(f"unresolved refs: {summary['unresolved_nodes']}")
        if summary["invalid_source_refs"]:
            issues.append(f"invalid source refs: {summary['invalid_source_refs']}")

    print("=" * 60)
    print("Knowledge graph checked" if args.check else "Knowledge graph generated")
    print("=" * 60)
    print(f"articles_scanned: {summary['articles_scanned']}")
    print(f"nodes: {summary['nodes']}")
    print(f"resolved_nodes: {summary['resolved_nodes']}")
    print(f"unresolved_nodes: {summary['unresolved_nodes']}")
    print(f"edges: {summary['edges']}")
    print(f"resolved_edges: {summary['resolved_edges']}")
    print(f"unresolved_edges: {summary['unresolved_edges']}")
    print(f"link_mentions: {summary['link_mentions']}")
    print(f"valid_source_refs: {summary['valid_source_refs']}")
    print(f"invalid_source_refs: {summary['invalid_source_refs']}")
    print(f"isolated_concepts: {summary['isolated_concepts']}")
    print(f"backlink_nodes: {len(backlinks['nodes'])}")
    print(f"issues: {len(issues)}")
    for issue in issues:
        print(f"  - {issue}")

    if issues:
        sys.exit(1)


if __name__ == "__main__":
    main()
