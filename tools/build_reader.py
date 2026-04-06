#!/usr/bin/env python3
"""wiki/concepts/*.md から静的HTMLリーダーを生成"""
import json, os, html as html_mod

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(BASE, "wiki", "concepts")
OUT = os.path.join(BASE, "wiki", "reader.html")
META_FILE = os.path.join(BASE, "wiki", "_meta", "concepts.json")

# concepts.json から動的に META を構築
raw_meta = json.load(open(META_FILE, encoding="utf-8")) if os.path.exists(META_FILE) else []
meta_by_slug = {m["slug"]: m for m in raw_meta}

# wiki/concepts/ 内の全 .md ファイルを列挙し、concepts.json にない記事も取り込む
all_slugs = sorted(
    f[:-3] for f in os.listdir(WIKI) if f.endswith(".md")
)

META = []
for slug in all_slugs:
    if slug in meta_by_slug:
        m = meta_by_slug[slug]
        META.append({"slug": slug, "t": m.get("title_ja", slug), "tier": m.get("tier", 2)})
    else:
        # concepts.json にない場合はファイルの先頭 H1 からタイトルを取得
        fp = os.path.join(WIKI, slug + ".md")
        title = slug
        with open(fp, encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
        META.append({"slug": slug, "t": title, "tier": 2})

articles = {}
for m in META:
    fp = os.path.join(WIKI, m["slug"] + ".md")
    if os.path.exists(fp):
        with open(fp, encoding="utf-8") as f:
            articles[m["slug"]] = f.read()

# JSON encode with proper escaping for embedding in JS
data_json = json.dumps(articles, ensure_ascii=False)
# Escape for script tag
data_json = data_json.replace("</", "<\\/")
meta_json = json.dumps(META, ensure_ascii=False)

with open(OUT, "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Native Wiki</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Hiragino Sans',sans-serif;background:#0a0a0f;color:#e0e0e8;line-height:1.7}
.hdr{position:sticky;top:0;z-index:100;background:rgba(10,10,15,.96);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,.06);padding:12px 16px}
.hdr h1{font-size:15px;font-weight:600;color:#a0a0b0}
.hdr .sub{font-size:11px;color:#606070;margin-top:2px}
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
#av{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:#0a0a0f;z-index:200;overflow-y:auto;-webkit-overflow-scrolling:touch}
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
</style></head><body>
<div id="list">
<div class="hdr"><h1>AI Native Wiki</h1><div class="sub">15分野 × """ + str(len(META)) + """コンセプト</div></div>
<div class="nav" id="nav"></div>
<div class="cards" id="cards"></div>
</div>
<div id="av">
<div class="ah"><button class="back" onclick="closeA()">&#8592; 戻る</button><span class="tt" id="at"></span></div>
<div class="ab" id="ab"></div>
</div>
<script>
var A=""" + data_json + """;
var M=""" + meta_json + """;
var TL={1:"不変原理",2:"設計原理",3:"分析枠組み"};
var fi=0;
function md2h(s){
  return s
    .replace(/^### (.+)$/gm,'<h3>$1</h3>')
    .replace(/^## (.+)$/gm,'<h2>$1</h2>')
    .replace(/^# (.+)$/gm,'<h1>$1</h1>')
    .replace(/\\*\\*(.+?)\\*\\*/g,'<strong>$1</strong>')
    .replace(/\\*(.+?)\\*/g,'<em>$1</em>')
    .replace(/`(.+?)`/g,'<code>$1</code>')
    .replace(/^- (.+)$/gm,'<li>$1</li>')
    .replace(/((?:<li>[\\s\\S]*?<\\/li>\\n?)+)/gm,'<ul>$1</ul>')
    .replace(/^(?!<[hulo]|<li)(.+)$/gm,'<p>$1</p>');
}
function render(){
  var it=fi===0?M:M.filter(function(c){return c.tier===fi;});
  var h='';
  it.forEach(function(c){h+='<div class="card" onclick="openA(\\''+c.slug+'\\')"><span class="badge t'+c.tier+'">'+TL[c.tier]+'</span><h3>'+c.t+'</h3></div>';});
  document.getElementById('cards').innerHTML=h;
  var nh='<button class="btn'+(fi===0?' on':'')+'" onclick="sf(0)" style="margin-left:16px">全て</button>';
  [1,2,3].forEach(function(t){var n=M.filter(function(c){return c.tier===t;}).length;nh+='<button class="btn t'+t+(fi===t?' on':'')+'" onclick="sf('+t+')">'+['','★','◇','△'][t]+' '+TL[t]+' ('+n+')</button>';});
  document.getElementById('nav').innerHTML=nh;
}
function sf(t){fi=t;render();}
function openA(slug){
  var c=M.find(function(x){return x.slug===slug;});
  document.getElementById('at').textContent=c?c.t:slug;
  var md=A[slug];
  document.getElementById('ab').innerHTML=md?md2h(md):'<p>記事なし</p>';
  document.getElementById('av').className='open';
  document.getElementById('av').scrollTop=0;
}
function closeA(){document.getElementById('av').className='';}
render();
</script></body></html>""")

print(f"Generated: {os.path.getsize(OUT)} bytes")
print(f"Articles: {len(articles)}")
print(f"Path: {OUT}")
