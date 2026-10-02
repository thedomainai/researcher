#!/usr/bin/env python3
"""GA4 と Search Console から、公開サイトの計測値を取得して config/metrics.json に追記する。

ゴール(公開から 12 か月で累計 100 万 PV)に対する進捗と、日次の目標ペースとの差を表示する。
認証はサービスアカウントの鍵(既定: ~/.config/gcloud/claude-code-sa-key.json、環境変数 METRICS_SA_KEY で変更可)。
GA4 のプロパティ ID と Search Console のサイトは config/site.yaml の metrics ブロックに置く。
読み取り専用(GA4 は analytics.readonly、Search Console は webmasters.readonly)。

使い方:
  python3 tools/report_metrics.py            # 公開日から今日までを取得して保存し、要約を表示
  python3 tools/report_metrics.py --days 14  # 直近 14 日だけ取り直す
  python3 tools/report_metrics.py --no-save  # 保存せず表示だけ
"""

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
CONFIG = BASE / "config" / "site.yaml"
STORE = BASE / "config" / "metrics.json"


def credentials(scopes):
    from google.oauth2 import service_account
    import google.auth.transport.requests
    key = os.environ.get("METRICS_SA_KEY") or os.path.expanduser("~/.config/gcloud/claude-code-sa-key.json")
    creds = service_account.Credentials.from_service_account_file(key, scopes=scopes)
    creds.refresh(google.auth.transport.requests.Request())
    return creds.token


def post(url, token, body):
    req = urllib.request.Request(url, method="POST", data=json.dumps(body).encode("utf-8"),
                                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return json.loads(response.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        try:
            detail = json.loads(detail)["error"]["message"]
        except Exception:  # noqa: BLE001
            pass
        raise RuntimeError("HTTP %d: %s" % (exc.code, str(detail)[:200]))


def get(url, token):
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + token})
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.loads(response.read().decode("utf-8") or "{}")


def ga4_daily(property_id, start, end):
    token = credentials(["https://www.googleapis.com/auth/analytics.readonly"])
    url = "https://analyticsdata.googleapis.com/v1beta/%s:runReport" % property_id
    base = {"dateRanges": [{"startDate": start, "endDate": end}], "limit": 10000}
    daily = post(url, token, dict(base, dimensions=[{"name": "date"}],
                                  metrics=[{"name": "screenPageViews"}, {"name": "activeUsers"}, {"name": "sessions"}]))
    sources = post(url, token, dict(base, dimensions=[{"name": "date"}, {"name": "sessionDefaultChannelGroup"}],
                                    metrics=[{"name": "screenPageViews"}]))
    pages = post(url, token, dict(base, dimensions=[{"name": "pagePath"}], metrics=[{"name": "screenPageViews"}],
                                  orderBys=[{"metric": {"metricName": "screenPageViews"}, "desc": True}]))
    out = {}
    for row in daily.get("rows", []):
        d = row["dimensionValues"][0]["value"]
        date = "%s-%s-%s" % (d[:4], d[4:6], d[6:])
        v = [int(m["value"]) for m in row["metricValues"]]
        out[date] = {"pv": v[0], "users": v[1], "sessions": v[2], "channels": {}}
    for row in sources.get("rows", []):
        d = row["dimensionValues"][0]["value"]
        date = "%s-%s-%s" % (d[:4], d[4:6], d[6:])
        if date in out:
            out[date]["channels"][row["dimensionValues"][1]["value"]] = int(row["metricValues"][0]["value"])
    top = [(r["dimensionValues"][0]["value"], int(r["metricValues"][0]["value"])) for r in pages.get("rows", [])[:10]]
    return out, top


def search_console(site, start, end):
    token = credentials(["https://www.googleapis.com/auth/webmasters.readonly"])
    url = "https://www.googleapis.com/webmasters/v3/sites/%s/searchAnalytics/query" % urllib.parse.quote(site, safe="")
    data = post(url, token, {"startDate": start, "endDate": end, "dimensions": ["date"], "rowLimit": 1000})
    out = {}
    for row in data.get("rows", []):
        out[row["keys"][0]] = {"clicks": int(row["clicks"]), "impressions": int(row["impressions"]),
                               "position": round(row["position"], 1)}
    sm = get("https://www.googleapis.com/webmasters/v3/sites/%s/sitemaps" % urllib.parse.quote(site, safe=""), token)
    sitemaps = []
    for entry in sm.get("sitemap", []):
        contents = entry.get("contents") or []
        sitemaps.append({"path": entry.get("path"), "submitted": sum(int(c.get("submitted", 0)) for c in contents),
                         "indexed": sum(int(c.get("indexed", 0)) for c in contents),
                         "errors": int(entry.get("errors", 0) or 0), "warnings": int(entry.get("warnings", 0) or 0),
                         "last_downloaded": entry.get("lastDownloaded")})
    return out, sitemaps


def main():
    parser = argparse.ArgumentParser(description="GA4 と Search Console の計測値を取得する")
    parser.add_argument("--days", type=int, help="直近 N 日だけ取得する(既定: 公開日から)")
    parser.add_argument("--no-save", action="store_true")
    args = parser.parse_args()

    cfg = (yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}).get("metrics") or {}
    launch = dt.date.fromisoformat(cfg.get("launch_date", "2026-10-01"))
    goal = int(cfg.get("goal_pv", 1000000))
    horizon = dt.date.fromisoformat(cfg.get("goal_date", "2027-09-30"))
    today = dt.date.today()
    start = launch if not args.days else max(launch, today - dt.timedelta(days=args.days))
    s, e = start.isoformat(), today.isoformat()

    store = json.loads(STORE.read_text(encoding="utf-8")) if STORE.exists() else {"daily": {}, "sitemaps": [], "top_pages": []}
    errors = []
    try:
        ga, top = ga4_daily(cfg["ga4_property"], s, e)
        for date, row in ga.items():
            store["daily"].setdefault(date, {}).update(row)
        store["top_pages"] = top
    except Exception as exc:  # noqa: BLE001
        errors.append("GA4: %s" % exc)
    try:
        sc, sitemaps = search_console(cfg["search_console_site"], s, e)
        for date, row in sc.items():
            store["daily"].setdefault(date, {}).update({"sc": row})
        store["sitemaps"] = sitemaps
    except Exception as exc:  # noqa: BLE001
        errors.append("Search Console: %s" % exc)
    store["updated"] = dt.datetime.now().isoformat(timespec="seconds")
    if not args.no_save:
        STORE.write_text(json.dumps(store, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")

    daily = store["daily"]
    total = sum(v.get("pv", 0) for v in daily.values())
    days_total = (horizon - launch).days + 1
    elapsed = (today - launch).days + 1
    target_to_date = goal * elapsed / days_total
    recent = [daily.get((today - dt.timedelta(days=i)).isoformat(), {}).get("pv", 0) for i in range(1, 8)]
    print("公開 %s からの累計 PV: %s / %s (%.2f%%)" % (launch, format(total, ","), format(goal, ","), 100.0 * total / goal))
    print("線形ペースの目標(今日まで): %s。差: %s" % (format(int(target_to_date), ","), format(int(total - target_to_date), ",")))
    print("直近 7 日(昨日まで)の 1 日平均: %.0f PV。目標達成に必要な 1 日平均: %.0f PV" % (
        sum(recent) / 7.0, max(0.0, goal - total) / max(1, (horizon - today).days)))
    last = sorted(daily)[-5:]
    for d in last:
        row = daily[d]
        sc = row.get("sc") or {}
        print("  %s  PV %-5s ユーザー %-5s 検索クリック %-4s 表示 %-5s 流入 %s" % (
            d, row.get("pv", "-"), row.get("users", "-"), sc.get("clicks", "-"), sc.get("impressions", "-"), row.get("channels", {})))
    for sm in store.get("sitemaps", []):
        print("  sitemap %s: 送信 %s / インデックス %s / エラー %s" % (sm["path"], sm["submitted"], sm["indexed"], sm["errors"]))
    for message in errors:
        print("取得エラー: " + message, file=sys.stderr)
    return 1 if errors and len(errors) >= 2 else 0


if __name__ == "__main__":
    sys.exit(main())
