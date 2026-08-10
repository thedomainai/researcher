#!/usr/bin/env python3
"""
backfill_year.py — index.jsonl の year 欠落を markdown frontmatter から補完する

使い方:
  python3 tools/backfill_year.py             # 実行
  python3 tools/backfill_year.py --dry-run   # 確認のみ
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(ROOT, "raw", "index.jsonl")


def extract_year_from_frontmatter(filepath):
    """markdown ファイルの YAML frontmatter から year を抽出する。"""
    full_path = os.path.join(ROOT, "raw", filepath)
    if not os.path.exists(full_path):
        return None
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read(2000)  # frontmatter は先頭にある
    except Exception:
        return None

    # YAML frontmatter 内の year: <value> を探す
    m = re.search(r"^year:\s*(\d{4})", content, re.MULTILINE)
    if m:
        return int(m.group(1))

    # published フィールドから年を抽出（RSS記事用）
    m = re.search(r"^published:\s*[\"']?(\d{4})", content, re.MULTILINE)
    if m:
        return int(m.group(1))

    return None


def main():
    dry_run = "--dry-run" in sys.argv

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated = 0
    skipped_no_file = 0
    skipped_no_year = 0
    already_has_year = 0
    new_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            new_lines.append(line)
            continue

        entry = json.loads(line)

        if entry.get("year"):
            already_has_year += 1
            new_lines.append(json.dumps(entry, ensure_ascii=False))
            continue

        filepath = entry.get("file")
        if not filepath:
            skipped_no_file += 1
            new_lines.append(json.dumps(entry, ensure_ascii=False))
            continue

        year = extract_year_from_frontmatter(filepath)
        if year:
            entry["year"] = year
            updated += 1
        else:
            skipped_no_year += 1

        new_lines.append(json.dumps(entry, ensure_ascii=False))

    print(f"year あり（既存）: {already_has_year}")
    print(f"year 補完済み:     {updated}")
    print(f"file なし:         {skipped_no_file}")
    print(f"year 取得不可:     {skipped_no_year}")
    print(f"合計:              {len(new_lines)}")

    if dry_run:
        print("\n--dry-run: ファイルは更新しません")
    else:
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines) + "\n")
        print(f"\n{INDEX_PATH} を更新しました")


if __name__ == "__main__":
    main()
