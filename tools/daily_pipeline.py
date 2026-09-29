#!/usr/bin/env python3
"""日次の取得・リーディング・Wikiコンパイルを実行するオーケストレータ。

処理順:
  1. fetch_latest.py で新着論文・記事を取得
  2. tier_classify_cli.py で未分類の論文にTier分類を付与(claude -p 経由・サブスクリプション課金、1日あたり上限あり)
  3. daily_reading.py で当日のリーディングリストを生成
  4. compile_articles_cli.py で未コンパイルの Tier 1/2 論文から wiki 記事を増分生成し、
     新規記事があれば知識グラフと HTML(reader / graph / index)を再生成する
     (claude -p 経由・サブスクリプション課金。1 日 --compile-limit 件まで。--no-compile で止める)

compile_wiki.py は使わない。全コーパス再抽出型で concepts.json を上書きし、
Phase 4 のバリデーションが既存記事の内部リンクを潰すため(2026-08-18 の破損の原因)。

ネットワーク障害時は取得スクリプトの失敗を隠さず、Wikiコンパイルを
スキップして非ゼロ終了する。次回のlaunchd実行で再試行できる。
"""

import argparse
import fcntl
import os
import shlex
import subprocess
import sys
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent
TOOLS = BASE / "tools"
LOG_DIR = BASE / "logs"
LOCK_PATH = LOG_DIR / "daily_pipeline.lock"
STATE_PATH = BASE / "config" / "fetch_state.json"


def load_dotenv(path):
    """Load simple KEY=VALUE entries without printing secret values."""
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if not key or key in os.environ:
            continue
        try:
            parsed = shlex.split(value, comments=True)
            os.environ[key] = parsed[0] if parsed else ""
        except ValueError:
            os.environ[key] = value.strip().strip('"\'')


def load_fetch_state():
    if not STATE_PATH.exists():
        return {}
    import json

    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def run_step(label, command, env):
    print("\n" + "=" * 60)
    print(label)
    print("$ " + " ".join(shlex.quote(str(part)) for part in command))
    print("=" * 60)
    result = subprocess.run(
        command,
        cwd=str(BASE),
        env=env,
        text=True,
        capture_output=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    print("[%s] exit=%d" % (label, result.returncode))
    return result


def main():
    parser = argparse.ArgumentParser(description="研究ナレッジベースの日次パイプライン")
    parser.add_argument("--dry-run", action="store_true", help="取得確認のみ。ファイル変更・読書・コンパイルはしない")
    parser.add_argument("--domain", help="取得対象の分野を1つに限定")
    parser.add_argument("--since", help="取得開始日 (YYYY-MM-DD)")
    parser.add_argument("--no-rss", action="store_true", help="RSS取得をスキップ")
    parser.add_argument("--no-tier", action="store_true", help="Tier分類をスキップ")
    parser.add_argument("--tier-limit", type=int, default=200, help="1回に分類する論文数の上限(既定: 200)")
    parser.add_argument("--no-reading", action="store_true", help="日次リーディングリストをスキップ")
    parser.add_argument("--no-compile", action="store_true", help="wiki 記事の増分生成をスキップ")
    parser.add_argument("--compile-limit", type=int, default=60, help="1回に概念抽出へかける論文数の上限(既定: 60)")
    args = parser.parse_args()

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    lock_handle = open(LOCK_PATH, "a+", encoding="utf-8")
    try:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("別の日次パイプラインが実行中のためスキップします。")
        lock_handle.close()
        return 0

    load_dotenv(BASE / ".env")
    env = os.environ.copy()
    env.setdefault("PYTHONUNBUFFERED", "1")
    python = sys.executable

    fetch_command = [python, str(TOOLS / "fetch_latest.py")]
    if args.dry_run:
        fetch_command.append("--dry-run")
    if args.domain:
        fetch_command.extend(["--domain", args.domain])
    if args.since:
        fetch_command.extend(["--since", args.since])
    if args.no_rss:
        fetch_command.append("--no-rss")
    fetch_result = run_step("1/4 新着論文・記事の取得", fetch_command, env)

    if args.dry_run:
        return fetch_result.returncode

    tier_result = None
    if not args.no_tier:
        # Gemini の無料枠(1日20リクエスト)では足りないため、Claude Code の headless モードで分類する。
        # 従量課金の API キーは tier_classify_cli.py 側で子プロセスから外す。認証切れは終了コード 3。
        tier_result = run_step(
            "2/4 未分類論文のTier分類",
            [python, str(TOOLS / "tier_classify_cli.py"), "--limit", str(args.tier_limit)],
            env,
        )

    reading_result = None
    if not args.no_reading:
        reading_result = run_step(
            "3/4 日次リーディングリストの生成",
            [python, str(TOOLS / "daily_reading.py")],
            env,
        )

    compile_result = None
    if not args.no_compile and args.compile_limit > 0:
        # 未コンパイルの積み残し(2026-09-29 時点で 1,699 件)を毎日 compile_limit 件ずつ記事化する。
        # 取得の成否とは独立に走らせる(取得が失敗した日も積み残しの消化は進める)。
        # モデルは compile_articles_cli.py の既定(抽出・記事とも sonnet。根拠は同スクリプトの docstring)。認証切れは終了コード 3。
        compile_result = run_step(
            "4/4 wiki 記事の増分生成と HTML 再生成",
            [python, str(TOOLS / "compile_articles_cli.py"), "--limit", str(args.compile_limit)],
            env,
        )
    else:
        print("\n4/4 wiki 記事の増分生成: スキップ(--no-compile または --compile-limit 0)")

    results = [fetch_result, tier_result, reading_result, compile_result]
    failures = [result for result in results if result is not None and result.returncode != 0]
    print("\n" + "=" * 60)
    print("日次パイプライン完了: %s" % ("失敗あり" if failures else "成功"))
    print("=" * 60)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
