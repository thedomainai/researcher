"""
日次リーディングリスト生成

毎日5本の論文を Tier 1 優先で選定し、読みやすい Markdown を生成する。
読了管理は config/reading_state.json で行い、同じ論文が重複選定されない。

Usage:
    python tools/daily_reading.py              # 今日のリーディングリスト生成
    python tools/daily_reading.py --count 3    # 3本に変更
    python tools/daily_reading.py --domain complexity_science  # ドメイン指定
    python tools/daily_reading.py --done       # 今日のリストを読了済みにマーク
    python tools/daily_reading.py --stats      # 統計表示
    python tools/daily_reading.py --list       # 過去のリーディングリスト一覧
"""
import argparse
import datetime
import json
import os
import random
import sys
from typing import Optional

BASE = "/Users/yuta/workspace/projects/researcher"
INDEX_PATH = os.path.join(BASE, "raw", "index.jsonl")
STATE_PATH = os.path.join(BASE, "config", "reading_state.json")
DAILY_DIR = os.path.join(BASE, "wiki", "daily")

os.makedirs(DAILY_DIR, exist_ok=True)


# ============================================================
# 読了状態管理
# ============================================================

def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, "r") as f:
            return json.load(f)
    return {"read_files": [], "daily_logs": {}}


def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


# ============================================================
# インデックス読み込み
# ============================================================

def load_index():
    entries = []
    with open(INDEX_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


# ============================================================
# 論文選定
# ============================================================

def select_papers(entries, state, count=5, domain=None):
    """Tier 1 優先、未読、ドメインバランスを考慮して選定"""
    read_set = set(state.get("read_files", []))

    # フィルタ: 未読 + paper のみ（article は除外）
    candidates = [
        e for e in entries
        if e.get("type") == "paper"
        and e.get("file", "") not in read_set
        and e.get("tier") in (1, 2)
        and e.get("file", "")
    ]

    if domain:
        candidates = [e for e in candidates if e.get("domain") == domain]

    if not candidates:
        return []

    # Tier 1 を優先（Tier 1 に weight 3, Tier 2 に weight 1）
    tier1 = [e for e in candidates if e.get("tier") == 1]
    tier2 = [e for e in candidates if e.get("tier") == 2]

    # ドメインの多様性を確保するため、ドメインごとにグループ化
    by_domain = {}
    for e in tier1:
        d = e.get("domain", "unknown")
        by_domain.setdefault(d, []).append(e)

    selected = []

    # まず各ドメインから1本ずつ Tier 1 を選ぶ（ラウンドロビン）
    domains = list(by_domain.keys())
    random.shuffle(domains)
    for d in domains:
        if len(selected) >= count:
            break
        pool = by_domain[d]
        # 被引用数が多い順でソート（品質の代理指標）
        pool.sort(key=lambda x: int(x.get("citations", 0) or 0), reverse=True)
        selected.append(pool[0])

    # 足りなければ Tier 1 の残りから追加
    if len(selected) < count:
        remaining_t1 = [e for e in tier1 if e not in selected]
        remaining_t1.sort(key=lambda x: int(x.get("citations", 0) or 0), reverse=True)
        for e in remaining_t1:
            if len(selected) >= count:
                break
            selected.append(e)

    # それでも足りなければ Tier 2 から追加
    if len(selected) < count:
        tier2.sort(key=lambda x: int(x.get("citations", 0) or 0), reverse=True)
        for e in tier2:
            if len(selected) >= count:
                break
            selected.append(e)

    return selected[:count]


# ============================================================
# 論文本文読み込み
# ============================================================

def read_paper_content(file_path):
    full_path = os.path.join(BASE, "raw", file_path)
    if not os.path.exists(full_path):
        return None
    with open(full_path, "r") as f:
        return f.read()


# ============================================================
# リーディングリスト生成
# ============================================================

def generate_reading_list(selected, today_str):
    lines = []
    lines.append(f"# Daily Reading — {today_str}")
    lines.append("")
    lines.append(f"**{len(selected)}本** | Tier 1 優先 | 未読から選定")
    lines.append("")

    for i, entry in enumerate(selected, 1):
        title = entry.get("title", "Untitled")
        authors = entry.get("authors", "")
        year = entry.get("year", "")
        citations = entry.get("citations", 0)
        tier = entry.get("tier", "?")
        domain = entry.get("domain", "")
        file_path = entry.get("file", "")
        key_insight = entry.get("key_insight", "")
        tier_reasoning = entry.get("tier_reasoning", "")

        lines.append(f"## {i}. {title}")
        lines.append("")

        meta_parts = []
        if authors:
            meta_parts.append(f"**著者**: {authors}")
        if year:
            meta_parts.append(f"**年**: {year}")
        if citations:
            meta_parts.append(f"**被引用**: {citations}")
        meta_parts.append(f"**Tier**: {tier}")
        meta_parts.append(f"**分野**: {domain}")
        lines.append(" | ".join(meta_parts))
        lines.append("")

        if key_insight:
            lines.append(f"**Key Insight**: {key_insight}")
            lines.append("")

        # 論文本文を読み込んでAbstractを抽出
        content = read_paper_content(file_path)
        if content:
            # Abstract セクションを抽出
            abstract = ""
            in_abstract = False
            for line in content.split("\n"):
                if line.strip().startswith("## Abstract"):
                    in_abstract = True
                    continue
                if in_abstract:
                    if line.strip().startswith("## ") or line.strip().startswith("---"):
                        break
                    abstract += line + "\n"

            abstract = abstract.strip()
            if abstract:
                lines.append("### Abstract")
                lines.append("")
                lines.append(abstract)
                lines.append("")

        if tier_reasoning:
            lines.append("<details>")
            lines.append("<summary>Tier 分類理由</summary>")
            lines.append("")
            lines.append(tier_reasoning)
            lines.append("")
            lines.append("</details>")
            lines.append("")

        lines.append(f"**ファイル**: `raw/{file_path}`")
        lines.append("")

    return "\n".join(lines)


# ============================================================
# 統計
# ============================================================

def show_stats(state, entries):
    read_set = set(state.get("read_files", []))
    total_papers = len([e for e in entries if e.get("type") == "paper"])
    t1_papers = len([e for e in entries if e.get("type") == "paper" and e.get("tier") == 1])
    t2_papers = len([e for e in entries if e.get("type") == "paper" and e.get("tier") == 2])
    read_count = len(read_set)

    t1_unread = len([
        e for e in entries
        if e.get("type") == "paper" and e.get("tier") == 1
        and e.get("file", "") not in read_set
    ])
    t2_unread = len([
        e for e in entries
        if e.get("type") == "paper" and e.get("tier") == 2
        and e.get("file", "") not in read_set
    ])

    daily_count = len(state.get("daily_logs", {}))
    days_remaining_t1 = t1_unread // 5 if t1_unread >= 5 else 0

    print("リーディング統計:")
    print(f"  論文総数:         {total_papers}")
    print(f"  Tier 1:          {t1_papers} (未読: {t1_unread})")
    print(f"  Tier 2:          {t2_papers} (未読: {t2_unread})")
    print(f"  読了済み:         {read_count}")
    print(f"  リーディング実施日: {daily_count}日")
    print(f"  Tier 1 残日数:    約{days_remaining_t1}日分 (5本/日)")
    print()

    # ドメイン別の未読数
    domain_unread = {}
    for e in entries:
        if (e.get("type") == "paper" and e.get("tier") in (1, 2)
                and e.get("file", "") not in read_set):
            d = e.get("domain", "unknown")
            domain_unread[d] = domain_unread.get(d, 0) + 1

    if domain_unread:
        print("  ドメイン別未読 (Tier 1+2):")
        for d, c in sorted(domain_unread.items(), key=lambda x: -x[1]):
            print(f"    {d}: {c}")


# ============================================================
# 過去のリスト一覧
# ============================================================

def list_past():
    files = sorted(
        [f for f in os.listdir(DAILY_DIR) if f.endswith(".md") and f != ".gitkeep"],
        reverse=True
    )
    if not files:
        print("まだリーディングリストがありません。")
        return

    print("過去のリーディングリスト:")
    for f in files[:30]:
        date_str = f.replace(".md", "")
        path = os.path.join(DAILY_DIR, f)
        with open(path, "r") as fh:
            line_count = sum(1 for _ in fh)
        print(f"  {date_str} ({line_count}行)")


# ============================================================
# メイン
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="日次リーディングリスト生成")
    parser.add_argument("--count", type=int, default=5, help="選定本数（デフォルト: 5）")
    parser.add_argument("--domain", type=str, default=None, help="ドメイン指定")
    parser.add_argument("--done", action="store_true", help="今日のリストを読了済みにマーク")
    parser.add_argument("--stats", action="store_true", help="統計表示")
    parser.add_argument("--list", action="store_true", help="過去のリスト一覧")
    parser.add_argument("--date", type=str, default=None, help="日付指定 (YYYY-MM-DD)")
    args = parser.parse_args()

    state = load_state()
    entries = load_index()
    today_str = args.date or datetime.date.today().isoformat()

    if args.stats:
        show_stats(state, entries)
        return

    if args.list:
        list_past()
        return

    if args.done:
        # 今日のリストの論文を読了済みにマーク
        log = state.get("daily_logs", {}).get(today_str, [])
        if not log:
            print(f"  {today_str} のリーディングリストがありません。")
            return
        read_set = set(state.get("read_files", []))
        newly_read = 0
        for f in log:
            if f not in read_set:
                read_set.add(f)
                newly_read += 1
        state["read_files"] = sorted(read_set)
        save_state(state)
        print(f"  ✅ {newly_read}本を読了済みにマーク（{today_str}）")
        return

    # 既に今日のリストがある場合
    daily_path = os.path.join(DAILY_DIR, f"{today_str}.md")
    if os.path.exists(daily_path):
        print(f"  今日のリーディングリストは既に存在します: {daily_path}")
        with open(daily_path, "r") as f:
            print(f.read())
        return

    # 論文選定
    selected = select_papers(entries, state, count=args.count, domain=args.domain)
    if not selected:
        print("  未読の対象論文がありません。")
        return

    # リーディングリスト生成
    content = generate_reading_list(selected, today_str)

    # 保存
    with open(daily_path, "w") as f:
        f.write(content)

    # 状態更新
    selected_files = [e.get("file", "") for e in selected]
    state.setdefault("daily_logs", {})[today_str] = selected_files
    save_state(state)

    print(content)
    print()
    print(f"  💾 保存: {daily_path}")
    print(f"  読了後は `python tools/daily_reading.py --done` でマークしてください")


if __name__ == "__main__":
    main()
