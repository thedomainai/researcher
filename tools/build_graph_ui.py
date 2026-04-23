#!/usr/bin/env python3
"""Generate a dedicated web UI for the explicit knowledge graph."""

import json
import os

from lib.workspace_ui import render_workspace_sidebar

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPH_FILE = os.path.join(BASE, "wiki", "_meta", "concepts-graph.json")
GRAPH_DIR = os.path.join(BASE, "wiki", "graph")
OUT = os.path.join(GRAPH_DIR, "index.html")
LEGACY_OUT = os.path.join(BASE, "wiki", "graph.html")


def load_graph():
    with open(GRAPH_FILE, encoding="utf-8") as handle:
        return json.load(handle)


def render_html(graph):
    graph_json = json.dumps(graph, ensure_ascii=False).replace("</", "<\\/")
    summary = graph["summary"]
    sidebar_html = render_workspace_sidebar(
        active_view="atlas",
        summary_text=f'{summary["resolved_nodes"]} concepts / {summary["resolved_edges"]} edges / {summary["unresolved_nodes"]} unresolved refs',
        links={
            "atlas": "index.html",
            "reader": "../reader.html",
            "index": "../index.html",
        },
    )

    return """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Research Atlas</title>
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
  --night-0:#060913;
  --night-1:#0c1220;
  --night-2:#11192a;
  --night-3:#192538;
  --mist-0:rgba(255,255,255,.04);
  --mist-1:rgba(255,255,255,.08);
  --mist-2:rgba(255,255,255,.12);
  --steel:#82aef5;
  --steel-soft:rgba(130,174,245,.18);
  --violet-soft:rgba(121,210,197,.14);
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
.page-link.active .page-icon{
  background:rgba(30,43,67,.9);
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
  line-height:1.62;
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
  line-height:1.5;
}
.layout{
  display:grid;
  grid-template-columns:minmax(228px,248px) minmax(0,1fr);
  gap:18px;
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
.chip.active[data-kind="legacy"]{background:rgba(146,164,191,.18)}
.toggle{
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:12px 14px;
  border-radius:16px;
  background:rgba(16,25,42,.78);
  border:1px solid rgba(151,170,204,.12);
  font-size:13px;
}
.toggle input{width:18px;height:18px}
.range-wrap{
  display:grid;
  grid-template-columns:1fr auto;
  gap:10px;
  align-items:center;
}
.range-wrap input[type="range"]{width:100%}
.small{
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.5;
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
.ghost-link{
  display:inline-flex;
  width:100%;
  align-items:center;
  justify-content:center;
  text-decoration:none;
}
.list button:hover,.link-btn:hover,.ghost-btn:hover,.ghost-link:hover{background:rgba(21,33,56,.92)}
.list strong{
  display:block;
  font-size:14px;
  margin-bottom:4px;
  overflow-wrap:anywhere;
}
.list span{
  color:var(--ink-soft);
  font-size:12px;
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
  mask-image:linear-gradient(180deg, rgba(0,0,0,.7), transparent 80%);
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
  min-width:0;
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
  grid-template-rows:auto minmax(520px,1fr) auto;
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
.stage::before{
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  background:
    linear-gradient(180deg, rgba(255,255,255,.04), transparent 12%),
    radial-gradient(circle at 50% 0%, rgba(255,255,255,.08), transparent 38%);
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
  backdrop-filter:blur(16px);
}
.stage-canvas-shell{
  position:relative;
  min-height:clamp(500px, 66vh, 780px);
  border-radius:24px;
  overflow:hidden;
  border:1px solid rgba(151,170,204,.14);
  background:
    radial-gradient(circle at 18% 18%, rgba(130,174,245,.12), transparent 22%),
    radial-gradient(circle at 74% 16%, rgba(217,160,125,.1), transparent 26%),
    radial-gradient(circle at 50% 82%, rgba(121,210,197,.08), transparent 26%),
    linear-gradient(180deg, rgba(10,16,28,.96), rgba(7,11,20,.98));
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.05),
    inset 0 -1px 0 rgba(151,170,204,.08);
}
.stage-canvas-shell::before{
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  background:
    linear-gradient(180deg, rgba(255,255,255,.03), transparent 12%),
    radial-gradient(circle at 50% 0%, rgba(255,255,255,.07), transparent 38%);
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
  min-width:0;
}
.stage-chrome-note{
  color:var(--ink-soft);
  font-size:12px;
  min-width:0;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
}
.stage-chip.ghost{
  color:var(--ink-soft);
  background:rgba(18,29,48,.72);
}
#graph{
  position:absolute;
  inset:0;
  display:block;
  width:100%;
  height:100%;
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
  backdrop-filter:blur(16px);
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
}
.inspector-panel h2{
  margin-bottom:8px;
  font-size:30px;
}
.inspector-description{
  margin:0;
  color:var(--ink-soft);
  font-size:14px;
  line-height:1.72;
  display:-webkit-box;
  -webkit-line-clamp:4;
  -webkit-box-orient:vertical;
  overflow:hidden;
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
.inspector-lead{
  margin-top:14px;
  padding:14px 16px;
  border-radius:18px;
  background:rgba(16,25,42,.74);
  border:1px solid rgba(151,170,204,.14);
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
  grid-template-columns:repeat(2,minmax(0,1fr));
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
.dock{
  margin-top:18px;
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:10px;
}
.ghost-btn{
  border-radius:16px;
  min-width:0;
}
.ghost-link.primary{
  grid-column:1 / -1;
  background:linear-gradient(135deg, rgba(121,210,197,.18), rgba(130,174,245,.16));
  color:var(--ink);
  border-color:rgba(121,210,197,.18);
}
.inspector-grid{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:12px;
}
.inspector-card{
  min-width:0;
  padding:16px;
  border-radius:20px;
  background:rgba(14,22,38,.84);
  border:1px solid rgba(151,170,204,.12);
}
.inspector-card h3{
  margin:0;
}
.inspector-card-head{
  display:flex;
  flex-direction:column;
  gap:6px;
  margin-bottom:12px;
}
.inspector-card-head span{
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.inspector-connection-grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:10px;
}
.inspector-subsection{
  min-width:0;
}
.inspector-subsection-label{
  display:block;
  margin-bottom:8px;
  color:var(--ink-soft);
  font-size:11px;
  font-weight:600;
  letter-spacing:.14em;
  text-transform:uppercase;
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
.section-note{
  margin-top:10px;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.empty{
  padding:14px;
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
  .hero,.layout,.inspector-grid,.inspector-connection-grid{grid-template-columns:1fr}
  .panel{
    position:static;
    max-height:none;
    overflow:visible;
  }
  .stage{
    grid-template-rows:auto minmax(360px,1fr) auto;
  }
  .stage-toolbar{
    justify-content:flex-start;
  }
  .stage-canvas-shell{
    min-height:360px;
  }
  .dock{
    grid-template-columns:1fr;
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
  .metric-strip{grid-template-columns:1fr}
}
</style>
</head>
<body>
<div class="app-shell">
""" + sidebar_html + """
<main class="shell">
  <section class="hero">
    <div class="hero-card">
      <div class="eyebrow">Knowledge Atlas</div>
      <h1>知識構造を俯瞰し、次に読むべき概念を決める</h1>
      <p>
        この atlas は、concept を列挙するためではなく、接続の密度と coverage gap から「次に読むべき概念」を決めるための dashboard です。
        resolved graph を主面に置き、未解決参照は監査信号としてだけ扱います。
      </p>
    </div>
    <div class="metric-grid">
      <div class="metric"><div class="value">""" + str(summary["resolved_nodes"]) + """</div><div class="label">Resolved Concepts</div><div class="note">実記事を持つ concept node</div></div>
      <div class="metric"><div class="value">""" + str(summary["resolved_edges"]) + """</div><div class="label">Resolved Edges</div><div class="note">resolved concept 間の接続</div></div>
      <div class="metric"><div class="value">""" + str(summary["unresolved_nodes"]) + """</div><div class="label">Unresolved Refs</div><div class="note">まだ受け皿記事のない参照</div></div>
      <div class="metric"><div class="value">""" + str(summary["isolated_concepts"]) + """</div><div class="label">Isolated Concepts</div><div class="note">グラフ上で孤立している concept</div></div>
      <div class="metric"><div class="value">""" + str(summary["invalid_source_refs"]) + """</div><div class="label">Invalid Source Refs</div><div class="note">source path が壊れている記述</div></div>
      <div class="metric"><div class="value">""" + str(summary["link_mentions"]) + """</div><div class="label">Link Mentions</div><div class="note">全 wikilink 出現数</div></div>
    </div>
  </section>

  <section class="layout">
    <aside class="panel control-panel">
      <div class="section">
        <div class="panel-kicker">Control Tower</div>
        <h2>Focus the field</h2>
        <p class="panel-copy">
          検索、lens、priority queue だけで atlas の対象を切り替えます。
        </p>
      </div>
      <div class="section">
        <h3>Lens</h3>
        <label class="label" for="search">Search</label>
        <input id="search" class="input" placeholder="概念名 / slug / description">
        <div style="height:12px"></div>
        <label class="label">Tier</label>
        <div class="chips" id="tier-chips"></div>
        <div style="height:12px"></div>
        <label class="label" for="domain-filter">Domain</label>
        <select id="domain-filter" class="select"></select>
        <div style="height:12px"></div>
        <label class="label" for="degree-filter">Minimum Degree</label>
        <div class="range-wrap">
          <input id="degree-filter" type="range" min="0" max="20" value="0">
          <span id="degree-value" class="small">0+</span>
        </div>
      </div>
      <div class="section">
        <h3>Mode</h3>
        <div class="toggle"><span>Show isolated concepts</span><input id="show-isolated" type="checkbox" checked></div>
        <div style="height:10px"></div>
        <div class="toggle"><span>Show unresolved halo</span><input id="show-unresolved" type="checkbox" checked></div>
        <div style="height:10px"></div>
        <div class="toggle"><span>Neighborhood mode</span><input id="focus-mode" type="checkbox"></div>
      </div>
      <div class="section">
        <h3>Guided Paths</h3>
        <div class="list">
          <button id="focus-hubs"><strong>Top hubs</strong><span>接続密度の高い中心概念へ寄る</span></button>
          <button id="focus-islands"><strong>Isolated concepts</strong><span>孤立 concept の棚卸しを始める</span></button>
          <button id="focus-gaps"><strong>Gap-rich nodes</strong><span>未解決参照が集まる起点を拾う</span></button>
        </div>
      </div>
      <div class="section">
        <h3>Priority Nodes</h3>
        <div id="hub-list" class="list"></div>
      </div>
      <div class="section">
        <h3>Gap Watchlist</h3>
        <div id="gap-list" class="list"></div>
      </div>
    </aside>

    <div class="analysis-column">
      <div class="stage-shell">
        <div class="stage-header">
          <div class="stage-kicker">Workspace Canvas</div>
          <div class="stage-header-top">
            <div class="stage-title">
              <h2>Knowledge Field</h2>
              <p>resolved graph を主面に据え、hub・cluster・gap の3種類の判断を一画面で行うための field です。未解決参照は halo と Inspector にだけ残し、主面の可読性を守ります。</p>
            </div>
            <div class="stage-toolbar">
              <span class="stage-chip primary">Atlas-first</span>
              <span class="stage-chip">Gap-aware</span>
              <span class="stage-chip">Reader-ready</span>
            </div>
          </div>
          <div class="stage-meta-row">
            <div class="legend">
              <div class="legend-item"><span class="dot" style="background:var(--accent-rust)"></span>Tier 1</div>
              <div class="legend-item"><span class="dot" style="background:var(--accent-teal)"></span>Tier 2</div>
              <div class="legend-item"><span class="dot" style="background:var(--accent-blue)"></span>Tier 3</div>
              <div class="legend-item"><span class="dot" style="background:var(--accent-slate)"></span>Legacy / Untiered</div>
              <div class="legend-item"><span class="dot" style="background:var(--accent-amber)"></span>Unresolved halo</div>
            </div>
            <div class="stage-meta-card">
              <strong>Decision rule</strong>
              <span>まず cluster と hub を掴み、そのあと concept を選び、最後に Inspector から Reader へ渡します。</span>
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
              <span class="stage-mode-label">Knowledge canvas</span>
              <span class="stage-chrome-note">resolved concepts in primary plane</span>
            </div>
            <div class="stage-chrome-right">
              <span class="stage-chip ghost" id="chrome-scope">All tiers · All domains · Degree 0+</span>
              <span class="stage-chip ghost" id="chrome-selection">Selection: atlas overview</span>
            </div>
          </div>
          <div class="stage-canvas-shell" id="stage-canvas-shell">
            <canvas id="graph"></canvas>
          </div>
          <div class="stage-briefs">
            <div class="stage-brief-card primary">
              <span class="stage-brief-label">Current lens</span>
              <strong id="overlay-title">Atlas overview</strong>
              <span id="overlay-text">全 resolved concept を表示しています。ノードを選ぶと、その周辺関係と未解決参照が Inspector に出ます。</span>
            </div>
            <div class="stage-brief-card">
              <span class="stage-brief-label">Field state</span>
              <strong id="overlay-stats">0 nodes / 0 edges</strong>
              <span id="overlay-mode">Pan: drag, Zoom: wheel, Focus: click a node</span>
            </div>
          </div>
        </div>
      </div>

      <aside class="panel inspector-panel" id="inspector"></aside>
    </div>
  </section>
</main>
</div>

<script>
const GRAPH = """ + graph_json + """;
const resolvedNodes = GRAPH.nodes.filter(node => node.resolved);
const resolvedNodeMap = Object.fromEntries(resolvedNodes.map(node => [node.id, node]));
const resolvedEdges = GRAPH.edges.filter(edge => edge.resolved && resolvedNodeMap[edge.source] && resolvedNodeMap[edge.target]);
const unresolvedBySource = {};
const unresolvedGroupMap = {};
(GRAPH.unresolved_mentions || []).forEach(item => {
  if (!unresolvedBySource[item.source_slug]) unresolvedBySource[item.source_slug] = [];
  unresolvedBySource[item.source_slug].push(item);
  const key = item.raw_target || item.label || item.target;
  if (!key) return;
  if (!unresolvedGroupMap[key]){
    unresolvedGroupMap[key] = {
      raw_target: key,
      count: 0,
      sourceIds: new Set(),
      sourceTitles: new Set(),
    };
  }
  unresolvedGroupMap[key].count += 1;
  if (item.source_slug) unresolvedGroupMap[key].sourceIds.add(item.source_slug);
  if (item.source_title && unresolvedGroupMap[key].sourceTitles.size < 3){
    unresolvedGroupMap[key].sourceTitles.add(item.source_title);
  }
});
const unresolvedGroups = Object.values(unresolvedGroupMap).map(group => ({
  raw_target: group.raw_target,
  count: group.count,
  sourceIds: Array.from(group.sourceIds),
  sourceTitles: Array.from(group.sourceTitles),
})).sort((a, b) => b.count - a.count || a.raw_target.localeCompare(b.raw_target, 'ja'));

const domains = Array.from(new Set(resolvedNodes.flatMap(node => node.related_domains || []).filter(Boolean))).sort();
const adjacency = {};
resolvedNodes.forEach(node => adjacency[node.id] = new Set());
resolvedEdges.forEach(edge => {
  adjacency[edge.source].add(edge.target);
  adjacency[edge.target].add(edge.source);
});

const stageCanvasShell = document.getElementById('stage-canvas-shell');
const canvas = document.getElementById('graph');
const ctx = canvas.getContext('2d');
const overlayTitle = document.getElementById('overlay-title');
const overlayText = document.getElementById('overlay-text');
const overlayStats = document.getElementById('overlay-stats');
const overlayMode = document.getElementById('overlay-mode');
const chromeScope = document.getElementById('chrome-scope');
const chromeSelection = document.getElementById('chrome-selection');
let resizeFrame = null;

const state = {
  query: '',
  tier: 'all',
  domain: 'all',
  degreeMin: 0,
  showIsolated: true,
  showUnresolved: true,
  focusMode: false,
  selected: null,
  hovered: null,
  scale: 1,
  offsetX: 0,
  offsetY: 0,
  dragging: false,
  dragStartX: 0,
  dragStartY: 0,
  dragOffsetX: 0,
  dragOffsetY: 0,
  viewportSignature: '',
};

const colorByTier = {
  1: {inner: '#f0c7b0', outer: '#d5966b', glow: 'rgba(217,160,125,.28)'},
  2: {inner: '#b8eee7', outer: '#6dbfb5', glow: 'rgba(121,210,197,.24)'},
  3: {inner: '#bfd4fb', outer: '#7da5e8', glow: 'rgba(130,174,245,.26)'},
  legacy: {inner: '#c2cee0', outer: '#8fa0bc', glow: 'rgba(146,164,191,.24)'},
};

function viewportWidth(){
  return stageCanvasShell.clientWidth;
}

function viewportHeight(){
  return stageCanvasShell.clientHeight;
}

function viewportSignature(){
  return viewportWidth() + 'x' + viewportHeight();
}

function tierKey(node){
  if (node.tier === 1 || node.tier === 2 || node.tier === 3) return String(node.tier);
  return 'legacy';
}

function tierLabel(node){
  if (node.tier === 1) return 'Tier 1';
  if (node.tier === 2) return 'Tier 2';
  if (node.tier === 3) return 'Tier 3';
  return 'Legacy';
}

function paletteFor(node){
  return colorByTier[tierKey(node)] || colorByTier.legacy;
}

function unresolvedCount(node){
  return (unresolvedBySource[node.id] || []).length;
}

function radiusFor(node){
  return 5 + Math.min(16, Math.sqrt(node.degree || 0) * 1.5);
}

function normalize(text){
  return String(text || '').toLowerCase();
}

function compactText(text, max = 28){
  const value = String(text || '');
  if (value.length <= max) return value;
  return value.slice(0, max - 1) + '…';
}

function activeLensSummary(){
  const parts = [];
  parts.push(state.tier === 'all' ? 'All tiers' : 'Tier ' + state.tier);
  parts.push(state.domain === 'all' ? 'All domains' : state.domain);
  parts.push('Degree ' + state.degreeMin + '+');
  if (!state.showIsolated) parts.push('No islands');
  if (!state.showUnresolved) parts.push('Halo off');
  return parts.join(' · ');
}

function inspectorAssessment(node){
  const degree = node.degree || 0;
  const gaps = unresolvedCount(node);
  if (degree >= 18 && gaps >= 4){
    return '高接続の hub でありながら gap も多い concept です。構造理解の入口にも、coverage 改善の起点にもなります。';
  }
  if (degree >= 18){
    return '高接続の hub concept です。この周辺を読むと cluster 全体の文脈を短時間で掴みやすくなります。';
  }
  if (gaps >= 5){
    return 'gap が集中している concept です。既存 wiki の周辺文脈を確認しながら、次の執筆候補を判断するのに向いています。';
  }
  if (degree === 0){
    return '孤立している concept です。taxonomy 上の位置づけや関連リンク不足を点検する価値があります。';
  }
  if ((node.inbound_count || 0) > (node.outbound_count || 0)){
    return '他概念から参照されやすい anchor concept です。Reader に渡すと周辺理解の起点として機能します。';
  }
  return '周辺概念への橋渡しに向いた node です。近傍モードで local field を読むと移動先を決めやすくなります。';
}

function componentMap(){
  const visited = new Set();
  const byNode = {};
  let componentIndex = 0;
  resolvedNodes.forEach(node => {
    if (visited.has(node.id)) return;
    componentIndex += 1;
    const stack = [node.id];
    visited.add(node.id);
    while (stack.length){
      const current = stack.pop();
      byNode[current] = componentIndex;
      (adjacency[current] || []).forEach(next => {
        if (!visited.has(next)){
          visited.add(next);
          stack.push(next);
        }
      });
    }
  });
  return byNode;
}

const components = componentMap();

function initializeLayout(){
  const width = viewportWidth();
  const height = viewportHeight();
  const componentIds = Array.from(new Set(Object.values(components))).sort((a,b) => a-b);
  const centers = {};
  const centerRadius = Math.min(width, height) * 0.28;
  componentIds.forEach((id, index) => {
    const angle = (Math.PI * 2 * index) / Math.max(componentIds.length, 1) - Math.PI / 2;
    centers[id] = {
      x: width / 2 + Math.cos(angle) * centerRadius,
      y: height / 2 + Math.sin(angle) * centerRadius,
    };
  });

  resolvedNodes.forEach((node, index) => {
    const center = centers[components[node.id]] || {x: width / 2, y: height / 2};
    const angle = (index * 0.61803398875 % 1) * Math.PI * 2;
    const spread = 40 + (node.degree || 0) * 6;
    node.x = center.x + Math.cos(angle) * spread;
    node.y = center.y + Math.sin(angle) * spread;
    node.vx = 0;
    node.vy = 0;
    node.cx = center.x;
    node.cy = center.y;
  });
}

function simulate(iterations = 180){
  const repulsion = 2800;
  const spring = 0.015;
  const damping = 0.87;
  const centering = 0.0025;
  const nodes = resolvedNodes;
  const edges = resolvedEdges;

  for (let step = 0; step < iterations; step += 1){
    for (let i = 0; i < nodes.length; i += 1){
      const a = nodes[i];
      for (let j = i + 1; j < nodes.length; j += 1){
        const b = nodes[j];
        let dx = a.x - b.x;
        let dy = a.y - b.y;
        let dist2 = dx * dx + dy * dy + 0.1;
        let force = repulsion / dist2;
        let dist = Math.sqrt(dist2);
        dx /= dist;
        dy /= dist;
        a.vx += dx * force;
        a.vy += dy * force;
        b.vx -= dx * force;
        b.vy -= dy * force;
      }
    }

    edges.forEach(edge => {
      const a = resolvedNodeMap[edge.source];
      const b = resolvedNodeMap[edge.target];
      let dx = b.x - a.x;
      let dy = b.y - a.y;
      const dist = Math.sqrt(dx * dx + dy * dy) + 0.1;
      const target = 120 + (radiusFor(a) + radiusFor(b)) * 2.2;
      const force = (dist - target) * spring * edge.weight;
      dx /= dist;
      dy /= dist;
      a.vx += dx * force;
      a.vy += dy * force;
      b.vx -= dx * force;
      b.vy -= dy * force;
    });

    nodes.forEach(node => {
      node.vx += (node.cx - node.x) * centering;
      node.vy += (node.cy - node.y) * centering;
      node.vx *= damping;
      node.vy *= damping;
      node.x += node.vx;
      node.y += node.vy;
    });
  }
}

function resizeCanvas(){
  const ratio = window.devicePixelRatio || 1;
  canvas.width = viewportWidth() * ratio;
  canvas.height = viewportHeight() * ratio;
  canvas.style.width = viewportWidth() + 'px';
  canvas.style.height = viewportHeight() + 'px';
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
}

function relayout(force = false){
  const width = viewportWidth();
  const height = viewportHeight();
  if (!width || !height) return;

  const signature = viewportSignature();
  if (!force && signature === state.viewportSignature){
    return;
  }

  state.viewportSignature = signature;
  resizeCanvas();
  initializeLayout();
  simulate(force ? 180 : 120);

  if (state.selected && resolvedNodeMap[state.selected]){
    centerOnNode(resolvedNodeMap[state.selected]);
    return;
  }

  state.offsetX = viewportWidth() * 0.08;
  state.offsetY = viewportHeight() * 0.06;
  update();
}

function getFilteredNodes(){
  const query = normalize(state.query);
  return resolvedNodes.filter(node => {
    if (state.tier !== 'all' && tierKey(node) !== state.tier) return false;
    if (state.domain !== 'all' && !(node.related_domains || []).includes(state.domain)) return false;
    if ((node.degree || 0) < state.degreeMin) return false;
    if (!state.showIsolated && (node.degree || 0) === 0) return false;
    if (query){
      const haystack = [node.label, node.slug, node.description, ...(node.aliases || [])].join(' ');
      if (!normalize(haystack).includes(query)) return false;
    }
    return true;
  });
}

function neighborhoodIds(centerId, depth = 1){
  const seen = new Set([centerId]);
  let frontier = [centerId];
  for (let step = 0; step < depth; step += 1){
    const next = [];
    frontier.forEach(id => {
      (adjacency[id] || []).forEach(target => {
        if (!seen.has(target)){
          seen.add(target);
          next.push(target);
        }
      });
    });
    frontier = next;
  }
  return seen;
}

function currentGraph(){
  let nodes = getFilteredNodes();
  if (state.focusMode && state.selected){
    const scope = neighborhoodIds(state.selected, 1);
    nodes = nodes.filter(node => scope.has(node.id));
  }
  const allowed = new Set(nodes.map(node => node.id));
  const edges = resolvedEdges.filter(edge => allowed.has(edge.source) && allowed.has(edge.target));
  return {nodes, edges, allowed};
}

function worldToScreen(x, y){
  return {
    x: x * state.scale + state.offsetX,
    y: y * state.scale + state.offsetY,
  };
}

function screenToWorld(x, y){
  return {
    x: (x - state.offsetX) / state.scale,
    y: (y - state.offsetY) / state.scale,
  };
}

function drawBackground(){
  ctx.clearRect(0, 0, viewportWidth(), viewportHeight());
  ctx.save();
  const wash = ctx.createLinearGradient(0, 0, 0, viewportHeight());
  wash.addColorStop(0, 'rgba(11,17,30,0.94)');
  wash.addColorStop(1, 'rgba(7,11,20,0.98)');
  ctx.fillStyle = wash;
  ctx.fillRect(0, 0, viewportWidth(), viewportHeight());

  const glowA = ctx.createRadialGradient(viewportWidth() * 0.18, viewportHeight() * 0.16, 0, viewportWidth() * 0.18, viewportHeight() * 0.16, viewportWidth() * 0.3);
  glowA.addColorStop(0, 'rgba(130,174,245,0.12)');
  glowA.addColorStop(1, 'rgba(130,174,245,0)');
  ctx.fillStyle = glowA;
  ctx.fillRect(0, 0, viewportWidth(), viewportHeight());

  const glowB = ctx.createRadialGradient(viewportWidth() * 0.76, viewportHeight() * 0.2, 0, viewportWidth() * 0.76, viewportHeight() * 0.2, viewportWidth() * 0.34);
  glowB.addColorStop(0, 'rgba(217,160,125,0.1)');
  glowB.addColorStop(1, 'rgba(217,160,125,0)');
  ctx.fillStyle = glowB;
  ctx.fillRect(0, 0, viewportWidth(), viewportHeight());

  ctx.strokeStyle = 'rgba(151,170,204,.055)';
  ctx.lineWidth = 1;
  for (let x = 0; x < viewportWidth(); x += 36){
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, viewportHeight());
    ctx.stroke();
  }
  for (let y = 0; y < viewportHeight(); y += 36){
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(viewportWidth(), y);
    ctx.stroke();
  }
  ctx.strokeStyle = 'rgba(151,170,204,.1)';
  for (let x = 0; x < viewportWidth(); x += 144){
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, viewportHeight());
    ctx.stroke();
  }
  for (let y = 0; y < viewportHeight(); y += 144){
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(viewportWidth(), y);
    ctx.stroke();
  }
  ctx.restore();
}

function drawGraph(){
  drawBackground();
  const graph = currentGraph();
  overlayStats.textContent = graph.nodes.length + ' nodes / ' + graph.edges.length + ' edges';

  ctx.save();
  graph.edges.forEach(edge => {
    const a = resolvedNodeMap[edge.source];
    const b = resolvedNodeMap[edge.target];
    const p1 = worldToScreen(a.x, a.y);
    const p2 = worldToScreen(b.x, b.y);
    const alpha = state.selected && (edge.source === state.selected || edge.target === state.selected) ? .34 : .12;
    ctx.strokeStyle = 'rgba(151,170,204,' + alpha + ')';
    ctx.lineWidth = 1 + Math.min(2.5, edge.weight * .35);
    ctx.beginPath();
    ctx.moveTo(p1.x, p1.y);
    ctx.lineTo(p2.x, p2.y);
    ctx.stroke();
  });

  graph.nodes.forEach(node => {
    const p = worldToScreen(node.x, node.y);
    const radius = radiusFor(node) * state.scale;
    const isSelected = node.id === state.selected;
    const isHovered = node.id === state.hovered;
    const unresolved = unresolvedCount(node);
    const palette = paletteFor(node);

    if (state.showUnresolved && unresolved && (isSelected || isHovered)){
      const halo = radius + 14;
      const count = Math.min(unresolved, 18);
      for (let i = 0; i < count; i += 1){
        const angle = (Math.PI * 2 * i) / count;
        const hx = p.x + Math.cos(angle) * halo;
        const hy = p.y + Math.sin(angle) * halo;
        ctx.fillStyle = 'rgba(241,187,116,.72)';
        ctx.beginPath();
        ctx.arc(hx, hy, 2.2, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    const fill = ctx.createRadialGradient(
      p.x - radius * 0.42,
      p.y - radius * 0.5,
      Math.max(1, radius * 0.12),
      p.x,
      p.y,
      Math.max(2, radius * 1.05)
    );
    fill.addColorStop(0, palette.inner);
    fill.addColorStop(0.48, palette.inner);
    fill.addColorStop(1, palette.outer);
    ctx.shadowColor = isSelected ? palette.glow : (isHovered ? palette.glow : 'rgba(2,6,23,0)');
    ctx.shadowBlur = isSelected ? 18 : (isHovered ? 12 : 8);
    ctx.fillStyle = fill;
    ctx.beginPath();
    ctx.arc(p.x, p.y, radius, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    ctx.lineWidth = isSelected ? 2.6 : (isHovered ? 1.8 : 1.1);
    ctx.strokeStyle = isSelected ? 'rgba(237,243,255,.92)' : 'rgba(237,243,255,.16)';
    ctx.stroke();

    const shouldLabel = isSelected || isHovered || radius > 10 || (node.degree || 0) > 18 || (state.query && normalize(node.label).includes(normalize(state.query)));
    if (shouldLabel){
      ctx.fillStyle = '#edf3ff';
      ctx.font = '12px "Avenir Next", "Segoe UI", sans-serif';
      ctx.textAlign = 'center';
      ctx.shadowColor = 'rgba(7,11,20,.88)';
      ctx.shadowBlur = 6;
      ctx.fillText(node.label, p.x, p.y - radius - 8);
      ctx.shadowBlur = 0;
    }
  });
  ctx.restore();
}

function pickNode(clientX, clientY){
  const rect = canvas.getBoundingClientRect();
  const x = clientX - rect.left;
  const y = clientY - rect.top;
  let best = null;
  let bestDist = Infinity;
  currentGraph().nodes.forEach(node => {
    const p = worldToScreen(node.x, node.y);
    const dist = Math.hypot(p.x - x, p.y - y);
    if (dist < radiusFor(node) * state.scale + 8 && dist < bestDist){
      best = node;
      bestDist = dist;
    }
  });
  return best;
}

function detailPill(text){
  return '<span class="pill">' + text + '</span>';
}

function renderList(items, emptyText, formatter){
  if (!items || !items.length){
    return '<div class="empty">' + emptyText + '</div>';
  }
  return '<div class="text-list">' + items.map(formatter).join('') + '</div>';
}

function sourceButtons(items, title, limit = 5){
  if (!items.length) return '<div class="empty">' + title + ' はありません。</div>';
  const visible = items.slice(0, limit);
  const more = items.length > visible.length
    ? '<div class="section-note">+' + (items.length - visible.length) + ' more concept(s)</div>'
    : '';
  return '<div class="list">' + visible.map(item => {
    return '<button class="link-btn" data-slug="' + item.id + '"><strong>' + item.label + '</strong><span>' + (item.weight || 1) + ' connection(s)</span></button>';
  }).join('') + '</div>' + more;
}

function bestNodeForGap(group){
  return group.sourceIds
    .map(id => resolvedNodeMap[id])
    .filter(Boolean)
    .sort((a, b) => (unresolvedCount(b) - unresolvedCount(a)) || ((b.degree || 0) - (a.degree || 0)))[0] || null;
}

function renderInspector(){
  const container = document.getElementById('inspector');
  const node = resolvedNodeMap[state.selected] || resolvedNodes.slice().sort((a,b) => (b.degree || 0) - (a.degree || 0))[0];
  if (!state.selected) state.selected = node.id;

  const inbound = resolvedEdges
    .filter(edge => edge.target === node.id)
    .map(edge => ({id: edge.source, label: resolvedNodeMap[edge.source].label, weight: edge.weight}))
    .sort((a, b) => b.weight - a.weight || a.label.localeCompare(b.label, 'ja'));
  const outbound = resolvedEdges
    .filter(edge => edge.source === node.id)
    .map(edge => ({id: edge.target, label: resolvedNodeMap[edge.target].label, weight: edge.weight}))
    .sort((a, b) => b.weight - a.weight || a.label.localeCompare(b.label, 'ja'));
  const unresolved = (unresolvedBySource[node.id] || []).slice().sort((a,b) => a.raw_target.localeCompare(b.raw_target, 'ja'));
  const domainsHtml = (node.related_domains || []).map(domain => detailPill(domain)).join('');
  const sourceHtml = (node.key_sources || []).slice(0, 2).map(src => '<div class="text-item"><strong>' + src + '</strong><small>key source</small></div>').join('');

  container.innerHTML = ''
    + '<div class="section">'
    + '<div class="inspector-head">'
      + '<div class="inspector-head-copy">'
        + '<div class="eyebrow">Inspector</div>'
        + '<h2>' + node.label + '</h2>'
      + '</div>'
      + '<a class="ghost-link primary" href="../reader.html#' + encodeURIComponent(node.id) + '">Open in reader</a>'
    + '</div>'
    + '<p class="inspector-description">' + (node.description || 'この concept には description がまだ付いていません。') + '</p>'
    + '<div class="inspector-lead">' + inspectorAssessment(node) + '</div>'
    + '<div class="pill-row">'
      + detailPill(tierLabel(node))
      + detailPill(node.metadata_source || 'article')
      + detailPill('degree ' + (node.degree || 0))
      + detailPill('in ' + (node.inbound_count || 0))
      + detailPill('out ' + (node.outbound_count || 0))
      + detailPill('unresolved ' + unresolved.length)
    + '</div>'
    + '<div class="metric-strip">'
      + '<div class="mini"><div class="v">' + (node.degree || 0) + '</div><div class="k">Degree</div></div>'
      + '<div class="mini"><div class="v">' + (node.inbound_count || 0) + '</div><div class="k">Backlinks</div></div>'
      + '<div class="mini"><div class="v">' + (node.outbound_count || 0) + '</div><div class="k">Outbound</div></div>'
      + '<div class="mini"><div class="v">' + unresolved.length + '</div><div class="k">Gaps</div></div>'
    + '</div>'
    + '<div class="dock">'
      + '<button class="ghost-btn" id="center-selected">Center in atlas</button>'
      + '<button class="ghost-btn" id="toggle-focus">' + (state.focusMode ? 'Exit neighborhood' : 'Neighborhood mode') + '</button>'
    + '</div>'
    + '</div>'
    + '<div class="section">'
      + '<div class="inspector-grid">'
        + '<div class="inspector-card">'
          + '<div class="inspector-card-head"><h3>Context</h3><span>Domains と key sources から、この concept の置き場所を短く確認します。</span></div>'
          + (domainsHtml || '<div class="empty">related_domains はまだありません。</div>')
          + (sourceHtml ? '<div style="height:12px"></div>' + sourceHtml : '<div class="section-note">key_sources はまだありません。</div>')
        + '</div>'
        + '<div class="inspector-card">'
          + '<div class="inspector-card-head"><h3>Connections</h3><span>移動先候補として有効な outbound と backlinks の上位だけを出します。</span></div>'
          + '<div class="inspector-connection-grid">'
            + '<div class="inspector-subsection"><span class="inspector-subsection-label">Outbound</span>' + sourceButtons(outbound, 'outbound concepts', 2) + '</div>'
            + '<div class="inspector-subsection"><span class="inspector-subsection-label">Backlinks</span>' + sourceButtons(inbound, 'backlinks', 2) + '</div>'
          + '</div>'
        + '</div>'
        + '<div class="inspector-card">'
          + '<div class="inspector-card-head"><h3>Gap Audit</h3><span>未解決参照の上位だけを表示し、coverage 改善の入口を見せます。</span></div>'
          + renderList(unresolved.slice(0, 2), '未解決参照はありません。', item => (
            '<div class="text-item"><strong>' + item.raw_target + '</strong>'
            + '<span>' + item.section + ' / line ' + item.line + '</span>'
            + (item.candidates && item.candidates.length ? '<small>candidates: ' + item.candidates.slice(0,5).join(', ') + '</small>' : '')
            + '</div>'
          ))
          + (unresolved.length > 2 ? '<div class="section-note">+' + (unresolved.length - 2) + ' more unresolved reference(s)</div>' : '')
        + '</div>'
      + '</div>'
    + '</div>';

  document.getElementById('center-selected').onclick = () => centerOnNode(node);
  document.getElementById('toggle-focus').onclick = () => {
    state.focusMode = !state.focusMode;
    document.getElementById('focus-mode').checked = state.focusMode;
    update();
  };
  container.querySelectorAll('[data-slug]').forEach(button => {
    button.addEventListener('click', () => {
      state.selected = button.dataset.slug;
      syncHash();
      update();
    });
  });
}

function centerOnNode(node){
  const targetX = viewportWidth() / 2 - node.x * state.scale;
  const targetY = viewportHeight() / 2 - node.y * state.scale;
  state.offsetX = targetX;
  state.offsetY = targetY;
  update();
}

function syncHash(){
  if (state.selected){
    history.replaceState(null, '', '#node=' + encodeURIComponent(state.selected));
  }
}

function restoreHash(){
  const hash = location.hash.replace(/^#/, '');
  if (!hash.startsWith('node=')) return;
  const slug = decodeURIComponent(hash.slice(5));
  if (resolvedNodeMap[slug]) state.selected = slug;
}

function updateHubList(){
  const hubs = resolvedNodes.slice().sort((a,b) => ((b.degree || 0) - (a.degree || 0)) || (unresolvedCount(b) - unresolvedCount(a))).slice(0, 5);
  document.getElementById('hub-list').innerHTML = hubs.map(node => (
    '<button data-slug="' + node.id + '"><strong>' + node.label + '</strong><span>degree ' + (node.degree || 0) + ' / unresolved ' + unresolvedCount(node) + '</span></button>'
  )).join('');
  document.querySelectorAll('#hub-list [data-slug]').forEach(button => {
    button.addEventListener('click', () => {
      state.selected = button.dataset.slug;
      syncHash();
      update();
    });
  });
}

function updateGapList(){
  const gaps = unresolvedGroups.slice(0, 5);
  document.getElementById('gap-list').innerHTML = gaps.map((group, index) => (
    '<button data-gap-index="' + index + '"><strong>' + group.raw_target + '</strong><span>' + group.count + ' mentions / ' + group.sourceIds.length + ' concepts</span></button>'
  )).join('');
  document.querySelectorAll('#gap-list [data-gap-index]').forEach(button => {
    button.addEventListener('click', () => {
      const group = gaps[Number(button.dataset.gapIndex)];
      const target = bestNodeForGap(group);
      if (!target) return;
      state.selected = target.id;
      state.focusMode = true;
      document.getElementById('focus-mode').checked = true;
      syncHash();
      centerOnNode(target);
    });
  });
}

function update(){
  const graph = currentGraph();
  drawGraph();
  renderInspector();

  const selected = resolvedNodeMap[state.selected];
  overlayTitle.textContent = state.focusMode ? 'Neighborhood lens' : 'Atlas overview';
  overlayText.textContent = selected
    ? selected.label + ' を中心に、resolved link と unresolved halo を同時に表示しています。'
    : '全 resolved concept を表示しています。';
  const modeText = state.focusMode
    ? 'Focused neighborhood active. Selected concept を起点に 1-hop の関係だけを残しています。'
    : 'Pan: drag, Zoom: wheel, Focus: click a node';
  overlayMode.textContent = modeText;
  chromeScope.textContent = activeLensSummary();
  chromeSelection.textContent = selected
    ? (state.focusMode ? '1-hop around ' + compactText(selected.label, 24) : 'Selection: ' + compactText(selected.label, 24))
    : 'Selection: atlas overview';
}

function wireControls(){
  const tierChips = document.getElementById('tier-chips');
  const tiers = [
    ['all', 'All', 'legacy'],
    ['1', 'Tier 1', 'tier1'],
    ['2', 'Tier 2', 'tier2'],
    ['3', 'Tier 3', 'tier3'],
    ['legacy', 'Legacy', 'legacy'],
  ];
  tierChips.innerHTML = tiers.map(([value, label, kind]) => (
    '<button class="chip' + (value === 'all' ? ' active' : '') + '" data-tier="' + value + '" data-kind="' + kind + '">' + label + '</button>'
  )).join('');
  tierChips.querySelectorAll('[data-tier]').forEach(button => {
    button.addEventListener('click', () => {
      state.tier = button.dataset.tier;
      tierChips.querySelectorAll('[data-tier]').forEach(node => node.classList.toggle('active', node === button));
      update();
    });
  });

  const domainFilter = document.getElementById('domain-filter');
  domainFilter.innerHTML = '<option value="all">All domains</option>' + domains.map(domain => '<option value="' + domain + '">' + domain + '</option>').join('');
  domainFilter.addEventListener('change', event => {
    state.domain = event.target.value;
    update();
  });

  document.getElementById('search').addEventListener('input', event => {
    state.query = event.target.value;
    update();
  });

  const degreeFilter = document.getElementById('degree-filter');
  const degreeValue = document.getElementById('degree-value');
  degreeFilter.addEventListener('input', event => {
    state.degreeMin = Number(event.target.value);
    degreeValue.textContent = state.degreeMin + '+';
    update();
  });

  document.getElementById('show-isolated').addEventListener('change', event => {
    state.showIsolated = event.target.checked;
    update();
  });
  document.getElementById('show-unresolved').addEventListener('change', event => {
    state.showUnresolved = event.target.checked;
    update();
  });
  document.getElementById('focus-mode').addEventListener('change', event => {
    state.focusMode = event.target.checked;
    update();
  });

  document.getElementById('focus-hubs').addEventListener('click', () => {
    state.query = '';
    document.getElementById('search').value = '';
    state.degreeMin = 10;
    degreeFilter.value = 10;
    degreeValue.textContent = '10+';
    state.showIsolated = false;
    document.getElementById('show-isolated').checked = false;
    const target = resolvedNodes.slice().sort((a,b) => (b.degree || 0) - (a.degree || 0))[0];
    if (target) state.selected = target.id;
    update();
  });

  document.getElementById('focus-islands').addEventListener('click', () => {
    state.query = '';
    document.getElementById('search').value = '';
    state.degreeMin = 0;
    degreeFilter.value = 0;
    degreeValue.textContent = '0+';
    state.showIsolated = true;
    document.getElementById('show-isolated').checked = true;
    state.focusMode = false;
    document.getElementById('focus-mode').checked = false;
    const isolated = resolvedNodes.find(node => (node.degree || 0) === 0);
    if (isolated) state.selected = isolated.id;
    update();
  });

  document.getElementById('focus-gaps').addEventListener('click', () => {
    const target = resolvedNodes.slice().sort((a,b) => unresolvedCount(b) - unresolvedCount(a))[0];
    if (target) state.selected = target.id;
    state.focusMode = true;
    document.getElementById('focus-mode').checked = true;
    update();
  });
}

function wireCanvas(){
  canvas.addEventListener('mousemove', event => {
    const node = pickNode(event.clientX, event.clientY);
    state.hovered = node ? node.id : null;
    drawGraph();
  });

  canvas.addEventListener('mouseleave', () => {
    state.hovered = null;
    drawGraph();
  });

  canvas.addEventListener('mousedown', event => {
    const node = pickNode(event.clientX, event.clientY);
    if (node){
      state.selected = node.id;
      syncHash();
      update();
      return;
    }
    state.dragging = true;
    state.dragStartX = event.clientX;
    state.dragStartY = event.clientY;
    state.dragOffsetX = state.offsetX;
    state.dragOffsetY = state.offsetY;
  });

  window.addEventListener('mousemove', event => {
    if (!state.dragging) return;
    state.offsetX = state.dragOffsetX + (event.clientX - state.dragStartX);
    state.offsetY = state.dragOffsetY + (event.clientY - state.dragStartY);
    drawGraph();
  });
  window.addEventListener('mouseup', () => state.dragging = false);

  canvas.addEventListener('wheel', event => {
    event.preventDefault();
    const rect = canvas.getBoundingClientRect();
    const mx = event.clientX - rect.left;
    const my = event.clientY - rect.top;
    const world = screenToWorld(mx, my);
    const factor = event.deltaY > 0 ? 0.92 : 1.08;
    state.scale = Math.max(0.45, Math.min(2.8, state.scale * factor));
    state.offsetX = mx - world.x * state.scale;
    state.offsetY = my - world.y * state.scale;
    drawGraph();
  }, {passive:false});
}

function boot(){
  restoreHash();
  if (!state.selected){
    state.selected = resolvedNodes.slice().sort((a,b) => (b.degree || 0) - (a.degree || 0))[0].id;
  }
  wireControls();
  wireCanvas();
  updateHubList();
  updateGapList();
  if ('ResizeObserver' in window){
    const observer = new ResizeObserver(() => {
      if (resizeFrame){
        cancelAnimationFrame(resizeFrame);
      }
      resizeFrame = requestAnimationFrame(() => {
        resizeFrame = null;
        relayout();
      });
    });
    observer.observe(stageCanvasShell);
  }
  relayout(true);
}

window.addEventListener('resize', () => {
  relayout(true);
});

boot();
</script>
</body>
</html>"""


def build_graph_ui():
    graph = load_graph()
    html = render_html(graph)
    os.makedirs(GRAPH_DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(html)
    with open(LEGACY_OUT, "w", encoding="utf-8") as handle:
        handle.write(
            "<!DOCTYPE html><html><head>"
            '<meta charset="utf-8"><meta http-equiv="refresh" content="0; url=graph/index.html">'
            "<title>Research Atlas</title></head>"
            '<body><p><a href="graph/index.html">Research Atlas</a></p></body></html>'
        )
    return {
        "path": OUT,
        "legacy_path": LEGACY_OUT,
        "size": os.path.getsize(OUT),
    }


def main():
    result = build_graph_ui()
    print(f"Generated: {result['size']} bytes")
    print(f"Path: {result['path']}")
    print(f"Legacy redirect: {result['legacy_path']}")


if __name__ == "__main__":
    main()
