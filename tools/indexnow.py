#!/usr/bin/env python3
"""更新した記事の URL を IndexNow(Bing・Yandex 等)へ通知する。アカウントは要らない。

鍵は config/site.yaml の search.indexnow_key(公開値)。サイトに <key>.txt として配信されている必要があるため、
GitHub Pages の配置が終わった後(.github/workflows/pages.yml の notify ジョブ)に実行する。

使い方:
  python3 tools/indexnow.py --since-days 3   # 直近 3 日に公開・更新した記事と一覧ページ
  python3 tools/indexnow.py --all            # 全 URL(初回・URL 構成を変えたとき)
  python3 tools/indexnow.py --all --dry-run
"""

import argparse
import datetime as dt
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_site  # noqa: E402

ENDPOINT = "https://api.indexnow.org/indexnow"


def main():
    parser = argparse.ArgumentParser(description="IndexNow へ更新 URL を通知する")
    parser.add_argument("--since-days", type=int, default=3)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config = build_site.load_config()
    key = (config.get("search") or {}).get("indexnow_key") or ""
    if not key:
        print("indexnow: 鍵が未設定のためスキップ")
        return 0
    base = config["site"]["url"]
    catalog = build_site.load_catalog(config)
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.since_days)
    urls = []
    for item in catalog:
        if not args.all:
            try:
                modified = dt.datetime.fromisoformat(item["modified"])
            except ValueError:
                continue
            if modified < cutoff:
                continue
        urls.append("%s/%s" % (base, item["path"]))
    if urls:
        urls = [base + "/", base + "/concepts/"] + ["%s/clusters/%s/" % (base, c["key"]) for c in config["clusters"]] + urls
    if not urls:
        print("indexnow: 通知対象なし")
        return 0
    print("indexnow: %d URL" % len(urls))
    if args.dry_run:
        print("\n".join(urls[:10]))
        return 0
    host = urlparse(base).netloc
    status = 0
    for start in range(0, len(urls), 10000):
        payload = {"host": host, "key": key, "keyLocation": "%s/%s.txt" % (base, key), "urlList": urls[start:start + 10000]}
        request = urllib.request.Request(
            ENDPOINT, data=json.dumps(payload).encode("utf-8"), method="POST",
            headers={"Content-Type": "application/json; charset=utf-8"})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                print("indexnow: HTTP %d" % response.status)
        except urllib.error.HTTPError as exc:
            print("indexnow: HTTP %d %s" % (exc.code, exc.read().decode("utf-8", "replace")[:200]), file=sys.stderr)
            status = 1
        except urllib.error.URLError as exc:
            print("indexnow: 接続失敗 %s" % exc, file=sys.stderr)
            status = 1
    return status


if __name__ == "__main__":
    sys.exit(main())
