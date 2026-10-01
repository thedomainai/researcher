"""X API v2 の薄いラッパー(OAuth 1.0a ユーザーコンテキスト)。

投稿: POST https://api.x.com/2/tweets
鍵の所在:
  X_CONSUMER_KEY / X_CONSUMER_SECRET            アプリ共通(Developer Portal の Keys and tokens)
  <PREFIX>_ACCESS_TOKEN / <PREFIX>_ACCESS_SECRET  アカウントごと(tools/x_authorize.py で取得)
"""

import os

try:
    from requests_oauthlib import OAuth1Session
except ImportError:  # pragma: no cover
    OAuth1Session = None

API_BASE = "https://api.x.com"
REQUEST_TOKEN_URL = API_BASE + "/oauth/request_token"
AUTHORIZE_URL = API_BASE + "/oauth/authorize"
ACCESS_TOKEN_URL = API_BASE + "/oauth/access_token"


class XConfigError(RuntimeError):
    pass


def app_keys():
    key = os.environ.get("X_CONSUMER_KEY", "").strip()
    secret = os.environ.get("X_CONSUMER_SECRET", "").strip()
    if not key or not secret:
        raise XConfigError("X_CONSUMER_KEY / X_CONSUMER_SECRET が未設定です(.env に置く)")
    return key, secret


def account_tokens(prefix):
    token = os.environ.get(prefix + "_ACCESS_TOKEN", "").strip()
    secret = os.environ.get(prefix + "_ACCESS_SECRET", "").strip()
    if not token or not secret:
        return None
    return token, secret


def session(prefix):
    if OAuth1Session is None:
        raise XConfigError("requests_oauthlib が無い(pip3 install --user requests_oauthlib)")
    key, secret = app_keys()
    tokens = account_tokens(prefix)
    if not tokens:
        raise XConfigError("%s_ACCESS_TOKEN / %s_ACCESS_SECRET が未設定です" % (prefix, prefix))
    return OAuth1Session(key, client_secret=secret, resource_owner_key=tokens[0], resource_owner_secret=tokens[1])


def post_tweet(prefix, text, timeout=30):
    """投稿して tweet id を返す。失敗は RuntimeError(本文に HTTP ステータスと応答を含む)。"""
    sess = session(prefix)
    response = sess.post(API_BASE + "/2/tweets", json={"text": text}, timeout=timeout)
    if response.status_code not in (200, 201):
        raise RuntimeError("X API %d: %s" % (response.status_code, response.text[:300]))
    data = response.json().get("data") or {}
    return data.get("id", "")


def whoami(prefix, timeout=30):
    sess = session(prefix)
    response = sess.get(API_BASE + "/2/users/me", timeout=timeout)
    if response.status_code != 200:
        raise RuntimeError("X API %d: %s" % (response.status_code, response.text[:300]))
    return response.json().get("data") or {}
