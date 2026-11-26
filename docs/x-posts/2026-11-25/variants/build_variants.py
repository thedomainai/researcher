#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""図 2(媒介モデル)を、3 つの方向性で描き分ける。方向性の比較用。

  A-illustration : イラスト調(太い輪郭線・手描きの揺らぎ・ステッカーの影)
  B-3d-pop       : 3D ポップ(粘土のような立体・太い管の矢印・光沢)
  C-glass        : リキッドグラス(ぼかした色の光・半透明の板・発光する線)

使い方: python3 build_variants.py   # 同じフォルダに HTML と PNG を書き出す
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = ("/Users/yuta/Library/Caches/ms-playwright/chromium_headless_shell-1243/"
          "chrome-headless-shell-mac-arm64/chrome-headless-shell")

NW, NH = 250, 78
XN, MN, YN = (72, 322), (475, 182), (878, 322)

ICON = {
    "ai": '<svg viewBox="0 0 24 24"><path d="M12 2.5l2.3 6.2 6.2 2.3-6.2 2.3L12 19.5l-2.3-6.2L3.5 11l6.2-2.3z"/><circle cx="19" cy="4.5" r="1.6"/></svg>',
    "id": '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4.2"/><path d="M4 21c.6-4.6 3.8-7 8-7s7.4 2.4 8 7z"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24"><path d="M20.5 3.5C11 3 4.5 7.5 4.5 14.5c0 1.6.5 3 1.300 4.200C8 13 12 9.500 16.500 7.500 12.500 10.500 9.300 14.500 7.500 20c6.500 1.500 13-2.500 13-16.500z"/></svg>',
}

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

THEMES = {
    "A-illustration": {
        "css": """
body{background:#FBF5E9;color:#2D2A32;font-family:'Hiragino Maru Gothic ProN','Hiragino Sans',sans-serif}
h1{font-weight:700}
h1 em{font-style:normal;background:linear-gradient(transparent 58%,#FFD45C 58%,#FFD45C 92%,transparent 92%);padding:0 4px}
.sub{color:#6B6470}
.node{border:2.6px solid #2D2A32;border-radius:24px;box-shadow:5px 6px 0 #2D2A32}
.node svg{fill:#2D2A32}
.nx{background:#FFE2A8}.nm{background:#FFA48F}.ny{background:#AEE0C6}
.mid,.cap{color:#4A4550}
.track div{border:2.6px solid #2D2A32;box-sizing:border-box}
.t1{background:#F1E9D8;border-radius:13px 4px 4px 13px}
.t2{background:#FFA48F;border-radius:4px 13px 13px 4px;box-shadow:4px 5px 0 #2D2A32}
.note,.src{color:#6B6470}
.dots{position:absolute;inset:0;background-image:radial-gradient(#2D2A3214 1.3px,transparent 1.4px);background-size:22px 22px}
""",
        "pre": '<div class="dots"></div>',
        "defs": ('<filter id="wob" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="7"/>'
                 '<feDisplacementMap in="SourceGraphic" scale="5"/></filter>'
                 '<marker id="ah" viewBox="0 0 14 14" refX="11" refY="7" markerWidth="14" markerHeight="14" orient="auto" markerUnits="userSpaceOnUse">'
                 '<path d="M2 2 L12 7 L2 12" fill="none" stroke="#2D2A32" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></marker>'),
        "wire": 'fill="none" stroke="#2D2A32" stroke-width="2.6" stroke-linecap="round" marker-end="url(#ah)" filter="url(#wob)"',
        "wire_direct": 'fill="none" stroke="#2D2A32" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="1 9" marker-end="url(#ah)"',
        "inset": 12,
    },
    "B-3d-pop": {
        "css": """
body{background:linear-gradient(135deg,#ECEBFF 0%,#FDEBF4 55%,#FFF3DE 100%);color:#26215C;
  font-family:'Hiragino Maru Gothic ProN','Hiragino Sans',sans-serif}
h1{font-weight:700}
h1 em{font-style:normal;color:#F0478F}
.sub{color:#5E5A8A}
.node{border-radius:30px;color:#fff;text-shadow:0 1px 2px rgba(0,0,0,.25)}
.node svg{fill:#fff;filter:drop-shadow(0 1px 1px rgba(0,0,0,.25))}
.nx{background:linear-gradient(180deg,#8E80FF,#5846E6);box-shadow:0 20px 28px -10px rgba(88,70,230,.6),inset 0 -9px 14px rgba(20,10,90,.35),inset 0 7px 10px rgba(255,255,255,.5)}
.nm{background:linear-gradient(180deg,#FF8FC0,#EE3F88);box-shadow:0 20px 28px -10px rgba(238,63,136,.6),inset 0 -9px 14px rgba(120,10,60,.35),inset 0 7px 10px rgba(255,255,255,.5)}
.ny{background:linear-gradient(180deg,#45E0BE,#0FAE88);box-shadow:0 20px 28px -10px rgba(15,174,136,.6),inset 0 -9px 14px rgba(0,80,60,.35),inset 0 7px 10px rgba(255,255,255,.5)}
.mid,.cap{color:#4B4780;font-weight:600}
.track{height:32px;gap:5px}
.t1{background:linear-gradient(180deg,#F4F3FF,#CFCBEF);border-radius:16px;box-shadow:0 12px 18px -8px rgba(80,70,160,.45),inset 0 -6px 9px rgba(60,50,140,.22),inset 0 5px 7px #fff}
.t2{background:linear-gradient(180deg,#FF8FC0,#EE3F88);border-radius:16px;box-shadow:0 12px 18px -8px rgba(238,63,136,.6),inset 0 -6px 9px rgba(120,10,60,.3),inset 0 5px 7px rgba(255,255,255,.55)}
.pl{top:518px}
.note,.src{color:#6F6B99}
.ball{position:absolute;border-radius:50%}
""",
        "pre": ('<div class="ball" style="left:1040px;top:-50px;width:190px;height:190px;background:radial-gradient(circle at 32% 28%,#FFE08A,#FFB020 60%,#E88A00);box-shadow:0 24px 30px -12px rgba(232,138,0,.5)"></div>'
                '<div class="ball" style="left:20px;top:150px;width:34px;height:34px;background:radial-gradient(circle at 32% 28%,#FFC2DC,#F0478F 65%);box-shadow:0 10px 12px -6px rgba(240,71,143,.55)"></div>'),
        "defs": ('<linearGradient id="g1" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#6D5CF0"/><stop offset="1" stop-color="#F0478F"/></linearGradient>'
                 '<linearGradient id="g2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F0478F"/><stop offset="1" stop-color="#12B892"/></linearGradient>'
                 '<filter id="sh" filterUnits="userSpaceOnUse" x="0" y="0" width="1200" height="675"><feDropShadow dx="0" dy="7" stdDeviation="5" flood-color="#5846E6" flood-opacity=".35"/></filter>'
                 + "".join('<marker id="ah%s" viewBox="0 0 12 12" refX="4" refY="6" markerWidth="26" markerHeight="26" orient="auto" markerUnits="userSpaceOnUse">'
                           '<path d="M2.500 2.200 L9.800 6 L2.500 9.800 Z" fill="%s" stroke="%s" stroke-width="2.200" stroke-linejoin="round"/></marker>' % (k, c, c)
                           for k, c in (("1", "#F0478F"), ("2", "#12B892"), ("3", "#B7B2E6")))),
        "wire": None,
        "inset": 22,
    },
    "C-glass": {
        "css": """
body{background:#0A0F1F;color:#F4F7FF;font-family:'Hiragino Sans','Helvetica Neue',sans-serif}
h1{font-weight:600;letter-spacing:.01em}
h1 em{font-style:normal;background:linear-gradient(90deg,#7DD3FC,#C4B5FD);-webkit-background-clip:text;color:transparent}
.sub{color:rgba(230,236,255,.7);font-weight:300}
.blob{position:absolute;border-radius:50%;filter:blur(60px)}
.panel{position:absolute;left:40px;top:146px;width:1120px;height:452px;border-radius:32px;background:rgba(255,255,255,.045);
  border:1px solid rgba(255,255,255,.16);box-shadow:inset 0 1px 0 rgba(255,255,255,.25)}
.node{border-radius:26px;font-weight:600;background:linear-gradient(135deg,rgba(255,255,255,.26),rgba(255,255,255,.07));
  -webkit-backdrop-filter:blur(22px) saturate(170%);backdrop-filter:blur(22px) saturate(170%);
  border:1px solid rgba(255,255,255,.42);box-shadow:0 14px 40px rgba(0,0,0,.35),inset 0 1px 0 rgba(255,255,255,.7),inset 0 -1px 0 rgba(255,255,255,.12)}
.node svg{fill:rgba(255,255,255,.92)}
.nm{background:linear-gradient(135deg,rgba(196,181,253,.42),rgba(125,211,252,.14));box-shadow:0 14px 44px rgba(124,58,237,.45),inset 0 1px 0 rgba(255,255,255,.75)}
.lab{font-weight:600}
.mid,.cap{color:rgba(230,236,255,.78);font-weight:300}
.track{height:22px;gap:4px}
.t1{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);border-radius:11px;box-sizing:border-box;box-shadow:inset 0 1px 0 rgba(255,255,255,.4)}
.t2{background:linear-gradient(90deg,#7DD3FC,#A78BFA);border-radius:11px;box-shadow:0 0 22px rgba(167,139,250,.75),inset 0 1px 0 rgba(255,255,255,.7)}
.pl{font-weight:300}.pl b{font-weight:600}
.note,.src{color:rgba(230,236,255,.6);font-weight:300}
""",
        "pre": ('<div class="blob" style="left:-80px;top:180px;width:420px;height:420px;background:#2563EB;opacity:.75"></div>'
                '<div class="blob" style="left:400px;top:20px;width:400px;height:360px;background:#7C3AED;opacity:.8"></div>'
                '<div class="blob" style="left:800px;top:240px;width:440px;height:420px;background:#0D9488;opacity:.75"></div>'
                '<div class="blob" style="left:520px;top:420px;width:260px;height:220px;background:#DB2777;opacity:.45"></div>'
                '<div class="panel"></div>'),
        "defs": ('<filter id="glow" x="-20%" y="-60%" width="140%" height="220%"><feGaussianBlur stdDeviation="3.500" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
                 '<marker id="ah" viewBox="0 0 12 12" refX="9.500" refY="6" markerWidth="13" markerHeight="13" orient="auto" markerUnits="userSpaceOnUse">'
                 '<path d="M2.500 2.500 L10 6 L2.500 9.500" fill="none" stroke="#fff" stroke-width="1.600" stroke-linecap="round" stroke-linejoin="round"/></marker>'),
        "wire": 'fill="none" stroke="#fff" stroke-width="1.600" stroke-linecap="round" marker-end="url(#ah)" filter="url(#glow)" opacity=".95"',
        "wire_direct": 'fill="none" stroke="#fff" stroke-width="1.600" stroke-linecap="round" marker-end="url(#ah)" opacity=".55"',
        "inset": 10,
    },
    # B の形(丸み・厚み)を残し、色を 1 色・質感を艶消し・影を無彩色にした版
    "B2-calm": {
        "css": """
body{background:radial-gradient(1300px 760px at 28% 0%,#F8F7F4,#E8E6E1);color:#23262B;font-family:'Hiragino Sans','Helvetica Neue',sans-serif}
h1{font-weight:600;letter-spacing:.01em}
h1 em{font-style:normal;color:#2F6264}
.sub{color:#6E7278;font-weight:300}
.node{border-radius:28px;font-weight:600;font-size:18px;color:#23262B;background:linear-gradient(180deg,#FFFFFF,#F1EFEB);
  box-shadow:0 1px 1px rgba(40,38,32,.10),0 3px 6px rgba(40,38,32,.08),0 24px 34px -16px rgba(40,38,32,.30),inset 0 1px 0 #fff,inset 0 -7px 10px rgba(60,55,45,.06)}
.node svg{fill:#9A9EA4;width:21px;height:21px}
.nm{background:linear-gradient(180deg,#3F7678,#2B585A);color:#F6F5F1;
  box-shadow:0 1px 1px rgba(20,40,40,.20),0 3px 6px rgba(20,40,40,.14),0 24px 34px -16px rgba(20,45,46,.50),inset 0 1px 0 rgba(255,255,255,.24),inset 0 -8px 12px rgba(0,0,0,.14)}
.nm svg{fill:#C9DCDB}
.lab{font-weight:500;font-size:19px}
.mid,.cap{color:#5B5F66;font-weight:400}
.track{height:28px;gap:6px}
.t1{background:linear-gradient(180deg,#DEDCD6,#E9E7E2);border-radius:14px;box-shadow:inset 0 2px 4px rgba(40,38,32,.16),0 1px 0 rgba(255,255,255,.9)}
.t2{background:linear-gradient(180deg,#3F7678,#2B585A);border-radius:14px;
  box-shadow:0 2px 4px rgba(20,40,40,.16),0 14px 20px -10px rgba(20,45,46,.50),inset 0 1px 0 rgba(255,255,255,.24),inset 0 -5px 8px rgba(0,0,0,.14)}
.pl{top:516px;font-weight:400;color:#5B5F66}.pl b{font-weight:600;color:#23262B}
.pl[style*="right"] b{color:#2F6264}
.note,.src{color:#8A8E94}
""",
        "pre": "",
        "defs": "".join('<marker id="%s" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="15" markerHeight="15" orient="auto" markerUnits="userSpaceOnUse">'
                        '<path d="M3 2.800 L9.500 6 L3 9.200 Z" fill="%s" stroke="%s" stroke-width="1.600" stroke-linejoin="round"/></marker>' % (k, c, c)
                        for k, c in (("ah", "#2F6264"), ("ahd", "#A4A7AB"))),
        "wire": 'fill="none" stroke="#2F6264" stroke-width="2.400" stroke-linecap="round" marker-end="url(#ah)"',
        "wire_direct": 'fill="none" stroke="#A4A7AB" stroke-width="2.400" stroke-linecap="round" marker-end="url(#ahd)"',
        "inset": 12,
    },
    # B2 の落ち着いた色のまま、質感をすりガラスと液体に替えた版(明るい地)
    "C2-calm-glass": {
        "css": """
body{background:#F3F2EE;color:#1F2A2C;font-family:'Hiragino Sans','Helvetica Neue',sans-serif}
h1{font-weight:600;letter-spacing:.01em}
h1 em{font-style:normal;color:#2F6264}
.sub{color:#5F6B6E;font-weight:300}
.blob{position:absolute;filter:blur(46px)}
.node{border-radius:39px;font-weight:600;font-size:18px;color:#1F2A2C;
  background:linear-gradient(135deg,rgba(255,255,255,.66),rgba(255,255,255,.26));
  -webkit-backdrop-filter:blur(20px) saturate(150%);backdrop-filter:blur(20px) saturate(150%);
  border:1px solid rgba(255,255,255,.85);
  box-shadow:0 16px 32px -14px rgba(28,54,58,.34),0 2px 5px rgba(28,54,58,.07),inset 0 1px 0 #fff,inset 0 -10px 16px -8px rgba(255,255,255,.55)}
.node::before{content:"";position:absolute;left:16px;right:16px;top:5px;height:22px;border-radius:20px;
  background:linear-gradient(180deg,rgba(255,255,255,.75),rgba(255,255,255,0))}
.node svg{fill:#5E7D80;width:21px;height:21px;position:relative}
.node span{position:relative}
.nm{color:#fff;background:linear-gradient(135deg,rgba(54,112,115,.80),rgba(36,82,86,.62));border:1px solid rgba(255,255,255,.55);
  box-shadow:0 18px 34px -14px rgba(22,62,66,.60),0 2px 5px rgba(22,62,66,.14),inset 0 1px 0 rgba(255,255,255,.55),inset 0 -10px 16px -8px rgba(160,220,222,.35)}
.nm::before{background:linear-gradient(180deg,rgba(255,255,255,.34),rgba(255,255,255,0))}
.nm svg{fill:#DCEDEC}
.lab{font-weight:500;font-size:19px}
.mid,.cap{color:#4E5A5D;font-weight:400}
.track{height:28px;gap:6px}
.t1,.t2{border-radius:14px;box-sizing:border-box;position:relative}
.t1{background:linear-gradient(180deg,rgba(255,255,255,.34),rgba(255,255,255,.62));border:1px solid rgba(255,255,255,.9);
  -webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);
  box-shadow:inset 0 2px 5px rgba(28,54,58,.14),0 8px 16px -10px rgba(28,54,58,.25)}
.t2{background:linear-gradient(180deg,rgba(70,136,139,.92),rgba(36,82,86,.92));border:1px solid rgba(255,255,255,.6);
  box-shadow:0 12px 22px -10px rgba(22,62,66,.60),inset 0 -6px 9px rgba(10,40,44,.25)}
.t2::before{content:"";position:absolute;left:10px;right:10px;top:3px;height:8px;border-radius:6px;
  background:linear-gradient(180deg,rgba(255,255,255,.55),rgba(255,255,255,0))}
.pl{top:516px;font-weight:400;color:#4E5A5D}.pl b{font-weight:600;color:#1F2A2C}
.pl[style*="right"] b{color:#2F6264}
.note,.src{color:#7C8689}
""",
        "pre": ('<div class="blob" style="left:330px;top:90px;width:560px;height:330px;background:#3F8387;opacity:.50;border-radius:58% 42% 63% 37%/46% 58% 42% 54%"></div>'
                '<div class="blob" style="left:-40px;top:250px;width:420px;height:300px;background:#E6C7A0;opacity:.75;border-radius:44% 56% 38% 62%/55% 43% 57% 45%"></div>'
                '<div class="blob" style="left:800px;top:230px;width:460px;height:320px;background:#A9C4D2;opacity:.80;border-radius:61% 39% 47% 53%/40% 60% 40% 60%"></div>'
                '<div class="blob" style="left:520px;top:400px;width:420px;height:180px;background:#CFE3DD;opacity:.80;border-radius:50%"></div>'),
        "defs": "".join('<marker id="%s" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="15" markerHeight="15" orient="auto" markerUnits="userSpaceOnUse">'
                        '<path d="M3 2.800 L9.500 6 L3 9.200 Z" fill="%s" stroke="%s" stroke-width="1.600" stroke-linejoin="round"/></marker>' % (k, c, c)
                        for k, c in (("ah", "#24575A"), ("ahd", "#8C999C"))),
        "wire": 'fill="none" stroke="#24575A" stroke-width="2.200" stroke-linecap="round" marker-end="url(#ah)"',
        "wire_direct": 'fill="none" stroke="#8C999C" stroke-width="2.200" stroke-linecap="round" marker-end="url(#ahd)"',
        "inset": 12,
    },
    # 端末(CLI)の画面の様式。等幅の文字・細い罫線・直角の線・ブロック文字の棒
    "D-terminal": {
        "css": """
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
""",
        "pre": "",
        "defs": "".join('<marker id="%s" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="13" markerHeight="13" orient="auto" markerUnits="userSpaceOnUse">'
                        '<path d="M3 2.500 L9.500 6 L3 9.500" fill="none" stroke="%s" stroke-width="1.600" stroke-linecap="round" stroke-linejoin="round"/></marker>' % (k, c)
                        for k, c in (("ah", "#6FB7AC"), ("ahd", "#6A7078"))),
        "wire": 'fill="none" stroke="#6FB7AC" stroke-width="1.500" stroke-linejoin="round" marker-end="url(#ah)"',
        "wire_direct": 'fill="none" stroke="#6A7078" stroke-width="1.500" stroke-dasharray="5 5" marker-end="url(#ahd)"',
        "inset": 8,
        "ortho": True,
    },
}


def wires(name, t):
    g = t["inset"]
    xc, yc = XN[0] + NW / 2, XN[1] + NH / 2
    mc = MN[1] + NH / 2
    p1 = "M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" % (xc, XN[1] - g, xc + 8, mc, MN[0] - g, mc)
    p2 = "M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" % (MN[0] + NW + g, mc, YN[0] + NW / 2 - 8, mc, YN[0] + NW / 2, YN[1] - g)
    p3 = "M%.1f,%.1f L%.1f,%.1f" % (XN[0] + NW + g, yc, YN[0] - g, yc)
    if t.get("ortho"):
        p1 = "M%.1f,%.1f V%.1f H%.1f" % (xc, XN[1] - g, mc, MN[0] - g)
        p2 = "M%.1f,%.1f H%.1f V%.1f" % (MN[0] + NW + g, mc, YN[0] + NW / 2, YN[1] - g)
    if name == "B-3d-pop":
        base = 'fill="none" stroke-width="11" stroke-linecap="round" filter="url(#sh)"'
        return ('<path d="%s" stroke="url(#g1)" marker-end="url(#ah1)" %s/>' % (p1, base)
                + '<path d="%s" stroke="url(#g2)" marker-end="url(#ah2)" %s/>' % (p2, base)
                + '<path d="%s" stroke="#B7B2E6" marker-end="url(#ah3)" %s/>' % (p3, base))
    return ('<path d="%s" %s/><path d="%s" %s/><path d="%s" %s/>' % (p1, t["wire"], p2, t["wire"], p3, t["wire_direct"]))


def page(name, t):
    def node(pos, cls, icon, label):
        return '<div class="node %s" style="left:%dpx;top:%dpx">%s<span>%s</span></div>' % (cls, pos[0], pos[1], ICON[icon], label)
    yc = XN[1] + NH / 2
    parts = [
        '<!doctype html><meta charset="utf-8"><style>%s%s</style><body>' % (BASE_CSS, t["css"]),
        t["pre"],
        '<h1>AI ナッジの効果の <em>37.9%</em> は、自己アイデンティティを経由する</h1>',
        '<div class="sub">AI によるライフスタイル・ナッジと持続可能な消費行動の、部分媒介モデルの推定結果</div>',
        '<svg class="wires" width="1200" height="675" viewBox="0 0 1200 675"><defs>%s</defs>%s</svg>' % (t["defs"], wires(name, t)),
        node(XN, "nx", "ai", "AI によるナッジ"),
        node(MN, "nm", "id", "自己アイデンティティ"),
        node(YN, "ny", "leaf", "持続可能な消費行動"),
        '<div class="lab" style="right:%dpx;top:226px"><i>β</i> = 0.312***</div>' % (1200 - 204),
        '<div class="lab" style="left:1002px;top:226px"><i>β</i> = 0.509***</div>',
        '<div class="mid" style="top:290px">間接効果 <i style="font-family:\'STIX Two Text\',serif">β</i> = 0.159 [95% CI 0.110, 0.207]</div>',
        '<div class="mid" style="top:%dpx">直接効果</div>' % (yc + 18),
        '<div class="cap">総効果の内訳</div>',
        '<div class="track"><div class="t1" style="width:62.1%"></div><div class="t2" style="flex:1"></div></div>',
        '<div class="pl" style="left:72px">直接効果 <b>62.1%</b></div>',
        '<div class="pl" style="right:72px">自己アイデンティティを経由する間接効果 <b>37.9%</b></div>',
        '<div class="note">*** <i>p</i> &lt; .001。<i>n</i> = 406（インドのデジタル市場の消費者）、5 週間隔の 2 波調査、PLS-SEM。調整変数 3 つの交互作用は有意でない。</div>',
        '<div class="src">出典: Rajratna, “AI-Based Lifestyle Nudges and Sustainable Consumption in Digital Marketplaces” (2026) の要旨の数値から作図。</div>',
        "</body>",
    ]
    return "\n".join(parts)


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    for name, t in THEMES.items():
        with open(os.path.join(HERE, name + ".html"), "w", encoding="utf-8") as f:
            f.write(page(name, t))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={"width": 1200, "height": 675}, device_scale_factor=2)
        for name in THEMES:
            pg.goto("file://" + os.path.join(HERE, name + ".html"))
            pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(HERE, name + ".png"))
            print("ok", name)
        b.close()
