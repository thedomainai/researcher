#!/usr/bin/env python3
"""分野情報の無い記事に、claude -p(haiku)で分野(config/sources.yaml の research_domains)を付ける。

対象: build_site.load_catalog() で domain_source が "guess"(メタデータにも出典論文にも分野が無い)の記事。
出力: wiki/_meta/domain_overrides.json({slug: {"domains": [...], "cluster": key, "at": ..}})。
      build_site.py はメタデータ → この上書き → 出典論文 → 語の推定 の順で分野を決める。

使い方:
  python3 tools/classify_domains_cli.py --limit 60      # 日次パイプラインの既定
  python3 tools/classify_domains_cli.py --dry-run
"""

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.claude_cli import call_claude, AuthError, strip_code_fence  # noqa: E402
import build_site  # noqa: E402

OVERRIDES = Path(build_site.OVERRIDES_FILE)
BATCH = 20

SYSTEM_PROMPT = """あなたは学際的な研究ナレッジベースの司書です。日本語の概念記事に、最も関連の深い学問分野を 1〜3 つ割り当てます。
分野は与えられた一覧のキーから選びます。一覧に無いキーは使いません。先頭に最も代表的な分野を置きます。
出力は JSON 配列だけ: [{"slug": "...", "domains": ["key1", "key2"]}, ...]"""


def main():
    parser = argparse.ArgumentParser(description="分野の無い記事を claude -p で分類する")
    parser.add_argument("--limit", type=int, default=60)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config = build_site.load_config()
    labels = config["domain_labels"]
    catalog = build_site.load_catalog(config)
    targets = [i for i in catalog if i["domain_source"] == "guess"][: args.limit]
    if not targets:
        print("classify_domains: 対象なし")
        return 0
    print("classify_domains: %d 件を分類" % len(targets))
    overrides = build_site.load_json(str(OVERRIDES), {})
    domain_list = "\n".join("- %s: %s" % (k, v) for k, v in labels.items())
    done = 0
    for start in range(0, len(targets), BATCH):
        batch = targets[start:start + BATCH]
        articles = "\n\n".join(
            "### slug: %s\nタイトル: %s\n要約: %s\n本文冒頭: %s" % (
                i["slug"], i["title"], i["description"], build_site.truncate(build_site.first_paragraph(i["markdown"]), 400))
            for i in batch)
        prompt = "## 分野一覧(キー: 名称)\n%s\n\n## 記事\n%s\n\n各記事に分野を割り当て、JSON 配列で返してください。" % (domain_list, articles)
        if args.dry_run:
            print(prompt[:1500] + "\n...")
            continue
        try:
            text, _usage = call_claude(prompt, SYSTEM_PROMPT, model="haiku", timeout=300, retries=2)
            rows = json.loads(strip_code_fence(text))
        except AuthError as exc:
            print("classify_domains: claude の認証切れ: %s" % str(exc)[:100], file=sys.stderr)
            return 3
        except (ValueError, RuntimeError) as exc:
            print("classify_domains: バッチ %d の失敗: %s" % (start // BATCH + 1, str(exc)[:200]), file=sys.stderr)
            continue
        valid = {i["slug"] for i in batch}
        stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        for row in rows if isinstance(rows, list) else []:
            slug = row.get("slug")
            domains = [d for d in (row.get("domains") or []) if d in labels and d in config["domain_to_cluster"]]
            if slug in valid and domains:
                overrides[slug] = {"domains": domains[:3], "cluster": config["domain_to_cluster"][domains[0]], "at": stamp}
                done += 1
        OVERRIDES.write_text(json.dumps(overrides, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print("classify_domains: %d 件に分野を付与 -> %s" % (done, OVERRIDES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
