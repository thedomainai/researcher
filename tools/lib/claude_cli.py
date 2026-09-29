# -*- coding: utf-8 -*-
"""`claude -p`(Claude Code の headless モード)を関数として呼ぶ共通ヘルパー。

サブスクリプション認証(claude.ai ログイン)で動かすための取り決めをここに集約する。

  - 従量課金の API キー(ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN)は子プロセスから外す。
    残っていると Claude Code が API 課金に切り替わる
  - `--tools "" --setting-sources ""` で Claude Code 本体のツール定義・CLAUDE.md・rules を
    読ませない。これが無いと 1 回の呼び出しごとに約 7.5 万トークンの固定文脈が乗る
    (2026-09-29 計測: 74,952 → 165 トークン)。`--bare` は OAuth を読まず "Not logged in" になる
  - 認証切れ(OAuth session expired)は AuthError で区別する。呼び出し側は何も書き換えず
    終了コード 3 で止め、`claude auth login` を待つ
  - 応答は `--output-format json` で受け、本文と usage(トークン数・API 換算額)を返す
"""

import json
import os
import subprocess
import time


class AuthError(RuntimeError):
    pass


def find_claude():
    """claude の実行ファイルを探す。launchd の PATH には ~/.volta/bin 等が入っておらず、
    PATH 任せだと "No such file or directory: 'claude'" で毎回失敗する(2026-09-27/28 の実例)。"""
    explicit = os.environ.get("CLAUDE_BIN")
    if explicit:
        return explicit
    home = os.path.expanduser("~")
    for cand in (
        os.path.join(home, ".volta/tools/image/packages/@anthropic-ai/claude-code/bin/claude"),
        os.path.join(home, ".volta/bin/claude"),
        os.path.join(home, ".local/bin/claude"),
        "/opt/homebrew/bin/claude",
        "/usr/local/bin/claude",
    ):
        if os.path.exists(cand):
            return cand
    return "claude"


CLAUDE_BIN = find_claude()


def _child_env():
    env = {k: v for k, v in os.environ.items() if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")}
    env["CLAUDECODE"] = ""  # ネストした Claude Code セッションからでも起動できるようにする
    # 認証情報(キーチェーン)の読み出しには HOME / USER / LOGNAME が要る。最小環境では欠けるので補う
    home = os.path.expanduser("~")
    env.setdefault("HOME", home)
    env.setdefault("USER", os.path.basename(home))
    env.setdefault("LOGNAME", env["USER"])
    # node の実行ファイルと claude 本体が入っているディレクトリを PATH に足す
    extra = [os.path.dirname(CLAUDE_BIN), os.path.join(home, ".volta/bin"), "/opt/homebrew/bin", "/usr/local/bin"]
    env["PATH"] = ":".join([d for d in extra if d] + [env.get("PATH", "/usr/bin:/bin")])
    return env


def call_claude(prompt, system_prompt, model="haiku", timeout=600, retries=3, cwd=None):
    """claude -p を呼び、(本文テキスト, usage dict) を返す。認証切れは AuthError。

    usage には input_tokens / cache_creation_input_tokens / cache_read_input_tokens /
    output_tokens / total_cost_usd(API 換算の参考値。課金の証拠ではない)を入れる。
    """
    cmd = [
        CLAUDE_BIN, "-p", "--model", model, "--output-format", "json",
        "--system-prompt", system_prompt,
        "--tools", "", "--setting-sources", "",
        "--no-session-persistence",
    ]
    env = _child_env()
    last_msg = ""
    for attempt in range(retries):
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, env=env, timeout=timeout, cwd=cwd)
        try:
            data = json.loads(r.stdout)
        except ValueError:
            data = {}
        text = data.get("result") or ""
        if data.get("is_error") or r.returncode != 0:
            last_msg = text or r.stderr[:300]
            low = last_msg.lower()
            if "authenticate" in low or "oauth" in low or "login" in low or "not logged in" in low:
                raise AuthError(last_msg)
            if attempt < retries - 1:
                time.sleep(20 * (attempt + 1))
                continue
            raise RuntimeError("claude -p 失敗: %s" % last_msg[:300])
        u = data.get("usage") or {}
        usage = {
            "model": model,
            "input_tokens": int(u.get("input_tokens") or 0),
            "cache_creation_input_tokens": int(u.get("cache_creation_input_tokens") or 0),
            "cache_read_input_tokens": int(u.get("cache_read_input_tokens") or 0),
            "output_tokens": int(u.get("output_tokens") or 0),
            "total_cost_usd": float(data.get("total_cost_usd") or 0.0),
        }
        return text, usage
    raise RuntimeError("claude -p: 再試行上限 (%s)" % last_msg[:200])


def strip_code_fence(text):
    """```json ... ``` のフェンスを外す。"""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1] if "\n" in cleaned else ""
        if cleaned.rstrip().endswith("```"):
            cleaned = cleaned.rstrip()[:-3]
    return cleaned.strip()


class UsageTally(object):
    """複数回の呼び出しの usage を合算する。"""

    def __init__(self):
        self.calls = 0
        self.by_model = {}

    def add(self, usage):
        self.calls += 1
        m = self.by_model.setdefault(usage["model"], {"calls": 0, "in": 0, "out": 0, "usd": 0.0})
        m["calls"] += 1
        m["in"] += usage["input_tokens"] + usage["cache_creation_input_tokens"] + usage["cache_read_input_tokens"]
        m["out"] += usage["output_tokens"]
        m["usd"] += usage["total_cost_usd"]

    def summary(self):
        parts = []
        for model, m in sorted(self.by_model.items()):
            parts.append("%s: %d回 入力%d 出力%d (API換算 $%.3f)" % (model, m["calls"], m["in"], m["out"], m["usd"]))
        return "; ".join(parts) if parts else "呼び出しなし"
