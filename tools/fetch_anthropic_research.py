#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""anthropic.com/research の新着記事を検知して保存する。

Anthropic は RSS も通知の仕組みも出していないので、サイトマップを定期的に読み、
まだ index に無い /research/<slug> を新着として取得する(ポーリング)。

保存先(raw/ wiki/ とは別。日次パイプライン・Tier 分類の対象外):
  feeds/anthropic_research/index.jsonl      1 記事 1 行(url, slug, title, description, published, lastmod, first_seen, file)
  feeds/anthropic_research/posts/<公開日>-<slug>.md   本文(リポジトリが公開のため git 管理外)

使い方:
  python3 tools/fetch_anthropic_research.py            # 新着だけ取得
  python3 tools/fetch_anthropic_research.py --dry-run  # 新着の URL を表示するだけ
  python3 tools/fetch_anthropic_research.py --limit 5  # 1 回の取得件数を絞る
  python3 tools/fetch_anthropic_research.py --notify   # 新着があれば macOS の通知を出す

更新日(lastmod)の変化では取り直さない。サイト側の一括更新で全記事の lastmod が
同時に変わることがあるため。取り直すときは index の行と本文を消してから実行する。
"""

import argparse
import datetime
import fcntl
import html
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional

BASE = Path(__file__).resolve().parent.parent
OUT_DIR = BASE / "feeds" / "anthropic_research"
INDEX_PATH = OUT_DIR / "index.jsonl"
POSTS_DIR = OUT_DIR / "posts"
LOCK_PATH = OUT_DIR / ".lock"

SITEMAP_URL = "https://www.anthropic.com/sitemap.xml"
ARTICLE_RE = re.compile(r"^https://www\.anthropic\.com/research/([^/]+)$")
USER_AGENT = "Mozilla/5.0 (compatible; research-feed-reader)"
REQUEST_INTERVAL_SEC = 1.0

SKIP_TAGS = {"nav", "aside", "svg", "button", "script", "style", "dl", "noscript", "form"}
HEADINGS = {"h1": "#", "h2": "##", "h3": "###", "h4": "####", "h5": "#####"}
BLOCK_TAGS = {"p", "li", "blockquote", "figcaption", "td", "th"} | set(HEADINGS)
VOID_TAGS = {"img", "br", "hr", "input", "meta", "link", "source", "wbr"}


def http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as res:
        return res.read().decode("utf-8", errors="replace")


def sitemap_articles() -> List[Dict[str, str]]:
    xml = http_get(SITEMAP_URL)
    found = []
    for block in re.findall(r"<url>(.*?)</url>", xml, flags=re.S):
        loc = re.search(r"<loc>(.*?)</loc>", block)
        if not loc:
            continue
        url = html.unescape(loc.group(1).strip())
        m = ARTICLE_RE.match(url)
        if not m:
            continue
        lastmod = re.search(r"<lastmod>(.*?)</lastmod>", block)
        found.append({"url": url, "slug": m.group(1), "lastmod": lastmod.group(1).strip() if lastmod else ""})
    return found


class ArticleText(HTMLParser):
    """<article> の中身を Markdown 風のテキストにする。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_article = 0
        self.skip_depth = 0
        self.pre_depth = 0
        self.blocks = []  # type: List[str]
        self.buf = []  # type: List[str]
        self.prefix = ""
        self.href = None  # type: Optional[str]
        self.link_buf = []  # type: List[str]

    def _flush(self):
        if self.pre_depth:
            text = "".join(self.buf).strip("\n")
            if text.strip():
                self.blocks.append("```\n" + text + "\n```")
        else:
            text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
            if text:
                self.blocks.append(self.prefix + text)
        self.buf = []
        self.prefix = ""

    def handle_starttag(self, tag, attrs):
        if tag == "article":
            self.in_article += 1
            return
        if not self.in_article or tag in VOID_TAGS:
            if self.in_article and tag == "br" and not self.skip_depth:
                self.buf.append("\n" if self.pre_depth else " ")
            return
        if self.skip_depth or tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if tag == "pre":
            self._flush()
            self.pre_depth += 1
        elif tag in BLOCK_TAGS and not self.pre_depth:
            self._flush()
            if tag in HEADINGS:
                self.prefix = HEADINGS[tag] + " "
            elif tag == "li":
                self.prefix = "- "
            elif tag == "blockquote":
                self.prefix = "> "
        elif tag == "a" and not self.pre_depth:
            self.href = dict(attrs).get("href")
            self.link_buf = []

    def handle_endtag(self, tag):
        if tag == "article":
            if self.in_article:
                self._flush()
                self.in_article -= 1
            return
        if not self.in_article or tag in VOID_TAGS:
            return
        if self.skip_depth:
            self.skip_depth -= 1
            return
        if tag == "pre" and self.pre_depth:
            self._flush()
            self.pre_depth -= 1
        elif tag in BLOCK_TAGS and not self.pre_depth:
            self._flush()
        elif tag == "a" and self.href is not None:
            text = "".join(self.link_buf)
            href = self.href
            self.href = None
            if href.startswith("/"):
                href = "https://www.anthropic.com" + href
            if text.strip() and href.startswith("http"):
                self.buf.append("[" + text.strip() + "](" + href + ")")
            else:
                self.buf.append(text)

    def handle_data(self, data):
        if not self.in_article or self.skip_depth:
            return
        if self.href is not None and not self.pre_depth:
            self.link_buf.append(data)
        else:
            self.buf.append(data)


def meta(page: str, prop: str) -> str:
    m = re.search(r'<meta[^>]+(?:property|name)="' + re.escape(prop) + r'"[^>]+content="([^"]*)"', page)
    return html.unescape(m.group(1)).strip() if m else ""


def parse_article(page: str) -> Dict[str, str]:
    parser = ArticleText()
    parser.feed(page)
    parser.close()
    title = meta(page, "og:title")
    if not title:
        m = re.search(r"<title>(.*?)</title>", page, flags=re.S)
        title = html.unescape(m.group(1)).strip() if m else ""
    published = meta(page, "article:published_time")[:10]
    if not published:
        m = re.search(r'"datePublished":"(\d{4}-\d{2}-\d{2})', page) or re.search(r'<time dateTime="(\d{4}-\d{2}-\d{2})', page)
        published = m.group(1) if m else ""
    return {
        "title": title,
        "description": meta(page, "og:description"),
        "published": published,
        "body": "\n\n".join(parser.blocks),
    }


def load_index() -> Dict[str, dict]:
    known = {}
    if INDEX_PATH.exists():
        for line in INDEX_PATH.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                known[row["url"]] = row
    return known


def yaml_str(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def save_post(entry: Dict[str, str], art: Dict[str, str], now: str) -> dict:
    name = (art["published"] or "undated") + "-" + re.sub(r"[^A-Za-z0-9._-]", "-", entry["slug"]) + ".md"
    path = POSTS_DIR / name
    front = [
        "---",
        "title: " + yaml_str(art["title"]),
        "url: " + entry["url"],
        "published: " + yaml_str(art["published"]),
        "description: " + yaml_str(art["description"]),
        "fetched: " + yaml_str(now),
        "---",
        "",
    ]
    path.write_text("\n".join(front) + art["body"] + "\n", encoding="utf-8")
    row = {
        "url": entry["url"],
        "slug": entry["slug"],
        "title": art["title"],
        "description": art["description"],
        "published": art["published"],
        "lastmod": entry["lastmod"],
        "first_seen": now,
        "body_chars": len(art["body"]),
        "file": str(path.relative_to(BASE)),
    }
    with INDEX_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def notify(rows: List[dict]) -> None:
    title = "Anthropic Research: 新着 %d 件" % len(rows)
    body = " / ".join(r["title"] for r in rows[:3])
    script = "display notification %s with title %s" % (json.dumps(body, ensure_ascii=False), json.dumps(title, ensure_ascii=False))
    subprocess.run(["osascript", "-e", script], check=False)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true", help="新着の URL を表示するだけで保存しない")
    ap.add_argument("--limit", type=int, default=0, help="1 回に取得する件数の上限(0 は無制限)")
    ap.add_argument("--notify", action="store_true", help="新着があれば macOS の通知を出す")
    args = ap.parse_args()

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    lock = LOCK_PATH.open("w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        print("別の実行が進行中のため終了します")
        return 0

    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    try:
        entries = sitemap_articles()
    except (urllib.error.URLError, OSError) as e:
        print("[%s] サイトマップを取得できません: %s" % (now, e), file=sys.stderr)
        return 1
    if not entries:
        print("[%s] サイトマップに /research/ の記事が 1 件も無い。サイトの構造が変わった可能性" % now, file=sys.stderr)
        return 1

    known = load_index()
    first_run = not known
    fresh = sorted((e for e in entries if e["url"] not in known), key=lambda e: e["lastmod"])
    if args.limit:
        fresh = fresh[: args.limit]
    print("[%s] サイトマップ %d 件 / 取得済み %d 件 / 新着 %d 件" % (now, len(entries), len(known), len(fresh)))
    if args.dry_run:
        for e in fresh:
            print("  " + e["lastmod"][:10] + " " + e["url"])
        return 0

    saved, failed = [], 0
    for e in fresh:
        try:
            art = parse_article(http_get(e["url"]))
        except (urllib.error.URLError, OSError) as err:
            failed += 1
            print("  取得失敗 %s: %s" % (e["url"], err), file=sys.stderr)
            time.sleep(REQUEST_INTERVAL_SEC)
            continue
        if not art["title"]:
            failed += 1
            print("  題名を読めないため保存しない(次回に再試行): " + e["url"], file=sys.stderr)
        else:
            row = save_post(e, art, now)
            saved.append(row)
            print("  保存 %s %s (%d 字)" % (row["published"], row["title"], row["body_chars"]))
        time.sleep(REQUEST_INTERVAL_SEC)

    if saved and args.notify and not first_run:
        notify(saved)
    print("保存 %d 件 / 失敗 %d 件" % (len(saved), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
