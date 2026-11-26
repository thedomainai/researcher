#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""X のポストに付ける図 3 枚を、端末(CLI)の画面の様式で書き出す。

様式と部品は ../terminal_style.py にある(今後の図も同じものを使う)。図 2 は variants/build_variants.py の D-terminal を使う。
以前の様式(白地・紺)は build_figures.py に残してある。

使い方: python3 build_terminal.py   # 同じフォルダの 0*.html と 0*.png を書き換える
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, os.path.join(HERE, "variants"))
from terminal_style import (ACC, BG, BODY, EDGE, FLOW, INK, L, MUTED, PANEL, SEC,  # noqa: E402
                            COMPONENT_CSS, marker, render, seg, shell)
from build_variants import THEMES, page  # noqa: E402  (図 2 は比較用の D-terminal をそのまま使う)

T = THEMES["D-terminal"]
EXTRA_CSS = COMPONENT_CSS


# ---------------------------------------------------------------- 図 1
def fig_security():
    x0, bx, bw, bh = 212, 640, 210, 104
    offs = [-39, -26, -13, 0, 13, 26, 39]
    svg, html = [], []

    def panel(cy, tag, title, desc, mode, r1, r2, acc):
        top, bot = cy - bh / 2, cy + bh / 2
        html.append('<div class="ph" style="top:%dpx"><span class="tag">%s</span><b>%s</b><span class="cm"># %s</span></div>' % (cy - 106, tag, title, desc))
        html.append('<div class="t" style="left:72px;top:%dpx;color:%s">攻撃者の入力</div>' % (cy - 10, BODY))
        html.append('<div class="t" style="left:%dpx;top:%dpx">帯域 W</div>' % (x0, cy - 70))
        svg.append('<rect x="%d" y="%.1f" width="%d" height="%d" rx="8" fill="%s" stroke="%s" stroke-width="1"/>' % (bx, top, bw, bh, PANEL, EDGE))
        if mode == "model":
            for d in offs:
                svg.append(seg(x0, cy + d, bx - 8, cy + d, FLOW, 1.2, "af"))
            svg.append('<clipPath id="mc"><rect x="%d" y="%.1f" width="%d" height="%d" rx="8"/></clipPath>' % (bx, top, bw, bh))
            svg.append('<g clip-path="url(#mc)"><rect x="%d" y="%.1f" width="28" height="%d" fill="%s" opacity=".16"/>'
                       '<rect x="%d" y="%.1f" width="28" height="%d" fill="url(#blk)"/></g>' % (bx, top, bh, ACC, bx, top, bh))
            svg.append(seg(bx + 28, top, bx + 28, bot, ACC, 1))
            html.append('<div class="t" style="left:%dpx;top:%dpx;width:%dpx;text-align:center;color:%s;font-size:17px;font-weight:600">モデル</div>' % (bx + 28, cy - 12, bw - 28, INK))
            svg.append(seg(bx + 14, bot + 1, bx + 14, bot + 22, ACC, 1))
            html.append('<div class="t" style="left:%dpx;top:%dpx;color:%s">防御層：ノイズの抑制・信号の強化</div>' % (bx, bot + 28, BODY))
        else:
            gx, gw, slit = 430, 8, 21
            for d in offs:
                if abs(d) <= 13:
                    svg.append(seg(x0, cy + d, bx - 8, cy + d, FLOW, 1.2, "af"))
                else:
                    svg.append(seg(x0, cy + d, gx - 16, cy + d, FLOW, 1.2))
                    svg.append(seg(gx - 12, cy + d - 3.5, gx - 5, cy + d + 3.5, ACC, 1.4))
                    svg.append(seg(gx - 12, cy + d + 3.5, gx - 5, cy + d - 3.5, ACC, 1.4))
            svg.append('<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="%s"/>' % (gx, top, gw, bh / 2 - slit, ACC))
            svg.append('<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="%s"/>' % (gx, cy + slit, gw, bh / 2 - slit, ACC))
            html.append('<div class="t" style="left:%dpx;top:%dpx">実効帯域 W′ &lt; W</div>' % (gx + gw + 14, cy - 50))
            html.append('<div class="t" style="left:%dpx;top:%dpx;width:%dpx;text-align:center;color:%s;font-size:17px;font-weight:600">モデル</div>' % (bx, cy - 12, bw, INK))
            svg.append(seg(gx + gw / 2, bot + 1, gx + gw / 2, bot + 22, ACC, 1))
            html.append('<div class="t" style="left:%dpx;top:%dpx;color:%s">境界の制約：許可する情報流とエージェントの行動を限定</div>' % (gx, bot + 28, BODY))
        svg.append(seg(bx + bw + 8, cy, 912, cy, BODY, 1.2, "ai"))
        html.append('<div class="t" style="left:932px;top:%dpx">%s</div>' % (cy - 24, r1))
        html.append('<div class="t" style="left:932px;top:%dpx"><b%s>%s</b></div>' % (cy + 2, ' class="acc"' if acc else "", r2))

    panel(258, "a", "モデルの内部で防ぐ", "従来の中心的な方式", "model", "適応的な攻撃に対し", "効果が逓減する", False)
    panel(482, "b", "システムの境界で防ぐ", "モデルに届く前に経路を絞る方式", "system", "敵対的な影響に", "より強い上限を課す", True)
    defs = (marker("af", FLOW) + marker("ai", BODY)
            + '<pattern id="blk" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="3" height="6" fill="%s" opacity=".55"/></pattern>' % ACC)
    body = ('<svg class="wires" width="1200" height="675" viewBox="0 0 1200 675"><defs>%s</defs>%s</svg>' % (defs, "".join(svg))
            + "\n".join(html))
    return shell("防御を置く層と、適応的な攻撃に対する限界",
                 "マルチモーダル基盤モデルの防御を、情報理論（チャネル容量・信号・ノイズ・帯域）で整理した概念図",
                 "出典: Sun et al., “SoK: The Security-Safety Continuum of Multimodal Foundation Models” (2026) の要旨に基づく概念図。数値は含まない。",
                 body)


# ---------------------------------------------------------------- 図 2
def fig_nudge():
    extra = ('<div class="t" style="left:878px;top:410px;width:250px;text-align:center;font-size:14px;color:%s">R² = 0.459</div>' % MUTED)
    html = page("D-terminal", T)
    assert html.count("</body>") == 1
    # 上下の余白を揃えるため、経路図(箱・係数・矢印・R²)を 20px 上げ、内訳の棒との間を広げる
    lift = ".node,.lab,.mid,svg.wires,.t{translate:0 -20px}"
    return html.replace("</body>", extra + "\n</body>").replace("<style>", "<style>" + EXTRA_CSS + lift, 1)


# ---------------------------------------------------------------- 図 3
def fig_event():
    unit = 100                    # 1 倍あたりの幅
    rows = [(210, 1.00, EDGE, "ユーザー内プラセボ", "基準", False),
            (334, 3.42, ACC, "既知のヌル時刻", "何も起こさない", True),
            (458, 4.32, "#9CA2AA", "実際のイベント", "AI の応答", False)]
    html = ['<div class="t" style="left:72px;top:160px">事後の検索活動（ユーザー内プラセボ = 1）</div>']
    svg = []
    for v in range(0, 6):
        x = L + v * unit
        svg.append(seg(x, 200, x, 558, SEC if v == 1 else "#26292D", 1, None, "4 4" if v == 1 else None))
        html.append('<div class="tick" style="left:%dpx">%d</div>' % (x, v))
    svg.append(seg(L, 558, L + 5 * unit, 558, EDGE, 1))
    for top, v, col, name, cm, acc in rows:
        w = v * unit
        html.append('<div class="row" style="top:%dpx">%s<span class="cm"># %s</span></div>' % (top, name, cm))
        html.append('<div class="bar" style="top:%dpx;width:%.1fpx;background:repeating-linear-gradient(90deg,%s 0 9px,%s 9px 12px)"></div>' % (top + 32, w, col, BG))
        html.append('<div class="val%s" style="left:%.1fpx;top:%dpx">%.2f 倍</div>' % (" acc" if acc else "", L + w + 14, top + 32, v))
    notes = [("既知のヌル時刻", "何の作用も持たないと分かっている時刻。<br>この時刻の後の増加は、効果ではなく、<br>すでに続いていたタスクの継続を表す。"),
             ("読み取り", "実際のイベントの後は 4.32 倍。<br>ただし、何も起こさない時刻の後でも<br>3.42 倍になる。"),
             ("対象", "事前活動と washout の基準を満たす<br>AI 応答（全体の 5.8%）。")]
    html.append('<div class="notes">%s</div>' % "".join("<div><h3>%s</h3><p>%s</p></div>" % n for n in notes))
    body = '<svg class="wires" width="1200" height="675" viewBox="0 0 1200 675">%s</svg>' % "".join(svg) + "\n".join(html)
    return shell("何も起こさない時刻でも、事後の検索活動は <em>3.42 倍</em>になる",
                 "利用者が自分で選んだ時点（AI アシスタントを開く等）を起点にしたときの、事後の検索活動の比",
                 "出典: Iannelli &amp; Ai, “Event-Time Confounding Under Bursty Human Dynamics” (2026), arXiv:2608.21294 の要旨の数値から作図。",
                 body)


if __name__ == "__main__":
    render([("01-security", fig_security()), ("02-nudge", fig_nudge()), ("03-event-time", fig_event())], HERE)
