#!/usr/bin/env python3
"""領域クラスター別の X アカウントへ、公開サイトの記事を自動投稿する。

選定: そのクラスターの未投稿記事から、新着(new_article_days 以内に公開)→ Tier 1 → Tier 2 の順。
本文: claude -p(haiku、サブスクリプション課金)で 110 字以内の日本語の紹介文を作り、記事 URL を添える。
      LLM が使えないときは「タイトル + 説明」の定型文で代替する。
記録: config/x_post_state.json(slug ごとの投稿日時・tweet id)。同じ記事は同じアカウントに二度投稿しない。
鍵:   .env の X_CONSUMER_KEY / X_CONSUMER_SECRET と、アカウントごとの <PREFIX>_ACCESS_TOKEN / _ACCESS_SECRET。
      鍵の無いアカウントは静かにスキップする(日次パイプラインを止めない)。

使い方:
  python3 tools/post_x.py --dry-run             # 投稿文の生成まで行い、投稿はしない
  python3 tools/post_x.py --cluster ai --limit 1
  python3 tools/post_x.py                       # 全アカウント、既定の posts_per_day 件ずつ
"""

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import x_api  # noqa: E402
from lib.claude_cli import call_claude, AuthError  # noqa: E402
from daily_pipeline import load_dotenv  # noqa: E402
import build_site  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
ACCOUNTS = BASE / "config" / "x_accounts.yaml"
STATE = BASE / "config" / "x_post_state.json"
URL_LENGTH = 23  # X は URL を t.co で 23 字に数える
TEXT_LIMIT = 280

SYSTEM_PROMPT = """あなたは研究ナレッジベース「Researcher」の編集者です。学術論文をもとに生成された日本語記事を、X(旧 Twitter)で紹介する投稿文を書きます。

制約:
- 日本語。全角 110 字以内(URL は後から別に付けるので含めない)
- 記事の核心の洞察を 1 つ、具体的に書く。「〜について解説」のような空疎な要約は禁止
- 煽り・誇張・断定の強すぎる表現は禁止。論文に基づく記述であることが伝わる落ち着いた文体
- 絵文字は使わない。ハッシュタグは最大 2 つ、末尾にまとめる(例: #組織設計 #AI)
- 出力は投稿文だけ。前置き・引用符・説明は不要"""


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"posted": {}, "runs": []}


def save_state(state):
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def weighted_len(text):
    """X の文字数(簡易): 全角・漢字は 2、それ以外は 1 として 280 上限と比べる。"""
    total = 0
    for ch in text:
        total += 2 if ord(ch) > 0x2E7F else 1
    return total


def fallback_text(item, cluster_label, hashtags):
    body = "【%s】%s" % (item["title"], item["description"])
    body = build_site.truncate(body, 100)
    return "%s\n%s" % (body, " ".join(hashtags)) if hashtags else body


def generate_text(item, cluster_label, hashtags, use_llm=True):
    if use_llm:
        prompt = (
            "記事タイトル: %s\n領域: %s\n要約: %s\n使ってよいハッシュタグ: %s\n\n本文(冒頭):\n%s\n\n上の記事を紹介する投稿文を 1 つ書いてください。"
            % (item["title"], cluster_label, item["description"], " ".join(hashtags) or "なし", item["markdown"][:2500])
        )
        try:
            text, _usage = call_claude(prompt, SYSTEM_PROMPT, model="haiku", timeout=180, retries=2)
            text = text.strip().strip('"「」')
            if text and len(text) <= 150:
                return text, "llm"
        except AuthError as exc:
            print("post_x: claude の認証切れ。定型文で代替します(%s)" % str(exc)[:80], file=sys.stderr)
        except Exception as exc:  # noqa: BLE001
            print("post_x: 投稿文の生成に失敗。定型文で代替します(%s)" % str(exc)[:120], file=sys.stderr)
    return fallback_text(item, cluster_label, hashtags), "fallback"


def compose(text, url):
    full = "%s\n%s" % (text, url)
    # URL は 23 字換算なので、本文側だけで上限を見る
    while weighted_len(text) + 1 + URL_LENGTH > TEXT_LIMIT and len(text) > 10:
        text = text[:-1]
        full = "%s…\n%s" % (text.rstrip(), url)
    return full


def pick_candidates(catalog, cluster_key, posted, new_days, limit):
    now = dt.datetime.now(dt.timezone.utc)
    pool = []
    for item in catalog:
        if item["cluster"] != cluster_key or item["tier"] == 3:
            continue
        key = "%s:%s" % (cluster_key, item["slug"])
        if key in posted:
            continue
        try:
            published = dt.datetime.fromisoformat(item["published"])
            if published.tzinfo is None:
                published = published.replace(tzinfo=dt.timezone.utc)
        except ValueError:
            published = now
        is_new = (now - published).days <= new_days
        pool.append((0 if is_new else 1, item["tier"], -published.timestamp(), item["title"], item))
    pool.sort(key=lambda row: row[:4])
    return [row[-1] for row in pool[:limit]]


def main():
    parser = argparse.ArgumentParser(description="X への自動投稿")
    parser.add_argument("--dry-run", action="store_true", help="投稿せず、文面だけ表示する")
    parser.add_argument("--cluster", help="特定のクラスターだけ")
    parser.add_argument("--limit", type=int, help="1 アカウントあたりの投稿数(既定: 設定の posts_per_day)")
    parser.add_argument("--no-llm", action="store_true", help="claude -p を使わず定型文で投稿する")
    args = parser.parse_args()

    load_dotenv(BASE / ".env")
    spec = yaml.safe_load(ACCOUNTS.read_text(encoding="utf-8"))
    defaults = spec.get("defaults") or {}
    per_day = args.limit or int(defaults.get("posts_per_day", 2))
    new_days = int(defaults.get("new_article_days", 14))
    hashtags_max = int(defaults.get("hashtags_max", 2))

    config = build_site.load_config()
    labels = {c["key"]: c["label"] for c in config["clusters"]}
    base_url = config["site"]["url"]
    catalog = build_site.load_catalog(config)
    state = load_state()
    posted = state.setdefault("posted", {})

    summary = []
    failures = 0
    for account in spec.get("accounts", []):
        cluster = account["cluster"]
        if args.cluster and cluster != args.cluster:
            continue
        if not account.get("enabled", True):
            continue
        prefix = account["env_prefix"]
        has_keys = x_api.account_tokens(prefix) is not None
        try:
            x_api.app_keys()
            app_ok = True
        except x_api.XConfigError:
            app_ok = False
        if not (has_keys and app_ok) and not args.dry_run:
            summary.append("%s: 鍵なし(スキップ)" % cluster)
            continue

        hashtags = [h for h in (account.get("hashtags") or [])][:hashtags_max]
        candidates = pick_candidates(catalog, cluster, posted, new_days, per_day)
        if not candidates:
            summary.append("%s: 未投稿の記事なし" % cluster)
            continue
        for item in candidates:
            url = "%s/%s" % (base_url, item["path"])
            text, source = generate_text(item, labels[cluster], hashtags, use_llm=not args.no_llm)
            full = compose(text, url)
            if args.dry_run:
                print("\n--- [%s] %s (%s)\n%s" % (cluster, item["slug"], source, full))
                continue
            try:
                tweet_id = x_api.post_tweet(prefix, full)
            except Exception as exc:  # noqa: BLE001
                failures += 1
                print("post_x: %s の投稿に失敗: %s" % (cluster, str(exc)[:200]), file=sys.stderr)
                break  # 同じアカウントで続けて失敗させない(レート制限・凍結の疑い)
            posted["%s:%s" % (cluster, item["slug"])] = {
                "cluster": cluster, "slug": item["slug"], "tweet_id": tweet_id,
                "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "source": source,
            }
            save_state(state)
            summary.append("%s: %s -> tweet %s" % (cluster, item["slug"], tweet_id))

    if not args.dry_run:
        state.setdefault("runs", []).append({
            "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "posted": sum(1 for s in summary if "-> tweet" in s), "failures": failures,
        })
        state["runs"] = state["runs"][-90:]
        save_state(state)
    if summary:
        print("\n".join(summary))
    elif not args.dry_run:
        print("post_x: 対象アカウントなし")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
