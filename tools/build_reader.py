#!/usr/bin/env python3
"""Generate a static HTML reader from wiki articles and graph metadata."""

from collections import Counter
import json
import os

from lib.workspace_ui import render_workspace_sidebar

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_CONCEPTS = os.path.join(BASE, "wiki", "concepts")
META_FILE = os.path.join(BASE, "wiki", "_meta", "concepts.json")
GRAPH_FILE = os.path.join(BASE, "wiki", "_meta", "concepts-graph.json")
BACKLINKS_FILE = os.path.join(BASE, "wiki", "_meta", "backlinks.json")
OUT = os.path.join(BASE, "wiki", "reader.html")


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def collect_meta():
    raw_meta = load_json(META_FILE, [])
    meta_by_slug = {item["slug"]: item for item in raw_meta if item.get("slug")}

    meta = []
    for filename in sorted(os.listdir(WIKI_CONCEPTS)):
        if not filename.endswith(".md"):
            continue
        slug = filename[:-3]
        path = os.path.join(WIKI_CONCEPTS, filename)
        title = slug
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                if line.startswith("# "):
                    title = line[2:].strip()
                    break

        item = meta_by_slug.get(slug, {})
        meta.append(
            {
                "slug": slug,
                "title": item.get("title_ja", title),
                "tier": item.get("tier", 2),
            }
        )
    return meta


def collect_articles(meta):
    articles = {}
    for item in meta:
        path = os.path.join(WIKI_CONCEPTS, item["slug"] + ".md")
        if os.path.exists(path):
            with open(path, encoding="utf-8") as handle:
                articles[item["slug"]] = handle.read()
    return articles


def render_reader_html(meta, articles, graph, backlinks):
    article_json = json.dumps(articles, ensure_ascii=False).replace("</", "<\\/")
    meta_json = json.dumps(meta, ensure_ascii=False)
    graph_json = json.dumps(graph, ensure_ascii=False).replace("</", "<\\/")
    backlinks_json = json.dumps(backlinks, ensure_ascii=False).replace("</", "<\\/")

    summary = (graph or {}).get("summary", {})
    tier_counts = Counter(item.get("tier", 2) for item in meta)
    article_count = len(meta)
    resolved_edges = summary.get("resolved_edges", summary.get("edges", 0))
    unresolved_refs = summary.get("unresolved_nodes", 0)
    link_mentions = summary.get("link_mentions", 0)
    summary_text = (
        f"{article_count} articles / "
        f"{resolved_edges} resolved edges / "
        f"{unresolved_refs} unresolved refs"
        if summary
        else f"17分野 × {article_count}コンセプト"
    )
    sidebar_html = render_workspace_sidebar(
        active_view="reader",
        summary_text=summary_text,
        links={
            "atlas": "graph/index.html",
            "reader": "reader.html",
            "index": "index.html",
        },
    )
    template = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Article Reader</title>
<style>
:root{
  --page-gap:20px;
  --rail-width:264px;
  --paper:#060913;
  --paper-strong:#0c1220;
  --ink:#edf3ff;
  --ink-soft:#9baecc;
  --line:rgba(151,170,204,.16);
  --line-strong:rgba(214,227,255,.16);
  --accent-rust:#d9a07d;
  --accent-teal:#79d2c5;
  --accent-blue:#82aef5;
  --accent-amber:#f1bb74;
  --accent-slate:#92a4bf;
  --card:rgba(9,15,28,.74);
  --card-strong:rgba(13,20,36,.86);
  --shadow:0 24px 72px rgba(2,6,23,.45);
}
*{box-sizing:border-box}
html,body{height:100%}
body{
  margin:0;
  min-height:100%;
  color:var(--ink);
  font-family:"Avenir Next","Segoe UI",sans-serif;
  background:
    radial-gradient(circle at top left, rgba(121,210,197,.11), transparent 26%),
    radial-gradient(circle at top right, rgba(217,160,125,.12), transparent 22%),
    radial-gradient(circle at bottom, rgba(130,174,245,.11), transparent 30%),
    linear-gradient(180deg, rgba(17,25,42,.92), rgba(7,10,19,.98)),
    var(--paper);
}
body::before{
  content:"";
  position:fixed;
  inset:0;
  pointer-events:none;
  opacity:.42;
  background-image:
    linear-gradient(rgba(151,170,204,.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(151,170,204,.04) 1px, transparent 1px);
  background-size:32px 32px;
}
.app-shell{
  position:relative;
  z-index:1;
  display:grid;
  grid-template-columns:minmax(0,var(--rail-width)) minmax(0,1fr);
  gap:var(--page-gap);
  align-items:start;
  min-height:100%;
  padding:var(--page-gap);
}
.page-rail{
  position:sticky;
  top:var(--page-gap);
  align-self:start;
  min-width:0;
  z-index:40;
}
.page-rail-card{
  min-height:calc(100vh - (var(--page-gap) * 2));
  background:linear-gradient(180deg, rgba(11,17,31,.96), rgba(8,13,24,.88));
  border:1px solid var(--line-strong);
  backdrop-filter:blur(18px);
  box-shadow:var(--shadow);
  border-radius:28px;
  padding:18px 16px;
  display:flex;
  flex-direction:column;
  gap:14px;
}
.page-rail-head{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:12px;
  padding:4px 2px 2px;
}
.page-rail-eyebrow{
  color:var(--ink-soft);
  font-size:11px;
  font-weight:600;
  letter-spacing:.16em;
  text-transform:uppercase;
}
.page-rail-badge{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  min-width:56px;
  padding:7px 10px;
  border-radius:999px;
  background:rgba(20,31,52,.78);
  border:1px solid var(--line);
  color:var(--ink-soft);
  font-size:11px;
}
.page-nav{
  display:flex;
  flex-direction:column;
  gap:8px;
}
.page-link{
  display:grid;
  grid-template-columns:44px minmax(0,1fr);
  align-items:center;
  gap:12px;
  min-height:68px;
  padding:12px;
  border-radius:20px;
  text-decoration:none;
  color:var(--ink-soft);
  border:1px solid rgba(151,170,204,.12);
  background:rgba(14,22,40,.62);
  transition:background .18s ease, color .18s ease, transform .18s ease, border-color .18s ease, box-shadow .18s ease;
}
.page-link:hover{
  background:rgba(19,29,50,.92);
  color:var(--ink);
  border-color:rgba(151,170,204,.24);
  transform:translateY(-1px);
  box-shadow:0 12px 34px rgba(2,6,23,.28);
}
.page-link.active{
  color:var(--ink);
  border-color:rgba(121,210,197,.22);
  background:linear-gradient(135deg, rgba(121,210,197,.16), rgba(130,174,245,.16));
  box-shadow:0 14px 32px rgba(6,10,22,.36);
}
.page-icon{
  width:44px;
  height:44px;
  border-radius:14px;
  display:flex;
  align-items:center;
  justify-content:center;
  background:rgba(26,37,59,.82);
  border:1px solid rgba(151,170,204,.12);
  color:var(--ink);
}
.page-icon svg{
  width:18px;
  height:18px;
}
.page-copy{
  display:flex;
  flex-direction:column;
  align-items:flex-start;
  min-width:0;
}
.page-link strong{
  font-size:13px;
  letter-spacing:.08em;
  text-transform:uppercase;
}
.page-copy span{
  margin-top:4px;
  font-size:12px;
  line-height:1.45;
}
.page-meta{
  margin-top:auto;
  padding:14px;
  border-radius:22px;
  background:rgba(16,25,43,.78);
  border:1px solid var(--line);
}
.page-meta strong{
  display:block;
  font-size:16px;
  letter-spacing:-.03em;
}
.page-meta span{
  display:block;
  margin-top:6px;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.shell{
  position:relative;
  min-height:100%;
  min-width:0;
  padding:0 0 24px;
}
.hero{
  display:grid;
  grid-template-columns:minmax(0,1fr);
  gap:12px;
  margin-bottom:14px;
}
.panel,.stage-shell{
  min-width:0;
  background:var(--card);
  border:1px solid var(--line-strong);
  backdrop-filter:blur(10px);
  box-shadow:var(--shadow);
  border-radius:26px;
}
.hero-card{
  min-width:0;
  padding:2px 2px 0;
  background:transparent;
  border:0;
  box-shadow:none;
}
.eyebrow{
  display:inline-block;
  padding:0;
  color:var(--ink-soft);
  font-size:11px;
  font-weight:600;
  letter-spacing:.12em;
  text-transform:uppercase;
}
.hero h1{
  margin:10px 0 6px;
  font-family:"Avenir Next","Segoe UI",sans-serif;
  font-size:clamp(22px,2.3vw,30px);
  line-height:1.15;
  letter-spacing:-.03em;
}
.hero p{
  margin:0;
  max-width:72ch;
  color:var(--ink-soft);
  font-size:13px;
  line-height:1.65;
}
.metric-grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:10px;
}
.metric{
  padding:12px 0 0;
  background:transparent;
  border-top:1px solid rgba(151,170,204,.12);
}
.metric .value{
  font-size:24px;
  font-weight:700;
  letter-spacing:-.04em;
}
.metric .label{
  margin-top:4px;
  font-size:11px;
  letter-spacing:.12em;
  text-transform:uppercase;
  color:var(--ink-soft);
}
.metric .note{
  margin-top:4px;
  color:var(--ink-soft);
  font-size:11px;
  line-height:1.45;
}
.layout{
  display:grid;
  grid-template-columns:minmax(320px,372px) minmax(0,1fr);
  gap:20px;
  align-items:start;
}
.analysis-column{
  min-width:0;
  display:grid;
  grid-template-columns:minmax(0,1fr);
  gap:18px;
}
.panel{
  padding:18px;
  position:sticky;
  top:24px;
  display:flex;
  flex-direction:column;
  gap:0;
  max-height:calc(100vh - 48px);
  overflow:auto;
  scrollbar-width:thin;
  scrollbar-color:rgba(151,170,204,.18) transparent;
}
.panel::-webkit-scrollbar{
  width:10px;
}
.panel::-webkit-scrollbar-thumb{
  background:rgba(151,170,204,.16);
  border-radius:999px;
  border:2px solid transparent;
  background-clip:padding-box;
}
.panel::-webkit-scrollbar-track{
  background:transparent;
}
.reader-queue-panel{
  padding:22px;
  background:linear-gradient(180deg, rgba(11,17,31,.94), rgba(9,14,26,.86));
  border-color:rgba(214,227,255,.12);
  box-shadow:0 18px 56px rgba(2,6,23,.34);
}
.panel h2,.panel h3{
  margin:0 0 12px;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  letter-spacing:-.02em;
}
.panel-kicker{
  display:inline-flex;
  align-items:center;
  gap:8px;
  margin-bottom:10px;
  color:var(--ink-soft);
  font-size:11px;
  font-weight:600;
  letter-spacing:.16em;
  text-transform:uppercase;
}
.panel-copy{
  margin:0;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.6;
}
.section{
  padding-top:16px;
  margin-top:16px;
  border-top:1px solid var(--line);
}
.section:first-of-type{
  padding-top:0;
  margin-top:0;
  border-top:0;
}
.queue-controls{
  display:flex;
  flex-direction:column;
  gap:14px;
}
.queue-control-card{
  min-width:0;
  padding:0;
  border:0;
  border-radius:0;
  background:transparent;
}
.queue-control-card + .queue-control-card{
  padding-top:14px;
  border-top:1px solid rgba(151,170,204,.12);
}
.queue-status-card{
  display:flex;
  flex-direction:column;
  justify-content:flex-start;
  gap:8px;
}
.queue-status-label{
  color:var(--ink-soft);
  font-size:11px;
  font-weight:600;
  letter-spacing:.14em;
  text-transform:uppercase;
}
.label{
  display:block;
  margin-bottom:8px;
  font-size:11px;
  letter-spacing:.12em;
  text-transform:uppercase;
  color:var(--ink-soft);
}
.input,.select{
  width:100%;
  border:1px solid rgba(151,170,204,.16);
  background:rgba(15,24,41,.9);
  border-radius:14px;
  padding:12px 14px;
  color:var(--ink);
  font-size:14px;
}
.input::placeholder{
  color:rgba(155,174,204,.72);
}
.chips{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
}
.chip{
  border:1px solid rgba(151,170,204,.16);
  background:rgba(18,29,48,.82);
  color:var(--ink-soft);
  padding:9px 12px;
  border-radius:999px;
  cursor:pointer;
  font-size:12px;
  line-height:1;
}
.chip.active{
  color:var(--ink);
  border-color:transparent;
  background:rgba(121,210,197,.16);
}
.chip.active[data-kind="tier1"]{background:rgba(217,160,125,.18)}
.chip.active[data-kind="tier2"]{background:rgba(121,210,197,.18)}
.chip.active[data-kind="tier3"]{background:rgba(130,174,245,.18)}
.small{
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.list{
  display:flex;
  flex-direction:column;
  gap:8px;
}
.list button,.link-btn,.ghost-btn,.ghost-link{
  width:100%;
  text-align:left;
  border:1px solid rgba(151,170,204,.12);
  background:rgba(16,25,42,.78);
  border-radius:16px;
  padding:12px 14px;
  color:var(--ink);
  cursor:pointer;
}
.list button:hover,.link-btn:hover,.ghost-btn:hover,.ghost-link:hover{
  background:rgba(21,33,56,.92);
}
.list button strong,.link-btn strong{
  display:block;
  font-size:13px;
  line-height:1.4;
}
.list button span,.link-btn span{
  display:block;
  margin-top:6px;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.ghost-link{
  display:inline-flex;
  width:100%;
  align-items:center;
  justify-content:center;
  text-decoration:none;
}
.ghost-link.primary{
  background:linear-gradient(135deg, rgba(121,210,197,.18), rgba(130,174,245,.16));
  color:var(--ink);
  border-color:rgba(121,210,197,.18);
}
.queue-status{
  color:var(--ink-soft);
  font-size:13px;
  line-height:1.6;
}
.queue-list{
  margin-top:12px;
}
.queue-card{
  border:1px solid rgba(151,170,204,.12);
  background:rgba(15,24,41,.82);
  border-radius:18px;
  padding:14px;
  cursor:pointer;
  transition:transform .18s ease, border-color .18s ease, box-shadow .18s ease, background .18s ease;
}
.queue-card:hover{
  transform:translateY(-1px);
  border-color:rgba(151,170,204,.24);
  box-shadow:0 14px 28px rgba(2,6,23,.26);
  background:rgba(20,31,52,.92);
}
.queue-card.active{
  border-color:rgba(121,210,197,.2);
  background:linear-gradient(135deg, rgba(121,210,197,.18), rgba(130,174,245,.12));
}
.queue-card strong{
  display:block;
  font-size:14px;
  line-height:1.45;
  overflow-wrap:anywhere;
}
.queue-card p{
  margin:8px 0 0;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.queue-meta{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  margin-top:10px;
}
.queue-meta span,.tier-badge{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  padding:6px 8px;
  border-radius:999px;
  background:rgba(18,29,48,.78);
  border:1px solid rgba(151,170,204,.12);
  color:var(--ink-soft);
  font-size:11px;
}
.tier-badge.tier-1{background:rgba(217,160,125,.18); color:var(--ink)}
.tier-badge.tier-2{background:rgba(121,210,197,.18); color:var(--ink)}
.tier-badge.tier-3{background:rgba(130,174,245,.18); color:var(--ink)}
.stage-shell{
  position:relative;
  min-width:0;
  overflow:hidden;
  container-type:inline-size;
  padding:18px;
  background:
    radial-gradient(circle at 16% 12%, rgba(130,174,245,.16), transparent 24%),
    radial-gradient(circle at 84% 18%, rgba(217,160,125,.12), transparent 28%),
    linear-gradient(180deg, rgba(13,20,36,.96), rgba(10,16,28,.92));
  border:1px solid rgba(214,227,255,.12);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.06),
    0 24px 70px rgba(2,6,23,.48);
}
.stage-shell::before{
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  background:
    linear-gradient(180deg, rgba(255,255,255,.04), transparent 18%),
    linear-gradient(90deg, rgba(151,170,204,.035) 1px, transparent 1px),
    linear-gradient(rgba(151,170,204,.028) 1px, transparent 1px);
  background-size:auto, 32px 32px, 32px 32px;
  mask-image:linear-gradient(180deg, rgba(0,0,0,.7), transparent 80%);
}
.stage-header{
  position:relative;
  z-index:2;
  display:flex;
  flex-direction:column;
  gap:14px;
  padding:2px 2px 14px;
}
.stage-kicker{
  color:var(--ink-soft);
  font-size:11px;
  font-weight:600;
  letter-spacing:.18em;
  text-transform:uppercase;
}
.stage-header-top{
  display:grid;
  grid-template-columns:minmax(0,1fr) auto;
  align-items:start;
  gap:18px;
}
.stage-title h2{
  margin:0;
  font-family:"Avenir Next","Segoe UI",sans-serif;
  color:var(--ink);
  font-size:28px;
  font-weight:650;
  letter-spacing:-.04em;
}
.stage-title p{
  margin:8px 0 0;
  max-width:66ch;
  color:var(--ink-soft);
  font-size:13px;
  line-height:1.7;
}
.stage-toolbar{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  max-width:min(100%,320px);
  justify-content:flex-end;
  justify-self:end;
}
.stage-chip{
  display:inline-flex;
  align-items:center;
  gap:8px;
  padding:8px 12px;
  border-radius:999px;
  border:1px solid rgba(151,170,204,.16);
  background:rgba(18,29,48,.72);
  color:var(--ink-soft);
  font-size:12px;
  line-height:1;
  max-width:100%;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
}
.stage-chip.primary{
  color:var(--ink);
  background:linear-gradient(135deg, rgba(130,174,245,.18), rgba(121,210,197,.14));
  border-color:rgba(130,174,245,.24);
}
.stage-chip.link{
  text-decoration:none;
}
.stage-meta-row{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:12px;
}
.stage-meta-card{
  padding:12px 2px 0;
  border-radius:0;
  border:0;
  border-top:1px solid rgba(151,170,204,.12);
  background:transparent;
}
.stage-meta-card strong{
  display:block;
  color:var(--ink);
  font-size:13px;
  font-weight:600;
}
.stage-meta-card span{
  display:block;
  margin-top:6px;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.reader-stage{
  position:relative;
  min-width:0;
  display:grid;
  grid-template-columns:minmax(0,1fr);
  gap:14px;
}
.stage-chrome{
  position:relative;
  z-index:3;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:12px;
  padding:10px 4px 14px;
  border-radius:0;
  background:transparent;
  border:0;
  border-bottom:1px solid rgba(151,170,204,.12);
}
.stage-chrome-left,.stage-chrome-right{
  display:flex;
  align-items:center;
  gap:10px;
  min-width:0;
  flex-wrap:wrap;
}
.stage-window-dots{
  display:none;
}
.stage-mode-label{
  color:var(--ink);
  font-size:12px;
  font-weight:600;
  letter-spacing:.08em;
  text-transform:uppercase;
}
.stage-chrome-note{
  color:var(--ink-soft);
  font-size:12px;
  min-width:0;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
}
.article-body-card{
  position:relative;
  min-width:0;
  display:grid;
  grid-template-columns:minmax(0,1fr);
  border-radius:18px;
  border:0;
  background:linear-gradient(180deg, rgba(10,16,29,.94), rgba(8,13,23,.98));
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.06);
  overflow:hidden;
}
.article-metric-strip{
  display:grid;
  grid-template-columns:repeat(4,minmax(0,1fr));
  gap:1px;
  background:rgba(151,170,204,.08);
}
.article-metric{
  padding:14px 16px;
  background:rgba(15,24,41,.84);
}
.article-metric .value{
  font-size:22px;
  font-weight:700;
  letter-spacing:-.04em;
}
.article-metric .label{
  margin-top:4px;
  color:var(--ink-soft);
  font-size:11px;
  letter-spacing:.12em;
  text-transform:uppercase;
}
.article-body{
  width:min(100%,94ch);
  margin:0 auto;
  padding:34px clamp(34px,4vw,52px) 42px;
  max-width:none;
}
.article-body h2{
  margin:28px 0 12px;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  font-size:28px;
  line-height:1.18;
  letter-spacing:-.03em;
}
.article-body h3{
  margin:22px 0 10px;
  font-size:18px;
  line-height:1.3;
}
.article-body p,
.article-body li,
.article-body blockquote{
  color:var(--ink);
  font-size:15px;
  line-height:1.88;
}
.article-body p{
  margin:0 0 14px;
}
.article-body ul,
.article-body ol{
  margin:0 0 16px;
  padding-left:22px;
}
.article-body li{
  margin-bottom:8px;
}
.article-body hr{
  margin:24px 0;
  border:0;
  border-top:1px solid rgba(151,170,204,.14);
}
.article-body blockquote{
  margin:0 0 16px;
  padding:12px 16px;
  border-left:3px solid rgba(121,210,197,.34);
  background:rgba(16,25,42,.72);
  border-radius:0 14px 14px 0;
}
.article-body code{
  padding:2px 6px;
  border-radius:6px;
  background:rgba(151,170,204,.12);
  color:var(--ink);
  font-size:13px;
}
.article-body table{
  width:100%;
  border-collapse:collapse;
  margin:0 0 20px;
  display:block;
  overflow-x:auto;
}
.article-body thead{
  background:rgba(151,170,204,.08);
}
.article-body th,
.article-body td{
  padding:10px 12px;
  border:1px solid rgba(151,170,204,.12);
  text-align:left;
  font-size:13px;
  line-height:1.55;
  vertical-align:top;
  min-width:140px;
}
.stage-briefs{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:12px;
}
.stage-brief-card{
  display:flex;
  flex-direction:column;
  justify-content:flex-start;
  min-height:108px;
  padding:14px 0 0;
  border-radius:0;
  background:transparent;
  border:0;
  border-top:1px solid rgba(151,170,204,.12);
  backdrop-filter:none;
}
.stage-brief-card.primary{
  border-top-color:rgba(130,174,245,.28);
}
.stage-brief-label{
  color:var(--ink-soft);
  font-size:11px;
  font-weight:600;
  letter-spacing:.14em;
  text-transform:uppercase;
}
.stage-brief-card strong{
  display:block;
  margin-top:8px;
  font-size:13px;
  color:var(--ink);
}
.stage-brief-card span{
  display:block;
  margin-top:6px;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.inspector-panel{
  min-width:0;
  position:relative;
  display:flex;
  flex-direction:column;
  gap:0;
  padding:20px;
  top:auto;
  max-height:none;
  overflow:visible;
  background:linear-gradient(180deg, rgba(11,17,31,.92), rgba(9,14,26,.86));
  border-color:rgba(214,227,255,.12);
  box-shadow:0 20px 52px rgba(2,6,23,.28);
}
.inspector-head{
  display:flex;
  align-items:flex-start;
  justify-content:space-between;
  gap:12px;
}
.inspector-head-copy{
  min-width:0;
}
.inspector-head .ghost-link{
  width:auto;
  min-width:168px;
}
.inspector-panel h2{
  margin:0;
  font-size:30px;
}
.inspector-description{
  margin:12px 0 0;
  color:var(--ink-soft);
  font-size:14px;
  line-height:1.72;
}
.inspector-lead{
  margin-top:14px;
  padding:12px 0 0;
  border-radius:0;
  background:transparent;
  border:0;
  border-top:1px solid rgba(151,170,204,.12);
  color:var(--ink);
  font-size:13px;
  line-height:1.65;
}
.pill-row{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  margin-top:14px;
}
.pill{
  display:inline-flex;
  align-items:center;
  gap:6px;
  padding:8px 10px;
  border-radius:999px;
  background:rgba(18,29,48,.78);
  border:1px solid rgba(151,170,204,.12);
  color:var(--ink-soft);
  font-size:12px;
  overflow-wrap:anywhere;
}
.metric-strip{
  display:grid;
  grid-template-columns:repeat(4,minmax(0,1fr));
  gap:10px;
  margin-top:16px;
}
.mini{
  padding:12px 14px;
  border-radius:18px;
  background:rgba(16,25,42,.78);
  border:1px solid rgba(151,170,204,.12);
}
.mini .v{
  font-size:24px;
  font-weight:700;
  letter-spacing:-.04em;
}
.mini .k{
  margin-top:4px;
  color:var(--ink-soft);
  font-size:11px;
  letter-spacing:.12em;
  text-transform:uppercase;
}
.companion-grid{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:20px;
}
.companion-card{
  min-width:0;
  padding:14px 0 0;
  border-radius:0;
  background:transparent;
  border:0;
  border-top:1px solid rgba(151,170,204,.12);
}
.companion-card-head{
  display:flex;
  flex-direction:column;
  gap:6px;
  margin-bottom:12px;
}
.companion-card-head span{
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.companion-actions{
  margin-top:18px;
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:10px;
}
.text-list{
  display:flex;
  flex-direction:column;
  gap:10px;
}
.text-item{
  padding:12px 14px;
  border-radius:18px;
  background:rgba(17,26,45,.82);
  border:1px solid rgba(151,170,204,.12);
}
.text-item strong{
  display:block;
  font-size:13px;
  overflow-wrap:anywhere;
}
.text-item span,.text-item small{
  display:block;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
  overflow-wrap:anywhere;
}
.wikilink{
  display:inline-flex;
  align-items:center;
  gap:6px;
  border-radius:999px;
  padding:5px 10px;
  border:1px solid rgba(130,174,245,.28);
  background:rgba(130,174,245,.12);
  color:var(--ink);
  font-size:12px;
  cursor:pointer;
  text-decoration:none;
  vertical-align:middle;
}
.wikilink.unresolved{
  border-color:rgba(241,187,116,.28);
  background:rgba(241,187,116,.12);
  color:var(--ink-soft);
}
.empty{
  padding:14px;
  border-radius:18px;
  background:rgba(16,25,42,.74);
  border:1px dashed rgba(151,170,204,.18);
  color:var(--ink-soft);
  font-size:13px;
}
.section-note{
  margin-top:10px;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
@container (max-width: 980px){
  .stage-header-top,
  .stage-meta-row{
    grid-template-columns:1fr;
  }
  .stage-toolbar{
    justify-self:start;
    max-width:none;
    justify-content:flex-start;
  }
  .stage-chrome{
    flex-direction:column;
    align-items:flex-start;
  }
  .stage-chrome-right{
    width:100%;
    flex-direction:column;
    align-items:stretch;
  }
  .stage-chip{
    white-space:normal;
  }
}
@container (max-width: 720px){
  .stage-briefs{
    grid-template-columns:1fr;
  }
}
@media (max-width: 1120px){
  .app-shell{grid-template-columns:1fr}
  .page-rail{
    position:static;
    top:auto;
  }
  .page-rail-card{
    min-height:0;
  }
}
@media (max-width: 900px){
  .page-rail-card{
    padding:12px;
  }
  .page-meta,.page-rail-head{
    display:none;
  }
  .page-nav{
    display:grid;
    grid-template-columns:repeat(3,minmax(0,1fr));
  }
  .page-link{
    grid-template-columns:1fr;
    justify-items:center;
    text-align:center;
    min-height:74px;
    gap:8px;
  }
  .page-copy{
    align-items:center;
  }
  .page-copy span{
    text-align:center;
  }
  .shell{
    padding:18px;
  }
  .hero,.layout,.companion-grid,.companion-actions,.metric-strip,.article-metric-strip{grid-template-columns:1fr}
  .panel{
    position:static;
    max-height:none;
    overflow:visible;
  }
  .inspector-head{
    flex-direction:column;
  }
  .inspector-head .ghost-link{
    width:100%;
    min-width:0;
  }
}
@media (max-width: 640px){
  .metric-grid{grid-template-columns:1fr}
  .article-body{
    padding:22px 18px;
  }
}
</style>
</head>
<body>
<div class="app-shell">
  __SIDEBAR_HTML__

  <main class="shell reader-main">
    <section class="hero">
      <div class="hero-card">
        <div class="eyebrow">Article Reader</div>
        <h1>記事を読み、関連概念へ移動する</h1>
        <p>
          左で記事を選び、中央で本文を読み、必要に応じて右側の接続情報や Atlas に移ります。
          読書と移動を同じ画面の中で続けられる reader です。
        </p>
      </div>
      <div class="metric-grid">
        <div class="metric"><div class="value">__ARTICLE_COUNT__</div><div class="label">Articles</div><div class="note">読める concept article 総数</div></div>
        <div class="metric"><div class="value">__TIER1_COUNT__</div><div class="label">Tier 1</div><div class="note">不変原理として扱う記事</div></div>
        <div class="metric"><div class="value">__TIER2_COUNT__</div><div class="label">Tier 2</div><div class="note">設計原理として読む記事</div></div>
        <div class="metric"><div class="value">__TIER3_COUNT__</div><div class="label">Tier 3</div><div class="note">分析枠組みとして読む記事</div></div>
        <div class="metric"><div class="value">__RESOLVED_EDGE_COUNT__</div><div class="label">Resolved Edges</div><div class="note">本文から辿れる resolved 構造</div></div>
        <div class="metric"><div class="value">__LINK_MENTION_COUNT__</div><div class="label">Link Mentions</div><div class="note">wikilink と参照運動量</div></div>
      </div>
    </section>

    <section class="layout">
      <aside class="panel control-panel reader-queue-panel">
        <div class="section">
          <div class="panel-kicker">Reading Queue</div>
          <h2>Pick the next article</h2>
          <p class="panel-copy">
            検索、tier、sorting、guided paths で読む記事を決めます。左列は一覧ではなく、本文へ入る前の選択面です。
          </p>
        </div>
        <div class="section">
          <div class="queue-controls">
            <div class="queue-control-card">
              <label class="label" for="search">Search</label>
              <input id="search" class="input" placeholder="概念名 / title / description">
            </div>
            <div class="queue-control-card">
              <label class="label">Tier</label>
              <div class="chips" id="tier-chips"></div>
            </div>
            <div class="queue-control-card">
              <label class="label" for="sort-select">Sort</label>
              <select id="sort-select" class="select">
                <option value="connected">Most connected</option>
                <option value="alphabetical">Alphabetical</option>
                <option value="gaps">Gap-rich</option>
              </select>
            </div>
            <div class="queue-control-card queue-status-card">
              <span class="queue-status-label">Queue scope</span>
              <div id="queue-status" class="queue-status"></div>
            </div>
          </div>
        </div>
        <div class="section">
          <h3>Guided Paths</h3>
          <div class="list">
            <button id="focus-hubs"><strong>Top hubs</strong><span>中心概念から読む</span></button>
            <button id="focus-foundations"><strong>Tier 1 foundations</strong><span>基礎概念から読む</span></button>
            <button id="focus-gaps"><strong>Gap-rich concepts</strong><span>未解決参照が多い記事から読む</span></button>
          </div>
        </div>
        <div class="section">
          <h3>Article Queue</h3>
          <div id="article-list" class="queue-list list"></div>
        </div>
      </aside>

      <div class="analysis-column">
        <div class="stage-shell reader-stage-shell">
          <div class="stage-header">
            <div class="stage-kicker">Reading Stage</div>
            <div class="stage-header-top">
              <div class="stage-title">
                <h2 id="stage-title">Loading...</h2>
                <p id="stage-description">記事を選択すると、その本文と構造への接続がここに表示されます。</p>
              </div>
              <div class="stage-toolbar">
                <span class="stage-chip primary" id="stage-tier-chip">Tier</span>
                <span class="stage-chip" id="stage-link-chip">0 related</span>
                <a class="stage-chip link" id="stage-open-atlas" href="graph/index.html">Open in atlas</a>
              </div>
            </div>
            <div class="stage-meta-row">
              <div class="stage-meta-card">
                <strong>Reading rule</strong>
                <span>まず本文で意味を取り、そのあと companion で接続先を決め、必要なら Atlas で全体構造を見直します。</span>
              </div>
              <div class="stage-meta-card">
                <strong>Traversal model</strong>
                <span id="stage-traversal">wikilink は本文内の局所移動、companion は構造移動、Atlas は俯瞰移動のために使います。</span>
              </div>
            </div>
          </div>

          <article class="reader-stage" id="reader-stage">
            <div class="stage-chrome">
              <div class="stage-chrome-left">
                <div class="stage-window-dots">
                  <span class="stage-window-dot"></span>
                  <span class="stage-window-dot"></span>
                  <span class="stage-window-dot"></span>
                </div>
                <span class="stage-mode-label">Reading</span>
                <span class="stage-chrome-note">scope and current selection</span>
              </div>
              <div class="stage-chrome-right">
                <span class="stage-chip" id="chrome-scope">All tiers · Most connected</span>
                <span class="stage-chip" id="chrome-selection">Selection: none</span>
              </div>
            </div>

            <div class="article-body-card">
              <div class="article-metric-strip" id="article-metric-strip"></div>
              <div class="article-body" id="article-body"></div>
            </div>

            <div class="stage-briefs">
              <div class="stage-brief-card primary">
                <span class="stage-brief-label">Current focus</span>
                <strong id="brief-title">Loading</strong>
                <span id="brief-text">記事を選択すると、この concept の読みどころが出ます。</span>
              </div>
              <div class="stage-brief-card">
                <span class="stage-brief-label">Traversal</span>
                <strong id="brief-stats">0 related / 0 backlinks</strong>
                <span id="brief-mode">本文内 wikilink と companion から次の concept へ移動できます。</span>
              </div>
            </div>
          </article>
        </div>

        <aside class="panel inspector-panel reader-companion" id="reader-companion"></aside>
      </div>
    </section>
  </main>
</div>

<script>
const ARTICLE_TEXT = __ARTICLE_JSON__;
const META = __META_JSON__;
const GRAPH = __GRAPH_JSON__;
const BACKLINKS = __BACKLINKS_JSON__;

const TIER_LABELS = {
  1: 'Tier 1',
  2: 'Tier 2',
  3: 'Tier 3',
};

const TIER_NAMES = {
  1: '不変原理',
  2: '設計原理',
  3: '分析枠組み',
};

const GRAPH_NODE_MAP = Object.fromEntries((GRAPH.nodes || []).filter((node) => node.resolved).map((node) => [node.id, node]));
const BACKLINK_NODES = (BACKLINKS && BACKLINKS.nodes) || {};

function esc(value){
  return String(value || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function normalize(value){
  return String(value || '').toLowerCase();
}

function compact(value, limit = 90){
  const text = String(value || '').trim();
  if (!text) return '';
  if (text.length <= limit) return text;
  return text.slice(0, limit - 1) + '…';
}

function backlinkNode(slug){
  return BACKLINK_NODES[slug] || {inbound: [], outbound: []};
}

function nodeForSlug(slug){
  return GRAPH_NODE_MAP[slug] || null;
}

function unresolvedCountForItems(items){
  return (items || []).filter((item) => !item.resolved).reduce((sum, item) => sum + (item.weight || 1), 0);
}

const ARTICLES = META.map((item) => {
  const node = nodeForSlug(item.slug) || {};
  const backlink = backlinkNode(item.slug);
  const inbound = (backlink.inbound || []).slice().sort((a, b) => (b.weight || 0) - (a.weight || 0) || String(a.label || '').localeCompare(String(b.label || ''), 'ja'));
  const outboundAll = (backlink.outbound || []).slice().sort((a, b) => (b.weight || 0) - (a.weight || 0) || String(a.label || '').localeCompare(String(b.label || ''), 'ja'));
  const outbound = outboundAll.filter((edge) => edge.resolved);
  const unresolved = outboundAll.filter((edge) => !edge.resolved);
  return {
    slug: item.slug,
    title: item.title,
    tier: item.tier,
    description: node.description || '',
    degree: node.degree || (outbound.length + inbound.length),
    inbound,
    outbound,
    unresolved,
    inboundCount: node.inbound_count || inbound.length,
    outboundCount: node.outbound_count || outbound.length,
    unresolvedCount: unresolvedCountForItems(outboundAll),
    domains: node.related_domains || [],
    keySources: node.key_sources || [],
    metadataSource: node.metadata_source || 'article',
  };
});

const ARTICLE_MAP = Object.fromEntries(ARTICLES.map((article) => [article.slug, article]));

const state = {
  query: '',
  tier: 'all',
  sort: 'connected',
  selected: null,
};

function tierKind(tier){
  if (tier === 1) return 'tier1';
  if (tier === 2) return 'tier2';
  if (tier === 3) return 'tier3';
  return 'legacy';
}

function tierBadge(article){
  return '<span class="tier-badge tier-' + article.tier + '">' + esc(TIER_LABELS[article.tier] || 'Tier') + ' · ' + esc(TIER_NAMES[article.tier] || '') + '</span>';
}

function readingAssessment(article){
  if (article.tier === 1 && article.degree >= 8){
    return '基礎概念であり、他記事の読み筋を決める anchor article です。最初に読む価値が高い記事です。';
  }
  if (article.unresolvedCount >= 5){
    return '未解決参照が多く、coverage gap を含んだ記事です。本文理解と gap audit を同時に進める入口になります。';
  }
  if (article.inboundCount >= article.outboundCount + 3){
    return '多くの記事から参照される anchor article です。backlinks を見ると周辺 cluster を広げやすくなります。';
  }
  if (article.outboundCount >= article.inboundCount + 3){
    return '他概念へ橋をかける bridge article です。関連概念へ読み進める中継点として機能します。';
  }
  return '本文理解を起点に、related concepts と backlinks の両方向へ広げやすい記事です。';
}

function filteredArticles(){
  let items = ARTICLES.slice();
  if (state.tier !== 'all'){
    items = items.filter((article) => String(article.tier) === String(state.tier));
  }
  if (state.query){
    const query = normalize(state.query);
    items = items.filter((article) => {
      const haystack = [
        article.title,
        article.slug,
        article.description,
        ...(article.domains || []),
      ].join(' ');
      return normalize(haystack).includes(query);
    });
  }
  if (state.sort === 'alphabetical'){
    items.sort((a, b) => a.title.localeCompare(b.title, 'ja'));
  } else if (state.sort === 'gaps'){
    items.sort((a, b) => (b.unresolvedCount - a.unresolvedCount) || (b.degree - a.degree) || a.title.localeCompare(b.title, 'ja'));
  } else {
    items.sort((a, b) => (b.degree - a.degree) || (b.inboundCount - a.inboundCount) || a.title.localeCompare(b.title, 'ja'));
  }
  return items;
}

function ensureSelected(items){
  if (state.selected && ARTICLE_MAP[state.selected] && items.some((article) => article.slug === state.selected)){
    return;
  }
  state.selected = items[0] ? items[0].slug : null;
}

function syncHash(){
  const url = location.pathname + (location.search || '');
  if (state.selected){
    history.replaceState(null, '', url + '#' + encodeURIComponent(state.selected));
    return;
  }
  history.replaceState(null, '', url);
}

function restoreHash(){
  const hash = location.hash.replace(/^#/, '');
  if (!hash) return null;
  const slug = decodeURIComponent(hash);
  return ARTICLE_MAP[slug] ? slug : null;
}

function sourceLinkMap(slug){
  const backlink = backlinkNode(slug);
  const map = {};
  (backlink.outbound || []).forEach((item) => {
    (item.raw_targets || []).forEach((raw) => {
      map[raw] = item;
    });
  });
  return map;
}

function renderWikilinkToken(sourceSlug, inner){
  let target = inner;
  let label = inner;
  if (inner.indexOf('|') !== -1){
    const parts = inner.split('|');
    target = parts[0].trim();
    label = parts.slice(1).join('|').trim();
  }
  const linkMap = sourceLinkMap(sourceSlug);
  const matched = linkMap[target];
  if (matched && matched.resolved && ARTICLE_MAP[matched.id]){
    return '<button class="wikilink" onclick="event.stopPropagation();selectArticle(\\'' + matched.id + '\\')">' + esc(label) + '</button>';
  }
  if (ARTICLE_MAP[target]){
    return '<button class="wikilink" onclick="event.stopPropagation();selectArticle(\\'' + target + '\\')">' + esc(label) + '</button>';
  }
  return '<span class="wikilink unresolved">' + esc(label) + '</span>';
}

function renderInline(sourceSlug, text){
  const tokens = [];
  let value = String(text || '').replace(/\\[\\[([^\\]]+)\\]\\]/g, function(_, inner){
    const token = '__WL' + tokens.length + '__';
    tokens.push(inner);
    return token;
  });
  value = esc(value);
  value = value.replace(/`([^`]+)`/g, '<code>$1</code>');
  value = value.replace(/\\*\\*([^*]+)\\*\\*/g, '<strong>$1</strong>');
  value = value.replace(/\\*([^*]+)\\*/g, '<em>$1</em>');
  value = value.replace(/__WL(\\d+)__/g, function(_, index){
    return renderWikilinkToken(sourceSlug, tokens[Number(index)]);
  });
  return value;
}

function stripLeadingTitle(markdown){
  return String(markdown || '').replace(/^# .+\\n+/, '').trim();
}

function isSpecialLine(line){
  const text = line.trim();
  return !text
    || /^#{1,3}\\s/.test(text)
    || /^---+$/.test(text)
    || /^>\\s/.test(text)
    || /^-\\s/.test(text)
    || /^\\d+\\.\\s/.test(text)
    || /^\\|.*\\|$/.test(text);
}

function tableCells(line){
  return line.split('|').map((cell) => cell.trim()).filter((cell, index, array) => !(cell === '' && (index === 0 || index === array.length - 1)));
}

function markdownToHtml(slug, markdown){
  const lines = stripLeadingTitle(markdown).replace(/\\r/g, '').split('\\n');
  const html = [];
  let index = 0;

  while (index < lines.length){
    const raw = lines[index];
    const line = raw.trim();

    if (!line){
      index += 1;
      continue;
    }

    if (/^---+$/.test(line)){
      html.push('<hr>');
      index += 1;
      continue;
    }

    if (/^###\\s+/.test(line)){
      html.push('<h3>' + renderInline(slug, raw.replace(/^###\\s+/, '')) + '</h3>');
      index += 1;
      continue;
    }

    if (/^##\\s+/.test(line)){
      html.push('<h2>' + renderInline(slug, raw.replace(/^##\\s+/, '')) + '</h2>');
      index += 1;
      continue;
    }

    if (/^>\\s+/.test(line)){
      const block = [];
      while (index < lines.length && /^>\\s+/.test(lines[index].trim())){
        block.push(renderInline(slug, lines[index].trim().replace(/^>\\s+/, '')));
        index += 1;
      }
      html.push('<blockquote>' + block.join('<br>') + '</blockquote>');
      continue;
    }

    if (/^\\|.*\\|$/.test(line) && index + 1 < lines.length && /^\\|?[-:|\\s]+\\|?$/.test(lines[index + 1].trim())){
      const rows = [tableCells(lines[index])];
      index += 2;
      while (index < lines.length && /^\\|.*\\|$/.test(lines[index].trim())){
        rows.push(tableCells(lines[index]));
        index += 1;
      }
      const head = rows[0] || [];
      const body = rows.slice(1);
      html.push('<table><thead><tr>' + head.map((cell) => '<th>' + renderInline(slug, cell) + '</th>').join('') + '</tr></thead><tbody>' + body.map((row) => '<tr>' + row.map((cell) => '<td>' + renderInline(slug, cell) + '</td>').join('') + '</tr>').join('') + '</tbody></table>');
      continue;
    }

    if (/^-\\s+/.test(line)){
      const items = [];
      while (index < lines.length && /^-\\s+/.test(lines[index].trim())){
        items.push(lines[index].trim().replace(/^-\\s+/, ''));
        index += 1;
      }
      html.push('<ul>' + items.map((item) => '<li>' + renderInline(slug, item) + '</li>').join('') + '</ul>');
      continue;
    }

    if (/^\\d+\\.\\s+/.test(line)){
      const items = [];
      while (index < lines.length && /^\\d+\\.\\s+/.test(lines[index].trim())){
        items.push(lines[index].trim().replace(/^\\d+\\.\\s+/, ''));
        index += 1;
      }
      html.push('<ol>' + items.map((item) => '<li>' + renderInline(slug, item) + '</li>').join('') + '</ol>');
      continue;
    }

    const paragraph = [];
    while (index < lines.length && !isSpecialLine(lines[index])){
      paragraph.push(lines[index].trim());
      index += 1;
    }
    html.push('<p>' + paragraph.map((part) => renderInline(slug, part)).join('<br>') + '</p>');
  }

  return html.join('') || '<p>記事本文がまだありません。</p>';
}

function detailPill(text){
  return '<span class="pill">' + esc(text) + '</span>';
}

function renderConnectionList(items, emptyText, limit){
  const visible = (items || []).slice(0, limit);
  if (!visible.length){
    return '<div class="empty">' + emptyText + '</div>';
  }
  return '<div class="list">' + visible.map((item) => (
    '<button class="link-btn" data-slug="' + item.id + '"><strong>' + esc(item.label) + '</strong><span>' + (item.weight || 1) + ' connection(s)</span></button>'
  )).join('') + '</div>' + ((items || []).length > visible.length ? '<div class="section-note">+' + ((items || []).length - visible.length) + ' more concept(s)</div>' : '');
}

function renderUnresolvedList(items){
  const visible = (items || []).slice(0, 5);
  if (!visible.length){
    return '<div class="empty">未解決参照はありません。</div>';
  }
  return '<div class="text-list">' + visible.map((item) => (
    '<div class="text-item"><strong>' + esc(item.label || item.raw_targets && item.raw_targets[0] || 'unresolved') + '</strong><span>' + (item.weight || 1) + ' mention(s)</span>' + (item.candidates && item.candidates.length ? '<small>candidates: ' + esc(item.candidates.slice(0, 5).join(', ')) + '</small>' : '') + '</div>'
  )).join('') + '</div>' + ((items || []).length > visible.length ? '<div class="section-note">+' + ((items || []).length - visible.length) + ' more unresolved reference(s)</div>' : '');
}

function renderQueue(items){
  const list = document.getElementById('article-list');
  const filtered = items || [];
  document.getElementById('queue-status').textContent = filtered.length + ' article(s) shown';
  if (!filtered.length){
    list.innerHTML = '<div class="empty">一致するコンセプトがありません。検索語または tier を変えてください。</div>';
    return;
  }
  list.innerHTML = filtered.map((article) => (
    '<div class="queue-card' + (article.slug === state.selected ? ' active' : '') + '" data-slug="' + article.slug + '">'
      + tierBadge(article)
      + '<strong>' + esc(article.title) + '</strong>'
      + '<p>' + esc(compact(article.description || '概要がまだ付いていません。', 84)) + '</p>'
      + '<div class="queue-meta">'
        + '<span>deg ' + article.degree + '</span>'
        + '<span>in ' + article.inboundCount + '</span>'
        + '<span>out ' + article.outboundCount + '</span>'
        + '<span>gaps ' + article.unresolvedCount + '</span>'
      + '</div>'
    + '</div>'
  )).join('');
  list.querySelectorAll('[data-slug]').forEach((button) => {
    button.addEventListener('click', () => selectArticle(button.dataset.slug));
  });
}

function activeScopeLabel(items){
  const tier = state.tier === 'all' ? 'All tiers' : ('Tier ' + state.tier);
  const sort = state.sort === 'alphabetical' ? 'Alphabetical' : (state.sort === 'gaps' ? 'Gap-rich' : 'Most connected');
  return tier + ' · ' + sort + ' · ' + items.length + ' article(s)';
}

function renderStage(article, items){
  document.getElementById('stage-title').textContent = article.title;
  document.getElementById('stage-description').textContent = article.description || 'この concept には description がまだ付いていません。';
  document.getElementById('stage-tier-chip').textContent = (TIER_LABELS[article.tier] || 'Tier') + ' · ' + (TIER_NAMES[article.tier] || '');
  document.getElementById('stage-link-chip').textContent = article.outboundCount + ' related / ' + article.inboundCount + ' backlinks';
  document.getElementById('stage-open-atlas').href = 'graph/index.html#node=' + encodeURIComponent(article.slug);
  document.getElementById('stage-traversal').textContent = article.outboundCount + ' related concept と ' + article.inboundCount + ' backlinks から読み筋を伸ばせます。gap-rich な場合は unresolved も companion で確認できます。';
  document.getElementById('chrome-scope').textContent = activeScopeLabel(items);
  document.getElementById('chrome-selection').textContent = 'Selection: ' + article.title;
  document.getElementById('brief-title').textContent = compact(readingAssessment(article), 48);
  document.getElementById('brief-text').textContent = readingAssessment(article);
  document.getElementById('brief-stats').textContent = article.outboundCount + ' related / ' + article.inboundCount + ' backlinks / ' + article.unresolvedCount + ' gaps';
  document.getElementById('brief-mode').textContent = '本文内の wikilink、companion の関連概念、Atlas handoff を使って理解の粒度を切り替えられます。';

  document.getElementById('article-metric-strip').innerHTML = ''
    + '<div class="article-metric"><div class="value">' + article.degree + '</div><div class="label">Degree</div></div>'
    + '<div class="article-metric"><div class="value">' + article.inboundCount + '</div><div class="label">Backlinks</div></div>'
    + '<div class="article-metric"><div class="value">' + article.outboundCount + '</div><div class="label">Related</div></div>'
    + '<div class="article-metric"><div class="value">' + article.unresolvedCount + '</div><div class="label">Gap Signals</div></div>';
  document.getElementById('article-body').innerHTML = markdownToHtml(article.slug, ARTICLE_TEXT[article.slug] || '');
}

function renderCompanion(article){
  const container = document.getElementById('reader-companion');
  const domainsHtml = (article.domains || []).map((domain) => detailPill(domain)).join('');
  const sourcesHtml = (article.keySources || []).slice(0, 4).map((source) => '<div class="text-item"><strong>' + esc(source) + '</strong><small>key source</small></div>').join('');
  container.innerHTML = ''
    + '<div class="section">'
      + '<div class="inspector-head">'
        + '<div class="inspector-head-copy">'
          + '<div class="eyebrow">Reading Companion</div>'
          + '<h2>' + esc(article.title) + '</h2>'
        + '</div>'
      + '</div>'
      + '<p class="inspector-description">' + esc(article.description || 'この article には短い summary がまだ付いていません。') + '</p>'
      + '<div class="inspector-lead">' + esc(readingAssessment(article)) + '</div>'
      + '<div class="pill-row">'
        + detailPill(TIER_LABELS[article.tier] || 'Tier')
        + detailPill(article.metadataSource)
        + detailPill('degree ' + article.degree)
        + detailPill('in ' + article.inboundCount)
        + detailPill('out ' + article.outboundCount)
        + detailPill('gaps ' + article.unresolvedCount)
      + '</div>'
      + '<div class="metric-strip">'
        + '<div class="mini"><div class="v">' + article.degree + '</div><div class="k">Degree</div></div>'
        + '<div class="mini"><div class="v">' + article.inboundCount + '</div><div class="k">Backlinks</div></div>'
        + '<div class="mini"><div class="v">' + article.outboundCount + '</div><div class="k">Related</div></div>'
        + '<div class="mini"><div class="v">' + article.unresolvedCount + '</div><div class="k">Gaps</div></div>'
      + '</div>'
      + '<div class="companion-actions">'
        + '<a class="ghost-link primary" href="graph/index.html#node=' + encodeURIComponent(article.slug) + '">Open in atlas</a>'
        + '<button class="ghost-btn" id="jump-top">Jump to stage top</button>'
      + '</div>'
    + '</div>'
    + '<div class="section">'
      + '<div class="companion-grid">'
        + '<div class="companion-card">'
          + '<div class="companion-card-head"><h3>Context</h3><span>domains と key sources から、この article の置き場所と根拠を短く確認します。</span></div>'
          + (domainsHtml || '<div class="empty">related_domains はまだありません。</div>')
          + (sourcesHtml ? '<div style="height:12px"></div>' + sourcesHtml : '<div class="section-note">key_sources はまだありません。</div>')
        + '</div>'
        + '<div class="companion-card">'
          + '<div class="companion-card-head"><h3>Connections</h3><span>次に読む候補として有効な related concept と backlinks の上位だけを出します。</span></div>'
          + '<div class="section" style="padding-top:0;margin-top:0;border-top:0"><h3 style="font-size:14px;margin-bottom:10px">Related concepts</h3>' + renderConnectionList(article.outbound, '関連 concept はありません。', 5) + '</div>'
          + '<div class="section"><h3 style="font-size:14px;margin-bottom:10px">Backlinks</h3>' + renderConnectionList(article.inbound, 'バックリンクはありません。', 5) + '</div>'
        + '</div>'
        + '<div class="companion-card">'
          + '<div class="companion-card-head"><h3>Gap Audit</h3><span>未解決参照は本文理解の邪魔ではなく、coverage gap の補助信号として扱います。</span></div>'
          + renderUnresolvedList(article.unresolved)
        + '</div>'
      + '</div>'
    + '</div>';

  container.querySelectorAll('[data-slug]').forEach((button) => {
    button.addEventListener('click', () => selectArticle(button.dataset.slug));
  });
  document.getElementById('jump-top').addEventListener('click', () => {
    document.querySelector('.reader-stage-shell').scrollIntoView({block: 'start', behavior: 'smooth'});
  });
}

function renderEmptyStage(){
  document.getElementById('stage-title').textContent = 'No article selected';
  document.getElementById('stage-description').textContent = '検索条件に一致する article がありません。query または tier を変えると、読める article がここに表示されます。';
  document.getElementById('stage-tier-chip').textContent = 'Queue empty';
  document.getElementById('stage-link-chip').textContent = '0 related / 0 backlinks';
  document.getElementById('stage-open-atlas').href = 'graph/index.html';
  document.getElementById('stage-traversal').textContent = 'Queue が空のときは検索語、tier、sort を調整して読書候補を戻します。';
  document.getElementById('chrome-scope').textContent = activeScopeLabel([]);
  document.getElementById('chrome-selection').textContent = 'Selection: none';
  document.getElementById('brief-title').textContent = 'Queue is empty';
  document.getElementById('brief-text').textContent = '検索条件に一致する記事がありません。';
  document.getElementById('brief-stats').textContent = '0 related / 0 backlinks / 0 gaps';
  document.getElementById('brief-mode').textContent = '検索語または tier を変えると queue が再描画されます。';
  document.getElementById('article-metric-strip').innerHTML = ''
    + '<div class="article-metric"><div class="value">0</div><div class="label">Degree</div></div>'
    + '<div class="article-metric"><div class="value">0</div><div class="label">Backlinks</div></div>'
    + '<div class="article-metric"><div class="value">0</div><div class="label">Related</div></div>'
    + '<div class="article-metric"><div class="value">0</div><div class="label">Gap Signals</div></div>';
  document.getElementById('article-body').innerHTML = '<div class="empty">一致する article がありません。検索条件を調整してください。</div>';
}

function renderEmptyCompanion(){
  document.getElementById('reader-companion').innerHTML = ''
    + '<div class="section">'
      + '<div class="eyebrow">Reading Companion</div>'
      + '<h2>No article selected</h2>'
      + '<p class="inspector-description">queue に表示される article がないため、companion も待機状態です。</p>'
      + '<div class="inspector-lead">検索条件を緩めると、Atlas handoff・related concepts・backlinks がここに出ます。</div>'
    + '</div>';
}

function renderTierChips(){
  const tierChips = document.getElementById('tier-chips');
  const tiers = [
    ['all', 'All', 'legacy'],
    ['1', 'Tier 1', 'tier1'],
    ['2', 'Tier 2', 'tier2'],
    ['3', 'Tier 3', 'tier3'],
  ];
  tierChips.innerHTML = tiers.map(([value, label, kind]) => (
    '<button class="chip' + (String(state.tier) === value ? ' active' : '') + '" data-tier="' + value + '" data-kind="' + kind + '">' + label + '</button>'
  )).join('');
  tierChips.querySelectorAll('[data-tier]').forEach((button) => {
    button.addEventListener('click', () => {
      state.tier = button.dataset.tier;
      renderAll(true);
    });
  });
}

function renderAll(preserveScroll){
  const items = filteredArticles();
  ensureSelected(items);
  renderTierChips();
  renderQueue(items);
  if (!state.selected){
    renderEmptyStage();
    renderEmptyCompanion();
    syncHash();
    return;
  }
  const article = ARTICLE_MAP[state.selected];
  renderStage(article, items);
  renderCompanion(article);
  syncHash();
  if (!preserveScroll){
    document.querySelector('.reader-stage-shell').scrollIntoView({block: 'start', behavior: 'smooth'});
  }
}

function selectArticle(slug, preserveScroll){
  if (!ARTICLE_MAP[slug]) return;
  state.selected = slug;
  renderAll(!!preserveScroll);
}

window.selectArticle = selectArticle;

function wireControls(){
  document.getElementById('search').addEventListener('input', (event) => {
    state.query = event.target.value.trim();
    renderAll(true);
  });

  document.getElementById('sort-select').addEventListener('change', (event) => {
    state.sort = event.target.value;
    renderAll(true);
  });

  document.getElementById('focus-hubs').addEventListener('click', () => {
    state.query = '';
    state.tier = 'all';
    state.sort = 'connected';
    document.getElementById('search').value = '';
    document.getElementById('sort-select').value = 'connected';
    const target = ARTICLES.slice().sort((a, b) => (b.degree - a.degree) || a.title.localeCompare(b.title, 'ja'))[0];
    if (target){
      state.selected = target.slug;
    }
    renderAll(false);
  });

  document.getElementById('focus-foundations').addEventListener('click', () => {
    state.query = '';
    state.tier = '1';
    state.sort = 'connected';
    document.getElementById('search').value = '';
    document.getElementById('sort-select').value = 'connected';
    const target = ARTICLES.filter((article) => article.tier === 1).sort((a, b) => (b.degree - a.degree) || a.title.localeCompare(b.title, 'ja'))[0];
    if (target){
      state.selected = target.slug;
    }
    renderAll(false);
  });

  document.getElementById('focus-gaps').addEventListener('click', () => {
    state.query = '';
    state.tier = 'all';
    state.sort = 'gaps';
    document.getElementById('search').value = '';
    document.getElementById('sort-select').value = 'gaps';
    const target = ARTICLES.slice().sort((a, b) => (b.unresolvedCount - a.unresolvedCount) || (b.degree - a.degree) || a.title.localeCompare(b.title, 'ja'))[0];
    if (target){
      state.selected = target.slug;
    }
    renderAll(false);
  });
}

window.addEventListener('hashchange', () => {
  const hashSlug = restoreHash();
  if (hashSlug){
    selectArticle(hashSlug, true);
  }
});

function boot(){
  const hashSlug = restoreHash();
  const defaultArticle = ARTICLES.slice().sort((a, b) => (b.degree - a.degree) || a.title.localeCompare(b.title, 'ja'))[0];
  state.selected = hashSlug || (defaultArticle ? defaultArticle.slug : null);
  wireControls();
  renderAll(true);
}

boot();
</script>
</body>
</html>"""

    return (
        template.replace("__ARTICLE_JSON__", article_json)
        .replace("__META_JSON__", meta_json)
        .replace("__GRAPH_JSON__", graph_json)
        .replace("__BACKLINKS_JSON__", backlinks_json)
        .replace("__SUMMARY_TEXT__", summary_text)
        .replace("__SIDEBAR_HTML__", sidebar_html)
        .replace("__ARTICLE_COUNT__", str(article_count))
        .replace("__TIER1_COUNT__", str(tier_counts.get(1, 0)))
        .replace("__TIER2_COUNT__", str(tier_counts.get(2, 0)))
        .replace("__TIER3_COUNT__", str(tier_counts.get(3, 0)))
        .replace("__RESOLVED_EDGE_COUNT__", str(resolved_edges))
        .replace("__LINK_MENTION_COUNT__", str(link_mentions))
    )


def build_reader():
    meta = collect_meta()
    articles = collect_articles(meta)
    graph = load_json(GRAPH_FILE, {})
    backlinks = load_json(BACKLINKS_FILE, {"nodes": {}})

    html = render_reader_html(meta, articles, graph, backlinks)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(html)

    return {
        "articles": len(articles),
        "path": OUT,
        "size": os.path.getsize(OUT),
    }


def main():
    result = build_reader()
    print(f"Generated: {result['size']} bytes")
    print(f"Articles: {result['articles']}")
    print(f"Path: {result['path']}")


if __name__ == "__main__":
    main()
