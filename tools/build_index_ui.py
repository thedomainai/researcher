#!/usr/bin/env python3
"""Generate a dedicated web UI for the workspace index."""

from collections import Counter
import json
import os

from build_reader import collect_meta, load_json
from lib.workspace_ui import render_workspace_sidebar

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPH_FILE = os.path.join(BASE, "wiki", "_meta", "concepts-graph.json")
OUT = os.path.join(BASE, "wiki", "index.html")


def build_catalog_items(meta, graph):
    resolved_nodes = {
        node["id"]: node for node in graph.get("nodes", []) if node.get("resolved")
    }
    unresolved_counts = Counter(
        item.get("source_slug")
        for item in graph.get("unresolved_mentions", [])
        if item.get("source_slug")
    )

    catalog = []
    for item in meta:
        node = resolved_nodes.get(item["slug"], {})
        catalog.append(
            {
                "slug": item["slug"],
                "title": item["title"],
                "tier": item.get("tier"),
                "description": node.get("description") or item.get("description") or "説明未設定",
                "domains": node.get("related_domains") or item.get("related_domains") or [],
                "degree": node.get("degree", 0),
                "inbound": node.get("inbound_count", 0),
                "outbound": node.get("outbound_count", 0),
                "gaps": unresolved_counts.get(item["slug"], 0),
            }
        )
    return catalog


def render_index_html(catalog, graph):
    graph_json = json.dumps(graph, ensure_ascii=False).replace("</", "<\\/")
    catalog_json = json.dumps(catalog, ensure_ascii=False).replace("</", "<\\/")
    summary = graph.get("summary", {})
    tier_counts = Counter(item.get("tier") for item in catalog)
    domains = sorted(
        {
            domain
            for item in catalog
            for domain in item.get("domains", [])
            if domain
        }
    )

    summary_text = (
        f'{summary.get("resolved_nodes", len(catalog))} concepts / '
        f'{summary.get("resolved_edges", 0)} edges / '
        f'{summary.get("unresolved_nodes", 0)} unresolved refs'
    )
    sidebar_html = render_workspace_sidebar(
        active_view="index",
        summary_text=summary_text,
        links={
            "atlas": "graph/index.html",
            "reader": "reader.html",
            "index": "index.html",
        },
    )

    return """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wiki Index</title>
<style>
:root{
  --page-gap:20px;
  --rail-width:264px;
  --bg-0:#060913;
  --bg-1:#0c1220;
  --bg-2:#11192a;
  --bg-3:#192538;
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
  --card-soft:rgba(12,19,33,.62);
  --surface-raise:rgba(17,26,45,.86);
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
    linear-gradient(180deg, rgba(17,25,42,.92), rgba(7,10,19,.98));
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
  grid-template-columns:minmax(0, 1.4fr) minmax(320px, .8fr);
  gap:18px;
  margin-bottom:18px;
}
.hero-card,.metric-grid,.panel,.stage-shell{
  min-width:0;
  background:var(--card);
  border:1px solid var(--line-strong);
  backdrop-filter:blur(10px);
  box-shadow:var(--shadow);
  border-radius:26px;
}
.hero-card{
  padding:24px;
}
.eyebrow{
  display:inline-flex;
  align-items:center;
  gap:10px;
  padding:8px 12px;
  border-radius:999px;
  background:rgba(21,33,56,.78);
  color:var(--ink-soft);
  font-size:12px;
  letter-spacing:.12em;
  text-transform:uppercase;
}
.hero h1{
  margin:18px 0 10px;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  font-size:clamp(28px,3.4vw,46px);
  line-height:1.02;
  letter-spacing:-.03em;
}
.hero p{
  margin:0;
  max-width:58ch;
  color:var(--ink-soft);
  font-size:14px;
  line-height:1.68;
}
.metric-grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:1px;
  overflow:hidden;
}
.metric{
  padding:18px 18px 16px;
  background:var(--card-strong);
}
.metric .value{
  font-size:30px;
  font-weight:700;
  letter-spacing:-.04em;
}
.metric .label{
  margin-top:6px;
  font-size:12px;
  letter-spacing:.12em;
  text-transform:uppercase;
  color:var(--ink-soft);
}
.metric .note{
  margin-top:8px;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
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
  padding:22px;
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
.panel::-webkit-scrollbar{width:10px}
.panel::-webkit-scrollbar-thumb{
  background:rgba(151,170,204,.16);
  border-radius:999px;
  border:2px solid transparent;
  background-clip:padding-box;
}
.panel::-webkit-scrollbar-track{background:transparent}
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
.chip.active[data-kind="legacy"]{background:rgba(146,164,191,.18)}
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
.list button,.ghost-link{
  width:100%;
  text-align:left;
  border:1px solid rgba(151,170,204,.12);
  background:rgba(16,25,42,.78);
  border-radius:16px;
  padding:12px 14px;
  color:var(--ink);
  cursor:pointer;
}
.list button:hover,.ghost-link:hover{
  background:rgba(21,33,56,.92);
}
.list strong{
  display:block;
  font-size:14px;
  margin-bottom:4px;
  overflow-wrap:anywhere;
}
.list span{
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
  overflow-wrap:anywhere;
}
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
  mask-image:linear-gradient(180deg, rgba(0,0,0,.7), transparent 82%);
}
.stage-header{
  position:relative;
  z-index:2;
  display:flex;
  flex-direction:column;
  gap:16px;
  padding:6px 6px 18px;
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
  font-size:30px;
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
}
.stage-chip.primary{
  color:var(--ink);
  background:linear-gradient(135deg, rgba(130,174,245,.18), rgba(121,210,197,.14));
  border-color:rgba(130,174,245,.24);
}
.stage-meta-row{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:12px;
}
.legend{
  display:flex;
  flex-wrap:wrap;
  gap:8px 12px;
  justify-content:flex-start;
}
.legend-item{
  display:flex;
  align-items:center;
  gap:8px;
  padding:9px 12px;
  border-radius:999px;
  border:1px solid rgba(151,170,204,.14);
  background:rgba(16,25,42,.72);
  font-size:12px;
  color:var(--ink-soft);
}
.dot{
  width:10px;
  height:10px;
  border-radius:999px;
}
.stage-meta-card{
  padding:12px 14px;
  border-radius:18px;
  border:1px solid rgba(151,170,204,.14);
  background:rgba(16,25,42,.72);
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
.stage{
  position:relative;
  min-height:0;
  display:grid;
  grid-template-rows:auto minmax(360px,1fr) auto;
  gap:14px;
  padding:16px;
  border-radius:28px;
  border:1px solid rgba(151,170,204,.12);
  background:
    radial-gradient(circle at 18% 18%, rgba(130,174,245,.08), transparent 22%),
    radial-gradient(circle at 74% 16%, rgba(217,160,125,.08), transparent 26%),
    radial-gradient(circle at 50% 82%, rgba(121,210,197,.08), transparent 26%),
    linear-gradient(180deg, rgba(11,17,30,.92), rgba(9,14,25,.96));
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.05),
    inset 0 -1px 0 rgba(151,170,204,.08);
}
.stage-chrome{
  position:relative;
  z-index:3;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:12px;
  padding:12px 14px;
  border-radius:18px;
  background:rgba(16,25,42,.74);
  border:1px solid rgba(151,170,204,.14);
}
.stage-chrome-left,.stage-chrome-right{
  display:flex;
  align-items:center;
  gap:10px;
  min-width:0;
  flex-wrap:wrap;
}
.stage-window-dots{
  display:flex;
  gap:6px;
}
.stage-window-dot{
  width:8px;
  height:8px;
  border-radius:999px;
  background:rgba(151,170,204,.28);
}
.stage-window-dot:nth-child(1){background:rgba(217,160,125,.78)}
.stage-window-dot:nth-child(2){background:rgba(130,174,245,.8)}
.stage-window-dot:nth-child(3){background:rgba(121,210,197,.78)}
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
.catalog-stage-body{
  min-width:0;
  width:100%;
  max-width:100%;
  display:flex;
  flex-direction:column;
  gap:14px;
}
.catalog-summary-strip{
  min-width:0;
  width:100%;
  max-width:100%;
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:10px;
}
.catalog-summary-card{
  min-width:0;
  width:100%;
  max-width:100%;
  padding:14px 16px;
  border-radius:18px;
  border:1px solid rgba(151,170,204,.12);
  background:rgba(14,22,38,.84);
}
.catalog-summary-card strong{
  display:block;
  font-size:13px;
  overflow-wrap:anywhere;
}
.catalog-summary-card span{
  display:block;
  margin-top:6px;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
  overflow-wrap:anywhere;
}
.catalog-sections{
  min-width:0;
  width:100%;
  max-width:100%;
  display:flex;
  flex-direction:column;
  gap:14px;
}
.catalog-section{
  min-width:0;
  width:100%;
  max-width:100%;
  padding:18px;
  border-radius:22px;
  border:1px solid rgba(151,170,204,.12);
  background:rgba(12,18,31,.84);
}
.catalog-section-head{
  display:flex;
  align-items:flex-end;
  justify-content:space-between;
  gap:12px;
  margin-bottom:14px;
}
.catalog-section-head h3{
  margin:0;
  font-size:22px;
  letter-spacing:-.03em;
}
.catalog-section-head span{
  color:var(--ink-soft);
  font-size:12px;
  overflow-wrap:anywhere;
}
.catalog-grid{
  min-width:0;
  width:100%;
  max-width:100%;
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:12px;
}
.catalog-card{
  min-width:0;
  width:100%;
  max-width:100%;
  padding:16px;
  border-radius:20px;
  border:1px solid rgba(151,170,204,.12);
  background:linear-gradient(180deg, rgba(17,26,45,.82), rgba(12,19,34,.8));
}
.catalog-card h4{
  margin:0;
  font-size:16px;
  line-height:1.45;
  overflow-wrap:anywhere;
}
.catalog-card p{
  margin:10px 0 0;
  color:var(--ink-soft);
  font-size:13px;
  line-height:1.65;
}
.catalog-meta{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  margin-top:12px;
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
  font-size:11px;
}
.catalog-actions{
  min-width:0;
  width:100%;
  max-width:100%;
  margin-top:14px;
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:10px;
}
.catalog-action{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  padding:10px 12px;
  border-radius:14px;
  border:1px solid rgba(151,170,204,.14);
  background:rgba(16,25,42,.74);
  color:var(--ink);
  text-decoration:none;
  font-size:12px;
}
.catalog-action.primary{
  background:linear-gradient(135deg, rgba(121,210,197,.18), rgba(130,174,245,.16));
  border-color:rgba(121,210,197,.18);
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
  padding:16px;
  border-radius:18px;
  background:rgba(15,24,41,.82);
  border:1px solid rgba(151,170,204,.14);
}
.stage-brief-card.primary{
  background:linear-gradient(135deg, rgba(130,174,245,.18), rgba(121,210,197,.12));
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
.stage-brief-card strong + span{
  display:block;
  margin-top:6px;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.empty{
  padding:16px;
  border-radius:18px;
  background:rgba(16,25,42,.74);
  border:1px dashed rgba(151,170,204,.18);
  color:var(--ink-soft);
  font-size:13px;
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
}
@media (max-width: 1120px){
  .app-shell{grid-template-columns:1fr}
  .page-rail{position:static; top:auto}
  .page-rail-card{min-height:0}
}
@media (max-width: 900px){
  .page-rail-card{padding:12px}
  .page-meta,.page-rail-head{display:none}
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
  .page-copy{align-items:center}
  .page-copy span{text-align:center}
  .shell{padding:18px}
  .hero,.layout,.catalog-grid,.catalog-actions,.catalog-summary-strip{grid-template-columns:1fr}
  .panel{
    position:static;
    max-height:none;
    overflow:visible;
  }
  .stage{grid-template-rows:auto minmax(300px,1fr) auto}
  .catalog-section-head{
    flex-direction:column;
    align-items:flex-start;
  }
}
@media (max-width: 640px){
  .metric-grid{grid-template-columns:1fr}
}
</style>
</head>
<body>
<div class="app-shell">
  __SIDEBAR_HTML__

  <main class="shell">
    <section class="hero">
      <div class="hero-card">
        <div class="eyebrow">Wiki Index</div>
        <h1>全 concept の存在を確認し、次に見る入口を選ぶ</h1>
        <p>
          この index は graph の topology を読む画面ではなく、concept の所在と分類を静かに棚卸しする catalog です。
          Atlas へ飛ぶ前の俯瞰、Reader へ入る前の見取り図として機能します。
        </p>
      </div>
      <div class="metric-grid">
        <div class="metric"><div class="value">__ARTICLE_COUNT__</div><div class="label">Cataloged Concepts</div><div class="note">記事を持つ concept 総数</div></div>
        <div class="metric"><div class="value">__TIER1_COUNT__</div><div class="label">Tier 1</div><div class="note">不変原理として読む概念</div></div>
        <div class="metric"><div class="value">__TIER2_COUNT__</div><div class="label">Tier 2</div><div class="note">設計原理として扱う概念</div></div>
        <div class="metric"><div class="value">__TIER3_COUNT__</div><div class="label">Tier 3</div><div class="note">分析枠組みとして扱う概念</div></div>
        <div class="metric"><div class="value">__DOMAIN_COUNT__</div><div class="label">Domains</div><div class="note">関連分野のユニーク数</div></div>
        <div class="metric"><div class="value">__ISOLATED_COUNT__</div><div class="label">Isolated Concepts</div><div class="note">グラフ上で孤立している概念</div></div>
      </div>
    </section>

    <section class="layout">
      <aside class="panel control-panel">
        <div class="section">
          <div class="panel-kicker">Catalog Lens</div>
          <h2>Filter the inventory</h2>
          <p class="panel-copy">
            検索・tier・domain・並び順で catalog を切り替えます。ここでは分析よりも「存在確認」と「入口選び」を優先します。
          </p>
        </div>
        <div class="section">
          <label class="label" for="search">Search</label>
          <input id="search" class="input" placeholder="概念名 / slug / description">
          <div style="height:14px"></div>
          <label class="label">Tier</label>
          <div class="chips" id="tier-chips"></div>
          <div style="height:14px"></div>
          <label class="label" for="domain-filter">Domain</label>
          <select id="domain-filter" class="select"></select>
          <div style="height:14px"></div>
          <label class="label" for="sort-select">Sort</label>
          <select id="sort-select" class="select">
            <option value="alphabetical">Alphabetical</option>
            <option value="connected">Most connected</option>
            <option value="gaps">Gap-rich</option>
          </select>
        </div>
        <div class="section">
          <h3>Guided Paths</h3>
          <div class="list">
            <button id="focus-foundations"><strong>Tier 1 foundations</strong><span>基礎概念だけに寄る</span></button>
            <button id="focus-connected"><strong>Most connected</strong><span>中心性の高い概念から atlas / reader へ入る</span></button>
            <button id="focus-gaps"><strong>Gap-rich concepts</strong><span>未解決参照が多い記事を棚卸しする</span></button>
          </div>
        </div>
        <div class="section">
          <h3>Scope</h3>
          <div class="list">
            <button type="button"><strong id="scope-count">0 concepts</strong><span id="scope-note">catalog を読み込んでいます。</span></button>
          </div>
        </div>
      </aside>

      <div class="analysis-column">
        <div class="stage-shell">
          <div class="stage-header">
            <div class="stage-kicker">Catalog Board</div>
            <div class="stage-header-top">
              <div class="stage-title">
                <h2>Workspace Index</h2>
                <p>tier と domain の軸で concept を整理し、Reader に入る前の見取り図を作るための board です。Graph の密度ではなく、catalog の網羅性と入口の明瞭さを優先します。</p>
              </div>
              <div class="stage-toolbar">
                <span class="stage-chip primary">Inventory-first</span>
                <span class="stage-chip">Reader-ready</span>
                <span class="stage-chip">Atlas-linked</span>
              </div>
            </div>
            <div class="stage-meta-row">
              <div class="legend">
                <div class="legend-item"><span class="dot" style="background:var(--accent-rust)"></span>Tier 1</div>
                <div class="legend-item"><span class="dot" style="background:var(--accent-teal)"></span>Tier 2</div>
                <div class="legend-item"><span class="dot" style="background:var(--accent-blue)"></span>Tier 3</div>
                <div class="legend-item"><span class="dot" style="background:var(--accent-slate)"></span>Legacy</div>
              </div>
              <div class="stage-meta-card">
                <strong>Decision rule</strong>
                <span>catalog で候補を絞り、Reader で本文へ入り、必要なら Atlas で周辺構造へ移ります。</span>
              </div>
            </div>
          </div>
          <div class="stage" id="stage">
            <div class="stage-chrome">
              <div class="stage-chrome-left">
                <div class="stage-window-dots">
                  <span class="stage-window-dot"></span>
                  <span class="stage-window-dot"></span>
                  <span class="stage-window-dot"></span>
                </div>
                <span class="stage-mode-label">Catalog canvas</span>
                <span class="stage-chrome-note">inventory grouped by tier and filtered by lens</span>
              </div>
              <div class="stage-chrome-right">
                <span class="stage-chip" id="chrome-scope">All tiers · All domains</span>
                <span class="stage-chip" id="chrome-selection">Selection: catalog overview</span>
              </div>
            </div>
            <div class="catalog-stage-body">
              <div class="catalog-summary-strip">
                <div class="catalog-summary-card">
                  <strong id="summary-primary">Catalog overview</strong>
                  <span id="summary-text">全 concept を tier ごとに表示しています。</span>
                </div>
                <div class="catalog-summary-card">
                  <strong id="summary-secondary">0 visible concepts</strong>
                  <span id="summary-secondary-text">scope を切り替えると件数が変わります。</span>
                </div>
                <div class="catalog-summary-card">
                  <strong>Available domains</strong>
                  <span>__DOMAIN_COUNT__ domains / unresolved refs __UNRESOLVED_COUNT__</span>
                </div>
              </div>
              <div class="catalog-sections" id="catalog-sections"></div>
            </div>
            <div class="stage-briefs">
              <div class="stage-brief-card primary">
                <span class="stage-brief-label">What this view is for</span>
                <strong>網羅確認と入口選びに集中する</strong>
                <span>構造比較よりも、どの concept が存在していて、どこから読むかを決めるための目録 view です。</span>
              </div>
              <div class="stage-brief-card">
                <span class="stage-brief-label">How to use it</span>
                <strong>Search → Filter → Open</strong>
                <span>検索とフィルタで scope を狭め、Reader または Atlas へ直接渡します。</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</div>

<script>
const GRAPH = __GRAPH_JSON__;
const CATALOG = __CATALOG_JSON__;
const DOMAINS = __DOMAINS_JSON__;
const tierLabelMap = {1:'Tier 1', 2:'Tier 2', 3:'Tier 3', legacy:'Legacy'};
const tierSectionOrder = [1, 2, 3, 'legacy'];

const state = {
  query: '',
  tier: 'all',
  domain: 'all',
  sort: 'alphabetical',
};

const tierChips = document.getElementById('tier-chips');
const searchInput = document.getElementById('search');
const domainFilter = document.getElementById('domain-filter');
const sortSelect = document.getElementById('sort-select');
const scopeCount = document.getElementById('scope-count');
const scopeNote = document.getElementById('scope-note');
const chromeScope = document.getElementById('chrome-scope');
const chromeSelection = document.getElementById('chrome-selection');
const summaryPrimary = document.getElementById('summary-primary');
const summaryText = document.getElementById('summary-text');
const summarySecondary = document.getElementById('summary-secondary');
const summarySecondaryText = document.getElementById('summary-secondary-text');
const catalogSections = document.getElementById('catalog-sections');

function normalize(text){
  return String(text || '').toLowerCase();
}

function tierKey(item){
  return item.tier === 1 || item.tier === 2 || item.tier === 3 ? item.tier : 'legacy';
}

function tierBadge(item){
  const tier = tierKey(item);
  return tier === 'legacy' ? 'Legacy' : 'Tier ' + tier;
}

function escapeHtml(text){
  return String(text || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function activeScopeText(){
  const parts = [];
  parts.push(state.tier === 'all' ? 'All tiers' : tierLabelMap[state.tier]);
  parts.push(state.domain === 'all' ? 'All domains' : state.domain);
  return parts.join(' · ');
}

function filteredCatalog(){
  const query = normalize(state.query);
  const items = CATALOG.filter(item => {
    if (state.tier !== 'all' && String(tierKey(item)) !== String(state.tier)) return false;
    if (state.domain !== 'all' && !(item.domains || []).includes(state.domain)) return false;
    if (query){
      const haystack = [
        item.title,
        item.slug,
        item.description,
        ...(item.domains || []),
      ].join(' ');
      if (!normalize(haystack).includes(query)) return false;
    }
    return true;
  });

  const sorted = items.slice();
  if (state.sort === 'connected'){
    sorted.sort((a, b) => (b.degree - a.degree) || a.title.localeCompare(b.title, 'ja'));
  } else if (state.sort === 'gaps'){
    sorted.sort((a, b) => (b.gaps - a.gaps) || (b.degree - a.degree) || a.title.localeCompare(b.title, 'ja'));
  } else {
    sorted.sort((a, b) => a.title.localeCompare(b.title, 'ja'));
  }
  return sorted;
}

function renderTierChips(){
  const chips = [
    {value: 'all', label: 'All', kind: 'all'},
    {value: '1', label: 'Tier 1', kind: 'tier1'},
    {value: '2', label: 'Tier 2', kind: 'tier2'},
    {value: '3', label: 'Tier 3', kind: 'tier3'},
    {value: 'legacy', label: 'Legacy', kind: 'legacy'},
  ];
  tierChips.innerHTML = chips.map(item =>
    '<button class="chip' + (String(state.tier) === item.value ? ' active' : '') + '" data-tier="' + item.value + '" data-kind="' + item.kind + '">' + item.label + '</button>'
  ).join('');
}

function renderDomainFilter(){
  const options = ['<option value="all">All domains</option>'].concat(
    DOMAINS.map(domain => '<option value="' + domain + '">' + domain + '</option>')
  );
  domainFilter.innerHTML = options.join('');
  domainFilter.value = state.domain;
}

function renderSections(){
  const items = filteredCatalog();
  const grouped = new Map();
  tierSectionOrder.forEach(key => grouped.set(String(key), []));
  items.forEach(item => {
    const key = String(tierKey(item));
    if (!grouped.has(key)) grouped.set(key, []);
    grouped.get(key).push(item);
  });

  const sections = tierSectionOrder
    .map(key => String(key))
    .filter(key => (grouped.get(key) || []).length)
    .map(key => {
      const sectionItems = grouped.get(key) || [];
      return `
        <section class="catalog-section">
          <div class="catalog-section-head">
            <div>
              <h3>${tierLabelMap[key]}</h3>
              <span>${sectionItems.length} concepts</span>
            </div>
            <span>${key === 'legacy' ? '補助的 catalog' : 'workspace entrypoints'}</span>
          </div>
          <div class="catalog-grid">
            ${sectionItems.map(item => `
              <article class="catalog-card" data-slug="${escapeHtml(item.slug)}">
                <h4>${escapeHtml(item.title)}</h4>
                <p>${escapeHtml(item.description)}</p>
                <div class="catalog-meta">
                  <span class="pill">${tierBadge(item)}</span>
                  <span class="pill">Degree ${item.degree || 0}</span>
                  <span class="pill">Gaps ${item.gaps || 0}</span>
                  ${(item.domains || []).slice(0, 2).map(domain => '<span class="pill">' + escapeHtml(domain) + '</span>').join('')}
                </div>
                <div class="catalog-actions">
                  <a class="catalog-action primary" href="reader.html#${encodeURIComponent(item.slug)}">Open in reader</a>
                  <a class="catalog-action" href="graph/index.html#node=${encodeURIComponent(item.slug)}">Open in atlas</a>
                </div>
              </article>
            `).join('')}
          </div>
        </section>
      `;
    });

  catalogSections.innerHTML = sections.length ? sections.join('') : '<div class="empty">条件に一致する concept がありません。Search / Tier / Domain を調整してください。</div>';
  scopeCount.textContent = items.length + ' visible concepts';
  scopeNote.textContent = state.sort === 'connected'
    ? '中心性の高い順に並べています。'
    : state.sort === 'gaps'
      ? '未解決参照の多い順に並べています。'
      : '五十音に近い順で並べています。';
  chromeScope.textContent = activeScopeText();
  chromeSelection.textContent = items.length ? 'Selection: ' + items[0].title : 'Selection: catalog overview';
  summaryPrimary.textContent = items.length ? 'Catalog in scope' : 'Catalog empty';
  summaryText.textContent = items.length
    ? activeScopeText() + ' の条件で section を再構成しています。'
    : '検索条件を緩めると catalog が再表示されます。';
  summarySecondary.textContent = items.length + ' visible concepts';
  summarySecondaryText.textContent = 'Tier sections: ' + sections.length + ' / sort: ' + state.sort;
}

function wireControls(){
  searchInput.addEventListener('input', event => {
    state.query = event.target.value || '';
    renderAll();
  });
  domainFilter.addEventListener('change', event => {
    state.domain = event.target.value || 'all';
    renderAll();
  });
  sortSelect.addEventListener('change', event => {
    state.sort = event.target.value || 'alphabetical';
    renderAll();
  });
  tierChips.addEventListener('click', event => {
    const chip = event.target.closest('[data-tier]');
    if (!chip) return;
    state.tier = chip.dataset.tier;
    renderAll();
  });
  document.getElementById('focus-foundations').addEventListener('click', () => {
    state.tier = '1';
    state.sort = 'alphabetical';
    renderAll();
  });
  document.getElementById('focus-connected').addEventListener('click', () => {
    state.tier = 'all';
    state.sort = 'connected';
    renderAll();
  });
  document.getElementById('focus-gaps').addEventListener('click', () => {
    state.tier = 'all';
    state.sort = 'gaps';
    renderAll();
  });
}

function renderAll(){
  renderTierChips();
  renderSections();
}

renderDomainFilter();
wireControls();
renderAll();
</script>
</body>
</html>""".replace("__GRAPH_JSON__", graph_json) \
        .replace("__CATALOG_JSON__", catalog_json) \
        .replace("__DOMAINS_JSON__", json.dumps(domains, ensure_ascii=False)) \
        .replace("__SIDEBAR_HTML__", sidebar_html) \
        .replace("__ARTICLE_COUNT__", str(len(catalog))) \
        .replace("__TIER1_COUNT__", str(tier_counts.get(1, 0))) \
        .replace("__TIER2_COUNT__", str(tier_counts.get(2, 0))) \
        .replace("__TIER3_COUNT__", str(tier_counts.get(3, 0))) \
        .replace("__DOMAIN_COUNT__", str(len(domains))) \
        .replace("__ISOLATED_COUNT__", str(summary.get("isolated_concepts", 0))) \
        .replace("__UNRESOLVED_COUNT__", str(summary.get("unresolved_nodes", 0)))


def build_index_ui():
    meta = collect_meta()
    graph = load_json(GRAPH_FILE, {})
    catalog = build_catalog_items(meta, graph)
    html = render_index_html(catalog, graph)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(html)

    return {
        "path": OUT,
        "size": os.path.getsize(OUT),
        "articles": len(catalog),
    }


def main():
    result = build_index_ui()
    print(f"Generated: {result['size']} bytes")
    print(f"Articles: {result['articles']}")
    print(f"Path: {result['path']}")


if __name__ == "__main__":
    main()
