# -*- coding: utf-8 -*-
"""日次パイプラインのネットワーク待ちと git のリトライ。

launchd の 6:00 起動は、スリープ復帰の直後でネットワークがまだ上がっていないことがある。
2026-11 に `Could not resolve host: github.com` と、github.com:443 への 75 秒の接続失敗で
origin への追従(0/6)と push(5/6)が失敗した。接続できるまで待ち、git の通信は数回やり直す。
"""

import socket
import subprocess
import sys
import time


def wait_for_host(host="github.com", port=443, max_wait=900, interval=30):
    """host:port に TCP で接続できるまで最大 max_wait 秒待つ。つながれば True。"""
    deadline = time.time() + max_wait
    attempt = 0
    while True:
        attempt += 1
        try:
            with socket.create_connection((host, port), timeout=10):
                if attempt > 1:
                    print("net: %s:%d に接続できました(%d 回目)" % (host, port, attempt))
                return True
        except OSError as exc:
            if time.time() + interval > deadline:
                print("net: %s:%d に %d 秒つながりません: %s" % (host, port, max_wait, exc), file=sys.stderr)
                return False
            if attempt == 1:
                print("net: %s:%d に未接続のため待機します(最大 %d 秒): %s" % (host, port, max_wait, exc))
            time.sleep(interval)


def git_retry(cwd, *args, attempts=4, wait=30):
    """ネットワークを使う git コマンド(fetch / push)を、失敗したら wait 秒ずつ延ばして再試行する。"""
    result = None
    for i in range(attempts):
        result = subprocess.run(["git", *args], cwd=str(cwd), text=True, capture_output=True)
        if result.returncode == 0:
            return result
        if i < attempts - 1:
            print("net: git %s が失敗。%d 秒後に再試行(%d/%d): %s"
                  % (" ".join(args), wait * (i + 1), i + 1, attempts - 1,
                     (result.stderr or result.stdout).strip()[:200]), file=sys.stderr)
            wait_for_host(max_wait=wait * (i + 1), interval=10)
    return result
