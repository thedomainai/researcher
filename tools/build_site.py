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
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from collections import OrderedDict, defaultdict
from urllib.parse import quote

import yaml

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS_DIR = os.path.join(BASE, "wiki", "concepts")
META_FILE = os.path.join(BASE, "wiki", "_meta", "concepts.json")
BACKLINKS_FILE = os.path.join(BASE, "wiki", "_meta", "backlinks.json")
OVERRIDES_FILE = os.path.join(BASE, "wiki", "_meta", "domain_overrides.json")
SUMMARIES_FILE = os.path.join(BASE, "wiki", "_meta", "summaries.json")
INDEX_FILE = os.path.join(BASE, "raw", "index.jsonl")
SITE_CONFIG = os.path.join(BASE, "config", "site.yaml")
SOURCES_CONFIG = os.path.join(BASE, "config", "sources.yaml")
GRAPH_UI = os.path.join(BASE, "wiki", "graph", "index.html")
DEFAULT_OUT = os.path.join(BASE, "site")

TIER_LABEL = {1: "不変原理", 2: "設計原理", 3: "参考"}
TIER_INFO = {}
TIER_PURPOSE = ""
# 記事末尾「次の一歩」の列名。案内文(ガイド・導入文)もここから出す。
NEXT_LABEL = {
    "field": "同じ分野を読む",
    "base": "この記事が参照する概念",
    "apply": "この記事を参照する概念",
    "forward": "設計原理に進む",
    "back": "不変原理に戻る",
    "cross": "別の領域の見方",
}


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
    global TIER_PURPOSE
    notes = (sources.get("tier_classification") or {})
    config["tier_notes"] = {
        1: list((notes.get("tier1") or {}).get("invariant_constraints") or []),
        2: list((notes.get("tier2") or {}).get("vanishing_constraints") or []),
        3: list((notes.get("tier3") or {}).get("skip_indicators") or []),
    }
    tiers = config.get("tiers") or {}
    TIER_PURPOSE = tiers.get("purpose") or ""
    for entry in tiers.get("items") or []:
        TIER_INFO[int(entry["tier"])] = entry
        TIER_LABEL[int(entry["tier"])] = entry["label"]
    return config


SOURCE_RECORDS = defaultdict(list)   # slug -> [index.jsonl の record]
SOURCE_BY_TITLE = {}                 # 正規化した題名 -> record
SOURCE_BY_FILE = {}                  # raw からの相対パス -> record
RAW_PATH = re.compile(r"`?raw/((?:papers|articles)/[^\s`)）]+?\.md)`?")


def scrub_paths(text):
    """本文に紛れた内部ファイルパスを消す(括弧ごと、または題名に置き換える)。"""
    text = re.sub(r"\s*[（(]\s*`?raw/[^)）\n]*?`?\s*[)）]", "", text)
    text = re.sub(r"\s*(?:—\s*)?[（(]+パス未確認[)）]+", "", text)
    text = re.sub(r"\n[ \t]*\*\*ファイルパス\*\*:[^\n]*", "", text)

    def named(match):
        record = SOURCE_BY_FILE.get(match.group(1))
        return record["title"] if record and record.get("title") else ""

    return RAW_PATH.sub(named, text)


def norm_title(text):
    return re.sub(r"[\W_]+", "", (text or "").lower())


def source_meta(record):
    """raw ファイルの frontmatter から、出典表示に使う著者・年・リンクを読む。"""
    meta = {"title": record.get("title") or "", "authors": record.get("authors") or record.get("author") or "",
            "year": str(record.get("year") or ""), "url": ""}
    path = os.path.join(BASE, "raw", record.get("file") or "")
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as handle:
            head = handle.read(2500)
        if head.startswith("---"):
            front = {}
            for line in head.split("---", 2)[1].splitlines():
                m = re.match(r"^([a-z_]+):\s*(.*)$", line.strip())
                if m:
                    front[m.group(1)] = m.group(2).strip().strip('"\'')
            meta["authors"] = meta["authors"] or front.get("authors") or front.get("author") or ""
            meta["year"] = meta["year"] or front.get("year") or ""
            doi = front.get("doi") or ""
            if doi and doi.lower() not in ("none", "null"):
                meta["url"] = doi if doi.startswith("http") else "https://doi.org/" + doi
            elif front.get("url", "").startswith("http"):
                meta["url"] = front["url"]
            elif front.get("arxiv_id") and front["arxiv_id"].lower() not in ("none", "null"):
                meta["url"] = "https://arxiv.org/abs/" + front["arxiv_id"]
            elif front.get("semantic_scholar_id") and front["semantic_scholar_id"].lower() not in ("none", "null"):
                meta["url"] = "https://www.semanticscholar.org/paper/" + front["semantic_scholar_id"]
            elif front.get("openalex_id") and front["openalex_id"].lower() not in ("none", "null"):
                oid = front["openalex_id"]
                meta["url"] = oid if oid.startswith("http") else "https://openalex.org/" + oid
    letters = [ch for ch in meta["title"] if ch.isalpha()]
    if letters and sum(1 for ch in letters if ch.isupper()) > 0.8 * len(letters):
        small = {"a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "with", "by", "at", "from", "as"}
        words = meta["title"].lower().split()
        meta["title"] = " ".join(w if (i and w in small) else w[:1].upper() + w[1:] for i, w in enumerate(words))
    names = [a.strip() for a in re.split(r",|;", meta["authors"]) if a.strip()]
    if len(names) > 3:
        meta["authors"] = ", ".join(names[:3]) + " ほか"
    return meta


def load_source_domains():
    """raw/index.jsonl から slug -> [domain...] と slug -> [tier...] を集める。"""
    by_slug = defaultdict(list)
    tiers = defaultdict(list)
    SOURCE_RECORDS.clear()
    SOURCE_BY_TITLE.clear()
    SOURCE_BY_FILE.clear()
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
            if record.get("title"):
                SOURCE_BY_TITLE.setdefault(norm_title(record["title"]), record)
            if record.get("file"):
                SOURCE_BY_FILE[record["file"]] = record
            for slug in slugs or []:
                if slug:
                    SOURCE_RECORDS[slug].append(record)
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
    summaries = load_json(SUMMARIES_FILE, {})
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
        extra = summaries.get(slug) or {}
        description = extra.get("summary") or item.get("description") or truncate(first_paragraph(markdown), 120)
        if slug not in published:
            # まだコミットされていない新しい記事は、ファイルの更新時刻を公開日とみなす
            stamp = dt.datetime.fromtimestamp(os.path.getmtime(path), dt.timezone.utc).astimezone().isoformat(timespec="seconds")
            published[slug] = stamp
            modified.setdefault(slug, stamp)
        catalog.append({
            "slug": slug,
            "title": item.get("title_ja") or title,
            "title_en": item.get("title_en") or extra.get("title_en") or "",
            "why": extra.get("why") or "",
            "tier": tier,
            "description": description,
            "has_lead": bool(extra.get("summary") or item.get("description")),
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
                return '<a class="wikilink" data-slug="%s" href="%sconcepts/%s/">%s</a>' % (target, root, target, html.escape(label, quote=False))
            return '<span class="wikilink unresolved">%s</span>' % html.escape(label, quote=False)

        value = re.sub(r"\x00WL(\d+)\x00", restore_wl, value)

        def restore_link(match):
            label, url = links[int(match.group(1))]
            return '<a href="%s" rel="noopener nofollow" target="_blank">%s</a>' % (
                html.escape(url, quote=True), html.escape(label, quote=False))

        value = re.sub(r"\x00LK(\d+)\x00", restore_link, value)
        return value

    def render(self, slug, markdown, root):
        self.toc = []
        self.subtoc = {}
        used_anchors = set()
        body = re.sub(r"^# .+\n+", "", markdown.lstrip(), count=1)
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
                level = min(max(len(heading.group(1)), 2), 6)  # 記事の ## が h2(h1 はページ見出し)
                text = heading.group(2).strip()
                anchor = re.sub(r"[^\w\-ぁ-んァ-ヶ一-龠]+", "-", text).strip("-").lower() or "section"
                base_anchor, n_dup = anchor, 2
                while anchor in used_anchors:
                    anchor = "%s-%d" % (base_anchor, n_dup)
                    n_dup += 1
                used_anchors.add(anchor)
                if level in (2, 3):
                    plain = re.sub(r"\[\[(?:[^\]|]+\|)?([^\]]+)\]\]", r"\1", text)
                    plain = re.sub(r"[*`]", "", plain)
                    if level == 2:
                        self.toc.append((anchor, plain))
                    else:
                        self.subtoc.setdefault(self.toc[-1][0] if self.toc else "", []).append((anchor, plain))
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
                labels = [re.sub(r"[*`\[\]]", "", c) for c in cells(header)] if header else []
                for row in body_rows:
                    parts.append("<tr>%s</tr>" % "".join(
                        '<td data-label="%s">%s</td>' % (html.escape(labels[k] if k < len(labels) else "", quote=True), self.inline(slug, c, root))
                        for k, c in enumerate(cells(row))))
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
# ページ生成(デザイン v2: config/site_assets/site.css・site.js と対で動く)
# ---------------------------------------------------------------------------

ASSETS_DIR = os.path.join(BASE, "config", "site_assets")
FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600"
    "&family=JetBrains+Mono:wght@400;500"
    "&family=Shippori+Mincho+B1:wght@500;600;700;800"
    "&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap"
)
FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Crect width='32' height='32' rx='7' fill='%2316150f'/%3E"
    "%3Ccircle cx='16' cy='16' r='10' fill='none' stroke='%23f4f0e8' stroke-width='2'/%3E"
    "%3Ccircle cx='16' cy='16' r='4' fill='%23ff6b4f'/%3E%3C/svg%3E"
)
THEME_BOOT = (
    "<script>(function(){var d=document.documentElement;d.classList.add('js');"
    "try{var t=localStorage.getItem('theme');if(t)d.setAttribute('data-theme',t)}catch(e){}})()</script>"
)
ICON_SEARCH = '<svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="9" cy="9" r="6"/><path d="M14 14l4 4" stroke-linecap="round"/></svg>'
ICON_THEME = '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.8a6.2 6.2 0 0 1 0 12.4z" fill="currentColor"/></svg>'
BRAND_MARK = '<svg class="mark" viewBox="0 0 18 18" aria-hidden="true"><circle cx="9" cy="9" r="8.2"/><circle cx="9" cy="9" r="3"/></svg>'

_asset_versions = {}


def asset_version(name):
    if name not in _asset_versions:
        path = os.path.join(ASSETS_DIR, name)
        digest = "0"
        if os.path.exists(path):
            with open(path, "rb") as handle:
                digest = hashlib.sha1(handle.read()).hexdigest()[:10]
        _asset_versions[name] = digest
    return _asset_versions[name]


def esc(value):
    return html.escape(str(value or ""), quote=True)


def num(value):
    return "{:,}".format(value)


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


def verification_tags(config):
    search = config.get("search") or {}
    tags = []
    if search.get("google_site_verification"):
        tags.append('<meta name="google-site-verification" content="%s">' % esc(search["google_site_verification"]))
    if search.get("bing_site_verification"):
        tags.append('<meta name="msvalidate.01" content="%s">' % esc(search["bing_site_verification"]))
    return "\n".join(tags)


def short_label(cluster):
    return cluster.get("short") or cluster["label"].split("・")[0]


def cluster_of(config, key):
    return next(c for c in config["clusters"] if c["key"] == key)


def fmt_date(value):
    return value[:10] if value else ""


def dot_date(value):
    return value[:10].replace("-", ".") if value else ""


def tier_span(tier, tip=True):
    info = TIER_INFO.get(tier) or {}
    attr = ""
    if tip and info:
        attr = ' data-tip="%s"' % esc("%s: %s。%s" % (info.get("label", ""), info.get("short", ""), info.get("use", "")))
    return '<span class="tier" data-t="%d"%s>%s</span>' % (tier, attr, TIER_LABEL.get(tier, ""))


def tier_mark(tier):
    """文字だけが使える場所(属性・JSON・本文の括弧)用。"""
    return (TIER_INFO.get(tier) or {}).get("mark", "")


def tier_mark_html(tier):
    """分類の印。3 つとも同じ大きさの箱として CSS で描く(塗りの菱形 / 線の菱形 / 線の正方形)。色は領域に譲る。"""
    return '<i class="tm" data-t="%d" aria-hidden="true"></i>' % tier


def tier_counts(catalog):
    counts = {1: 0, 2: 0, 3: 0}
    for item in catalog:
        counts[item["tier"]] = counts.get(item["tier"], 0) + 1
    return counts


def layout(config, root, title, description, body, canonical, og_type="website", extra_head="",
           og_key="default", current="", footer=True, body_attrs=""):
    site = config["site"]
    def cur(name):
        return ' aria-current="page"' if current == name else ""
    header = (
        '<a class="skip" href="#main">本文へ移動</a>'
        '<header class="top"><div class="shell">'
        '<a class="brand" href="%(root)s" aria-label="%(short)s ホーム">%(mark)s<span class="word">%(short)s</span></a>'
        '<nav class="nav" aria-label="主要ナビゲーション">'
        '<a href="%(root)s#clusters"%(c1)s>領域</a><a href="%(root)sconcepts/"%(c2)s>記事</a>'
        '<a href="%(root)sgraph/"%(c3)s>アトラス</a><a class="guide" href="%(root)sguide/"%(c4)s>読み方</a></nav>'
        '<div class="tools"><button class="search-btn" type="button" data-search aria-label="記事を検索">%(isearch)s<span>検索</span><kbd>⌘K</kbd></button>'
        '<button class="icon-btn" type="button" data-theme-toggle aria-label="配色を切り替える">%(itheme)s</button></div>'
        '</div></header>'
    ) % {"root": root or "./", "short": esc(site["short_title"]), "mark": BRAND_MARK,
         "c1": cur("clusters"), "c2": cur("concepts"), "c3": cur("graph"), "c4": cur("guide"),
         "isearch": ICON_SEARCH, "itheme": ICON_THEME}
    foot = ""
    if footer:
        cluster_links = "".join(
            '<li data-c="%s"><a href="%sclusters/%s/"><i class="dot"></i>%s</a></li>' % (c["key"], root, c["key"], esc(c["label"]))
            for c in config["clusters"])
        foot = (
            '<footer class="foot"><div class="shell"><div class="foot-grid">'
            '<div><h2 class="mono">About</h2><p>%(about)s</p></div>'
            '<div><h2 class="mono">領域</h2><ul>%(clusters)s</ul></div>'
            '<div><h2 class="mono">索引</h2><ul>'
            '<li><a href="%(root)sguide/">読み方ガイド</a></li>'
            '<li><a href="%(root)sconcepts/">記事索引</a></li><li><a href="%(root)sgraph/">アトラス(知識グラフ)</a></li>'
            '<li><a href="%(root)sfeed.xml">RSS</a></li><li><a href="%(repo)s" rel="noopener">GitHub</a></li></ul></div>'
            '</div><div class="foot-wrap"><div class="foot-word" aria-hidden="true">%(short)s</div></div>'
            '<div class="foot-base mono"><span>© %(year)d %(author)s</span><span>記事は学術論文をもとに AI が生成 · 順次追加</span>'
            '<button type="button" class="foot-theme" data-theme-toggle>配色を切り替える</button></div>'
            '</div></footer>'
        ) % {"about": esc(site["description"].replace("30 を超える学問分野", "%d の学問分野" % config.get("_domain_count", 30))), "clusters": cluster_links, "root": root, "repo": esc(site["repo_url"]),
             "short": esc(site["short_title"]), "year": dt.date.today().year, "author": esc(site["author"])}
    og_image = "%s/assets/og-%s.png" % (site["url"], og_key)
    head = "\n".join(filter(None, [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>%s</title>" % esc(title),
        '<meta name="description" content="%s">' % esc(truncate(description, 160)),
        '<link rel="canonical" href="%s">' % esc(canonical),
        '<meta name="theme-color" content="#f4f0e8" media="(prefers-color-scheme: light)">',
        '<meta name="theme-color" content="#0f0f0c" media="(prefers-color-scheme: dark)">',
        '<meta property="og:site_name" content="%s">' % esc(site["short_title"]),
        '<meta property="og:type" content="%s">' % og_type,
        '<meta property="og:title" content="%s">' % esc(title),
        '<meta property="og:description" content="%s">' % esc(truncate(description, 160)),
        '<meta property="og:url" content="%s">' % esc(canonical),
        '<meta property="og:locale" content="ja_JP">',
        '<meta property="og:image" content="%s">' % esc(og_image),
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:image" content="%s">' % esc(og_image),
        verification_tags(config),
        '<link rel="icon" href="%s">' % FAVICON,
        '<link rel="alternate" type="application/rss+xml" title="%s" href="%sfeed.xml">' % (esc(site["short_title"]), root),
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link rel="stylesheet" href="%s">' % FONTS_URL,
        '<link rel="stylesheet" href="%sassets/site.css?v=%s">' % (root, asset_version("site.css")),
        THEME_BOOT,
        extra_head,
        analytics_snippet(config),
    ]))
    return (
        '<!DOCTYPE html>\n<html lang="ja" data-root="%s">\n<head>\n%s\n</head>\n<body%s>\n%s\n<main id="main">\n%s\n</main>\n%s\n'
        '<script src="%sassets/site.js?v=%s" defer></script>\n</body>\n</html>\n'
    ) % (root, head, (" " + body_attrs) if body_attrs else "", header, body, foot, root, asset_version("site.js"))


def brk(label):
    """「・」区切りの名称を、区切りの位置でだけ折り返すようにする。"""
    parts = label.split("・")
    return "".join('<span class="nb">%s%s</span>' % (esc(part), "・" if i < len(parts) - 1 else "") for i, part in enumerate(parts))


def crumbs_html(items):
    parts = []
    for index, (label, href) in enumerate(items):
        if index:
            parts.append('<span aria-hidden="true">/</span>')
        parts.append(('<a href="%s">%s</a>' % (esc(href), esc(label))) if href else "<span>%s</span>" % esc(label))
    return '<nav class="crumbs mono" aria-label="パンくず">%s</nav>' % "".join(parts)


def row_html(item, root, config):
    cluster = cluster_of(config, item["cluster"])
    search_text = " ".join([item["title"], item["title_en"], item["slug"]]).lower()
    return (
        '<li class="row" data-c="%s" data-t="%d" data-s="%s" data-slug="%s"><a href="%sconcepts/%s/">'
        '<span class="when mono">%s</span><span class="t">%s</span>'
        '<span class="m mono"><span class="cl"><i class="dot"></i>%s</span> %s</span>'
        '<span class="d">%s</span></a></li>'
    ) % (cluster["key"], item["tier"], esc(search_text), item["slug"], root, item["slug"], ("%d 参照" % item["degree"]) if item.get("degree") else "参照なし",
         esc(item["title"]), esc(short_label(cluster)), tier_span(item["tier"]), esc(item["description"]))


def rows_html(items, root, config):
    return '<ul class="rows">%s</ul>' % "".join(row_html(i, root, config) for i in items)


def filters_html(config, with_clusters, total):
    chips = []
    if with_clusters:
        chips.append('<div class="chips" role="group" aria-label="領域で絞り込む">%s</div>' % "".join(
            '<button class="chip" type="button" data-c="%s" data-f="c:%s" aria-pressed="false"><i class="dot"></i>%s</button>' % (
                c["key"], c["key"], esc(short_label(c))) for c in config["clusters"]))
    chips.append('<div class="chips" role="group" aria-label="分類で絞り込む">%s</div>' % "".join(
        '<button class="chip" type="button" data-f="t:%d" aria-pressed="false">%s %s</button>' % (t, tier_mark_html(t), TIER_LABEL[t]) for t in (1, 2, 3)))
    return (
        '<div class="filters"><span class="mono lab">絞り込み</span><input type="text" inputmode="search" placeholder="この一覧を絞り込む" aria-label="一覧を絞り込む">%s'
        '<button class="clear" type="button" hidden>条件を解除</button><span class="count mono" aria-live="polite">%s 件</span></div>'
    ) % ("".join(chips), num(total))


def tier_key_html(catalog, root):
    """仕分けの目的と 3 つの分類を、一覧の上に示す。"""
    counts = tier_counts(catalog)
    items = "".join(
        '<li><b>%s %s</b><span class="n">%s</span>%s</li>' % (
            tier_mark_html(t), TIER_LABEL[t], num(counts.get(t, 0)), esc((TIER_INFO.get(t) or {}).get("short", "")))
        for t in (1, 2, 3))
    return (
        '<p class="tier-why">%s<a href="%sguide/">読み方ガイド <span class="arr">→</span></a></p>'
        '<ul class="tier-key">%s</ul>'
        '<details class="tier-key-m"><summary>%s%s%s の意味</summary><ul>%s</ul></details>' % (esc(TIER_PURPOSE), root, items, tier_mark_html(1), tier_mark_html(2), tier_mark_html(3), items))


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def build_graph_data(catalog, backlinks, config):
    """記事どうしの参照(解決済みリンク)から、無向グラフと次数を作る。"""
    index = {item["slug"]: i for i, item in enumerate(catalog)}
    nodes = (backlinks or {}).get("nodes", {})
    pairs = set()
    for slug, i in index.items():
        for edge in (nodes.get(slug) or {}).get("outbound", []):
            j = index.get(edge.get("id"))
            if edge.get("resolved") and j is not None and j != i:
                pairs.add((min(i, j), max(i, j)))
    degree = [0] * len(catalog)
    neighbors = defaultdict(set)
    for i, j in pairs:
        degree[i] += 1
        degree[j] += 1
        neighbors[i].add(j)
        neighbors[j].add(i)
    for i, item in enumerate(catalog):
        item["degree"] = degree[i]
    return sorted(pairs), neighbors


def graph_payload(catalog, pairs, config, subset=None, with_desc=True):
    keys = [c["key"] for c in config["clusters"]]
    if subset is None:
        subset = list(range(len(catalog)))
    remap = {old: new for new, old in enumerate(subset)}
    nodes = []
    for old in subset:
        item = catalog[old]
        node = [item["slug"], item["title"], keys.index(item["cluster"]), item["tier"], item["degree"]]
        if with_desc:
            node.append(truncate(item["description"], 140))
        nodes.append(node)
    edges = [[remap[i], remap[j]] for i, j in pairs if i in remap and j in remap]
    return {"clusters": [[c["key"], c["label"], short_label(c)] for c in config["clusters"]], "nodes": nodes, "edges": edges}


def hero_subset(catalog, config, total=120, per_cluster=12):
    order = sorted(range(len(catalog)), key=lambda i: -catalog[i]["degree"])
    chosen = []
    for cluster in config["clusters"]:
        chosen.extend([i for i in order if catalog[i]["cluster"] == cluster["key"]][:per_cluster])
    seen = set(chosen)
    for i in order:
        if len(chosen) >= total:
            break
        if i not in seen:
            chosen.append(i)
            seen.add(i)
    return chosen


def related_items(slug, backlinks, by_slug, limit=6):
    node = (backlinks or {}).get("nodes", {}).get(slug) or {}
    seen = OrderedDict()
    for edge in node.get("outbound", []) + node.get("inbound", []):
        target = edge.get("id")
        if edge.get("resolved") and target in by_slug and target != slug:
            seen[target] = seen.get(target, 0) + (edge.get("weight") or 1)
    ranked = sorted(seen.items(), key=lambda kv: (-kv[1], -by_slug[kv[0]].get("degree", 0), by_slug[kv[0]]["title"]))
    return [by_slug[s] for s, _ in ranked[:limit]]


def cluster_bridges(catalog, pairs):
    """領域どうしの参照の本数。"""
    counts = defaultdict(int)
    for i, j in pairs:
        a, b = catalog[i]["cluster"], catalog[j]["cluster"]
        if a != b:
            counts[(a, b)] += 1
            counts[(b, a)] += 1
    return counts


def next_row(c, root, config):
    cl = cluster_of(config, c["cluster"])
    return (
        '<li data-slug="%s" data-c="%s"><a href="%sconcepts/%s/"><span class="t">%s</span>'
        '<span class="m mono"><i class="dot"></i>%s %s</span><span class="d">%s</span></a></li>'
    ) % (c["slug"], c["cluster"], root, c["slug"], esc(c["title"]), esc(short_label(cl)), tier_span(c["tier"]), esc(c["description"]))


def next_steps_html(item, config, by_slug, backlinks, catalog, root):
    """記事の末尾に出す「次の一歩」。読み手の意図(基礎へ・応用へ・設計へ・別の領域へ)ごとに道筋を分ける。"""
    node = (backlinks or {}).get("nodes", {}).get(item["slug"]) or {}

    def weights(edges):
        out = OrderedDict()
        for e in edges:
            t = e.get("id")
            if e.get("resolved") and t in by_slug and t != item["slug"]:
                out[t] = out.get(t, 0) + (e.get("weight") or 1)
        return out

    outw, inw = weights(node.get("outbound", [])), weights(node.get("inbound", []))
    both = OrderedDict()
    for d in (outw, inw):
        for t, w in d.items():
            both[t] = both.get(t, 0) + w

    def ranked(ws):
        return [by_slug[t] for t, _ in sorted(ws.items(), key=lambda kv: (-kv[1], -by_slug[kv[0]].get("degree", 0), by_slug[kv[0]]["title"]))]

    ranked_both = ranked(both)
    isolated = not ranked_both
    if isolated:
        # 記事どうしの参照が無い記事(行き止まりを作らないため): 同じ分野、無ければ同じ領域から選ぶ
        same_domain = [c for c in catalog if c["slug"] != item["slug"] and item["domains"] and c["domains"] and c["domains"][0] == item["domains"][0]]
        same_cluster = [c for c in catalog if c["slug"] != item["slug"] and c["cluster"] == item["cluster"]]
        pool = sorted(same_domain if len(same_domain) >= 3 else same_cluster, key=lambda c: (c["tier"] != 1, -c.get("degree", 0), c["title"]))
        if not pool:
            return ""
        main = pool[0]
    else:
        main = ranked_both[0]
    used = {main["slug"]}

    def take(cands, n=3):
        out = []
        for c in cands:
            if c["slug"] in used:
                continue
            out.append(c)
            used.add(c["slug"])
            if len(out) >= n:
                break
        return out

    if isolated:
        why = "同じ分野でよく参照される概念"
    elif main["slug"] in outw and main["slug"] in inw:
        why = "たがいに参照し合う概念"
    elif main["slug"] in outw:
        why = NEXT_LABEL["base"]
    else:
        why = NEXT_LABEL["apply"]
    base = take(ranked(outw))
    apply_ = take(ranked(inw))
    cross = take([c for c in ranked_both if c["cluster"] != item["cluster"]])
    field = take(pool[1:], 3) if isolated else []
    if item["tier"] == 1:
        want, head, sub = 2, NEXT_LABEL["forward"], "参照でつながっている設計原理"
    else:
        want, head, sub = 1, NEXT_LABEL["back"], "参照でつながっている不変原理"
    bridge = take([c for c in ranked_both if c["tier"] == want], 3)
    if not bridge:
        fill = sorted([c for c in catalog if c["cluster"] == item["cluster"] and c["tier"] == want], key=lambda c: -c.get("degree", 0))
        bridge = take(fill, 2)
        sub = "この記事とは参照が無いため、同じ領域から選びました"

    field_label = (config["domain_labels"].get(item["domains"][0], "同じ分野") if item["domains"] else "同じ領域")
    m1, m2 = tier_mark_html(1), tier_mark_html(2)
    rank_note = {1: "%s不変原理 → %s設計原理の順に読むと、原理から設計へ進めます" % (m1, m2),
                 2: "%s設計原理から%s不変原理へ戻ると、根拠を確かめられます" % (m2, m1),
                 3: "参考は辞書として引く記事です。不変原理に戻ると全体像がつかめます"}.get(item["tier"], "")
    # 各列は 1 本だけ要約つきで見せ、残りは題名だけの行にする(選ぶ負担を減らす)
    def col_html(ckey, title, hint, rows):
        if not rows:
            return ""
        first = rows[0]
        rest = "".join(
            '<li class="more-row" data-slug="%s" data-c="%s"><a href="%sconcepts/%s/"><span class="t">%s</span>'
            '<span class="m mono"><i class="dot"></i>%s %s</span></a></li>' % (
                c["slug"], c["cluster"], root, c["slug"], esc(c["title"]), esc(short_label(cluster_of(config, c["cluster"]))), tier_span(c["tier"], tip=False))
            for c in rows[1:])
        return (
            '<section class="next-col" data-k="%s"><h3><b>%s</b><small>%s</small></h3><ul>%s%s</ul></section>' % (
                ckey, title, hint, next_row(first, root, config), rest))
    cols = "".join(col_html(*spec) for spec in (
        ("field", NEXT_LABEL["field"], "この記事とは参照が無い、%s でつながりの多い概念" % field_label, field),
        ("base", NEXT_LABEL["base"], "背景として挙げられている記事(参照の向きから自動で選んでいます)", base),
        ("apply", NEXT_LABEL["apply"], "この記事を土台にしている記事(参照の向きから自動で選んでいます)", apply_),
        ("bridge", head, sub, bridge),
        ("cross", NEXT_LABEL["cross"], "上の列に入らなかった、ほかの領域の概念", cross),
    ))
    main_mark = "%s %s" % (tier_mark_html(main["tier"]), esc(TIER_LABEL.get(main["tier"], "")))
    cands = [main] + apply_ + base + bridge + cross
    cand_json = json.dumps([[c["slug"], c["title"], c["tier"]] for c in cands[:10]], ensure_ascii=False, separators=(",", ":"))
    cl = cluster_of(config, item["cluster"])
    n_cluster = sum(1 for c in catalog if c["cluster"] == item["cluster"])
    actions = (
        '<div class="next-actions">'
        '<a href="%sclusters/%s/"><span>この領域の記事を一覧する</span><b class="mono">%s</b></a>'
        '<a href="%sconcepts/?t=1"><span>不変原理を参照の多い順に読む</span><b class="mono">%s</b></a>'
        '<a href="%sgraph/#%s"><span>アトラスで位置を見る</span><b class="mono">→</b></a>'
        '<button type="button" data-search><span>別の言葉で探す</span><b class="mono">⌘K</b></button></div>'
    ) % (root, cl["key"], num(n_cluster), root, tier_mark_html(1), root, item["slug"])
    return (
        '<section class="sec art-end next" id="next-step" data-c="%s"><div class="shell"><header class="sec-head reveal">'
        '<span class="sec-no mono">次に読む</span><h2>次の一歩</h2>'
        '<p>%s。<a class="inline block" href="%sguide/">仕分けの基準を見る <span class="arr">→</span></a></p></header>'
        '<div class="next-grid reveal">'
        '<a class="next-main" data-slug="%s" data-c="%s" href="%sconcepts/%s/" data-cands="%s"><span class="mono">まず読むなら · %s · %s</span>'
        '<span class="t">%s</span><span class="d">%s</span><span class="go">この記事から続けて読む <i class="arr">→</i></span></a>'
        '<div class="next-cols">%s</div></div>'
        '<div class="reveal">%s</div></div>'
        '<aside class="next-bar" hidden aria-label="次に読む記事" data-cands="%s" data-root="%s"><span class="mono">次に読む</span>'
        '<a href="%sconcepts/%s/"><b>%s</b><i class="arr">→</i></a><button type="button" aria-label="この案内を閉じる">×</button></aside></section>'
    ) % (item["cluster"], ("この記事はまだ他の記事と参照でつながっていないため、同じ分野から選びました" if isolated else rank_note), root, main["slug"], main["cluster"], root, main["slug"], esc(cand_json), main_mark, esc(why),
         esc(main["title"]), esc(main["description"]), cols, actions, esc(cand_json), root, root, main["slug"], esc(main["title"]))


SECTION_SPLIT = re.compile(r"\n(?=##\s)")


def split_article(markdown, slug, drop_related):
    """本文と、出典の節・関連概念の節を分ける。出典は index の書誌から組み直す。"""
    sections = SECTION_SPLIT.split("\n" + markdown.strip())
    body, tail = [], []
    for section in sections:
        head = section.strip().splitlines()[0] if section.strip() else ""
        if re.match(r"##\s*(参考ソース|追加ソース|参考文献|出典|ソース)", head):
            tail.append(section)
        elif drop_related and re.match(r"##\s*関連(概念|コンセプト|する概念)", head):
            continue
        else:
            body.append(section)
    records = list(SOURCE_RECORDS.get(slug, []))
    seen = {r.get("file") for r in records}
    tail_text = "\n".join(tail)
    for path in RAW_PATH.findall(tail_text):
        record = SOURCE_BY_FILE.get(path)
        if record and record.get("file") not in seen:
            records.append(record)
            seen.add(record.get("file"))
    for candidate in re.findall(r"\[([^\]]{12,})\]\(|\"([^\"\n]{12,})\"|「([^」\n]{12,})」|\*\*タイトル\*\*:\s*([^\n(（]{12,})", tail_text):
        text = next((c for c in candidate if c), "")
        text = re.sub(r"\s*\(\d{4}\)\s*$", "", text).strip()
        record = SOURCE_BY_TITLE.get(norm_title(text))
        if record and record.get("file") not in seen:
            records.append(record)
            seen.add(record.get("file"))
    return scrub_paths("\n".join(body).strip()), tail_text, records


def clean_source_tail(text):
    text = scrub_paths(text)
    text = re.sub(r"`?raw/[^\s`)）]*`?", "", text)
    text = re.sub(r"##\s*追加ソース[^\n]*", "", text)
    text = re.sub(r"##\s*(参考ソース|参考文献|ソース)[^\n]*", "## 出典", text, count=1)
    return re.sub(r"##\s*(参考ソース|参考文献|ソース)[^\n]*", "", text)


def bibliography_html(records):
    items = []
    for record in records:
        meta = source_meta(record)
        title = esc(meta["title"])
        if meta["url"]:
            title = '<a href="%s" target="_blank" rel="noopener nofollow">%s</a>' % (esc(meta["url"]), title)
        lead = " ".join(filter(None, [esc(meta["authors"]), ("(%s)" % esc(meta["year"])) if meta["year"] else ""]))
        link_text = re.sub(r"^https?://(www\.)?", "", meta["url"]) if meta["url"] else ""
        items.append("<li>%s%s<cite>%s</cite>%s</li>" % (
            lead, ". " if lead else "", title, ('<span class="mono src-id">%s</span>' % esc(link_text)) if link_text else ""))
    return '<h2 id="sources">出典</h2><ol class="refs">%s</ol>' % "".join(items)


def count_sources(markdown):
    parts = re.split(r"(?:^|\n)## (?:参考ソース|追加ソース|参考文献|出典|ソース)[^\n]*\n", markdown)
    if len(parts) < 2:
        return 0
    total = 0
    for part in parts[1:]:
        block = re.split(r"\n## ", part)[0]
        table = [l for l in block.splitlines() if l.strip().startswith("|")]
        total += max(0, len(table) - 2) if table else 0
        total += sum(1 for l in block.splitlines() if re.match(r"^\s*[-*]\s+", l))
    return total


def build_article(item, config, renderer, backlinks, by_slug, out_dir, catalog=None, pairs=None, neighbors=None, index=None):
    root = "../../"
    site = config["site"]
    url = "%s/%s" % (site["url"], item["path"])
    cluster = cluster_of(config, item["cluster"])
    related = related_items(item["slug"], backlinks, by_slug)
    body_md, tail_md, records = split_article(item["markdown"], item["slug"], drop_related=len(related) >= 3)
    body_html = renderer.render(item["slug"], body_md, root)
    toc = list(renderer.toc)
    subtoc = dict(renderer.subtoc)
    handoff = ""
    if backlinks is not None:
        handoff = '<p class="handoff" hidden data-handoff><span class="mono">本文はここまで</span><a href="#next-step">次の一歩へ ↓</a><a class="hf-next" href="#"></a></p>'
    if records:
        body_html += handoff + bibliography_html(records)
        toc.append(("sources", "出典"))
        sources = len(records)
    else:
        cleaned = clean_source_tail(tail_md)
        sources = count_sources(tail_md)
        body_html += handoff
        if cleaned.strip():
            body_html += renderer.render(item["slug"], "# x\n\n" + cleaned, root)
            toc.extend(renderer.toc)
    source_anchor = next((a for a, t in toc if t == "出典"), "")
    minutes = max(1, int(round(len(item["markdown"]) / 600.0)))

    toc_items = "".join('<li><a href="#%s">%s</a></li>' % (esc(anchor), esc(text)) for anchor, text in toc)
    toc_full = "".join(
        '<li><a href="#%s">%s</a>%s</li>' % (
            esc(anchor), esc(text),
            ("<ul>%s</ul>" % "".join('<li><a href="#%s">%s</a></li>' % (esc(a), esc(t)) for a, t in subtoc[anchor][:8])) if subtoc.get(anchor) else "")
        for anchor, text in toc)
    toc_side = '<aside class="art-side side-toc">%s</aside>' % (
        ('<div class="side-block"><h2 class="mono">目次</h2><ol class="toc">%s</ol></div>' % toc_full) if toc else "")
    toc_mobile = ('<details class="art-toc-m"><summary>目次</summary><ol class="toc">%s</ol></details>' % toc_items) if toc else ""
    domain_links = "、".join(
        '<a href="%sdomains/%s/">%s</a>' % (root, d, esc(config["domain_labels"].get(d, d))) for d in item["domains"]) or "分野横断"
    ego_html = ""
    if neighbors is not None and index is not None:
        me = index[item["slug"]]
        near = sorted(neighbors.get(me, ()), key=lambda j: -catalog[j]["degree"])[:14]
        if len(near) >= 2:
            payload = graph_payload(catalog, pairs, config, [me] + near, with_desc=True)
            ego_html = (
                '<figure class="ego" aria-label="この概念とつながる記事の図"><canvas></canvas><div class="graph-tip"></div>'
                '<figcaption class="mono"><span>近傍 %d 概念 · 点に触れると名前</span><a href="%sgraph/#%s">アトラスで開く</a></figcaption>'
                '<script type="application/json" id="ego-graph">%s</script></figure>'
            ) % (len(neighbors.get(me, ())), root, item["slug"],
                 json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
    facts = [
        ("領域", '<a href="%sclusters/%s/">%s</a>' % (root, cluster["key"], esc(cluster["label"]))),
        ("分野", domain_links),
        ("分類", '%s %s<a class="fact-sub" href="%sguide/#tier-%d">%s</a>' % (
            tier_mark_html(item["tier"]), esc(TIER_LABEL.get(item["tier"], "")), root, item["tier"],
            esc((TIER_INFO.get(item["tier"]) or {}).get("short", "")))),
        ("公開", dot_date(item["published"])),
    ]
    if item["modified"] and item["modified"][:10] != item["published"][:10]:
        facts.append(("更新", dot_date(item["modified"])))
    facts.append(("参照", "%d 記事とつながる" % item.get("degree", 0)))
    facts_html = "".join("<dt>%s</dt><dd>%s</dd>" % (k, v) for k, v in facts)
    share_text = quote("%s | %s" % (item["title"], site["short_title"]))
    share = (
        '<div class="side-block"><h2 class="mono">共有</h2><div class="share">'
        '<a href="https://x.com/intent/post?text=%s&amp;url=%s" target="_blank" rel="noopener">X でポスト</a>'
        '<button type="button" data-copy>リンクをコピー</button></div></div>'
    ) % (share_text, quote(url, safe=""))
    side_meta = '<aside class="art-side side-meta"><div class="side-block"><h2 class="mono">この記事</h2><dl class="facts">%s</dl></div>%s</aside>' % (
        facts_html, share)

    related_html = next_steps_html(item, config, by_slug, backlinks, catalog, root)

    source_md = "%s/blob/main/wiki/concepts/%s.md" % (site["repo_url"], item["slug"])
    body = (
        '<div class="progress" aria-hidden="true"></div>'
        '<article data-c="%(ckey)s" data-slug="%(slug)s">'
        '<header class="art-head"><div class="shell">%(crumbs)s<div>'
        '<div class="art-kicker mono"><a href="%(root)sclusters/%(ckey)s/"><i class="dot"></i>%(clabel)s</a>%(tier)s</div>'
        '<h1>%(title)s</h1>%(en)s%(lede)s%(why)s%(src)s</div>%(ego)s</div></header>'
        '<div class="shell art-grid">%(toc_side)s<div class="art-main">%(toc_m)s<div class="prose">%(body)s'
        '<div class="notice"><span class="mono">Note</span><p>%(notice)s <a href="%(source)s" rel="noopener">原稿(Markdown)を GitHub で見る</a></p></div>'
        '</div></div>%(side_meta)s</div></article>%(related)s'
    ) % {
        "ckey": cluster["key"], "clabel": esc(cluster["label"]), "root": root, "slug": item["slug"],
        "crumbs": crumbs_html([(site["short_title"], root), (cluster["label"], root + "clusters/%s/" % cluster["key"]), (item["title"], None)]),
        "tier": ('<a class="tier-link" data-t="%d" href="%sguide/#tier-%d"><span class="mk">%s</span> %s'
                 '<span class="def">%s</span></a>') % (
            item["tier"], root, item["tier"], tier_mark_html(item["tier"]), esc(TIER_LABEL.get(item["tier"], "")),
            esc((TIER_INFO.get(item["tier"]) or {}).get("short", ""))) +
            '<a class="why-sort" href="%sguide/">AI 時代にも通用するかで仕分けしています <i class="arr">→</i></a>' % root,
        "why": ('<p class="art-why"><span class="mono">実務への含意</span><span>%s</span></p>' % esc(item["why"])) if item.get("why") else "",
        "src": '<p class="art-src">%s</p>' % (
            ('<a href="#%s">出典 %d 本をもとに AI が執筆</a> · 約 %d 分' % (esc(source_anchor), sources, minutes)) if sources and source_anchor
            else "論文をもとに AI が執筆 · 約 %d 分" % minutes),
        "ego": ego_html + (
            '<a class="art-atlas" href="%sgraph/#%s">%d 記事とつながる · アトラスで開く <span class="arr">→</span></a>' % (
                root, item["slug"], item.get("degree", 0)) if item.get("degree") else ""),
        "title": esc(item["title"]),
        "en": ('<p class="art-en" lang="en">%s</p>' % esc(item["title_en"])) if item["title_en"] else "",
        "lede": ('<p class="art-lede">%s</p>' % esc(item["description"])) if item["has_lead"] else "",
        "toc_side": toc_side, "side_meta": side_meta, "toc_m": toc_mobile, "body": body_html,
        "notice": esc(site["ai_notice"]), "source": esc(source_md), "related": related_html,
    }
    json_ld = {
        "@context": "https://schema.org", "@type": "Article", "headline": item["title"],
        "description": item["description"], "inLanguage": "ja", "isAccessibleForFree": True, "url": url,
        "author": {"@type": "Organization", "name": site["author"]},
        "publisher": {"@type": "Organization", "name": site["author"]},
        "about": [config["domain_labels"].get(d, d) for d in item["domains"]],
    }
    if item["published"]:
        json_ld["datePublished"] = item["published"]
    if item["modified"]:
        json_ld["dateModified"] = item["modified"]
    extra_head = '<script type="application/ld+json">%s</script>' % json.dumps(json_ld, ensure_ascii=False).replace("</", "<\\/")
    page = layout(config, root, "%s | %s" % (item["title"], site["short_title"]), item["description"], body, url,
                  og_type="article", extra_head=extra_head, og_key=cluster["key"], current="concepts")
    write(os.path.join(out_dir, "concepts", item["slug"], "index.html"), page)


def build_cluster_pages(catalog, config, out_dir, pairs=None):
    site = config["site"]
    root = "../../"
    bridges = cluster_bridges(catalog, pairs or [])
    for number, cluster in enumerate(config["clusters"], 1):
        items = [i for i in catalog if i["cluster"] == cluster["key"]]
        by_domain = defaultdict(list)
        for item in items:
            by_domain[item["domains"][0] if item["domains"] else "_other"].append(item)
        sections = []
        jumps = []
        def start_set(tier, number):
            picks = sorted([i for i in items if i["tier"] == tier], key=lambda i: -i.get("degree", 0))[:3]
            if len(picks) < 2:
                return ""
            info = TIER_INFO.get(tier) or {}
            cards = "".join(
                '<a href="%sconcepts/%s/" data-slug="%s" data-c="%s"><span class="t">%s</span><span class="d">%s</span>'
                '<span class="f mono">%d 件の参照</span></a>' % (
                    root, i["slug"], i["slug"], i["cluster"], esc(i["title"]), esc(i["description"]), i.get("degree", 0)) for i in picks)
            return (
                '<div class="start-set"><h3><b>%s %s %s</b><small>%s</small></h3><div class="rel">%s</div></div>' % (
                    "①②"[number - 1], tier_mark_html(tier), esc(info.get("label", "")), esc(info.get("use", "")), cards))
        starts_html = ""
        blocks = start_set(1, 1) + start_set(2, 2)
        if blocks:
            starts_html = '<div class="starts"><span class="mono">読む順番</span><div class="start-sets">%s</div></div>' % blocks
        near = sorted([(n, k) for (a_, k), n in bridges.items() if a_ == cluster["key"]], reverse=True)[:2]
        bridge_html = ""
        if near:
            bridge_html = (
                '<section class="bridge"><div class="shell"><span class="mono">隣の領域へ</span><div class="bridge-grid">%s</div></div></section>' % "".join(
                    '<a class="bridge-card" data-c="%s" href="%sclusters/%s/"><span class="t">%s</span><span class="d">%s</span>'
                    '<span class="f mono">この領域との参照 %s 本</span></a>' % (
                        k, root, k, esc(cluster_of(config, k)["label"]), esc(cluster_of(config, k)["tagline"]), num(n)) for n, k in near))
        for domain in cluster["domains"] + ["_other"]:
            group = by_domain.get(domain)
            if not group:
                continue
            group.sort(key=lambda i: (i["tier"], -i.get("degree", 0), i["title"]))
            label = config["domain_labels"].get(domain, "分野横断") if domain != "_other" else "分野横断"
            question = config["domain_questions"].get(domain, "") if domain != "_other" else ""
            sections.append(
                '<section class="group" id="%s"><div class="group-head"><span class="mono">%02d</span>'
                '<h2><em>%s</em>%s%s</h2><span class="mono"><span class="n">%s</span> 記事 · 参照の多い順</span></div>%s</section>' % (
                    esc(domain), len(sections) + 1, esc(domain.replace("_", " ").upper()), esc(label),
                    ("<small>%s</small>" % esc(question)) if question else "", num(len(group)), rows_html(group, root, config)))
            jumps.append((len(group), '<a class="chip" href="#%s">%s <span class="mono">%s</span></a>' % (esc(domain), esc(label), num(len(group)))))
        body = (
            '<header class="page-head" data-c="%(key)s"><div class="shell">%(crumbs)s'
            '<div><h1>%(label)s</h1><p class="lede">%(tag)s</p></div>'
            '<div class="big-no" aria-hidden="true">%(count)s<small>CONCEPTS · 領域 %(no)02d / %(total)02d</small></div></div></header>'
            '<div class="shell" data-c="%(key)s">%(starts)s<nav class="jump" aria-label="分野へ移動"><span class="mono lab">分野へ移動</span>%(jumps)s</nav></div>'
            '<div class="shell" data-c="%(key)s" style="margin-top:26px">%(filters)s%(sections)s<p class="empty" hidden>条件に合う記事がありません。</p></div>'
            '%(bridge)s<div style="height:clamp(60px,9vw,130px)"></div>'
        ) % {"key": cluster["key"], "label": brk(cluster["label"]), "tag": esc(cluster["tagline"]), "count": num(len(items)),
             "no": number, "total": len(config["clusters"]),
             "crumbs": crumbs_html([(site["short_title"], root), ("領域", root + "#clusters"), (cluster["label"], None)]),
             "filters": filters_html(config, False, len(items)), "sections": "".join(sections),
             "starts": starts_html, "bridge": bridge_html, "jumps": "".join(h for _, h in sorted(jumps, key=lambda x: -x[0]))}
        url = "%s/clusters/%s/" % (site["url"], cluster["key"])
        page = layout(config, root, "%s | %s" % (cluster["label"], site["short_title"]),
                      "%s — %s の概念記事 %d 本。" % (cluster["tagline"], cluster["label"], len(items)), body, url,
                      og_key=cluster["key"], current="clusters")
        write(os.path.join(out_dir, "clusters", cluster["key"], "index.html"), page)


def build_domain_pages(catalog, config, out_dir):
    site = config["site"]
    root = "../../"
    for domain, label in config["domain_labels"].items():
        items = [i for i in catalog if domain in i["domains"]]
        if not items:
            continue
        items.sort(key=lambda i: (i["tier"], -i.get("degree", 0), i["title"]))
        cluster = cluster_of(config, config["domain_to_cluster"][domain]) if domain in config["domain_to_cluster"] else None
        question = config["domain_questions"].get(domain, "")
        crumbs = [(site["short_title"], root)]
        if cluster:
            crumbs.append((cluster["label"], root + "clusters/%s/" % cluster["key"]))
        crumbs.append((label, None))
        ckey = cluster["key"] if cluster else ""
        body = (
            '<header class="page-head" data-c="%(ckey)s"><div class="shell">%(crumbs)s'
            '<div><h1>%(label)s</h1><p class="lede">%(q)s</p></div>'
            '<div class="big-no" aria-hidden="true">%(count)s<small>CONCEPTS · %(en)s</small></div></div></header>'
            '<div class="shell" data-c="%(ckey)s">%(filters)s%(rows)s<p class="empty" hidden>条件に合う記事がありません。</p></div>'
            '<div style="height:clamp(60px,9vw,130px)"></div>'
        ) % {"ckey": ckey, "crumbs": crumbs_html(crumbs), "label": esc(label), "q": esc(question), "count": num(len(items)),
             "en": esc(domain.replace("_", " ").upper()), "filters": filters_html(config, False, len(items)),
             "rows": rows_html(items, root, config)}
        url = "%s/domains/%s/" % (site["url"], domain)
        page = layout(config, root, "%s | %s" % (label, site["short_title"]), question or label, body, url,
                      og_key=ckey or "default", current="clusters")
        write(os.path.join(out_dir, "domains", domain, "index.html"), page)


def build_all_index(catalog, config, out_dir):
    site = config["site"]
    root = "../"
    items = catalog
    day_sections = []
    for number, cluster in enumerate(config["clusters"], 1):
        group = sorted([i for i in catalog if i["cluster"] == cluster["key"]], key=lambda i: (-i.get("degree", 0), i["tier"], i["title"]))
        if not group:
            continue
        day_sections.append(
            '<section class="group" id="%s" data-c="%s"><div class="group-head"><span class="mono">%02d</span>'
            '<h2><a href="%sclusters/%s/">%s</a><small>%s</small></h2>'
            '<span class="mono"><span class="n">%s</span> 記事 · 参照の多い順</span></div>%s</section>' % (
                cluster["key"], cluster["key"], number, root, cluster["key"], esc(cluster["label"]), esc(cluster["tagline"]),
                num(len(group)), rows_html(group, root, config)))
    body = (
        '<header class="page-head"><div class="shell">%(crumbs)s'
        '<div><h1>記事索引</h1><p class="lede">すべての概念記事を、領域ごと(%(domains)d の学問分野を 6 つの領域に束ねています)に、参照の多い順で並べています。領域・分類・語で絞り込めます。</p>%(key)s</div>'
        '<div class="big-no" aria-hidden="true" style="color:var(--ink)">%(count)s<small>CONCEPTS</small></div></div></header>'
        '<div class="shell">%(filters)s%(rows)s<p class="empty" hidden>条件に合う記事がありません。</p></div>'
        '<div style="height:clamp(60px,9vw,130px)"></div>'
    ) % {"crumbs": crumbs_html([(site["short_title"], root), ("記事索引", None)]), "count": num(len(items)),
         "filters": filters_html(config, True, len(items)), "rows": "".join(day_sections), "key": tier_key_html(catalog, root),
         "domains": len({d for i in catalog for d in i["domains"]})}
    page = layout(config, root, "記事索引 | %s" % site["short_title"], site["description"], body, site["url"] + "/concepts/",
                  current="concepts")
    write(os.path.join(out_dir, "concepts", "index.html"), page)


def home_tiers_html(catalog, root):
    counts = tier_counts(catalog)
    out = []
    for order, t in enumerate((1, 2, 3), 1):
        info = TIER_INFO.get(t) or {}
        out.append(
            '<li data-t="%d"><span class="no mono">%s</span><span class="mk" aria-hidden="true">%s</span>'
            '<h3>%s</h3><p class="def">%s</p><p class="q"><span class="mono">判定の問い</span>%s</p>'
            '<p class="use">%s</p><a class="go %s" href="%sconcepts/?t=%d">%s</a></li>' % (
                t, ("読む順 ①" if t == 1 else "読む順 ②") if t != 3 else "随時 · 必要なときに", tier_mark_html(t), esc(info.get("label", "")), esc(info.get("short", "")),
                esc(info.get("question", "")), esc(info.get("use", "")), "go-text" if t == 3 else "", root, t,
                ('<b>%s</b> 本を参照の多い順に読む <i class="arr">→</i>' % num(counts.get(t, 0))) if t != 3 else ('参考の記事 <b>%s</b> 本を見る <i class="arr">→</i>' % num(counts.get(t, 0)))))
    return "".join(out)


def build_home(catalog, config, out_dir, pairs, paper_count):
    site = config["site"]
    root = ""
    tier1 = sorted([i for i in catalog if i["tier"] == 1], key=lambda i: -i["degree"])[:6]
    shown = {i["slug"] for i in tier1}
    latest = sorted([i for i in catalog if i["slug"] not in shown], key=lambda i: (i["published"][:10], i["modified"], i["degree"]), reverse=True)[:8]
    domain_count = len({d for i in catalog for d in i["domains"]})

    rows = []
    for number, cluster in enumerate(config["clusters"], 1):
        members = [i for i in catalog if i["cluster"] == cluster["key"]]
        samples = sorted(members, key=lambda i: -i["degree"])[:3]
        rows.append(
            '<li><a class="cl-row" data-c="%s" href="clusters/%s/"><span class="cl-no mono"><i></i>%02d</span>'
            '<span class="cl-name">%s</span><span class="cl-tag">%s<small>%s</small></span>'
            '<span class="cl-count">%s<small>CONCEPTS</small></span><span class="cl-arr" aria-hidden="true">→</span></a></li>' % (
                cluster["key"], cluster["key"], number, brk(cluster["label"]), esc(cluster["tagline"]),
                esc(" / ".join(s["title"] for s in samples)), num(len(members))))
    cards = "".join(
        '<a class="card" data-c="%s" href="concepts/%s/"><span class="n">%02d</span><span class="t">%s</span>'
        '<span class="d">%s</span><span class="f mono"><i class="dot"></i>%s · %d LINKS</span></a>' % (
            item["cluster"], item["slug"], n, esc(item["title"]), esc(item["description"]),
            esc(short_label(cluster_of(config, item["cluster"]))), item["degree"])
        for n, item in enumerate(tier1, 1))
    hero_graph = json.dumps(graph_payload(catalog, pairs, config, hero_subset(catalog, config), with_desc=True),
                            ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    body = (
        '<section class="hero"><div class="hero-main">'
        '<div class="hero-canvas fade"><canvas aria-label="概念どうしのつながりを示す図。点を選ぶと記事を開けます"></canvas><div class="graph-tip"></div></div>'
        '<div class="shell hero-body"><div class="kicker mono fade">An atlas of invariant principles</div>'
        '<h1><span class="l"><span>AI が変えるもの。</span></span><span class="l"><span><em>変わらないもの。</em></span></span></h1>'
        '<p class="hero-lede fade">%(domains)d の学問分野、%(papers)s 本の論文から、知能が安くなった後にも残る構造を読み解く研究アトラス。'
        '記事は論文をもとに AI が書き、出典とともに順次追加されます。</p>'
        '<div class="hero-cta fade"><a class="btn solid" href="#clusters">領域から読む <span class="arr">↓</span></a>'
        '<a class="btn ghost" href="concepts/?t=1">不変原理から読む <span class="arr">→</span></a></div>'
        '<div class="fade hero-meta"><a class="hero-latest" href="concepts/%(latest_slug)s/"><span class="mono">新着</span><b>%(latest_title)s</b><span class="arr">→</span></a>'
        '<a class="hero-latest hero-resume" href="#" hidden><span class="mono">次の未読</span><b></b><span class="arr">→</span><small class="why"></small></a></div></div>'
        '<div class="hero-legend mono fade" aria-label="点の色は領域を表します">%(legend)s<a class="atlas-link" href="graph/">アトラスを開く →</a></div></div>'
        '<div class="shell"><div class="hero-stats fade">'
        '<div class="stat"><b>%(count)s</b><span class="mono">概念記事</span></div>'
        '<div class="stat"><b>%(papers)s</b><span class="mono">収録論文</span></div>'
        '<div class="stat"><b>%(domains)d</b><span class="mono">学問分野 · 6 領域に束ねる</span></div>'
        '<div class="stat"><b>%(edges)s</b><span class="mono">概念間の参照</span></div></div></div>'
        '<script type="application/json" id="hero-graph">%(graph)s</script></section>'

        '<section class="sec" id="clusters"><div class="shell"><header class="sec-head reveal"><span class="sec-no mono">01 — Fields</span>'
        '<h2>六つの領域</h2><p>%(domains)d の分野を、問いの近さで六つに束ねています。</p></header>'
        '<ul class="cl-list reveal">%(clusters)s</ul></div></section>'

        '<section class="sec" id="sorting"><div class="shell"><header class="sec-head reveal"><span class="sec-no mono">02 — Sorting</span>'
        '<h2>読む順番は、仕分けで決まります</h2><a class="more" href="guide/">読み方ガイド <span class="arr">→</span></a>'
        '<p>%(purpose)s</p></header>'
        '<ol class="tiers reveal">%(tiers)s</ol></div></section>'

        '<section class="sec"><div class="shell"><header class="sec-head reveal"><span class="sec-no mono">03 — Invariants</span>'
        '<h2>不変原理から読む</h2><a class="more" href="concepts/">すべての記事 <span class="arr">→</span></a>'
        '<p>%(inv_short)sと判断した原理のうち、他の概念から最も多く参照されているもの。</p></header>'
        '<div class="cards reveal">%(cards)s</div></div></section>'

        '<section class="sec"><div class="shell"><header class="sec-head reveal"><span class="sec-no mono">04 — Latest</span>'
        '<h2>最近の追加</h2><a class="more" href="concepts/">記事索引 <span class="arr">→</span></a>'
        '<p>直近に追加した記事から、ほかの概念とのつながりが多い順に。</p></header>'
        '<div class="reveal">%(latest)s</div></div></section>'

        '<section class="sec"><div class="shell"><header class="sec-head reveal"><span class="sec-no mono">05 — Method</span>'
        '<h2>つくりかた</h2><p>このサイトは、人が選び AI が読むという分担で運用しています。</p></header>'
        '<div class="method reveal">'
        '<div class="step"><span class="n mono">Step 01</span><h3>集める</h3><p>毎朝、%(domains)d 分野の検索式で学術データベースから論文を取得します。系統的レビュー、メタ分析、古典を優先します。</p></div>'
        '<div class="step"><span class="n mono">Step 02</span><h3>ふるいにかける</h3><p>抽象度・制約不変・メカニズムの 3 つの試験で分類します。すべて満たすものが不変原理、消えゆく制約に依るが構造的に価値があるものが設計原理です。<a class="inline" href="guide/">基準の詳細</a></p></div>'
        '<div class="step"><span class="n mono">Step 03</span><h3>書く</h3><p>残った論文から概念を抽出し、1 概念 1 記事で日本語にまとめます。記事どうしの参照は知識グラフとして保持します。取得は毎朝、公開はまとめて順次行います。</p></div></div>'
        '<div class="colophon reveal"><span class="mono">Note</span><p>記事は AI(大規模言語モデル)による自動生成で、人による査読を経ていません。各記事の末尾に出典を示しています。内容は必ず原典で確認してください。</p></div>'
        '</div></section>'
    ) % {
        "domains": domain_count, "papers": num(paper_count), "count": num(len(catalog)), "edges": num(len(pairs)),
        "graph": hero_graph, "clusters": "".join(rows), "cards": cards, "latest": rows_html(latest, root, config),
        "legend": "".join('<a data-c="%s" href="clusters/%s/"><i class="dot"></i>%s</a>' % (c["key"], c["key"], esc(short_label(c))) for c in config["clusters"]),
        "latest_slug": latest[0]["slug"], "latest_title": esc(latest[0]["title"]),
        "purpose": esc(TIER_PURPOSE), "tiers": home_tiers_html(catalog, root),
        "inv_short": esc((TIER_INFO.get(1) or {}).get("short", "")),
    }
    json_ld = {"@context": "https://schema.org", "@type": "WebSite", "name": site["short_title"], "url": site["url"] + "/",
               "description": site["description"], "inLanguage": "ja"}
    extra = '<script type="application/ld+json">%s</script>' % json.dumps(json_ld, ensure_ascii=False)
    page = layout(config, root, site["title"], site["description"], body, site["url"] + "/", extra_head=extra)
    write(os.path.join(out_dir, "index.html"), page)


def build_guide(catalog, config, out_dir):
    site = config["site"]
    root = "../"
    counts = tier_counts(catalog)
    notes = config.get("tier_notes") or {}
    panels = []
    note_head = {1: "拠り所とする、変わらない制約", 2: "AI で外れる制約の例", 3: "該当しやすい例"}
    for t in (1, 2, 3):
        info = TIER_INFO.get(t) or {}
        picks = sorted([i for i in catalog if i["tier"] == t], key=lambda i: -i.get("degree", 0))[:3]
        examples = "".join(
            '<li><a href="%sconcepts/%s/" data-slug="%s"><span class="t">%s</span><span class="d">%s</span></a></li>' % (
                root, i["slug"], i["slug"], esc(i["title"]), esc(i["description"])) for i in picks)
        note_items = "".join("<li>%s</li>" % esc(x) for x in notes.get(t, []))
        panels.append(
            '<article class="tier-panel" id="tier-%d" data-t="%d"><div class="tp-side"><header><span class="mk" aria-hidden="true">%s</span>'
            '<div><h3>%s</h3><p class="def">%s</p></div></header><p class="cnt mono"><b>%s</b> 本の記事</p>'
            '<a class="go" href="%sconcepts/?t=%d">%s %s %s 本を読む <i class="arr">→</i></a></div>'
            '<div class="tp-main"><dl><dt class="mono">判定の問い</dt><dd>%s</dd><dt class="mono">読み方</dt><dd>%s</dd></dl>'
            '%s<h4 class="mono">この分類の代表的な記事</h4><ul class="guide-ex">%s</ul></div></article>' % (
                t, t, tier_mark_html(t), esc(info.get("label", "")), esc(info.get("short", "")), num(counts.get(t, 0)),
                root, t, tier_mark_html(t), esc(info.get("label", "")), num(counts.get(t, 0)),
                esc(info.get("question", "")), esc(info.get("use", "")),
                ('<h4 class="mono">%s</h4><ul class="notes">%s</ul>' % (note_head[t], note_items)) if note_items else "",
                examples))
    steps = (
        ("領域を選ぶ", "ホームの「六つの領域」から、関心に近い問いの領域を選びます。", root + "#clusters", "領域を見る"),
        ("不変原理を 2〜3 本読む", "領域ページの「読む順番」の ① から。時代が変わっても残る考え方をつかみます。", root + "concepts/?t=1", "不変原理の一覧"),
        ("設計原理で実務に落とす", "記事の末尾「%s」から、参照でつながっている設計原理へ進みます。" % NEXT_LABEL["forward"], root + "concepts/?t=2", "設計原理の一覧"),
        ("出典で裏づける", "記事は AI が書いたものです。気になる主張は、記事末尾の出典から原典の論文で確かめてください。参考の記事は、必要なときに辞書のように引きます。", root + "guide/#limits", "分類と記事の限界"),
    )
    steps_html = "".join(
        '<li><span class="n mono">%s</span><h3>%s</h3><p>%s</p><a class="more" href="%s">%s <span class="arr">→</span></a></li>' % (
            "①②③④"[n - 1], esc(h), esc(p_), esc(href), esc(label)) for n, (h, p_, href, label) in enumerate(steps, 1))
    parts = (
        ("記事の冒頭", "1 文の要約と「実務への含意」だけで、読むかどうかを判断できます。分類は、冒頭の領域名の横にあります。"),
        ("近傍グラフ", "右上の図は、その概念とつながる記事の近さを示します。点に触れると名前、押すとその記事へ移ります。"),
        ("目次", "長い記事では、左の目次が現在地を示します。小見出しも辿れます。"),
        ("出典", "末尾の書誌から原典へ移れます。記事は AI が書いたものなので、内容は必ず原典で確かめてください。"),
        ("次の一歩", "末尾に「%s」「%s」「%s(不変原理の記事では「%s」)」「%s」を並べています。参照の向きから機械的に作った道筋です。" % (
            NEXT_LABEL["base"], NEXT_LABEL["apply"], NEXT_LABEL["forward"], NEXT_LABEL["back"], NEXT_LABEL["cross"])),
        ("検索と既読", "どのページからでも ⌘K か「/」で検索できます。読んだ記事には「既読」が付きます。この情報はお使いのブラウザの中にだけ保存し、外部には送りません。"),
    )
    parts_html = "".join("<li><b>%s</b><span>%s</span></li>" % (esc(h), esc(t)) for h, t in parts)
    total = sum(counts.values())
    body = (
        '<header class="page-head"><div class="shell">%(crumbs)s<div><h1>読み方ガイド</h1>'
        '<p class="lede">%(purpose)s このページでは、仕分けの基準と、おすすめの読み進め方を説明します。</p></div>'
        '<div class="big-no" aria-hidden="true" style="color:var(--ink)">3<small>TIERS · %(total)s CONCEPTS</small></div></div></header>'
        '<div class="shell guide">'
        '<section class="sec g-sec" id="purpose"><header class="sec-head"><span class="sec-no mono">01 — Purpose</span><h2>仕分けの目的</h2></header>'
        '<div class="g-two"><div><h3>読む順番を決める</h3><p>%(total)s 本の記事を、前から順に読む必要はありません。'
        '時代が変わっても残る不変原理から読み、実務に落とす段階で設計原理を読みます。参考は順番に入れず、必要なときに引きます。これが基本の順番です。</p></div>'
        '<div><h3>記事化の優先度を決める</h3><p>新しい論文は、不変原理と設計原理に当たるものだけを記事にします。'
        '参考に分類された論文は、新たには記事にしません。すでにある参考の記事は残しています。</p></div></div></section>'
        '<section class="sec g-sec" id="tiers"><header class="sec-head"><span class="sec-no mono">02 — Tiers</span><h2>三つの分類</h2>'
        '<p>三つの試験(抽象度・制約の不変性・メカニズム)で論文を判定し、すべて満たすものを不変原理としています。</p></header>'
        '<div class="tier-panels">%(panels)s</div></section>'
        '<section class="sec g-sec" id="order"><header class="sec-head"><span class="sec-no mono">03 — Order</span><h2>おすすめの読み進め方</h2></header>'
        '<ol class="g-steps">%(steps)s</ol></section>'
        '<section class="sec g-sec" id="anatomy"><header class="sec-head"><span class="sec-no mono">04 — Anatomy</span><h2>記事の使い方</h2></header>'
        '<ul class="g-parts">%(parts)s</ul></section>'
        '<section class="sec g-sec" id="limits"><header class="sec-head"><span class="sec-no mono">05 — Limits</span><h2>分類の限界</h2></header>'
        '<ul class="g-limits">'
        '<li>判定は論文ごとに AI(大規模言語モデル)が行っています。人による査読は入っていません。</li>'
        '<li>ほとんどの記事の分類は、出典にした論文の判定のうち、最も不変な側を引き継いでいます。記事そのものを個別に判定した結果ではありません。</li>'
        '<li>不変原理は %(t1)s 本で、全記事の約 %(pct)d%% を占めます。分類だけでは優先度の差が小さいため、各一覧の中は「他の記事から参照される数」の多い順に並べています。</li>'
        '<li>記事末尾の「%(nb)s」「%(na)s」は、記事どうしの参照の向きから機械的に作っています。内容の上で先に読むべき前提かどうかは、保証していません。</li>'
        '<li>基準は設定ファイルで定義しており、今後見直すことがあります。誤りや疑問は <a href="%(repo)s/issues" rel="noopener">GitHub の Issue</a> でお知らせください。</li>'
        '</ul></section></div><div style="height:clamp(60px,9vw,130px)"></div>'
    ) % {"crumbs": crumbs_html([(site["short_title"], root), ("読み方ガイド", None)]), "purpose": esc(TIER_PURPOSE),
         "total": num(total), "panels": "".join(panels), "steps": steps_html, "parts": parts_html, "repo": esc(site["repo_url"]),
         "t1": num(counts.get(1, 0)), "pct": int(round(100.0 * counts.get(1, 0) / max(1, total))),
         "nb": NEXT_LABEL["base"], "na": NEXT_LABEL["apply"]}
    page = layout(config, root, "読み方ガイド | %s" % site["short_title"],
                  "%s 三つの分類(不変原理・設計原理・参考)の基準と、おすすめの読み進め方。" % TIER_PURPOSE, body,
                  site["url"] + "/guide/", current="guide")
    write(os.path.join(out_dir, "guide", "index.html"), page)


def build_atlas(catalog, config, out_dir, pairs):
    site = config["site"]
    root = "../"
    legend = "".join(
        '<button type="button" data-c="%s" aria-pressed="true"><i class="dot"></i>%s <small>%s</small></button>' % (
            c["key"], esc(c["label"]), num(sum(1 for i in catalog if i["cluster"] == c["key"])))
        for c in config["clusters"])
    counts = tier_counts(catalog)
    tier_legend = '<span class="legend-sep mono">分類で絞る</span>' + "".join(
        '<button type="button" data-t="%d" aria-pressed="true"><span class="mk">%s</span>%s <small>%s</small></button>' % (
            t, tier_mark_html(t), esc(TIER_LABEL[t]), num(counts.get(t, 0))) for t in (1, 2, 3))
    body = (
        '<div class="atlas"><canvas aria-label="知識グラフ。点は概念、線は記事どうしの参照"></canvas>'
        '<div class="atlas-panel"><div class="kicker mono">Atlas</div><h1>概念の地図</h1>'
        '<p>%s の概念と、記事どうしの参照 %s 本。点を選ぶと概要が開きます。領域名を押すと表示を切り替えられます。</p>'
        '<div class="legend" role="group" aria-label="表示の切り替え">%s</div>'
        '<p class="atlas-shown mono" aria-live="polite"></p>'
        '<div class="atlas-help mono"><span class="for-mouse">ドラッグで移動 · ホイールで拡大</span><span class="for-touch">ドラッグで移動 · ピンチで拡大</span></div></div>'
        '<div class="atlas-zoom"><button type="button" data-zoom="in" aria-label="拡大">+</button>'
        '<button type="button" data-zoom="out" aria-label="縮小">−</button>'
        '<button type="button" data-zoom="fit" aria-label="全体を表示">◎</button></div>'
        '<div class="atlas-card" aria-live="polite"></div>'
        '<noscript><p style="padding:120px 24px">地図の表示には JavaScript が必要です。<a href="../concepts/">記事索引</a>をご覧ください。</p></noscript></div>'
    ) % (num(len(catalog)), num(len(pairs)), legend + tier_legend)
    page = layout(config, root, "アトラス(知識グラフ) | %s" % site["short_title"],
                  "%s の概念と %s 本の参照関係を地図として探索できます。" % (num(len(catalog)), num(len(pairs))),
                  body, site["url"] + "/graph/", current="graph", footer=False)
    write(os.path.join(out_dir, "graph", "index.html"), page)
    write(os.path.join(out_dir, "graph.json"),
          json.dumps(graph_payload(catalog, pairs, config), ensure_ascii=False, separators=(",", ":")))


def build_search_index(catalog, config, out_dir):
    keys = [c["key"] for c in config["clusters"]]
    items = sorted(catalog, key=lambda i: (i["published"], i["degree"]), reverse=True)
    payload = {
        "tiers": {str(t): "%s %s" % (tier_mark(t), TIER_LABEL[t]) for t in (1, 2, 3)},
        "clusters": [[c["key"], short_label(c)] for c in config["clusters"]],
        "items": [[i["slug"], i["title"], i["title_en"], truncate(i["description"], 140), keys.index(i["cluster"]), i["tier"], i.get("degree", 0)] for i in items],
    }
    write(os.path.join(out_dir, "search.json"), json.dumps(payload, ensure_ascii=False, separators=(",", ":")))


def build_404(config, out_dir):
    site = config["site"]
    base_path = "/" + site["url"].split("/", 3)[3].strip("/") + "/" if site["url"].count("/") > 2 else "/"
    body = (
        '<header class="page-head" style="border-bottom:0"><div class="shell"><div class="crumbs mono"><span>Error 404</span></div>'
        '<h1>この頁は、<br>まだ書かれていません。</h1><p class="lede">URL が変わったか、記事が統合された可能性があります。</p>'
        '<div class="hero-cta"><a class="btn solid" href="%sconcepts/?t=1">不変原理から読む <span class="arr">→</span></a>'
        '<a class="btn ghost" href="%sconcepts/">記事索引へ</a>'
        '<button class="btn ghost" type="button" data-search>検索する</button></div></div></header>'
        '<div style="height:18vh"></div>'
    ) % (base_path, base_path)
    page = layout(config, base_path, "ページが見つかりません | %s" % site["short_title"], site["description"], body, site["url"] + "/404.html")
    write(os.path.join(out_dir, "404.html"), page)


def build_feeds(catalog, config, out_dir):
    site = config["site"]
    base = site["url"]
    now = dt.datetime.now(dt.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    # sitemap
    urls = [("%s/" % base, "daily", "1.0"), ("%s/concepts/" % base, "daily", "0.6"), ("%s/graph/" % base, "weekly", "0.4"),
            ("%s/guide/" % base, "monthly", "0.7")]
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
    write(os.path.join(out_dir, ".nojekyll"), "")
    assets_src = os.path.join(BASE, "config", "site_assets")
    os.makedirs(os.path.join(out_dir, "assets"), exist_ok=True)
    if os.path.isdir(assets_src):
        for name in sorted(os.listdir(assets_src)):
            shutil.copyfile(os.path.join(assets_src, name), os.path.join(out_dir, "assets", name))
    indexnow_key = (config.get("search") or {}).get("indexnow_key") or ""
    if indexnow_key:
        write(os.path.join(out_dir, indexnow_key + ".txt"), indexnow_key)
    pairs, _neighbors = build_graph_data(catalog, backlinks, config)
    config["_domain_count"] = len({d for i in catalog for d in i["domains"]})
    paper_count = 0
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, encoding="utf-8") as handle:
            paper_count = sum(1 for line in handle if line.strip())
    index = {item["slug"]: i for i, item in enumerate(catalog)}
    for item in catalog:
        build_article(item, config, renderer, backlinks, by_slug, out_dir, catalog, pairs, _neighbors, index)
    build_cluster_pages(catalog, config, out_dir, pairs)
    build_domain_pages(catalog, config, out_dir)
    build_all_index(catalog, config, out_dir)
    build_guide(catalog, config, out_dir)
    build_home(catalog, config, out_dir, pairs, paper_count)
    build_atlas(catalog, config, out_dir, pairs)
    build_search_index(catalog, config, out_dir)
    build_404(config, out_dir)
    build_feeds(catalog, config, out_dir)

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
