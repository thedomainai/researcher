#!/usr/bin/env python3
"""Generate a dedicated web UI for the explicit knowledge graph."""

import json
import os

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

    return """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Research Atlas</title>
<style>
:root{
  --paper:#f4efe6;
  --paper-strong:#efe7db;
  --ink:#15202b;
  --ink-soft:#5a6774;
  --line:rgba(21,32,43,.12);
  --accent-rust:#c56a32;
  --accent-teal:#0f766e;
  --accent-blue:#2563eb;
  --accent-amber:#d97706;
  --accent-slate:#516273;
  --card:rgba(255,255,255,.58);
  --card-strong:rgba(255,255,255,.74);
  --shadow:0 18px 50px rgba(36,43,49,.08);
}
*{box-sizing:border-box}
html,body{height:100%}
body{
  margin:0;
  color:var(--ink);
  font-family:"Avenir Next","Segoe UI",sans-serif;
  background:
    radial-gradient(circle at top left, rgba(15,118,110,.09), transparent 28%),
    radial-gradient(circle at top right, rgba(197,106,50,.08), transparent 22%),
    linear-gradient(180deg, rgba(255,255,255,.7), rgba(255,255,255,0)),
    var(--paper);
}
.page-rail{
  position:fixed;
  left:24px;
  top:24px;
  width:82px;
  display:flex;
  flex-direction:column;
  gap:12px;
  z-index:40;
}
.page-rail-card{
  background:rgba(255,255,255,.72);
  border:1px solid rgba(255,255,255,.74);
  backdrop-filter:blur(10px);
  box-shadow:var(--shadow);
  border-radius:24px;
  padding:12px 10px;
  display:flex;
  flex-direction:column;
  gap:10px;
}
.page-rail-label{
  color:var(--ink-soft);
  font-size:10px;
  letter-spacing:.16em;
  text-transform:uppercase;
  text-align:center;
}
.page-link{
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  gap:6px;
  min-height:68px;
  padding:10px 8px;
  border-radius:18px;
  text-decoration:none;
  color:var(--ink-soft);
  border:1px solid rgba(21,32,43,.08);
  background:rgba(255,255,255,.6);
  transition:background .18s ease, color .18s ease, transform .18s ease;
}
.page-link:hover{
  background:#fff;
  color:var(--ink);
  transform:translateY(-1px);
}
.page-link.active{
  color:var(--ink);
  border-color:transparent;
  background:rgba(15,118,110,.16);
}
.page-link strong{
  font-size:11px;
  letter-spacing:.08em;
  text-transform:uppercase;
}
.page-link span{
  font-size:10px;
  text-align:center;
  line-height:1.3;
}
body::before{
  content:"";
  position:fixed;
  inset:0;
  pointer-events:none;
  opacity:.34;
  background-image:
    linear-gradient(rgba(21,32,43,.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(21,32,43,.03) 1px, transparent 1px);
  background-size:28px 28px;
}
.shell{
  position:relative;
  min-height:100%;
  padding:24px 24px 24px 126px;
}
.hero{
  display:grid;
  grid-template-columns:minmax(0, 1.4fr) minmax(320px, .8fr);
  gap:18px;
  margin-bottom:18px;
}
.hero-card,.metric-grid,.panel,.stage-shell{
  background:var(--card);
  border:1px solid rgba(255,255,255,.7);
  backdrop-filter:blur(10px);
  box-shadow:var(--shadow);
  border-radius:26px;
}
.hero-card{
  padding:28px;
}
.eyebrow{
  display:inline-flex;
  align-items:center;
  gap:10px;
  padding:8px 12px;
  border-radius:999px;
  background:rgba(255,255,255,.72);
  color:var(--ink-soft);
  font-size:12px;
  letter-spacing:.12em;
  text-transform:uppercase;
}
.hero h1{
  margin:18px 0 10px;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  font-size:clamp(32px,4vw,56px);
  line-height:1.02;
  letter-spacing:-.03em;
}
.hero p{
  margin:0;
  max-width:64ch;
  color:var(--ink-soft);
  font-size:15px;
  line-height:1.72;
}
.metric-grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:1px;
  overflow:hidden;
}
.metric{
  padding:22px 20px 18px;
  background:var(--card-strong);
}
.metric .value{
  font-size:34px;
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
  grid-template-columns:320px minmax(0,1fr) 360px;
  gap:18px;
  align-items:start;
}
.panel{
  padding:18px;
  position:sticky;
  top:24px;
}
.panel h2,.panel h3{
  margin:0 0 12px;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  letter-spacing:-.02em;
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
  border:1px solid rgba(21,32,43,.12);
  background:rgba(255,255,255,.76);
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
  border:1px solid rgba(21,32,43,.14);
  background:rgba(255,255,255,.76);
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
  background:rgba(15,118,110,.16);
}
.chip.active[data-kind="tier1"]{background:rgba(197,106,50,.16)}
.chip.active[data-kind="tier2"]{background:rgba(15,118,110,.16)}
.chip.active[data-kind="tier3"]{background:rgba(37,99,235,.16)}
.chip.active[data-kind="legacy"]{background:rgba(81,98,115,.18)}
.toggle{
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:12px 14px;
  border-radius:16px;
  background:rgba(255,255,255,.7);
  border:1px solid rgba(21,32,43,.08);
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
.hero-actions{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  margin-top:18px;
}
.list button,.link-btn,.ghost-btn,.ghost-link,.hero-link{
  width:100%;
  text-align:left;
  border:1px solid rgba(21,32,43,.08);
  background:rgba(255,255,255,.72);
  border-radius:16px;
  padding:12px 14px;
  color:var(--ink);
  cursor:pointer;
}
.ghost-link,.hero-link{
  display:inline-flex;
  width:auto;
  align-items:center;
  justify-content:center;
  text-decoration:none;
}
.list button:hover,.link-btn:hover,.ghost-btn:hover,.ghost-link:hover,.hero-link:hover{background:#fff}
.list strong{
  display:block;
  font-size:14px;
  margin-bottom:4px;
}
.list span{
  color:var(--ink-soft);
  font-size:12px;
}
.stage-shell{
  padding:16px;
}
.stage-header{
  display:flex;
  justify-content:space-between;
  align-items:flex-start;
  gap:18px;
  padding:8px 8px 14px;
}
.stage-title h2{
  margin:0;
  font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
  font-size:28px;
}
.stage-title p{
  margin:8px 0 0;
  color:var(--ink-soft);
  font-size:13px;
  line-height:1.6;
}
.legend{
  display:flex;
  flex-wrap:wrap;
  gap:8px 12px;
  justify-content:flex-end;
}
.legend-item{
  display:flex;
  align-items:center;
  gap:8px;
  font-size:12px;
  color:var(--ink-soft);
}
.dot{
  width:10px;
  height:10px;
  border-radius:999px;
}
.stage{
  position:relative;
  min-height:720px;
  border-radius:24px;
  overflow:hidden;
  border:1px solid rgba(21,32,43,.08);
  background:
    radial-gradient(circle at 20% 20%, rgba(15,118,110,.08), transparent 24%),
    radial-gradient(circle at 76% 18%, rgba(197,106,50,.08), transparent 24%),
    linear-gradient(180deg, rgba(255,255,255,.55), rgba(255,255,255,.15)),
    var(--paper-strong);
}
#graph{
  position:absolute;
  inset:0;
  width:100%;
  height:100%;
}
.stage-overlay{
  position:absolute;
  inset:auto 18px 18px 18px;
  display:flex;
  justify-content:space-between;
  align-items:flex-end;
  gap:18px;
  pointer-events:none;
}
.overlay-card{
  min-width:220px;
  max-width:320px;
  padding:14px 16px;
  border-radius:18px;
  background:rgba(255,255,255,.78);
  border:1px solid rgba(21,32,43,.08);
  backdrop-filter:blur(8px);
}
.overlay-card strong{
  display:block;
  margin-bottom:6px;
  font-size:13px;
}
.overlay-card span{
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.5;
}
.dossier h2{
  margin-bottom:8px;
  font-size:30px;
}
.dossier p{
  margin:0;
  color:var(--ink-soft);
  font-size:14px;
  line-height:1.72;
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
  background:rgba(255,255,255,.74);
  border:1px solid rgba(21,32,43,.08);
  color:var(--ink-soft);
  font-size:12px;
}
.metric-strip{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:10px;
  margin-top:16px;
}
.mini{
  padding:12px 14px;
  border-radius:18px;
  background:rgba(255,255,255,.72);
  border:1px solid rgba(21,32,43,.08);
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
  display:flex;
  gap:10px;
}
.ghost-btn{
  flex:1;
  border-radius:16px;
}
.text-list{
  display:flex;
  flex-direction:column;
  gap:10px;
}
.text-item{
  padding:12px 14px;
  border-radius:18px;
  background:rgba(255,255,255,.7);
  border:1px solid rgba(21,32,43,.08);
}
.text-item strong{
  display:block;
  font-size:13px;
}
.text-item span,.text-item small{
  display:block;
  color:var(--ink-soft);
  font-size:12px;
  line-height:1.55;
}
.empty{
  padding:14px;
  border-radius:18px;
  background:rgba(255,255,255,.58);
  border:1px dashed rgba(21,32,43,.12);
  color:var(--ink-soft);
  font-size:13px;
}
@media (max-width: 1200px){
  .layout{grid-template-columns:280px minmax(0,1fr)}
  .dossier{grid-column:1 / -1; position:static}
}
@media (max-width: 900px){
  .page-rail{
    position:static;
    width:auto;
    margin:0 0 18px;
  }
  .page-rail-card{
    flex-direction:row;
    align-items:stretch;
    justify-content:space-between;
  }
  .page-rail-label{
    display:none;
  }
  .page-link{
    flex:1;
    min-height:56px;
  }
  .shell{
    padding:18px;
  }
  .hero,.layout{grid-template-columns:1fr}
  .panel{position:static}
  .stage{min-height:560px}
  .legend{justify-content:flex-start}
}
@media (max-width: 640px){
  .metric-grid{grid-template-columns:1fr}
}
</style>
</head>
<body>
<aside class="page-rail">
  <div class="page-rail-card">
    <div class="page-rail-label">Pages</div>
    <a class="page-link active" href="index.html"><strong>Atlas</strong><span>Graph view</span></a>
    <a class="page-link" href="../reader.html"><strong>Reader</strong><span>Article view</span></a>
    <a class="page-link" href="../index.md"><strong>Index</strong><span>Wiki root</span></a>
  </div>
</aside>
<div class="shell">
  <section class="hero">
    <div class="hero-card">
      <div class="eyebrow">Research Atlas</div>
      <h1>知識の全体像を、つながりから読む</h1>
      <p>
        この UI は「何があるか」より先に、「どこがつながっていて、どこに穴があるか」を読むためのものです。
        resolved concept を主グラフに、未解決参照は選択ノードの輪郭として扱い、既存 wiki の構造と欠損の両方を同時に見渡せるようにしています。
      </p>
      <div class="hero-actions">
        <a class="hero-link" href="../reader.html">Article Reader</a>
        <a class="hero-link" href="../index.md">Wiki Index</a>
      </div>
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
    <aside class="panel">
      <div class="section">
        <h2>What</h2>
        <div class="small">
          全体構造、ハブ、孤立ノード、未解決参照を同じ画面で観測します。
          大きな円ほど degree が高く、色は tier、琥珀色は未解決参照の気配です。
        </div>
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
        <h3>How</h3>
        <div class="toggle"><span>Show isolated concepts</span><input id="show-isolated" type="checkbox" checked></div>
        <div style="height:10px"></div>
        <div class="toggle"><span>Show unresolved halo</span><input id="show-unresolved" type="checkbox" checked></div>
        <div style="height:10px"></div>
        <div class="toggle"><span>Neighborhood mode</span><input id="focus-mode" type="checkbox"></div>
      </div>
      <div class="section">
        <h3>Curated Views</h3>
        <div class="list">
          <button id="focus-hubs"><strong>Top hubs</strong><span>最も接続数の多いノードを中心に見る</span></button>
          <button id="focus-islands"><strong>Isolated concepts</strong><span>孤立 concept を洗い出す</span></button>
          <button id="focus-gaps"><strong>Unresolved-rich concepts</strong><span>未解決参照を多く抱える node を優先</span></button>
        </div>
      </div>
      <div class="section">
        <h3>Top Hubs</h3>
        <div id="hub-list" class="list"></div>
      </div>
      <div class="section">
        <h3>Gap Queue</h3>
        <div id="gap-list" class="list"></div>
      </div>
      <div class="section">
        <h3>Overall Form</h3>
        <div class="small">
          全体は atlas、右側は dossier です。まず中心の構造を掴み、次に個別ノードへ寄って、最後に未解決参照を次の執筆候補として読む構成にしています。
        </div>
      </div>
    </aside>

    <div class="stage-shell">
      <div class="stage-header">
        <div class="stage-title">
          <h2>Knowledge Field</h2>
          <p>resolved concept graph を主面に置き、未解決参照は選択ノードの halo としてだけ見せます。全件を一度に撒かず、読める密度を保つのがこの UI の基本方針です。</p>
        </div>
        <div class="legend">
          <div class="legend-item"><span class="dot" style="background:var(--accent-rust)"></span>Tier 1</div>
          <div class="legend-item"><span class="dot" style="background:var(--accent-teal)"></span>Tier 2</div>
          <div class="legend-item"><span class="dot" style="background:var(--accent-blue)"></span>Tier 3</div>
          <div class="legend-item"><span class="dot" style="background:var(--accent-slate)"></span>Legacy / Untiered</div>
          <div class="legend-item"><span class="dot" style="background:var(--accent-amber)"></span>Unresolved halo</div>
        </div>
      </div>
      <div class="stage" id="stage">
        <canvas id="graph"></canvas>
        <div class="stage-overlay">
          <div class="overlay-card">
            <strong id="overlay-title">Atlas view</strong>
            <span id="overlay-text">全 resolved concept を表示しています。ノードを選ぶと、その周辺関係と未解決参照が右側に出ます。</span>
          </div>
          <div class="overlay-card">
            <strong id="overlay-stats">0 nodes / 0 edges</strong>
            <span id="overlay-mode">Pan: drag, Zoom: wheel, Focus: click a node</span>
          </div>
        </div>
      </div>
    </div>

    <aside class="panel dossier" id="dossier"></aside>
  </section>
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

const stage = document.getElementById('stage');
const canvas = document.getElementById('graph');
const ctx = canvas.getContext('2d');
const overlayTitle = document.getElementById('overlay-title');
const overlayText = document.getElementById('overlay-text');
const overlayStats = document.getElementById('overlay-stats');

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
};

const colorByTier = {
  1: '#c56a32',
  2: '#0f766e',
  3: '#2563eb',
  legacy: '#516273',
};

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

function unresolvedCount(node){
  return (unresolvedBySource[node.id] || []).length;
}

function radiusFor(node){
  return 5 + Math.min(16, Math.sqrt(node.degree || 0) * 1.5);
}

function normalize(text){
  return String(text || '').toLowerCase();
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
  const width = stage.clientWidth;
  const height = stage.clientHeight;
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
  canvas.width = stage.clientWidth * ratio;
  canvas.height = stage.clientHeight * ratio;
  canvas.style.width = stage.clientWidth + 'px';
  canvas.style.height = stage.clientHeight + 'px';
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
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
  ctx.clearRect(0, 0, stage.clientWidth, stage.clientHeight);
  ctx.save();
  ctx.strokeStyle = 'rgba(21,32,43,.05)';
  ctx.lineWidth = 1;
  for (let x = 0; x < stage.clientWidth; x += 36){
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, stage.clientHeight);
    ctx.stroke();
  }
  for (let y = 0; y < stage.clientHeight; y += 36){
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(stage.clientWidth, y);
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
    const alpha = state.selected && (edge.source === state.selected || edge.target === state.selected) ? .38 : .12;
    ctx.strokeStyle = 'rgba(21,32,43,' + alpha + ')';
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

    if (state.showUnresolved && unresolved && (isSelected || isHovered)){
      const halo = radius + 14;
      const count = Math.min(unresolved, 18);
      for (let i = 0; i < count; i += 1){
        const angle = (Math.PI * 2 * i) / count;
        const hx = p.x + Math.cos(angle) * halo;
        const hy = p.y + Math.sin(angle) * halo;
        ctx.fillStyle = 'rgba(217,119,6,.55)';
        ctx.beginPath();
        ctx.arc(hx, hy, 2.2, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    ctx.fillStyle = colorByTier[tierKey(node)];
    ctx.beginPath();
    ctx.arc(p.x, p.y, radius, 0, Math.PI * 2);
    ctx.fill();

    ctx.lineWidth = isSelected ? 3 : (isHovered ? 2 : 1);
    ctx.strokeStyle = isSelected ? '#ffffff' : 'rgba(255,255,255,.65)';
    ctx.stroke();

    const shouldLabel = isSelected || isHovered || radius > 10 || (node.degree || 0) > 18 || (state.query && normalize(node.label).includes(normalize(state.query)));
    if (shouldLabel){
      ctx.fillStyle = '#15202b';
      ctx.font = '12px "Avenir Next", "Segoe UI", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(node.label, p.x, p.y - radius - 8);
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

function sourceButtons(items, title){
  if (!items.length) return '<div class="empty">' + title + ' はありません。</div>';
  return '<div class="list">' + items.map(item => {
    return '<button class="link-btn" data-slug="' + item.id + '"><strong>' + item.label + '</strong><span>' + (item.weight || 1) + ' connection(s)</span></button>';
  }).join('') + '</div>';
}

function bestNodeForGap(group){
  return group.sourceIds
    .map(id => resolvedNodeMap[id])
    .filter(Boolean)
    .sort((a, b) => (unresolvedCount(b) - unresolvedCount(a)) || ((b.degree || 0) - (a.degree || 0)))[0] || null;
}

function renderDossier(){
  const container = document.getElementById('dossier');
  const node = resolvedNodeMap[state.selected] || resolvedNodes.slice().sort((a,b) => (b.degree || 0) - (a.degree || 0))[0];
  if (!state.selected) state.selected = node.id;

  const inbound = resolvedEdges.filter(edge => edge.target === node.id).map(edge => ({id: edge.source, label: resolvedNodeMap[edge.source].label, weight: edge.weight}));
  const outbound = resolvedEdges.filter(edge => edge.source === node.id).map(edge => ({id: edge.target, label: resolvedNodeMap[edge.target].label, weight: edge.weight}));
  const unresolved = (unresolvedBySource[node.id] || []).slice().sort((a,b) => a.raw_target.localeCompare(b.raw_target, 'ja'));
  const domainsHtml = (node.related_domains || []).map(domain => detailPill(domain)).join('');
  const sourceHtml = (node.key_sources || []).slice(0, 6).map(src => '<div class="text-item"><strong>' + src + '</strong><small>key source</small></div>').join('');

  container.innerHTML = ''
    + '<div class="section">'
    + '<div class="eyebrow">Dossier</div>'
    + '<h2>' + node.label + '</h2>'
    + '<p>' + (node.description || 'この concept には description がまだ付いていません。') + '</p>'
    + '<div class="pill-row">'
      + detailPill(tierLabel(node))
      + detailPill(node.metadata_source || 'article')
      + detailPill('degree ' + (node.degree || 0))
      + detailPill('in ' + (node.inbound_count || 0))
      + detailPill('out ' + (node.outbound_count || 0))
      + detailPill('unresolved ' + unresolved.length)
    + '</div>'
    + '<div class="metric-strip">'
      + '<div class="mini"><div class="v">' + (node.inbound_count || 0) + '</div><div class="k">Backlinks</div></div>'
      + '<div class="mini"><div class="v">' + (node.outbound_count || 0) + '</div><div class="k">Outbound</div></div>'
      + '<div class="mini"><div class="v">' + unresolved.length + '</div><div class="k">Gaps</div></div>'
    + '</div>'
    + '<div class="dock">'
      + '<button class="ghost-btn" id="center-selected">Center in atlas</button>'
      + '<button class="ghost-btn" id="toggle-focus">' + (state.focusMode ? 'Exit neighborhood' : 'Neighborhood mode') + '</button>'
      + '<a class="ghost-link" href="../reader.html#' + encodeURIComponent(node.id) + '">Open in reader</a>'
    + '</div>'
    + '</div>'
    + '<div class="section"><h3>Domains</h3>' + (domainsHtml || '<div class="empty">related_domains はまだありません。</div>') + '</div>'
    + '<div class="section"><h3>Key Sources</h3>' + (sourceHtml || '<div class="empty">key_sources はまだありません。</div>') + '</div>'
    + '<div class="section"><h3>Outbound Concepts</h3>' + sourceButtons(outbound, 'outbound concepts') + '</div>'
    + '<div class="section"><h3>Backlinks</h3>' + sourceButtons(inbound, 'backlinks') + '</div>'
    + '<div class="section"><h3>Unresolved References</h3>' + renderList(unresolved, '未解決参照はありません。', item => (
      '<div class="text-item"><strong>' + item.raw_target + '</strong>'
      + '<span>' + item.section + ' / line ' + item.line + '</span>'
      + (item.candidates && item.candidates.length ? '<small>candidates: ' + item.candidates.slice(0,5).join(', ') + '</small>' : '')
      + '</div>'
    )) + '</div>';

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
  const targetX = stage.clientWidth / 2 - node.x * state.scale;
  const targetY = stage.clientHeight / 2 - node.y * state.scale;
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
  const hubs = resolvedNodes.slice().sort((a,b) => ((b.degree || 0) - (a.degree || 0)) || (unresolvedCount(b) - unresolvedCount(a))).slice(0, 8);
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
  const gaps = unresolvedGroups.slice(0, 8);
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
  renderDossier();

  const selected = resolvedNodeMap[state.selected];
  overlayTitle.textContent = state.focusMode ? 'Neighborhood view' : 'Atlas view';
  overlayText.textContent = selected
    ? selected.label + ' を中心に、resolved link と unresolved halo を同時に表示しています。'
    : '全 resolved concept を表示しています。';
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
  resizeCanvas();
  initializeLayout();
  simulate();
  restoreHash();
  if (!state.selected){
    state.selected = resolvedNodes.slice().sort((a,b) => (b.degree || 0) - (a.degree || 0))[0].id;
  }
  state.offsetX = stage.clientWidth * 0.1;
  state.offsetY = stage.clientHeight * 0.08;
  wireControls();
  wireCanvas();
  updateHubList();
  updateGapList();
  update();
}

window.addEventListener('resize', () => {
  resizeCanvas();
  update();
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
