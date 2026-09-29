#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""未分類の論文に Tier 分類を付ける(Claude Code の headless モード経由・サブスクリプション課金)。

pipeline_compile.py --tier-only と同じ判定基準・同じ書き戻し形式で、LLM の呼び出しだけを
`claude -p`(Claude Code の非対話モード)に置き換えたもの。API キーではなくログイン済みの
サブスクリプションで動くため、従量課金が発生しない。

  - 従量課金の API キー(ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN)は子プロセスから外す。
    残っていると Claude Code が API 課金に切り替わるため
  - 認証切れ(OAuth session expired)のときは何も書き換えず終了コード 3 で止まる。
    `claude login` を一度実行すると復旧する
  - 1 回の呼び出しで BATCH 件をまとめて判定し、JSON 配列で受け取る
  - claude -p の起動は lib/claude_cli.py に集約(--tools "" --setting-sources "" で
    1 回あたり約 7.5 万トークンの固定文脈を外す。2026-09-29)

使い方:
    python3 tools/tier_classify_cli.py --limit 200 [--domain neuroscience] [--dry-run]
"""

import argparse
import fcntl
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "raw")
INDEX_PATH = os.path.join(RAW, "index.jsonl")
BATCH = 10
MAX_CONSECUTIVE_FAILURES = 3   # 連続で失敗したら止める(利用枠の上限・障害を想定)
LOCK_PATH = os.path.join(BASE, "logs", "tier_classify.lock")
MODEL = "haiku"


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # tools/ を import パスに入れる
from lib.claude_cli import AuthError, call_claude as _call_claude  # noqa: E402

SYSTEM_PROMPT = (
    "あなたは研究論文の品質評価者です。与えられた論文を3つのテストで評価し、"
    "Tier分類をJSON形式で返してください。JSON以外は出力しないでください。"
)

CRITERIA = """以下の各論文について、AI nativeな社会・組織・システム設計への有用性を評価してください。

3つのテスト:
1. 抽象度テスト: この知見から具体的な対象(人間、現在の技術、現在の制度)を除去しても成立するか?
2. 制約不変テスト: この知見が依拠している制約条件は、AGI時代にも存続するか?
3. メカニズムテスト: この研究は「なぜ」を説明しているか、それとも「何が起きたか」を記述しているだけか?

分類:
- Tier 1(不変原理): 3テスト全てを満たす
- Tier 2(消滅制約の分析): テスト2で「消滅する制約」に依拠するが、その制約の構造的分析として価値がある
- Tier 3(スキップ): 条件依存的な現象記述または手法レベルの最適化

論文:
{papers}

各論文について次の JSON 配列だけを返してください(JSON 以外は出力しない):
[{{"n": 1, "tier": 1, "reasoning": "判定理由", "key_insight": "核心的知見の1行要約"}}]"""


def read_excerpt(entry):
    path = os.path.join(RAW, entry["file"])
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if entry.get("type") == "article":
        parts = content.split("---", 2)
        body = parts[2] if len(parts) >= 3 else content
        return body[:2000].strip()
    return content[:1500].strip()


def call_claude(prompt):
    """claude -p を呼び、本文テキストを返す。認証切れは AuthError。
    起動オプション(--tools "" --setting-sources "" で固定文脈を削る)は lib/claude_cli.py に集約。"""
    text, _usage = _call_claude(prompt, SYSTEM_PROMPT, model=MODEL)
    return text


def parse_batch(text, n):
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1]
        cleaned = cleaned.rsplit("```", 1)[0]
    m = re.search(r"\[.*\]", cleaned, re.S)
    arr = json.loads(m.group(0) if m else cleaned)
    out = {}
    for item in arr:
        try:
            k = int(item.get("n"))
            tier = int(item.get("tier"))
        except (TypeError, ValueError, AttributeError):
            continue
        if 1 <= k <= n and tier in (1, 2, 3):
            out[k] = {"tier": tier, "tier_reasoning": str(item.get("reasoning", "")),
                      "key_insight": str(item.get("key_insight", ""))}
    return out


def main():
    ap = argparse.ArgumentParser(description="claude -p による Tier 分類")
    ap.add_argument("--limit", type=int, default=200)
    ap.add_argument("--domain")
    ap.add_argument("--dry-run", action="store_true", help="対象を数えるだけ")
    args = ap.parse_args()

    # 同時に 2 本走ると index.jsonl の書き戻しが競合する。日次ジョブと手動の一括実行を排他にする
    os.makedirs(os.path.dirname(LOCK_PATH), exist_ok=True)
    lock = open(LOCK_PATH, "a+")
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("別の tier_classify_cli.py が実行中のためスキップします。")
        return 0

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index = [json.loads(line) for line in f if line.strip()]
    needs = [e for e in index if "tier" not in e]
    if args.domain:
        needs = [e for e in needs if e.get("domain") == args.domain]
    print("Tier未分類: %d 件(今回 %d 件まで)" % (len(needs), args.limit), flush=True)
    if args.dry_run or not needs:
        return 0
    needs = needs[: args.limit]

    counts = {1: 0, 2: 0, 3: 0}
    errors = 0
    done = 0
    consecutive_failures = 0
    for i in range(0, len(needs), BATCH):
        batch = [e for e in needs[i:i + BATCH]]
        items = []
        for e in batch:
            ex = read_excerpt(e)
            items.append((e, ex))
        listed = [(k + 1, e, ex) for k, (e, ex) in enumerate(items) if ex]
        if not listed:
            continue
        papers = "\n\n".join("### [%d] %s\n%s" % (k, e["title"], ex[:1500]) for k, e, ex in listed)
        try:
            text = call_claude(CRITERIA.format(papers=papers))
            results = parse_batch(text, len(items))
        except AuthError as e:
            print("認証エラー: %s\n`claude login` を実行してから再実行してください。" % str(e)[:200], flush=True)
            break_code = 3
            # ここまでの結果は書き戻す
            _write_back(index)
            return break_code
        except Exception as e:
            print("  ! バッチ失敗: %s" % str(e)[:200], flush=True)
            errors += len(listed)
            consecutive_failures += 1
            if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                print("連続 %d バッチが失敗したため中断します(利用枠の上限か障害の可能性)。" % consecutive_failures, flush=True)
                break
            continue
        consecutive_failures = 0
        for k, e, _ in listed:
            res = results.get(k)
            if not res:
                errors += 1
                print("  [%d] ERROR: %s" % (i + k, e["title"][:60]), flush=True)
                continue
            for row in index:
                if row["title"] == e["title"] and row["file"] == e["file"]:
                    row["tier"] = res["tier"]
                    row["tier_reasoning"] = res["tier_reasoning"]
                    row["key_insight"] = res["key_insight"]
                    break
            counts[res["tier"]] += 1
            done += 1
            label = {1: "不変原理", 2: "設計原理", 3: "スキップ"}[res["tier"]]
            print("  [%d/%d] Tier %d (%s): %s" % (i + k, len(needs), res["tier"], label, e["title"][:60]), flush=True)
        _write_back(index)  # バッチごとに書き戻す(途中で止まっても成果が残る)

    print("\nTier分類結果: T1=%d, T2=%d, T3=%d, エラー=%d(処理 %d 件)" % (counts[1], counts[2], counts[3], errors, done), flush=True)
    return 1 if (errors and not done) else 0


def _write_back(index):
    tmp = INDEX_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for e in index:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    os.replace(tmp, INDEX_PATH)


if __name__ == "__main__":
    sys.exit(main())
