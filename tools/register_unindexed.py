#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""raw/papers/ にファイルはあるが raw/index.jsonl に無い論文を、index の末尾に登録する。

index に無い論文は Tier 分類・リーディングリスト・記事生成のどれにも乗らない
(2026-11-24 の点検で 308 件。8〜9 月の取得分が中心)。fetch_latest.py には既存ファイルを
登録し直す機能が無いので、この道具で補う。

取り決め:
  - index.jsonl には追記しかしない(既存の行は書き換えない)
  - 同じ題名(fetch_latest.title_hash)が index に既にある論文は登録しない(重複ファイル)
  - 行の形は fetch_latest.py が書くものに合わせる。tier は付けない(翌日の Tier 分類が付ける)

使い方:
  python3 tools/register_unindexed.py            # 対象を数えるだけ
  python3 tools/register_unindexed.py --apply    # index.jsonl に追記
"""
import argparse
import collections
import fcntl
import hashlib
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "raw")
RAW_PAPERS = os.path.join(RAW, "papers")
INDEX_PATH = os.path.join(RAW, "index.jsonl")
LOCK_PATH = os.path.join(BASE, "logs", "fetch_latest.lock")


def title_hash(title):
    # fetch_latest.title_hash と同じ(httpx 等の import を避けるため写している)
    return hashlib.md5(re.sub(r"[^a-z0-9]", "", title.lower()).encode()).hexdigest()


def parse_paper(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    parts = content.split("---", 2)
    if not content.startswith("---") or len(parts) < 3:
        return None
    front, body = parts[1], parts[2]

    def field(key):
        m = re.search(r'^%s:\s*"?(.*?)"?\s*$' % re.escape(key), front, re.M)
        return m.group(1) if m else ""

    # 題名は見出し行から取る(フロントマターの題名は引用符を含むと壊れている)
    m = re.search(r"^# (.+)$", body, re.M)
    title = (m.group(1) if m else field("title")).strip()
    if not title:
        return None

    def number(key):
        try:
            return int(field(key))
        except ValueError:
            return 0

    return {
        "title": title,
        "paper_type": field("paper_type") or "primary",
        "citations": number("citations"),
        "domain": field("domain"),
        "source_api": field("source_api"),
        "year": number("year") or None,
        "type": "paper",
    }


def main():
    ap = argparse.ArgumentParser(description="index.jsonl に無い raw/papers の論文を登録する")
    ap.add_argument("--apply", action="store_true", help="index.jsonl に追記する(既定は数えるだけ)")
    args = ap.parse_args()

    # 取得と同じロックを取り、日次の取得と同時に index へ書かない
    os.makedirs(os.path.dirname(LOCK_PATH), exist_ok=True)
    lock = open(LOCK_PATH, "a+")
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("fetch_latest.py が実行中のため中止します。")
        return 1

    indexed_files = set()
    hashes = set()
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                e = json.loads(line)
                indexed_files.add(e.get("file", ""))
                if e.get("title"):
                    hashes.add(title_hash(e["title"]))

    new_rows = []
    duplicates = 0
    unreadable = []
    for dirpath, _, filenames in sorted(os.walk(RAW_PAPERS)):
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), RAW)
            if rel in indexed_files:
                continue
            paper = parse_paper(os.path.join(dirpath, fn))
            if paper is None:
                unreadable.append(rel)
                continue
            th = title_hash(paper["title"])
            if th in hashes:
                duplicates += 1
                continue
            hashes.add(th)
            if not paper["domain"]:
                paper["domain"] = rel.split(os.sep)[1]
            row = {"title": paper["title"], "paper_type": paper["paper_type"], "citations": paper["citations"],
                   "domain": paper["domain"], "file": rel, "source_api": paper["source_api"],
                   "year": paper["year"], "type": "paper"}
            new_rows.append(row)

    print("index に無い論文: 登録対象 %d 件 / 題名が既に index にある重複 %d 件 / 読めないファイル %d 件"
          % (len(new_rows), duplicates, len(unreadable)))
    for d, n in collections.Counter(r["domain"] for r in new_rows).most_common(8):
        print("  %s: %d" % (d, n))
    for rel in unreadable[:10]:
        print("  読めない: %s" % rel)

    if not args.apply or not new_rows:
        if new_rows:
            print("--apply を付けると index.jsonl に追記します。")
        return 0

    with open(INDEX_PATH, "rb") as f:
        f.seek(-1, os.SEEK_END)
        ends_with_newline = f.read(1) == b"\n"
    with open(INDEX_PATH, "a", encoding="utf-8") as f:
        if not ends_with_newline:
            f.write("\n")
        for row in new_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print("index.jsonl に %d 件を追記しました。" % len(new_rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
