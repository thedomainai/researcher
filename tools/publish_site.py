#!/usr/bin/env python3
"""日次パイプラインの成果(取得した論文・生成した記事・メタデータ)をコミットして origin へ push する。

push を受けて GitHub Actions(.github/workflows/pages.yml)が公開サイトを再生成する。
サイトの生成自体はここでは行わない(ローカルの site/ は確認用で、git 管理外)。

コミット対象は次のパスに限る。ログや作業中のコード変更は含めない。
  raw/  wiki/  config/fetch_state.json  config/reading_state.json  config/x_post_state.json

使い方:
  python3 tools/publish_site.py            # 変更があればコミットして push
  python3 tools/publish_site.py --dry-run  # 何をコミットするかを表示するだけ
"""

import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
PATHS = ["raw", "wiki", "config/fetch_state.json", "config/reading_state.json", "config/x_post_state.json"]


def git(*args, check=True, capture=True):
    result = subprocess.run(["git", *args], cwd=str(BASE), text=True, capture_output=capture)
    if check and result.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), (result.stderr or result.stdout).strip()))
    return result


def main():
    parser = argparse.ArgumentParser(description="日次成果のコミットと push")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-push", action="store_true", help="コミットだけして push しない")
    args = parser.parse_args()

    existing = [p for p in PATHS if (BASE / p).exists()]
    status = git("status", "--porcelain", "--", *existing).stdout
    changed = [line for line in status.splitlines() if line.strip()]
    if not changed:
        print("publish: 変更なし")
        return 0
    added = sum(1 for l in changed if l.startswith("??") or l[0] == "A")
    modified = len(changed) - added
    print("publish: 変更 %d 件(新規 %d / 更新 %d)" % (len(changed), added, modified))
    if args.dry_run:
        for line in changed[:40]:
            print("  " + line)
        if len(changed) > 40:
            print("  ... 他 %d 件" % (len(changed) - 40))
        return 0

    git("add", "--", *existing)
    today = dt.date.today().isoformat()
    message = "data: daily pipeline %s (%d files)\n\nAutomated commit by tools/publish_site.py." % (today, len(changed))
    git("commit", "-q", "-m", message)
    print("publish: committed %s" % git("rev-parse", "--short", "HEAD").stdout.strip())
    if args.no_push:
        return 0

    git("fetch", "-q", "origin", "main")
    behind = git("rev-list", "--count", "HEAD..origin/main").stdout.strip()
    if behind != "0":
        # 他の場所からの push があれば、自分のコミットをその上に乗せ替える(未コミットの他ファイルは autostash で退避)
        rebase = git("rebase", "--autostash", "origin/main", check=False)
        if rebase.returncode != 0:
            git("rebase", "--abort", check=False)
            print("publish: rebase に失敗。push を見送る(次回に再試行)", file=sys.stderr)
            print(rebase.stderr or rebase.stdout, file=sys.stderr)
            return 1
    push = git("push", "-q", "origin", "HEAD:main", check=False)
    if push.returncode != 0:
        print("publish: push 失敗\n" + (push.stderr or push.stdout), file=sys.stderr)
        return 1
    print("publish: pushed to origin/main")
    return 0


if __name__ == "__main__":
    sys.exit(main())
