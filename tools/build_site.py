#!/usr/bin/env python3
"""wiki/concepts の記事から、1 記事 1 URL の公開用静的サイトを生成する。

出力先: site/(git 管理外。GitHub Actions が同じスクリプトで生成して GitHub Pages へ配置する)

生成物:
  index.html                     トップ(クラスター一覧・最新記事・Tier 1 の入口)
  concepts/<slug>/index.html     記事ページ(OGP・JSON-LD・canonical・出典・AI 生成の注意書き)
  concepts/index.html            全記事一覧
  clusters/<key>/index.html      領域クラスター別の一覧
  domains/<domain>/index.html    分野別の一覧
  graph/index.html               知識グラフ(wiki/graph/index.html をそのまま複製)
  sitemap.xml / robots.txt / feed.xml / articles.json
  assets/site.css

設定は config/site.yaml。分野ラベルは config/sources.yaml から読む。
依存は標準ライブラリと PyYAML だけ(macOS 標準の Python 3.9 で動く)。

使い方:
  python3 tools/build_site.py                 # site/ を生成
  python3 tools/build_site.py --out /tmp/site # 出力先を変える
  python3 tools/build_site.py --site-url https://example.com   # URL を上書き(canonical・sitemap に効く)
"""

import argparse
import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import sys
from collections import OrderedDict, defaultdict

import yaml

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS_DIR = os.path.join(BASE, "wiki", "concepts")
META_FILE = os.path.join(BASE, "wiki", "_meta", "concepts.json")
BACKLINKS_FILE = os.path.join(BASE, "wiki", "_meta", "backlinks.json")
OVERRIDES_FILE = os.path.join(BASE, "wiki", "_meta", "domain_overrides.json")
INDEX_FILE = os.path.join(BASE, "raw", "index.jsonl")
SITE_CONFIG = os.path.join(BASE, "config", "site.yaml")
SOURCES_CONFIG = os.path.join(BASE, "config", "sources.yaml")
GRAPH_UI = os.path.join(BASE, "wiki", "graph", "index.html")
DEFAULT_OUT = os.path.join(BASE, "site")

TIER_LABEL = {1: "不変原理", 2: "設計原理", 3: "参考"}


# ---------------------------------------------------------------------------
# 読み込み
# ---------------------------------------------------------------------------

def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def load_config():
    with open(SITE_CONFIG, encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    with open(SOURCES_CONFIG, encoding="utf-8") as handle:
        sources = yaml.safe_load(handle)
    domain_labels = {}
    domain_questions = {}
    for key, spec in (sources.get("research_domains") or {}).items():
        if isinstance(spec, dict):
            domain_labels[key] = spec.get("label") or key
            domain_questions[key] = spec.get("core_question") or ""
    config["domain_labels"] = domain_labels
    config["domain_questions"] = domain_questions
    config["domain_to_cluster"] = {}
    for cluster in config["clusters"]:
        for domain in cluster["domains"]:
            config["domain_to_cluster"][domain] = cluster["key"]
    return config


def load_source_domains():
    """raw/index.jsonl から slug -> [domain...] と slug -> [tier...] を集める。"""
    by_slug = defaultdict(list)
    tiers = defaultdict(list)
    if not os.path.exists(INDEX_FILE):
        return by_slug, tiers
    with open(INDEX_FILE, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            slugs = record.get("wiki_slug")
            if isinstance(slugs, str):
                slugs = [slugs]
            domain = record.get("domain")
            tier = record.get("tier")
            for slug in slugs or []:
                if slug and domain and domain not in by_slug[slug]:
                    by_slug[slug].append(domain)
                if slug and tier in (1, 2, 3):
                    tiers[slug].append(tier)
    return by_slug, tiers


def load_git_dates():
    """記事ファイルごとの初回コミット日(公開日)と最終コミット日(更新日)。git が無ければ空。"""
    published = {}
    modified = {}
    try:
        output = subprocess.check_output(
            ["git", "log", "--format=@%aI", "--name-status", "--diff-filter=AM", "--", "wiki/concepts"],
            cwd=BASE, text=True, stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return published, modified
    current = None
    for line in output.splitlines():
        if line.startswith("@"):
            current = line[1:].strip()
            continue
        if not line or current is None:
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        path = parts[-1]
        if not path.startswith("wiki/concepts/") or not path.endswith(".md"):
            continue
        slug = os.path.basename(path)[:-3]
        # git log は新しい順に出るので、最初に見たものが最終更新、最後に見たものが初回
        modified.setdefault(slug, current)
        published[slug] = current
    return published, modified


# ---------------------------------------------------------------------------
# 記事カタログ
# ---------------------------------------------------------------------------

def first_paragraph(markdown):
    body = re.sub(r"^# .+\n+", "", markdown.strip())
    lines = []
    for line in body.splitlines():
        text = line.strip()
        if not text:
            if lines:
                break
            continue
        if text.startswith("#") or text.startswith("|") or text.startswith("---"):
            if lines:
                break
            continue
        lines.append(text)
    text = " ".join(lines)
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*`_]", "", text)
    return text.strip()


def truncate(text, limit):
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def guess_cluster(slug, title, config):
    haystack = (slug + " " + (title or "")).lower()
    for key, words in (config.get("cluster_keywords") or {}).items():
        for word in words:
            if word.lower() in haystack:
                return key
    return config["clusters"][-1]["key"]


def load_catalog(config=None):
    """全記事のメタデータ一覧。build とは独立に、post_x.py などからも使う。"""
    config = config or load_config()
    meta_by_slug = {item["slug"]: item for item in load_json(META_FILE, []) if item.get("slug")}
    overrides = load_json(OVERRIDES_FILE, {})
    source_domains, source_tiers = load_source_domains()
    published, modified = load_git_dates()
    domain_to_cluster = config["domain_to_cluster"]

    catalog = []
    for filename in sorted(os.listdir(CONCEPTS_DIR)):
        if not filename.endswith(".md"):
            continue
        slug = filename[:-3]
        path = os.path.join(CONCEPTS_DIR, filename)
        with open(path, encoding="utf-8") as handle:
            markdown = handle.read()
        title_match = re.match(r"^# (.+)$", markdown.lstrip(), re.M)
        title = title_match.group(1).strip() if title_match else slug
        item = meta_by_slug.get(slug, {})

        domains = [d for d in (item.get("related_domains") or []) if d in domain_to_cluster]
        domain_source = "meta"
        if not domains:
            domains = [d for d in (overrides.get(slug) or {}).get("domains", []) if d in domain_to_cluster]
            domain_source = "override"
        if not domains:
            domains = [d for d in source_domains.get(slug, []) if d in domain_to_cluster]
            domain_source = "sources"
        if domains:
            cluster = domain_to_cluster[domains[0]]
        else:
            cluster = (overrides.get(slug) or {}).get("cluster") or guess_cluster(slug, title, config)
            domain_source = "guess"

        # 記事の Tier: メタデータにあればそれ、無ければ出典論文の Tier の最小値(最も不変な側)
        if item.get("tier") in (1, 2, 3):
            tier = int(item["tier"])
        elif source_tiers.get(slug):
            tier = min(source_tiers[slug])
        else:
            tier = 2
        description = item.get("description") or truncate(first_paragraph(markdown), 120)
        if slug not in published:
            # まだコミットされていない新しい記事は、ファイルの更新時刻を公開日とみなす
            stamp = dt.datetime.fromtimestamp(os.path.getmtime(path), dt.timezone.utc).astimezone().isoformat(timespec="seconds")
            published[slug] = stamp
            modified.setdefault(slug, stamp)
        catalog.append({
            "slug": slug,
            "title": item.get("title_ja") or title,
            "title_en": item.get("title_en") or "",
            "tier": tier,
            "description": description,
            "has_lead": bool(item.get("description")),
            "domains": domains,
            "domain_source": domain_source,
            "cluster": cluster,
            "mechanisms": item.get("mechanisms") or [],
            "published": published.get(slug) or "",
            "modified": modified.get(slug) or published.get(slug) or "",
            "markdown": markdown,
            "path": "concepts/%s/" % slug,
        })
    return catalog


# ---------------------------------------------------------------------------
# Markdown -> HTML(記事の書式に合わせた最小実装)
# ---------------------------------------------------------------------------

class Renderer:
    def __init__(self, catalog, backlinks, repo_url=""):
        self.slugs = {item["slug"]: item for item in catalog}
        self.repo_url = repo_url.rstrip("/")
        self.backlinks = (backlinks or {}).get("nodes", {})
        self.title_to_slug = {}
        for item in catalog:
            self.title_to_slug.setdefault(item["title"], item["slug"])
            if item["title_en"]:
                self.title_to_slug.setdefault(item["title_en"], item["slug"])

    def link_map(self, slug):
        node = self.backlinks.get(slug) or {}
        mapping = {}
        for out in node.get("outbound", []):
            if not out.get("resolved"):
                continue
            for raw in out.get("raw_targets", []):
                mapping[raw] = out.get("id")
            for mention in out.get("mentions", []):
                raw = mention.get("raw_target")
                if raw:
                    mapping[raw] = out.get("id")
        return mapping

    def resolve_wikilink(self, slug, inner):
        target, label = inner, inner
        if "|" in inner:
            target, label = inner.split("|", 1)
            target, label = target.strip(), label.strip()
        mapping = self.link_map(slug)
        resolved = mapping.get(target)
        if resolved in self.slugs:
            return resolved, label
        if target in self.slugs:
            return target, label
        if target in self.title_to_slug:
            return self.title_to_slug[target], label
        return None, label

    def inline(self, slug, text, root):
        tokens = []

        def stash(match):
            tokens.append(match.group(1))
            return "\x00WL%d\x00" % (len(tokens) - 1)

        value = re.sub(r"\[\[([^\]]+)\]\]", stash, text)
        links = []

        def stash_link(match):
            links.append((match.group(1), match.group(2)))
            return "\x00LK%d\x00" % (len(links) - 1)

        value = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", stash_link, value)
        value = html.escape(value, quote=False)
        value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
        value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
        value = re.sub(r"(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])", r"<em>\1</em>", value)

        def restore_wl(match):
            inner = tokens[int(match.group(1))]
            target, label = self.resolve_wikilink(slug, inner)
            if target:
                return '<a class="wikilink" href="%sconcepts/%s/">%s</a>' % (root, target, html.escape(label, quote=False))
            return '<span class="wikilink unresolved">%s</span>' % html.escape(label, quote=False)

        value = re.sub(r"\x00WL(\d+)\x00", restore_wl, value)

        def restore_link(match):
            label, url = links[int(match.group(1))]
            return '<a href="%s" rel="noopener nofollow" target="_blank">%s</a>' % (
                html.escape(url, quote=True), html.escape(label, quote=False))

        value = re.sub(r"\x00LK(\d+)\x00", restore_link, value)
        return value

    def render(self, slug, markdown, root):
        body = re.sub(r"^# .+\n+", "", markdown.lstrip(), count=1)
        # 追加ソースの「ファイルパス: `raw/...`」は、公開リポジトリ上の原文へのリンクに置き換える
        body = re.sub(
            r"\*\*ファイルパス\*\*: `(raw/[^`]+)`",
            lambda m: "**原文**: [GitHub](%s/blob/main/%s)" % (self.repo_url, m.group(1)),
            body,
        )
        lines = body.splitlines()
        out = []
        i = 0
        n = len(lines)

        def is_table_line(line):
            s = line.strip()
            return s.startswith("|") and s.endswith("|") and len(s) > 1

        def is_sep_line(line):
            return re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$", line) is not None

        while i < n:
            line = lines[i]
            stripped = line.strip()
            if not stripped:
                i += 1
                continue
            if stripped.startswith("```"):
                code = []
                i += 1
                while i < n and not lines[i].strip().startswith("```"):
                    code.append(lines[i])
                    i += 1
                i += 1
                out.append("<pre><code>%s</code></pre>" % html.escape("\n".join(code), quote=False))
                continue
            heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
            if heading:
                level = min(len(heading.group(1)) + 1, 6)  # 記事の ## を h2 に揃える
                text = heading.group(2).strip()
                anchor = re.sub(r"[^\w\-ぁ-んァ-ヶ一-龠]+", "-", text).strip("-").lower() or "section"
                out.append('<h%d id="%s">%s</h%d>' % (level, html.escape(anchor), self.inline(slug, text, root), level))
                i += 1
                continue
            if re.match(r"^-{3,}$|^\*{3,}$", stripped):
                out.append("<hr>")
                i += 1
                continue
            if stripped.startswith(">"):
                quote = []
                while i < n and lines[i].strip().startswith(">"):
                    quote.append(lines[i].strip()[1:].strip())
                    i += 1
                out.append("<blockquote><p>%s</p></blockquote>" % self.inline(slug, " ".join(quote), root))
                continue
            if is_table_line(line):
                rows = []
                while i < n and is_table_line(lines[i]):
                    rows.append(lines[i].strip())
                    i += 1
                header = None
                body_rows = []
                for idx, row in enumerate(rows):
                    if is_sep_line(row):
                        if idx == 1:
                            header = rows[0]
                        continue
                    if idx == 0 and len(rows) > 1 and is_sep_line(rows[1]):
                        continue
                    body_rows.append(row)
                def cells(row):
                    return [c.strip() for c in row.strip().strip("|").split("|")]
                parts = ['<div class="table-wrap"><table>']
                if header:
                    parts.append("<thead><tr>%s</tr></thead>" % "".join(
                        "<th>%s</th>" % self.inline(slug, c, root) for c in cells(header)))
                parts.append("<tbody>")
                for row in body_rows:
                    parts.append("<tr>%s</tr>" % "".join(
                        "<td>%s</td>" % self.inline(slug, c, root) for c in cells(row)))
                parts.append("</tbody></table></div>")
                out.append("".join(parts))
                continue
            list_match = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
            if list_match:
                out.append(self.render_list(slug, lines, i, root))
                # render_list は消費した行数を self._consumed に置く
                i = self._consumed
                continue
            para = [stripped]
            i += 1
            while i < n:
                nxt = lines[i]
                s = nxt.strip()
                if (not s or s.startswith("#") or s.startswith(">") or s.startswith("```")
                        or is_table_line(nxt) or re.match(r"^-{3,}$", s)
                        or re.match(r"^(\s*)([-*+]|\d+[.)])\s+", nxt)):
                    break
                para.append(s)
                i += 1
            out.append("<p>%s</p>" % self.inline(slug, " ".join(para), root))
        return "\n".join(out)

    def render_list(self, slug, lines, start, root):
        """ネストした箇条書き・番号付きリストを 1 ブロックとして描画する。"""
        items = []  # (indent, ordered, text)
        i = start
        n = len(lines)
        while i < n:
            line = lines[i]
            m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
            if m:
                indent = len(m.group(1).replace("\t", "    "))
                ordered = m.group(2)[0].isdigit()
                items.append([indent, ordered, m.group(3).strip()])
                i += 1
                continue
            s = line.strip()
            if s and items and (len(line) - len(line.lstrip())) > items[-1][0] and not s.startswith("#") and not s.startswith("|"):
                items[-1][2] += " " + s  # 継続行
                i += 1
                continue
            break
        self._consumed = i

        html_parts = []
        stack = []  # [(indent, tag)]

        def close_to(indent):
            while stack and stack[-1][0] > indent:
                html_parts.append("</li></%s>" % stack.pop()[1])

        for indent, ordered, text in items:
            tag = "ol" if ordered else "ul"
            if not stack or indent > stack[-1][0]:
                stack.append((indent, tag))
                html_parts.append("<%s><li>%s" % (tag, self.inline(slug, text, root)))
            else:
                close_to(indent)
                if stack and stack[-1][0] == indent and stack[-1][1] != tag:
                    html_parts.append("</li></%s>" % stack.pop()[1])
                    stack.append((indent, tag))
                    html_parts.append("<%s><li>%s" % (tag, self.inline(slug, text, root)))
                elif stack:
                    html_parts.append("</li><li>%s" % self.inline(slug, text, root))
                else:
                    stack.append((indent, tag))
                    html_parts.append("<%s><li>%s" % (tag, self.inline(slug, text, root)))
        while stack:
            html_parts.append("</li></%s>" % stack.pop()[1])
        return "".join(html_parts)


# ---------------------------------------------------------------------------
# ページ生成
# ---------------------------------------------------------------------------

CSS = """
:root{--bg:#fbfaf7;--fg:#1f2430;--muted:#5d6675;--line:#e3dfd6;--accent:#1f6f8b;--accent-2:#b65c2e;--chip:#eef2f5;--card:#ffffff;--code:#f1efe9;--max:760px}
@media (prefers-color-scheme:dark){:root{--bg:#0f1319;--fg:#e8ecf2;--muted:#9aa5b5;--line:#2a313c;--accent:#7cc4dd;--accent-2:#e3a07a;--chip:#1b222c;--card:#151b23;--code:#1b222c}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans","Hiragino Kaku Gothic ProN","Noto Sans JP","Segoe UI",sans-serif;line-height:1.85;font-size:16px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:var(--max);margin:0 auto;padding:0 20px}
header.top{border-bottom:1px solid var(--line);background:var(--card)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 20px;flex-wrap:wrap}
header.top .brand{font-weight:700;letter-spacing:.02em;color:var(--fg)}
header.top nav{display:flex;gap:16px;font-size:14px;flex-wrap:wrap}
main{padding:28px 0 56px}
.crumbs{font-size:13px;color:var(--muted);margin-bottom:14px;display:flex;flex-wrap:wrap;gap:6px}
.crumbs a{color:var(--muted)}
h1{font-size:1.75rem;line-height:1.35;margin:.2em 0 .3em}
h2{font-size:1.3rem;margin:2em 0 .6em;padding-bottom:.25em;border-bottom:1px solid var(--line)}
h3{font-size:1.1rem;margin:1.6em 0 .5em}h4{font-size:1rem;margin:1.4em 0 .4em}
.sub{color:var(--muted);font-size:.95rem;margin:0 0 .6em}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 18px}
.chip{display:inline-block;font-size:12px;padding:2px 10px;border-radius:999px;background:var(--chip);color:var(--fg);border:1px solid var(--line)}
.chip.tier1{background:var(--accent);color:#fff;border-color:var(--accent)}
.chip.tier2{background:var(--accent-2);color:#fff;border-color:var(--accent-2)}
.lead{font-size:1.05rem;color:var(--muted);border-left:3px solid var(--accent);padding-left:14px;margin:0 0 22px}
article p{margin:0 0 1.1em}article ul,article ol{padding-left:1.5em;margin:0 0 1.1em}article li{margin:.2em 0}
article blockquote{margin:1em 0;padding:.4em 1em;border-left:3px solid var(--line);color:var(--muted)}
article code{background:var(--code);padding:.1em .35em;border-radius:4px;font-size:.9em}
article pre{background:var(--code);padding:12px;border-radius:6px;overflow:auto;font-size:.85em}
.table-wrap{overflow-x:auto;margin:1em 0}table{border-collapse:collapse;width:100%;font-size:.92em}
th,td{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}th{background:var(--chip)}
hr{border:0;border-top:1px solid var(--line);margin:2em 0}
.wikilink.unresolved{color:var(--muted);border-bottom:1px dotted var(--muted)}
.notice{margin-top:40px;padding:14px 16px;border:1px solid var(--line);border-radius:8px;background:var(--card);font-size:.9rem;color:var(--muted)}
.meta{font-size:.85rem;color:var(--muted);margin:6px 0 18px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;margin:16px 0 28px}
.card{display:block;padding:14px 16px;border:1px solid var(--line);border-radius:10px;background:var(--card);color:var(--fg)}
.card:hover{text-decoration:none;border-color:var(--accent)}
.card .t{font-weight:700;margin-bottom:4px}.card .d{font-size:.85rem;color:var(--muted)}
.list{list-style:none;padding:0;margin:0}.list li{padding:12px 0;border-bottom:1px solid var(--line)}
.list .t{font-weight:600}.list .d{font-size:.9rem;color:var(--muted);margin-top:2px}
.list .m{font-size:.78rem;color:var(--muted);margin-top:4px}
.related{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px;list-style:none;padding:0}
.related li{border:1px solid var(--line);border-radius:8px;padding:8px 12px;background:var(--card);font-size:.92rem}
footer.bottom{border-top:1px solid var(--line);padding:22px 0 40px;font-size:.85rem;color:var(--muted)}
footer.bottom .wrap{display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between}
.hero{padding:10px 0 8px}.hero p{font-size:1.05rem;color:var(--muted)}
.stats{display:flex;gap:18px;flex-wrap:wrap;font-size:.9rem;color:var(--muted);margin:6px 0 10px}
@media (max-width:600px){h1{font-size:1.45rem}body{font-size:15.5px}}
"""


def esc(value):
    return html.escape(str(value or ""), quote=True)


def analytics_snippet(config):
    parts = []
    ga4 = (config.get("analytics") or {}).get("ga4_measurement_id") or ""
    if ga4:
        parts.append(
            '<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>'
            "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
            "gtag('js',new Date());gtag('config','%s',{anonymize_ip:true});</script>" % (ga4, ga4))
    beacon = (config.get("analytics") or {}).get("cloudflare_beacon_token") or ""
    if beacon:
        parts.append(
            '<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
            'data-cf-beacon=\'{"token": "%s"}\'></script>' % beacon)
    return "".join(parts)


def layout(config, root, title, description, body, canonical, og_type="website", extra_head="", crumbs=None):
    site = config["site"]
    nav = (
        '<a href="%sconcepts/">記事一覧</a>'
        '<a href="%s#clusters">領域</a>'
        '<a href="%sgraph/">知識グラフ</a>'
        '<a href="%sfeed.xml">RSS</a>'
        '<a href="%s" rel="noopener">GitHub</a>' % (root, root, root, root, esc(site["repo_url"]))
    )
    crumbs_html = ""
    if crumbs:
        crumbs_html = '<div class="crumbs">%s</div>' % " › ".join(
            ('<a href="%s">%s</a>' % (esc(href), esc(label))) if href else "<span>%s</span>" % esc(label)
            for label, href in crumbs)
    return """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(description)s">
<link rel="canonical" href="%(canonical)s">
<meta property="og:site_name" content="%(site_title)s">
<meta property="og:type" content="%(og_type)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(description)s">
<meta property="og:url" content="%(canonical)s">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary">
<link rel="alternate" type="application/rss+xml" title="%(site_title)s" href="%(root)sfeed.xml">
<link rel="stylesheet" href="%(root)sassets/site.css">
%(extra_head)s
%(analytics)s
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="%(root)s">%(short)s</a><nav>%(nav)s</nav></div></header>
<main><div class="wrap">
%(crumbs)s
%(body)s
</div></main>
<footer class="bottom"><div class="wrap"><span>© %(year)d %(author)s · 記事は学術論文をもとに AI が自動生成しています</span><span><a href="%(root)sconcepts/">記事一覧</a> · <a href="%(root)ssitemap.xml">sitemap</a></span></div></footer>
</body>
</html>
""" % {
        "title": esc(title),
        "description": esc(truncate(description, 160)),
        "canonical": esc(canonical),
        "site_title": esc(site["short_title"]),
        "og_type": og_type,
        "root": root,
        "extra_head": extra_head,
        "analytics": analytics_snippet(config),
        "short": esc(site["short_title"]),
        "nav": nav,
        "crumbs": crumbs_html,
        "body": body,
        "year": dt.date.today().year,
        "author": esc(site["author"]),
    }


def tier_chip(tier):
    return '<span class="chip tier%d">Tier %d · %s</span>' % (tier, tier, TIER_LABEL.get(tier, ""))


def domain_chips(item, config, root):
    chips = [tier_chip(item["tier"])]
    cluster = next(c for c in config["clusters"] if c["key"] == item["cluster"])
    chips.append('<a class="chip" href="%sclusters/%s/">%s</a>' % (root, cluster["key"], esc(cluster["label"])))
    for domain in item["domains"]:
        chips.append('<a class="chip" href="%sdomains/%s/">%s</a>' % (root, domain, esc(config["domain_labels"].get(domain, domain))))
    return '<div class="chips">%s</div>' % "".join(chips)


def fmt_date(value):
    return value[:10] if value else ""


def list_items(items, root, show_date=False):
    parts = ['<ul class="list">']
    for item in items:
        meta = " · ".join(filter(None, [
            "Tier %d" % item["tier"],
            fmt_date(item["published"]) if show_date else "",
        ]))
        parts.append(
            '<li><a class="t" href="%sconcepts/%s/">%s</a>'
            '<div class="d">%s</div><div class="m">%s</div></li>' % (
                root, item["slug"], esc(item["title"]), esc(truncate(item["description"], 110)), esc(meta)))
    parts.append("</ul>")
    return "".join(parts)


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def related_items(slug, backlinks, by_slug, limit=12):
    node = (backlinks or {}).get("nodes", {}).get(slug) or {}
    seen = OrderedDict()
    for edge in node.get("outbound", []) + node.get("inbound", []):
        target = edge.get("id")
        if edge.get("resolved") and target in by_slug and target != slug:
            seen[target] = seen.get(target, 0) + (edge.get("weight") or 1)
    ranked = sorted(seen.items(), key=lambda kv: (-kv[1], by_slug[kv[0]]["title"]))
    return [by_slug[s] for s, _ in ranked[:limit]]


def build_article(item, config, renderer, backlinks, by_slug, out_dir):
    root = "../../"
    site = config["site"]
    url = "%s/%s" % (site["url"], item["path"])
    body_html = renderer.render(item["slug"], item["markdown"], root)
    cluster = next(c for c in config["clusters"] if c["key"] == item["cluster"])
    related = related_items(item["slug"], backlinks, by_slug)
    related_html = ""
    if related:
        related_html = "<h2>関連コンセプト</h2><ul class=\"related\">%s</ul>" % "".join(
            '<li><a href="%sconcepts/%s/">%s</a></li>' % (root, r["slug"], esc(r["title"])) for r in related)
    dates = " · ".join(filter(None, [
        ("公開 " + fmt_date(item["published"])) if item["published"] else "",
        ("更新 " + fmt_date(item["modified"])) if item["modified"] and item["modified"][:10] != item["published"][:10] else "",
    ]))
    source_md = "%s/blob/main/wiki/concepts/%s.md" % (site["repo_url"], item["slug"])
    body = """
<article>
<h1>%(title)s</h1>
%(sub)s
%(chips)s
%(lead)s
<div class="meta">%(dates)s</div>
%(body)s
%(related)s
<div class="notice">%(notice)s<br>原稿(Markdown): <a href="%(source_md)s" rel="noopener">GitHub</a></div>
</article>
""" % {
        "title": esc(item["title"]),
        "sub": ('<p class="sub">%s</p>' % esc(item["title_en"])) if item["title_en"] else "",
        "chips": domain_chips(item, config, root),
        "lead": ('<p class="lead">%s</p>' % esc(item["description"])) if item["has_lead"] else "",
        "dates": esc(dates),
        "body": body_html,
        "related": related_html,
        "notice": esc(site["ai_notice"]),
        "source_md": esc(source_md),
    }
    json_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": item["title"],
        "description": item["description"],
        "inLanguage": "ja",
        "isAccessibleForFree": True,
        "url": url,
        "author": {"@type": "Organization", "name": site["author"]},
        "publisher": {"@type": "Organization", "name": site["author"]},
        "about": [config["domain_labels"].get(d, d) for d in item["domains"]],
    }
    if item["published"]:
        json_ld["datePublished"] = item["published"]
    if item["modified"]:
        json_ld["dateModified"] = item["modified"]
    extra_head = '<script type="application/ld+json">%s</script>' % json.dumps(json_ld, ensure_ascii=False).replace("</", "<\\/")
    page = layout(
        config, root,
        title="%s | %s" % (item["title"], site["short_title"]),
        description=item["description"],
        body=body, canonical=url, og_type="article", extra_head=extra_head,
        crumbs=[(site["short_title"], root), (cluster["label"], root + "clusters/%s/" % cluster["key"]), (item["title"], None)],
    )
    write(os.path.join(out_dir, "concepts", item["slug"], "index.html"), page)


def build_cluster_pages(catalog, config, out_dir):
    site = config["site"]
    root = "../../"
    for cluster in config["clusters"]:
        items = [i for i in catalog if i["cluster"] == cluster["key"]]
        by_domain = defaultdict(list)
        for item in items:
            key = item["domains"][0] if item["domains"] else "_other"
            by_domain[key].append(item)
        sections = []
        for domain in cluster["domains"] + ["_other"]:
            group = by_domain.get(domain)
            if not group:
                continue
            label = config["domain_labels"].get(domain, "その他(分野推定)") if domain != "_other" else "分野横断"
            group.sort(key=lambda i: (i["tier"], i["title"]))
            heading = '<h2 id="%s">%s <span class="sub">(%d)</span></h2>' % (esc(domain), esc(label), len(group))
            if domain != "_other":
                heading += '<p class="sub">%s · <a href="%sdomains/%s/">分野ページへ</a></p>' % (
                    esc(config["domain_questions"].get(domain, "")), root, domain)
            sections.append(heading + list_items(group, root))
        body = '<h1>%s</h1><p class="lead">%s</p><div class="stats"><span>%d 記事</span><span>Tier 1: %d</span></div>%s' % (
            esc(cluster["label"]), esc(cluster["tagline"]), len(items), sum(1 for i in items if i["tier"] == 1), "".join(sections))
        url = "%s/clusters/%s/" % (site["url"], cluster["key"])
        page = layout(config, root, "%s | %s" % (cluster["label"], site["short_title"]), cluster["tagline"], body, url,
                      crumbs=[(site["short_title"], root), (cluster["label"], None)])
        write(os.path.join(out_dir, "clusters", cluster["key"], "index.html"), page)


def build_domain_pages(catalog, config, out_dir):
    site = config["site"]
    root = "../../"
    for domain, label in config["domain_labels"].items():
        items = [i for i in catalog if domain in i["domains"]]
        if not items:
            continue
        items.sort(key=lambda i: (i["tier"], i["title"]))
        cluster_key = config["domain_to_cluster"].get(domain)
        cluster = next((c for c in config["clusters"] if c["key"] == cluster_key), None)
        body = '<h1>%s</h1><p class="lead">%s</p><div class="stats"><span>%d 記事</span></div>%s' % (
            esc(label), esc(config["domain_questions"].get(domain, "")), len(items), list_items(items, root))
        url = "%s/domains/%s/" % (site["url"], domain)
        crumbs = [(site["short_title"], root)]
        if cluster:
            crumbs.append((cluster["label"], root + "clusters/%s/" % cluster["key"]))
        crumbs.append((label, None))
        page = layout(config, root, "%s | %s" % (label, site["short_title"]),
                      config["domain_questions"].get(domain, "") or label, body, url, crumbs=crumbs)
        write(os.path.join(out_dir, "domains", domain, "index.html"), page)


def build_all_index(catalog, config, out_dir):
    site = config["site"]
    root = "../"
    items = sorted(catalog, key=lambda i: (i["tier"], i["title"]))
    body = '<h1>記事一覧</h1><div class="stats"><span>%d 記事</span><span>Tier 1: %d</span><span>Tier 2: %d</span></div>%s' % (
        len(items), sum(1 for i in items if i["tier"] == 1), sum(1 for i in items if i["tier"] == 2), list_items(items, root, show_date=True))
    page = layout(config, root, "記事一覧 | %s" % site["short_title"], site["description"], body, site["url"] + "/concepts/",
                  crumbs=[(site["short_title"], root), ("記事一覧", None)])
    write(os.path.join(out_dir, "concepts", "index.html"), page)


def build_home(catalog, config, out_dir):
    site = config["site"]
    root = ""
    latest = sorted([i for i in catalog if i["published"]], key=lambda i: i["published"], reverse=True)[:12]
    tier1 = sorted([i for i in catalog if i["tier"] == 1], key=lambda i: i["published"], reverse=True)[:8]
    cards = []
    for cluster in config["clusters"]:
        count = sum(1 for i in catalog if i["cluster"] == cluster["key"])
        cards.append('<a class="card" href="clusters/%s/"><div class="t">%s</div><div class="d">%s · %d 記事</div></a>' % (
            cluster["key"], esc(cluster["label"]), esc(cluster["tagline"]), count))
    body = """
<div class="hero"><h1>%(title)s</h1><p>%(description)s</p>
<div class="stats"><span>%(count)d 記事</span><span>%(domains)d 分野</span><span>Tier 1(不変原理): %(t1)d</span></div></div>
<h2 id="clusters">領域から探す</h2>
<div class="cards">%(cards)s</div>
<h2>最新の記事</h2>%(latest)s
<h2>不変原理(Tier 1)から読む</h2>%(tier1)s
<p><a href="concepts/">すべての記事を見る →</a> · <a href="graph/">知識グラフで探索する →</a></p>
<div class="notice">このサイトの記事は、学術論文(主に系統的レビュー・メタ分析・古典)をもとに AI が日本語で自動生成し、毎日追加されています。各記事の末尾に出典を示しています。Tier 1 は AGI 時代にも変わらないと判断した構造的原理、Tier 2 は消えゆく制約を前提にした設計原理です。</div>
""" % {
        "title": esc(site["title"]),
        "description": esc(site["description"]),
        "count": len(catalog),
        "domains": len({d for i in catalog for d in i["domains"]}),
        "t1": sum(1 for i in catalog if i["tier"] == 1),
        "cards": "".join(cards),
        "latest": list_items(latest, root, show_date=True),
        "tier1": list_items(tier1, root),
    }
    page = layout(config, root, site["title"], site["description"], body, site["url"] + "/")
    write(os.path.join(out_dir, "index.html"), page)


def build_feeds(catalog, config, out_dir):
    site = config["site"]
    base = site["url"]
    now = dt.datetime.now(dt.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    # sitemap
    urls = [("%s/" % base, "daily", "1.0"), ("%s/concepts/" % base, "daily", "0.6"), ("%s/graph/" % base, "weekly", "0.4")]
    for cluster in config["clusters"]:
        urls.append(("%s/clusters/%s/" % (base, cluster["key"]), "daily", "0.7"))
    for domain in config["domain_labels"]:
        if any(domain in i["domains"] for i in catalog):
            urls.append(("%s/domains/%s/" % (base, domain), "weekly", "0.5"))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, freq, prio in urls:
        lines.append("<url><loc>%s</loc><changefreq>%s</changefreq><priority>%s</priority></url>" % (esc(loc), freq, prio))
    for item in catalog:
        lastmod = ("<lastmod>%s</lastmod>" % fmt_date(item["modified"])) if item["modified"] else ""
        lines.append("<url><loc>%s/%s</loc>%s<priority>%s</priority></url>" % (
            esc(base), esc(item["path"]), lastmod, "0.8" if item["tier"] == 1 else "0.6"))
    lines.append("</urlset>")
    write(os.path.join(out_dir, "sitemap.xml"), "\n".join(lines))
    write(os.path.join(out_dir, "robots.txt"), "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % base)
    # RSS
    latest = sorted([i for i in catalog if i["published"]], key=lambda i: i["published"], reverse=True)[:50]
    rss = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0"><channel>',
           "<title>%s</title><link>%s/</link><description>%s</description><language>ja</language><lastBuildDate>%s</lastBuildDate>" % (
               esc(site["short_title"]), esc(base), esc(site["description"]), now)]
    for item in latest:
        try:
            pub = dt.datetime.fromisoformat(item["published"]).astimezone(dt.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
        except ValueError:
            pub = now
        rss.append("<item><title>%s</title><link>%s/%s</link><guid>%s/%s</guid><pubDate>%s</pubDate><description>%s</description></item>" % (
            esc(item["title"]), esc(base), esc(item["path"]), esc(base), esc(item["path"]), pub, esc(item["description"])))
    rss.append("</channel></rss>")
    write(os.path.join(out_dir, "feed.xml"), "\n".join(rss))
    # 機械可読の一覧(X 配信や外部ツール用)
    public = [{k: v for k, v in i.items() if k != "markdown"} for i in catalog]
    for entry in public:
        entry["url"] = "%s/%s" % (base, entry["path"])
    write(os.path.join(out_dir, "articles.json"), json.dumps(public, ensure_ascii=False, indent=0))


def build(out_dir=None, site_url=None, quiet=False):
    config = load_config()
    if site_url:
        config["site"]["url"] = site_url.rstrip("/")
    out_dir = out_dir or DEFAULT_OUT
    catalog = load_catalog(config)
    backlinks = load_json(BACKLINKS_FILE, {})
    by_slug = {i["slug"]: i for i in catalog}
    renderer = Renderer(catalog, backlinks, config["site"]["repo_url"])

    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)
    write(os.path.join(out_dir, "assets", "site.css"), CSS.strip() + "\n")
    write(os.path.join(out_dir, ".nojekyll"), "")
    for item in catalog:
        build_article(item, config, renderer, backlinks, by_slug, out_dir)
    build_cluster_pages(catalog, config, out_dir)
    build_domain_pages(catalog, config, out_dir)
    build_all_index(catalog, config, out_dir)
    build_home(catalog, config, out_dir)
    build_feeds(catalog, config, out_dir)
    if os.path.exists(GRAPH_UI):
        os.makedirs(os.path.join(out_dir, "graph"), exist_ok=True)
        shutil.copyfile(GRAPH_UI, os.path.join(out_dir, "graph", "index.html"))

    sources = defaultdict(int)
    for item in catalog:
        sources[item["domain_source"]] += 1
    if not quiet:
        print("site: %d articles -> %s" % (len(catalog), out_dir))
        print("domain source: " + ", ".join("%s=%d" % kv for kv in sorted(sources.items())))
    return catalog


def main():
    parser = argparse.ArgumentParser(description="公開用の静的サイトを生成する")
    parser.add_argument("--out", help="出力先ディレクトリ(既定: site/)")
    parser.add_argument("--site-url", help="公開 URL を上書きする")
    args = parser.parse_args()
    build(args.out, args.site_url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
