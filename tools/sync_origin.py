#!/usr/bin/env python3
"""日次パイプラインの最初に、ローカル main を origin/main に追従させる(fast-forward のみ)。

クラウドのセッションや別のマシンが origin へ push していると、ローカルが遅れたまま
記事生成が走り、既に記事化された論文を二重に記事化する(2026-10-01 の実例: 15 本が重複)。
そのため、取得・生成の前に origin を取り込む。

安全側の設計:
  - fast-forward できるときだけ進める(`git merge --ff-only`)。作業ツリーの未コミット変更が
    取り込みと衝突するときは git が拒否するので、そのまま終了コード 1 で止める
  - ローカルにだけあるコミットがある(分岐している)ときは何もせず、終了コード 2 で知らせる。
    `git reset --keep origin/main` 等の判断は人(または担当セッション)に委ねる
  - ネットワーク障害で fetch できないときは終了コード 1(その日の publish は rebase 側で再び止まる)
"""

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def git(*args, check=False):
    return subprocess.run(["git", *args], cwd=str(BASE), text=True, capture_output=True, check=check)


def main():
    fetch = git("fetch", "-q", "origin", "main")
    if fetch.returncode != 0:
        print("sync: fetch に失敗: %s" % (fetch.stderr.strip() or fetch.stdout.strip())[:300], file=sys.stderr)
        return 1
    behind = git("rev-list", "--count", "HEAD..origin/main").stdout.strip()
    ahead = git("rev-list", "--count", "origin/main..HEAD").stdout.strip()
    if behind == "0":
        print("sync: origin/main と同期済み(ローカル先行 %s)" % ahead)
        return 0
    if ahead != "0":
        print("sync: ローカル main が origin/main と分岐しています(origin 先行 %s / ローカル先行 %s)。"
              "自動では進めません。`git reset --keep origin/main` などで揃えてください。" % (behind, ahead), file=sys.stderr)
        return 2
    merge = git("merge", "-q", "--ff-only", "origin/main")
    if merge.returncode != 0:
        print("sync: fast-forward できませんでした(未コミットの変更が衝突している可能性): %s"
              % (merge.stderr.strip() or merge.stdout.strip())[:300], file=sys.stderr)
        return 1
    print("sync: origin/main を取り込みました(%s コミット)" % behind)
    return 0


if __name__ == "__main__":
    sys.exit(main())
