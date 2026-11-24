#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""要旨(本文)が空の論文に、要旨を取り直して raw のファイルへ書き足す。

取得時に OpenAlex が要旨を持っていなかった論文は、題名と著者だけのファイルになる。
そのままでは概念抽出にかけられず、記事にならない(compile_articles_cli.py は対象から外す)。
要旨を次の順に探す。前の経路で見つかった論文は、後の経路には問い合わせない。

  1. OpenAlex    : openalex_id の一括取得(50 件/回)。取得後に要旨が登録された論文を拾う
  2. Semantic Scholar: DOI の一括取得(1 回)。鍵なし。429 は間隔を空けて再試行する
  3. Crossref    : DOI ごとに 1 件ずつ

取り決め:
  - 書き換えるのは、要旨が空のファイルだけ。「## Abstract」の節に本文を入れ、
    フロントマターに abstract_source(どこから取ったか)を足す
  - MIN_CHARS 字未満の要旨は採らない(題名の繰り返しや断片を避ける)
  - index.jsonl には触れない。要旨が入った未コンパイルの論文は、次の日次実行で記事生成の対象に戻る
  - 外へ送るのは論文の識別子(OpenAlex の ID・DOI)だけ

使い方:
  python3 tools/backfill_abstracts.py                 # Tier 1/2 を探すだけ(書き込まない)
  python3 tools/backfill_abstracts.py --apply         # 見つかった要旨を書き込む
  python3 tools/backfill_abstracts.py --tiers 1,2,3   # Tier 3 も対象にする
"""
import argparse
import collections
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "raw")
INDEX_PATH = os.path.join(RAW, "index.jsonl")
ENV_PATH = os.path.join(BASE, ".env")
MIN_CHARS = 200
USER_AGENT = "researcher-abstract-backfill/1.0"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compile_articles_cli import read_excerpt  # noqa: E402  (「本文が空」の判定を記事生成と揃える)


def load_env_key(name):
    if os.environ.get(name):
        return os.environ[name]
    if not os.path.exists(ENV_PATH):
        return ""
    with open(ENV_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("export "):
                line = line[7:].lstrip()
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip().strip("\"'")
    return ""


def http_json(url, data=None, retries=3, wait=5, timeout=20):
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    body = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    for attempt in range(retries):
        req = urllib.request.Request(url, data=body, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (429, 500, 502, 503) and attempt < retries - 1:
                time.sleep(wait * (attempt + 1))
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            if attempt < retries - 1:
                time.sleep(wait * (attempt + 1))
                continue
            raise
    return None


def clean(text):
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"^(abstract|summary)[:.\s]+", "", text, flags=re.I)


def inv_index_to_text(inv):
    words = []
    for word, positions in (inv or {}).items():
        for pos in positions:
            words.append((pos, word))
    words.sort()
    return " ".join(w for _, w in words)


def front_field(front, key):
    m = re.search(r'^%s:\s*"?(.*?)"?\s*$' % re.escape(key), front, re.M)
    return m.group(1).strip() if m else ""


def load_targets(tiers):
    targets = []
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            e = json.loads(line)
            if e.get("type") != "paper" or e.get("tier") not in tiers:
                continue
            path = os.path.join(RAW, e["file"])
            if not os.path.exists(path) or read_excerpt(e):
                continue
            with open(path, "r", encoding="utf-8", newline="") as fh:
                content = fh.read()
            parts = content.split("---", 2)
            front = parts[1] if content.startswith("---") and len(parts) >= 3 else ""
            oa = front_field(front, "openalex_id").rsplit("/", 1)[-1]
            doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", front_field(front, "doi"), flags=re.I).lower()
            targets.append({"entry": e, "path": path, "openalex": oa if re.match(r"^W\d+$", oa) else "", "doi": doi})
    return targets


def from_openalex(targets, found):
    key = load_env_key("OPENALEX_API_KEY")
    ids = [t["openalex"] for t in targets if t["openalex"] and t["path"] not in found]
    by_id = {t["openalex"]: t for t in targets if t["openalex"]}
    for start in range(0, len(ids), 50):
        params = {"filter": "openalex_id:" + "|".join(ids[start:start + 50]), "per-page": "50",
                  "select": "id,abstract_inverted_index"}
        if key:
            params["api_key"] = key
        res = http_json("https://api.openalex.org/works?" + urllib.parse.urlencode(params)) or {}
        for work in res.get("results", []):
            text = clean(inv_index_to_text(work.get("abstract_inverted_index")))
            t = by_id.get((work.get("id") or "").rsplit("/", 1)[-1])
            if t and len(text) >= MIN_CHARS:
                found[t["path"]] = ("openalex", text)
        time.sleep(0.2)


def from_semantic_scholar(targets, found):
    rest = [t for t in targets if t["doi"] and t["path"] not in found]
    for start in range(0, len(rest), 400):
        chunk = rest[start:start + 400]
        res = http_json("https://api.semanticscholar.org/graph/v1/paper/batch?fields=abstract",
                        data={"ids": ["DOI:" + t["doi"] for t in chunk]}, retries=3, wait=15) or []
        for t, paper in zip(chunk, res):
            text = clean((paper or {}).get("abstract"))
            if len(text) >= MIN_CHARS:
                found[t["path"]] = ("semantic_scholar", text)


def from_crossref(targets, found):
    # つながらない日に 1 件ごとの時間切れを待つと数時間かかる(2026-11-24 に 2 時間 47 分止まった)。
    # 続けて 3 件つながらなければ、この経路を打ち切る。
    failures = 0
    for t in targets:
        if not t["doi"] or t["path"] in found:
            continue
        try:
            res = http_json("https://api.crossref.org/works/" + urllib.parse.quote(t["doi"], safe="/"),
                            retries=1, timeout=10)
            failures = 0
        except Exception:
            res = None
            failures += 1
            if failures >= 3:
                raise RuntimeError("Crossref に続けて 3 件つながらないため打ち切り")
        text = clean(((res or {}).get("message") or {}).get("abstract"))
        if len(text) >= MIN_CHARS:
            found[t["path"]] = ("crossref", text)
        time.sleep(0.15)


def write_abstract(path, source, text):
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    parts = content.split("---", 2)
    if not content.startswith("---") or len(parts) < 3:
        return False
    front, body = parts[1], parts[2]
    m = re.search(r"^## Abstract[ \t]*\r?\n", body, re.M)
    if m:
        if body[m.end():].strip():
            return False  # 既に何か書かれている。上書きしない
        body = body[:m.end()] + "\n" + text + "\n"
    else:
        body = body.rstrip("\r\n") + "\n\n## Abstract\n\n" + text + "\n"
    front = front.rstrip("\r\n") + '\nabstract_source: "%s"\n' % source
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("---" + front + "---" + body)
    return True


def main():
    ap = argparse.ArgumentParser(description="要旨が空の論文に要旨を取り直す")
    ap.add_argument("--tiers", default="1,2", help="対象の Tier(既定 1,2)")
    ap.add_argument("--apply", action="store_true", help="見つかった要旨を raw のファイルに書き込む")
    args = ap.parse_args()
    tiers = {int(x) for x in args.tiers.split(",") if x.strip()}

    targets = load_targets(tiers)
    print("要旨が空の論文(Tier %s): %d 件 / OpenAlex の ID あり %d / DOI あり %d / どちらも無し %d" % (
        ",".join(str(t) for t in sorted(tiers)), len(targets),
        sum(1 for t in targets if t["openalex"]), sum(1 for t in targets if t["doi"]),
        sum(1 for t in targets if not t["openalex"] and not t["doi"])), flush=True)
    if not targets:
        return 0

    found = {}
    for label, fn in (("OpenAlex", from_openalex), ("Semantic Scholar", from_semantic_scholar), ("Crossref", from_crossref)):
        before = len(found)
        try:
            fn(targets, found)
        except Exception as e:
            print("  ! %s への問い合わせに失敗: %s" % (label, str(e)[:160]), flush=True)
        print("  %s: %d 件" % (label, len(found) - before), flush=True)

    by_path = {t["path"]: t for t in targets}
    pending_compile = sum(1 for p in found if not by_path[p]["entry"].get("wiki_compiled"))
    print("要旨が見つかった論文: %d / %d 件(うち未コンパイル %d 件) / 見つからない %d 件"
          % (len(found), len(targets), pending_compile, len(targets) - len(found)), flush=True)
    print("  経路別: %s" % dict(collections.Counter(src for src, _ in found.values())), flush=True)

    if not args.apply:
        print("--apply を付けると raw のファイルに書き込みます。")
        return 0
    written = sum(1 for path, (src, text) in sorted(found.items()) if write_abstract(path, src, text))
    print("書き込み: %d 件" % written, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
