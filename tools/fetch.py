#!/usr/bin/env python3
"""
fetch.py — 論文取得の統合CLIエントリポイント

Usage:
  python3 tools/fetch.py watch                            # 全分野の最新を取得
  python3 tools/fetch.py watch --domain neuroscience      # 特定分野のみ
  python3 tools/fetch.py watch --since 2026-04-01         # 日付指定
  python3 tools/fetch.py watch --dry-run                  # 取得せず確認のみ
  python3 tools/fetch.py watch --no-rss                   # RSS をスキップ

  python3 tools/fetch.py explore --domain neuroscience    # 分野の深探索
  python3 tools/fetch.py explore --domain neuroscience --depth 2 --limit 300
  python3 tools/fetch.py explore --domain neuroscience --seeds W1234,W5678
  python3 tools/fetch.py explore --domain neuroscience --resume
  python3 tools/fetch.py explore --domain neuroscience --tier
"""

import argparse
import os
import sys

# Ensure tools/ is on sys.path so `from lib.*` works
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    parser = argparse.ArgumentParser(
        prog="fetch.py",
        description="論文取得パイプライン: explore (深探索) / watch (日次監視)",
    )
    sub = parser.add_subparsers(dest="mode")

    # --- explore ---
    ep = sub.add_parser("explore", help="新ドメインの深探索")
    ep.add_argument("--domain", required=True, help="対象分野 (e.g., neuroscience)")
    ep.add_argument("--seeds", help="カンマ区切りの種論文ID (OA ID / DOI)")
    ep.add_argument("--depth", type=int, default=2, help="引用展開の深さ (default: 2)")
    ep.add_argument("--limit", type=int, default=300, help="最大保存件数 (default: 300)")
    ep.add_argument("--resume", action="store_true", help="前回の探索を再開")
    ep.add_argument("--tier", action="store_true", help="LLM Tier 分類を実行")
    ep.add_argument("--dry-run", action="store_true", help="保存せず確認のみ")

    # --- watch ---
    wp = sub.add_parser("watch", help="日次増分取得")
    wp.add_argument("--domain", default=None, help="特定分野のみ (省略で全分野)")
    wp.add_argument("--since", help="取得開始日 (YYYY-MM-DD)")
    wp.add_argument("--dry-run", action="store_true", help="保存せず確認のみ")
    wp.add_argument("--no-rss", action="store_true", help="RSS 取得をスキップ")

    args = parser.parse_args()

    if not args.mode:
        parser.print_help()
        sys.exit(1)

    if args.mode == "watch":
        from watch import run_watch
        run_watch(args)
    elif args.mode == "explore":
        from explore import run_explore
        run_explore(args)


if __name__ == "__main__":
    main()
