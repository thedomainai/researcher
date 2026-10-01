#!/usr/bin/env python3
"""記事ごとに、公開サイトの見出し部に出す 1 文の要約・実務への含意・英語名を claude -p で作る。

対象: wiki/_meta/summaries.json にまだ無い記事。
出力: wiki/_meta/summaries.json({slug: {"summary": .., "why": .., "title_en": .., "at": ..}})
      build_site.py が記事ヘッダーのリード、一覧の抜粋、meta description、検索索引に使う。

要約と含意は記事本文に書かれている範囲から作らせる(本文に無い主張を足さない)。
サブスクリプション課金(tools/lib/claude_cli.py)。認証切れは終了コード 3。

使い方:
  python3 tools/summarize_articles_cli.py --limit 120          # 日次パイプラインの既定
  python3 tools/summarize_articles_cli.py --limit 2000 --workers 4
"""

import argparse
import datetime as dt
import json
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.claude_cli import call_claude, AuthError, strip_code_fence  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
CONCEPTS = BASE / "wiki" / "concepts"
OUT = BASE / "wiki" / "_meta" / "summaries.json"
BATCH = 10

SYSTEM_PROMPT = """あなたは研究ナレッジベースの編集者です。学術論文をもとに書かれた日本語の概念記事を読み、記事の冒頭に置く短い案内文を作ります。

各記事について次の 3 つを返します。
- summary: 記事の核心の主張を 1 文で。60〜90 字。常体(だ・である調)。「〜とは」「本記事は」で始めない。何が・なぜ・どうなるかを具体的に書く。
- why: AI を導入・運用する組織にとっての含意を 1 文で。40〜70 字。常体。記事本文に書かれている範囲から導く。本文から導けない場合は空文字にする。
- title_en: 概念の英語名。本文に英語名があればそれを使う。無ければ自然な英訳。Title Case、8 語以内。

守ること:
- 本文に無い事実・数値・主張を足さない。誇張しない。
- 「重要である」「注目されている」のような中身の無い言い回しを使わない。
- 出力は JSON 配列だけ: [{"slug": "...", "summary": "...", "why": "...", "title_en": "..."}]"""

lock = threading.Lock()


def load():
    if OUT.exists():
        return json.loads(OUT.read_text(encoding="utf-8"))
    return {}


def excerpt(markdown, limit=1700):
    body = re.sub(r"^# .+\n+", "", markdown.strip())
    body = re.split(r"\n## (?:関連|参考|追加)", body)[0]
    body = re.sub(r"\[\[(?:[^\]|]+\|)?([^\]]+)\]\]", r"\1", body)
    return body[:limit]


def run_batch(batch, store, stats):
    articles = "\n\n".join("### slug: %s\nタイトル: %s\n本文:\n%s" % (slug, title, text) for slug, title, text in batch)
    prompt = "次の %d 記事それぞれについて、summary・why・title_en を作り、JSON 配列で返してください。\n\n%s" % (len(batch), articles)
    try:
        text, _usage = call_claude(prompt, SYSTEM_PROMPT, model=stats["model"], timeout=420, retries=2)
        rows = json.loads(strip_code_fence(text))
    except AuthError:
        stats["auth"] = True
        return
    except Exception as exc:  # noqa: BLE001
        stats["failed"] += 1
        print("summarize: バッチ失敗 %s" % str(exc)[:160], file=sys.stderr, flush=True)
        return
    valid = {slug for slug, _, _ in batch}
    stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    with lock:
        for row in rows if isinstance(rows, list) else []:
            slug = row.get("slug")
            summary = re.sub(r"\s+", " ", str(row.get("summary") or "")).strip()
            if slug in valid and 20 <= len(summary) <= 140:
                store[slug] = {
                    "summary": summary,
                    "why": re.sub(r"\s+", " ", str(row.get("why") or "")).strip()[:110],
                    "title_en": re.sub(r"\s+", " ", str(row.get("title_en") or "")).strip()[:90],
                    "at": stamp,
                }
                stats["done"] += 1
        OUT.write_text(json.dumps(store, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        print("summarize: %d 件完了" % stats["done"], flush=True)


def main():
    parser = argparse.ArgumentParser(description="記事の要約・含意・英語名を作る")
    parser.add_argument("--limit", type=int, default=120)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--model", default="sonnet")
    args = parser.parse_args()

    store = load()
    targets = []
    for path in sorted(CONCEPTS.glob("*.md")):
        slug = path.stem
        if slug in store:
            continue
        markdown = path.read_text(encoding="utf-8")
        match = re.match(r"^# (.+)$", markdown.lstrip(), re.M)
        targets.append((slug, match.group(1).strip() if match else slug, excerpt(markdown)))
        if len(targets) >= args.limit:
            break
    if not targets:
        print("summarize: 対象なし")
        return 0
    print("summarize: %d 件を処理(%s, %d 並列)" % (len(targets), args.model, args.workers), flush=True)
    stats = {"done": 0, "failed": 0, "auth": False, "model": args.model}
    batches = [targets[i:i + BATCH] for i in range(0, len(targets), BATCH)]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for batch in batches:
            pool.submit(run_batch, batch, store, stats)
    if stats["auth"]:
        print("summarize: claude の認証切れ", file=sys.stderr)
        return 3
    print("summarize: %d 件に付与 / 失敗バッチ %d" % (stats["done"], stats["failed"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
