#!/usr/bin/env python3
"""Generate a static HTML reader from wiki articles and graph metadata."""

import json
import os

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
    summary_text = (
        f"{summary.get('resolved_nodes', len(meta))} concepts / "
        f"{summary.get('edges', 0)} edges / "
        f"{summary.get('unresolved_nodes', 0)} unresolved refs"
        if summary
        else f"17分野 × {len(meta)}コンセプト"
    )

    return """<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Native Wiki</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Hiragino Sans',sans-serif;background:#0a0a0f;color:#e0e0e8;line-height:1.7;padding-left:112px}
.page-rail{position:fixed;left:16px;top:16px;bottom:16px;width:80px;z-index:320}
.page-rail-card{height:100%;display:flex;flex-direction:column;gap:10px;padding:12px 10px;background:rgba(18,18,28,.92);border:1px solid rgba(255,255,255,.06);border-radius:24px;backdrop-filter:blur(14px)}
.page-rail-label{font-size:10px;letter-spacing:.16em;color:#666678;text-transform:uppercase;text-align:center}
.page-link{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;min-height:68px;padding:10px 8px;border-radius:18px;border:1px solid rgba(255,255,255,.06);background:rgba(255,255,255,.03);text-decoration:none;color:#9ca3c9}
.page-link:hover{background:rgba(255,255,255,.08);color:#e0e4ff}
.page-link.active{background:rgba(130,140,255,.16);border-color:transparent;color:#eef1ff}
.page-link strong{font-size:11px;letter-spacing:.08em;text-transform:uppercase}
.page-link span{font-size:10px;text-align:center;line-height:1.3}
.hdr{position:sticky;top:0;z-index:100;background:rgba(10,10,15,.96);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,.06);padding:12px 16px}
.hdr-top{display:flex;align-items:center;justify-content:space-between;gap:12px}
.hdr h1{font-size:15px;font-weight:600;color:#a0a0b0}
.hdr .sub{font-size:11px;color:#606070;margin-top:2px}
.hdr-actions{display:flex;gap:10px;flex-wrap:wrap}
.hdr-link{display:inline-flex;align-items:center;justify-content:center;padding:8px 12px;border-radius:999px;border:1px solid rgba(130,140,255,.18);background:rgba(130,140,255,.08);color:#c9d0ff;text-decoration:none;font-size:12px}
.hdr-link:hover{background:rgba(130,140,255,.16)}
.search-wrap{padding:12px 16px 0}
.search{width:100%;padding:10px 12px;border-radius:12px;border:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.03);color:#e0e0e8;font-size:13px}
.search::placeholder{color:#707080}
.nav{padding:12px 0;overflow-x:auto;white-space:nowrap;-webkit-overflow-scrolling:touch}
.nav::-webkit-scrollbar{display:none}
.btn{display:inline-block;padding:6px 14px;margin:0 4px;font-size:12px;border-radius:20px;border:1px solid rgba(255,255,255,.1);background:transparent;color:#808090;cursor:pointer}
.btn.on{border-color:rgba(130,140,255,.4);background:rgba(130,140,255,.1);color:#a0a8ff}
.btn.t1.on{background:rgba(255,180,80,.1);color:#ffb850;border-color:rgba(255,180,80,.5)}
.btn.t2.on{background:rgba(80,200,180,.1);color:#50c8b4;border-color:rgba(80,200,180,.5)}
.btn.t3.on{background:rgba(160,140,200,.1);color:#a08cc8;border-color:rgba(160,140,200,.5)}
.cards{padding:0 16px 100px}
.card{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);border-radius:12px;padding:16px;margin-bottom:10px;cursor:pointer}
.card:active{background:rgba(255,255,255,.06)}
.badge{display:inline-block;font-size:10px;padding:2px 8px;border-radius:10px;font-weight:600;margin-bottom:8px}
.badge.t1{background:rgba(255,180,80,.15);color:#ffb850}
.badge.t2{background:rgba(80,200,180,.15);color:#50c8b4}
.badge.t3{background:rgba(160,140,200,.15);color:#a08cc8}
.card h3{font-size:16px;font-weight:600;color:#e8e8f0;margin-bottom:8px}
.card .meta{font-size:12px;color:#8a8a9c}
#av{display:none;position:fixed;top:0;left:112px;right:0;bottom:0;background:#0a0a0f;z-index:200;overflow-y:auto;-webkit-overflow-scrolling:touch}
#av.open{display:block}
.ah{position:sticky;top:0;z-index:10;background:rgba(10,10,15,.96);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,.06);padding:12px 16px;display:flex;align-items:center;gap:12px}
.ah .back{background:0 0;border:0;color:#a0a8ff;font-size:14px;cursor:pointer}
.ah .tt{font-size:13px;color:#909098;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.ab{padding:20px 16px 80px}
.ab h1{font-size:22px;font-weight:700;color:#f0f0f8;margin-bottom:16px;line-height:1.3}
.ab h2{font-size:17px;font-weight:600;color:#c8c8e0;margin-top:28px;margin-bottom:12px;padding-bottom:6px;border-bottom:1px solid rgba(255,255,255,.06)}
.ab h3{font-size:15px;font-weight:600;color:#b0b0c8;margin-top:20px;margin-bottom:8px}
.ab p{font-size:14px;color:#c0c0d0;margin-bottom:12px;line-height:1.75}
.ab ul{padding-left:20px;margin-bottom:12px}
.ab li{font-size:14px;color:#b0b0c0;margin-bottom:6px;line-height:1.6}
.ab strong{color:#e0e0f0}
.ab em{color:#b0b0d0}
.ab code{background:rgba(255,255,255,.06);padding:1px 5px;border-radius:3px;font-size:13px;color:#c0c0e0}
.graph{margin-top:24px;padding:16px;border:1px solid rgba(255,255,255,.06);border-radius:14px;background:rgba(255,255,255,.025)}
.graph h3{margin-top:0}
.graph h4{font-size:12px;letter-spacing:.04em;color:#7f7f92;text-transform:uppercase;margin-top:16px;margin-bottom:10px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip,.wikilink{display:inline-flex;align-items:center;gap:6px;border-radius:999px;padding:6px 10px;border:1px solid rgba(130,140,255,.22);background:rgba(130,140,255,.08);color:#c9d0ff;font-size:12px}
button.chip,button.wikilink{cursor:pointer}
.chip.unresolved,.wikilink.unresolved{border-color:rgba(255,180,80,.22);background:rgba(255,180,80,.08);color:#ffd49a}
.chip small{color:#8f95bb}
.empty{font-size:12px;color:#717184}
@media (max-width: 900px){
body{padding-left:0}
.page-rail{position:static;width:auto;padding:16px 16px 0}
.page-rail-card{height:auto;flex-direction:row;align-items:stretch}
.page-rail-label{display:none}
.page-link{flex:1;min-height:54px}
#av{left:0}
}
</style></head><body>
<aside class="page-rail"><div class="page-rail-card"><div class="page-rail-label">Pages</div><a class="page-link" href="graph/index.html"><strong>Atlas</strong><span>Graph view</span></a><a class="page-link active" href="reader.html"><strong>Reader</strong><span>Article view</span></a><a class="page-link" href="index.md"><strong>Index</strong><span>Wiki root</span></a></div></aside>
<div id="list">
<div class="hdr"><div class="hdr-top"><div><h1>AI Native Wiki</h1><div class="sub">""" + summary_text + """</div></div><div class="hdr-actions"><a class="hdr-link" href="graph/index.html">Knowledge Atlas</a></div></div></div>
<div class="search-wrap"><input id="search" class="search" placeholder="コンセプト名で検索"></div>
<div class="nav" id="nav"></div>
<div class="cards" id="cards"></div>
</div>
<div id="av">
<div class="ah"><button class="back" onclick="closeA()">&#8592; 戻る</button><span class="tt" id="at"></span></div>
<div class="ab" id="ab"></div>
</div>
<script>
var A=""" + article_json + """;
var M=""" + meta_json + """;
var G=""" + graph_json + """;
var B=""" + backlinks_json + """;
var TL={1:"不変原理",2:"設計原理",3:"分析枠組み"};
var fi=0;
var q='';

function esc(s){
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}

function nodeFor(slug){
  return (B.nodes && B.nodes[slug]) ? B.nodes[slug] : null;
}

function nodeStats(slug){
  var n=nodeFor(slug);
  if(!n){return {inbound:0,outbound:0};}
  return {inbound:(n.inbound||[]).length,outbound:(n.outbound||[]).length};
}

function sourceLinkMap(slug){
  var n=nodeFor(slug);
  var map={};
  if(!n){return map;}
  (n.outbound||[]).forEach(function(item){
    (item.raw_targets||[]).forEach(function(raw){
      map[raw]=item;
    });
  });
  return map;
}

function renderWikilinks(slug, text){
  var linkMap=sourceLinkMap(slug);
  return text.replace(/\\[\\[([^\\]]+)\\]\\]/g,function(_,inner){
    var target=inner;
    var label=inner;
    if(inner.indexOf('|')!==-1){
      var parts=inner.split('|');
      target=parts[0].trim();
      label=parts.slice(1).join('|').trim();
    }
    var item=linkMap[target];
    if(item && item.resolved && A[item.id]){
      return '<button class="wikilink" onclick="event.stopPropagation();openA(\\''+item.id+'\\')">'+esc(label)+'</button>';
    }
    return '<span class="wikilink unresolved">'+esc(label)+'</span>';
  });
}

function md2h(slug, text){
  var s=renderWikilinks(slug, text);
  return s
    .replace(/^### (.+)$/gm,'<h3>$1</h3>')
    .replace(/^## (.+)$/gm,'<h2>$1</h2>')
    .replace(/^# (.+)$/gm,'<h1>$1</h1>')
    .replace(/\\*\\*(.+?)\\*\\*/g,'<strong>$1</strong>')
    .replace(/\\*(.+?)\\*/g,'<em>$1</em>')
    .replace(/`(.+?)`/g,'<code>$1</code>')
    .replace(/^- (.+)$/gm,'<li>$1</li>')
    .replace(/((?:<li>[\\s\\S]*?<\\/li>\\n?)+)/gm,'<ul>$1</ul>')
    .replace(/^(?!<[hulo]|<li|<button|<span)(.+)$/gm,'<p>$1</p>');
}

function chip(item){
  var count=item.weight?'<small>×'+item.weight+'</small>':'';
  if(item.resolved && A[item.id]){
    return '<button class="chip" onclick="event.stopPropagation();openA(\\''+item.id+'\\')">'+esc(item.label)+count+'</button>';
  }
  return '<span class="chip unresolved">'+esc(item.label)+count+'</span>';
}

function graphPanel(slug){
  var node=nodeFor(slug);
  if(!node){return '';}
  var inbound=node.inbound||[];
  var outbound=node.outbound||[];
  var resolvedOutbound=outbound.filter(function(item){return item.resolved;});
  var unresolvedOutbound=outbound.filter(function(item){return !item.resolved;});
  var html='<div class="graph">';
  html+='<h3>Knowledge Graph</h3>';
  html+='<div class="empty">outbound '+outbound.length+' / inbound '+inbound.length+'</div>';

  html+='<h4>Related Concepts</h4>';
  html+=resolvedOutbound.length?'<div class="chips">'+resolvedOutbound.map(chip).join('')+'</div>':'<div class="empty">関連コンセプトはありません。</div>';

  html+='<h4>Backlinks</h4>';
  html+=inbound.length?'<div class="chips">'+inbound.map(chip).join('')+'</div>':'<div class="empty">バックリンクはありません。</div>';

  html+='<h4>Unresolved References</h4>';
  html+=unresolvedOutbound.length?'<div class="chips">'+unresolvedOutbound.map(chip).join('')+'</div>':'<div class="empty">未解決参照はありません。</div>';
  html+='</div>';
  return html;
}

function render(){
  var items=fi===0?M:M.filter(function(c){return c.tier===fi;});
  if(q){
    var qq=q.toLowerCase();
    items=items.filter(function(c){return c.title.toLowerCase().indexOf(qq)!==-1;});
  }

  var h='';
  items.forEach(function(c){
    var stats=nodeStats(c.slug);
    h+='<div class="card" onclick="openA(\\''+c.slug+'\\')">';
    h+='<span class="badge t'+c.tier+'">'+TL[c.tier]+'</span>';
    h+='<h3>'+esc(c.title)+'</h3>';
    h+='<div class="meta">out '+stats.outbound+' / in '+stats.inbound+'</div>';
    h+='</div>';
  });
  document.getElementById('cards').innerHTML=h||'<div class="empty" style="padding:16px">一致するコンセプトがありません。</div>';

  var nav='<button class="btn'+(fi===0?' on':'')+'" onclick="sf(0)" style="margin-left:16px">全て</button>';
  [1,2,3].forEach(function(t){
    var n=M.filter(function(c){return c.tier===t;}).length;
    nav+='<button class="btn t'+t+(fi===t?' on':'')+'" onclick="sf('+t+')">'+['','★','◇','△'][t]+' '+TL[t]+' ('+n+')</button>';
  });
  document.getElementById('nav').innerHTML=nav;
}

function sf(t){fi=t;render();}

function syncArticleHash(slug){
  var url=location.pathname+(location.search||'');
  if(slug){
    history.replaceState(null,'',url+'#'+encodeURIComponent(slug));
    return;
  }
  history.replaceState(null,'',url);
}

function openA(slug){
  var c=M.find(function(x){return x.slug===slug;});
  document.getElementById('at').textContent=c?c.title:slug;
  var md=A[slug];
  document.getElementById('ab').innerHTML=md?md2h(slug, md)+graphPanel(slug):'<p>記事なし</p>';
  document.getElementById('av').className='open';
  document.getElementById('av').scrollTop=0;
  syncArticleHash(slug);
}

function closeA(){
  document.getElementById('av').className='';
  syncArticleHash('');
}

document.getElementById('search').addEventListener('input', function(ev){
  q=ev.target.value.trim();
  render();
});

if(location.hash){
  var slug=decodeURIComponent(location.hash.slice(1));
  if(M.find(function(item){return item.slug===slug;})){
    openA(slug);
  }
}

render();
</script></body></html>"""


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
