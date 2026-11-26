#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""X のポストに付ける図の、共通の様式(端末・CLI の画面)。

2026-11-26 に決めた様式。新しい図はこのモジュールを import して作る。規則の全文は
docs/x-post-patterns.md の「図の様式」にある。

  - 地は黒に近い無彩色 #141517。真っ黒・色味のある暗色は使わない
  - 文字は等幅(SF Mono)。和文は Hiragino Sans に落ちる
  - 色は青緑 ACC の 1 色と無彩色だけ。青緑は、その図で言いたい 1 か所(結論・注目の値)に置く
  - 線は 1〜1.5px、直角に折る。箱は 1px の罫線と角 8px。影・光沢・グラデーションは使わない
  - 量は、ブロック文字の棒(9px の塊と 3px の隙間)で描く
  - 見出しは「> 」、副題と注記の見出しは「# 」、操作の見出しは「$ 」で始める
  - 本体(副題と出典のあいだ)は、上下の余白が揃うまで中身を縦に広げる。render() が測って知らせる

使い方:
  import sys, os; sys.path.insert(0, "<docs/x-posts のパス>")
  from terminal_style import shell, seg, marker, render, ACC, ...
  render([("01-foo", html_text), ...], out_dir)
"""
import os

CHROME = ("/Users/yuta/Library/Caches/ms-playwright/chromium_headless_shell-1243/"
          "chrome-headless-shell-mac-arm64/chrome-headless-shell")
W, H = 1200, 675
L, R = 72, 1128

# 色(この 10 色以外を足さない)
BG = "#141517"      # 地
PANEL = "#1A1C1F"   # 箱の面
INK = "#ECEEF1"     # 見出し・値
BODY = "#D7DADF"    # 本文
SEC = "#9CA2AA"     # 補足の文字
MUTED = "#7E848C"   # 出典・注記・コメント(# の後)
FLOW = "#7E848C"    # 流れを表す線
EDGE = "#565B63"    # 基準の棒・軸
HAIR = "#3A3E44"    # 罫線・箱の枠
ACC = "#6FB7AC"     # 青緑。図ごとに 1 か所

BASE_CSS = """
html,body{margin:0}
body{width:1200px;height:675px;position:relative;overflow:hidden}
.abs{position:absolute}
h1{position:absolute;left:72px;top:40px;margin:0;font-size:30px;line-height:1.3;white-space:nowrap}
.sub{position:absolute;left:72px;top:92px;font-size:17px;white-space:nowrap}
.node{position:absolute;width:250px;height:78px;display:flex;align-items:center;justify-content:center;gap:10px;
  font-size:19px;font-weight:700;box-sizing:border-box;white-space:nowrap}
.node svg{width:24px;height:24px;flex:none}
.lab{position:absolute;white-space:nowrap;font-size:20px;font-weight:700}
.lab i,.note i{font-family:'STIX Two Text','Times New Roman',serif;font-size:1.1em}
.mid{position:absolute;left:0;width:1200px;text-align:center;font-size:17px;white-space:nowrap}
.cap{position:absolute;left:72px;top:440px;font-size:16px}
.track{position:absolute;left:72px;top:470px;width:1056px;height:26px;display:flex;gap:3px}
.track div{height:100%}
.pl{position:absolute;top:510px;font-size:18px;white-space:nowrap}
.pl b{font-size:22px}
.note{position:absolute;left:72px;top:566px;font-size:14.5px;white-space:nowrap}
.src{position:absolute;left:72px;top:624px;font-size:14px;white-space:nowrap}
svg.wires{position:absolute;left:0;top:0}
"""

TERMINAL_CSS = """
body{background:#141517;color:#D7DADF;font-family:'SF Mono','Menlo','Hiragino Sans',monospace}
h1{font-weight:600;font-size:27px;color:#ECEEF1}
h1::before{content:"> ";color:#6FB7AC}
h1 em{font-style:normal;color:#6FB7AC}
.sub{color:#7E848C;font-size:15px}
.sub::before{content:"# "}
.node{border:1px solid #3A3E44;border-radius:8px;background:#1A1C1F;font-weight:500;font-size:17px;color:#ECEEF1;gap:12px}
.node svg{display:none}
.node::before{font-size:14px;color:#7E848C}
.nx::before{content:"x"}.nm::before{content:"m"}.ny::before{content:"y"}
.nm{border-color:#6FB7AC;box-shadow:0 0 0 3px rgba(111,183,172,.12)}
.nm::before{color:#6FB7AC}
.lab{font-weight:500;font-size:16px;color:#ECEEF1}
.lab i,.note i,.mid i{font-family:inherit!important;font-style:normal;font-size:1em!important}
.lab[style*="right"]{transform:translateX(-16px)}
.lab[style*="left"]{transform:translateX(12px)}
.mid,.cap{color:#9CA2AA;font-size:15px}
.cap::before{content:"$ "; color:#6FB7AC}
.track{height:22px;gap:6px;top:474px}
.t1{background:repeating-linear-gradient(90deg,#3A3E44 0 9px,transparent 9px 12px)}
.t2{background:repeating-linear-gradient(90deg,#6FB7AC 0 9px,transparent 9px 12px)}
.pl{font-size:16px;color:#9CA2AA;top:514px}.pl b{font-weight:600;color:#ECEEF1;font-size:20px}
.pl[style*="right"] b{color:#6FB7AC}
.pl[style*="right"]::after{content:"";display:inline-block;width:10px;height:20px;background:#6FB7AC;margin-left:8px;vertical-align:-3px}
.note,.src{color:#7E848C;font-size:13px}
"""

# 部品: .ph(パネルの見出し)・.t(短い文字)・.row/.bar/.val/.tick(横棒グラフ)・.notes(右の注記の列)
COMPONENT_CSS = """
.ph{position:absolute;left:72px;font-size:17px;white-space:nowrap;color:#ECEEF1}
.ph .tag{color:#6FB7AC;margin-right:14px}
.ph b{font-weight:600}
.ph .cm{color:#7E848C;font-size:15px;margin-left:16px}
.t{position:absolute;white-space:nowrap;font-size:15px;color:#9CA2AA}
.t b{font-weight:600;color:#ECEEF1;font-size:17px}
.t b.acc{color:#6FB7AC}
.row{position:absolute;left:72px;white-space:nowrap;font-size:16px;color:#ECEEF1;background:#141517;padding:2px 10px 2px 0}
.row .cm{color:#7E848C;margin-left:14px}
.bar{position:absolute;left:72px;height:34px}
.val{position:absolute;font-size:22px;line-height:34px;font-weight:600;color:#ECEEF1;white-space:nowrap}
.val.acc{color:#6FB7AC}
.tick{position:absolute;top:566px;font-size:13px;color:#7E848C;transform:translateX(-50%)}
.notes{position:absolute;left:724px;top:160px;width:404px}
.notes div{border-top:1px solid #3A3E44;padding:16px 0 26px}
.notes h3{margin:0 0 10px;font-size:16.5px;font-weight:600;color:#ECEEF1}
.notes h3::before{content:"# ";color:#6FB7AC}
.notes p{margin:0;font-size:15px;line-height:26px;color:#9CA2AA}
"""

CSS = BASE_CSS + TERMINAL_CSS + COMPONENT_CSS


def marker(mid, color):
    """線の終点に付ける、開いた矢じり(> の形)。"""
    return ('<marker id="%s" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="13" markerHeight="13" orient="auto" markerUnits="userSpaceOnUse">'
            '<path d="M3 2.500 L9.500 6 L3 9.500" fill="none" stroke="%s" stroke-width="1.600" stroke-linecap="round" stroke-linejoin="round"/></marker>' % (mid, color))


def seg(x1, y1, x2, y2, color, w=1.2, mk=None, dash=None):
    """直線 1 本。mk に marker の id を渡すと矢じりが付く。"""
    return '<path d="M%.1f,%.1f L%.1f,%.1f" fill="none" stroke="%s" stroke-width="%s"%s%s/>' % (
        x1, y1, x2, y2, color, w, ' marker-end="url(#%s)"' % mk if mk else "", ' stroke-dasharray="%s"' % dash if dash else "")


def blocks(color, gap_color=BG):
    """ブロック文字の棒の背景(9px の塊と 3px の隙間)。"""
    return "repeating-linear-gradient(90deg,%s 0 9px,%s 9px 12px)" % (color, gap_color)


def shell(title, sub, source, body, extra_css=""):
    """1 枚の HTML。title の中の <em> が青緑になる。"""
    return "\n".join([
        '<!doctype html><meta charset="utf-8"><style>%s%s</style><body>' % (CSS, extra_css),
        "<h1>%s</h1>" % title,
        '<div class="sub">%s</div>' % sub,
        body,
        '<div class="src">%s</div>' % source,
        "</body>",
    ])


# 本体の上下の余白を測る。見出し(h1)・副題(.sub)・出典(.src)を除き、実際に描かれているもの
# (文字・SVG の図形・塗りのある箱・罫線)の範囲を取る。余白(padding)は数えない
_MEASURE = """() => {
  const skip = el => el.closest('h1,.sub,.src,defs,marker,pattern,clipPath');
  let top = Infinity, bottom = -Infinity;
  const add = (t, b) => { if (b > t || b === t) { top = Math.min(top, t); bottom = Math.max(bottom, b); } };
  for (const el of document.body.querySelectorAll('*')) {
    if (skip(el) || el.matches('svg.wires')) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    if (el instanceof SVGGraphicsElement && !(el instanceof SVGSVGElement)) {
      if (['path','rect','line','polygon','circle','text'].includes(el.tagName)) add(r.top, r.bottom);
      continue;
    }
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden') continue;
    const filled = cs.backgroundImage !== 'none' || !/rgba\\(0, 0, 0, 0\\)|transparent/.test(cs.backgroundColor);
    const sides = ['Top','Right','Bottom','Left'].every(k => parseFloat(cs['border' + k + 'Width']) > 0);
    if ((filled && !el.matches('.row')) || sides) add(r.top, r.bottom);
    else {
      if (parseFloat(cs.borderTopWidth) > 0) add(r.top, r.top + parseFloat(cs.borderTopWidth));
      if (parseFloat(cs.borderBottomWidth) > 0) add(r.bottom - parseFloat(cs.borderBottomWidth), r.bottom);
    }
    for (const n of el.childNodes) {
      if (n.nodeType !== 3 || !n.textContent.trim()) continue;
      const rg = document.createRange(); rg.selectNodeContents(n);
      for (const tr of rg.getClientRects()) add(tr.top, tr.bottom);
    }
  }
  const sub = document.querySelector('.sub').getBoundingClientRect().bottom;
  const src = document.querySelector('.src').getBoundingClientRect().top;
  const over = [...document.body.querySelectorAll('*')].filter(el => {
    const r = el.getBoundingClientRect();
    return r.width > 0 && (r.right > 1200.5 || r.left < -0.5);
  }).length;
  return {top: Math.round(top - sub), bottom: Math.round(src - bottom), over};
}"""

BALANCE_TOLERANCE = 12   # 上下の余白の差の許容(px)


def render(figs, out_dir, scale=2):
    """figs: [(名前, HTML), ...]。HTML と PNG を書き出し、本体の上下の余白を測って表示する。

    戻り値は余白が揃っていない(差が BALANCE_TOLERANCE を超える)か、横にはみ出した図の名前の一覧。
    """
    from playwright.sync_api import sync_playwright
    for name, html in figs:
        with open(os.path.join(out_dir, name + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
    bad = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=scale)
        for name, _ in figs:
            pg.goto("file://" + os.path.join(out_dir, name + ".html"))
            pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(out_dir, name + ".png"))
            m = pg.evaluate(_MEASURE)
            ok = abs(m["top"] - m["bottom"]) <= BALANCE_TOLERANCE and m["over"] == 0
            print("%s %s  本体の余白 上 %dpx / 下 %dpx%s" % (
                "ok  " if ok else "WARN", name, m["top"], m["bottom"],
                "" if m["over"] == 0 else "  横にはみ出し %d 要素" % m["over"]))
            if not ok:
                bad.append(name)
        b.close()
    if bad:
        print("上下の余白が揃っていない図: %s(中身を縦に広げてから、位置で揃える)" % ", ".join(bad))
    return bad
