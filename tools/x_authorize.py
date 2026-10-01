#!/usr/bin/env python3
"""X アカウントのアクセストークンを PIN 方式(OAuth 1.0a out-of-band)で取得し、.env に書き込む。

前提: .env に X_CONSUMER_KEY / X_CONSUMER_SECRET(Developer Portal のアプリ鍵。
      アプリの User authentication settings で Read and write を有効にしておく)。

使い方(アカウントごとに 1 回):
  python3 tools/x_authorize.py --cluster cognition
  → 表示された URL をブラウザで開き、そのクラスター用の X アカウントでログインして承認し、
    表示された PIN を入力する。.env に X_COGNITION_ACCESS_TOKEN / _ACCESS_SECRET が追記される。
"""

import argparse
import os
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import x_api  # noqa: E402
from daily_pipeline import load_dotenv  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
ENV_PATH = BASE / ".env"
ACCOUNTS = BASE / "config" / "x_accounts.yaml"


def upsert_env(path, values):
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    for key, value in values.items():
        pattern = re.compile(r"^(export\s+)?%s=" % re.escape(key))
        replaced = False
        for idx, line in enumerate(lines):
            if pattern.match(line.strip()):
                lines[idx] = "export %s=%s" % (key, value)
                replaced = True
        if not replaced:
            lines.append("export %s=%s" % (key, value))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    os.chmod(path, 0o600)


def main():
    parser = argparse.ArgumentParser(description="X アカウントの認可(PIN 方式)")
    parser.add_argument("--cluster", required=True, help="config/x_accounts.yaml の cluster キー")
    args = parser.parse_args()

    load_dotenv(ENV_PATH)
    accounts = yaml.safe_load(ACCOUNTS.read_text(encoding="utf-8"))["accounts"]
    account = next((a for a in accounts if a["cluster"] == args.cluster), None)
    if not account:
        print("未知の cluster: %s" % args.cluster, file=sys.stderr)
        return 2
    prefix = account["env_prefix"]

    from requests_oauthlib import OAuth1Session

    key, secret = x_api.app_keys()
    oauth = OAuth1Session(key, client_secret=secret, callback_uri="oob")
    try:
        request = oauth.fetch_request_token(x_api.REQUEST_TOKEN_URL)
    except Exception as exc:  # noqa: BLE001
        print("request_token の取得に失敗: %s" % exc, file=sys.stderr)
        print("Developer Portal でアプリの User authentication settings(OAuth 1.0a, Read and write)を確認してください。", file=sys.stderr)
        return 1
    url = oauth.authorization_url(x_api.AUTHORIZE_URL)
    print("\n1. 次の URL をブラウザで開き、cluster=%s 用の X アカウントでログインして承認してください:\n\n   %s\n" % (args.cluster, url))
    pin = input("2. 表示された PIN を入力: ").strip()
    oauth = OAuth1Session(
        key, client_secret=secret,
        resource_owner_key=request["oauth_token"], resource_owner_secret=request["oauth_token_secret"],
        verifier=pin,
    )
    tokens = oauth.fetch_access_token(x_api.ACCESS_TOKEN_URL)
    upsert_env(ENV_PATH, {
        prefix + "_ACCESS_TOKEN": tokens["oauth_token"],
        prefix + "_ACCESS_SECRET": tokens["oauth_token_secret"],
    })
    os.environ[prefix + "_ACCESS_TOKEN"] = tokens["oauth_token"]
    os.environ[prefix + "_ACCESS_SECRET"] = tokens["oauth_token_secret"]
    me = x_api.whoami(prefix)
    print("\n認可完了: @%s (id %s) を cluster=%s として .env に保存しました。" % (me.get("username"), me.get("id"), args.cluster))
    if account.get("handle") and account["handle"] != me.get("username"):
        print("注意: config/x_accounts.yaml の handle(%s)と一致しません。" % account["handle"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
