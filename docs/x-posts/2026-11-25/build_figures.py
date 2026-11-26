#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""X のポストに付ける図 3 枚を、座標を計算して SVG(HTML)に書き出す。

線の端点は図形の辺の中点から一定の間隔(GAP)を空けて置き、矢じりは線の終点に
三角形として描く(線が矢じりを突き抜けない)。PNG への変換は render.py が行う。

使い方: python3 build_figures.py   # 同じフォルダに 0*.html を書き出す
"""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 675
L, R = 72, 1128
INK, SEC, MUTED, HAIR = "#16181d", "#4a4f57", "#757a82", "#c9ccd1"
ACC, ACC_SOFT, NEUTRAL = "#1f4e79", "#e8eef5", "#b9bec6"
SANS = "'Helvetica Neue','Hiragino Sans',sans-serif"
MATH = "'STIX Two Text','Times New Roman',serif"
GAP = 6          # 線の端点と図形の辺の間隔
RX = 12          # 箱の角の丸み
AL, AH = 11, 3.6  # 矢じりの長さと半幅


def text(x, y, s, size=17, weight=300, fill=INK, anchor="start"):
    return '<text x="%.2f" y="%.2f" font-size="%s" font-weight="%s" fill="%s" text-anchor="%s">%s</text>' % (
        x, y, size, weight, fill, anchor, s)


def it(s):
    return '<tspan font-family="%s" font-style="italic" font-size="1.08em">%s</tspan>' % (MATH, s)


def line(x1, y1, x2, y2, color=INK, w=1, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="%s" stroke-width="%s" stroke-linecap="round"%s/>' % (
        x1, y1, x2, y2, color, w, d)


def rect(x, y, w, h, stroke=INK, fill="none", sw=1, rx=0):
    return '<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" rx="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (
        x, y, w, h, rx, fill, stroke, sw)


def arrow(x1, y1, x2, y2, color=INK, w=1):
    """(x2, y2) を矢じりの先端にする。線は矢じりの底辺の中点で止める。"""
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    bx, by = x2 - ux * AL, y2 - uy * AL
    px, py = -uy * AH, ux * AH
    tx, ty = x2 - ux * 1.6, y2 - uy * 1.6   # 角を丸める線の太さの分だけ、先端を内側に置く
    return line(x1, y1, bx, by, color, w) + (
        '<polygon points="%.2f,%.2f %.2f,%.2f %.2f,%.2f" fill="%s" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>' % (
            tx, ty, bx + px, by + py, bx - px, by - py, color, color))


def frame(title, sub, source, body):
    parts = [
        '<!doctype html><meta charset="utf-8"><style>html,body{margin:0;background:#fff}</style>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" font-family="%s">' % (W, H, W, H, SANS),
        '<rect width="%d" height="%d" fill="#fff"/>' % (W, H),
        text(L, 76, title, 27, 600),
        text(L, 109, sub, 16.5, 300, SEC),
        line(L, 132, R, 132, HAIR, 0.75),
        body,
        line(L, 610, R, 610, HAIR, 0.75),
        text(L, 637, source, 14.5, 300, MUTED),
        "</svg>",
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------- 図 1
def fig_security():
    b = ['<defs><pattern id="h" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         '<line x1="0" y1="0" x2="0" y2="7" stroke="%s" stroke-width="1"/></pattern></defs>' % ACC]
    x0, bx, bw, bh = 196, 640, 210, 104   # 流れの始点、モデルの箱
    offs = [-39, -26, -13, 0, 13, 26, 39]

    def panel(cy, tag, title, desc, defended):
        o = [text(L, cy - 88, '<tspan font-weight="600">%s</tspan><tspan dx="14" font-weight="600">%s</tspan>'
                  '<tspan dx="14" fill="%s" font-size="15.5">%s</tspan>' % (tag, title, SEC, desc), 18)]
        o.append(text(L, cy + 6, "攻撃者の入力", 17))
        top, bot = cy - bh / 2, cy + bh / 2
        if defended == "model":
            for d in offs:
                o.append(arrow(x0, cy + d, bx - GAP, cy + d, SEC, 1))
            o.append(text(x0, cy - 54, "チャネルの帯域 %s" % it("W"), 15.5, 300, SEC))
            o.append('<clipPath id="mc"><rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" rx="%s"/></clipPath>' % (bx, top, bw, bh, RX))
            o.append('<g clip-path="url(#mc)">' + rect(bx, top, 28, bh, "none", ACC_SOFT, 0)
                     + rect(bx, top, 28, bh, "none", "url(#h)", 0) + '</g>')
            o.append('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" stroke="%s" stroke-width="1"/>' % (bx + 28, top, bx + 28, bot, ACC))
            o.append(rect(bx, top, bw, bh, INK, "none", 1.25, RX))
            o.append(text(bx + 28 + (bw - 28) / 2, cy + 6.5, "モデル", 18, 600, INK, "middle"))
            o.append(line(bx + 14, bot, bx + 14, bot + 22, ACC, 1))
            o.append(text(bx, bot + 42, "防御層：ノイズの抑制・信号の強化", 15.5, 300, INK))
        else:
            gx, gw, slit = 430, 8, 21
            for d in offs:
                if abs(d) <= 13:
                    o.append(arrow(x0, cy + d, bx - GAP, cy + d, SEC, 1))
                else:
                    o.append(line(x0, cy + d, gx, cy + d, SEC, 1))
            o.append(rect(gx, top, gw, bh / 2 - slit, "none", ACC, 0, gw / 2))
            o.append(rect(gx, cy + slit, gw, bh / 2 - slit, "none", ACC, 0, gw / 2))
            o.append(text(x0, cy - 54, "チャネルの帯域 %s" % it("W"), 15.5, 300, SEC))
            o.append(text(gx + gw + 14, cy - 34, "実効帯域 %s &lt; %s" % (it("W′"), it("W")), 15.5, 300, SEC))
            o.append(rect(bx, top, bw, bh, INK, "none", 1.25, RX))
            o.append(text(bx + bw / 2, cy + 6.5, "モデル", 18, 600, INK, "middle"))
            o.append(line(gx + gw / 2, bot, gx + gw / 2, bot + 22, ACC, 1))
            o.append(text(gx, bot + 42, "境界の制約：許可する情報流とエージェントの行動を限定", 15.5, 300, INK))
        o.append(arrow(bx + bw + GAP, cy, 916, cy, INK, 1))
        return o

    b += panel(250, "a", "モデルの内部で防ぐ", "従来の中心的な方式", "model")
    b.append(text(932, 250 - 6, "適応的な攻撃に対し", 16.5, 300, SEC))
    b.append(text(932, 250 + 19, "効果が逓減する", 17.5, 600))
    b += panel(468, "b", "システムの境界で防ぐ", "モデルに届く前に経路を絞る方式", "system")
    b.append(text(932, 468 - 6, "敵対的な影響に", 16.5, 300, SEC))
    b.append(text(932, 468 + 19, "より強い上限を課す", 17.5, 600))
    return frame("防御を置く層と、適応的な攻撃に対する限界",
                 "マルチモーダル基盤モデルの防御を、情報理論（チャネル容量・信号・ノイズ・帯域）で整理した概念図",
                 "出典: Sun, Chang, Pearce, Xiao, Li, “SoK: The Security-Safety Continuum of Multimodal Foundation Models” (2026) の要旨に基づく概念図。数値は含まない。",
                 "\n".join(b))


# ---------------------------------------------------------------- 図 2
def fig_nudge():
    bw, bh = 240, 64
    X, M, Y = (L, 318), (480, 178), (R - bw, 318)
    b = [rect(X[0], X[1], bw, bh, INK, "none", 1.25, RX),
         rect(M[0], M[1], bw, bh, ACC, ACC_SOFT, 1.25, RX),
         rect(Y[0], Y[1], bw, bh, INK, "none", 1.25, RX)]
    for (x, y), s in ((X, "AI によるナッジ"), (M, "自己アイデンティティ"), (Y, "持続可能な消費行動")):
        b.append(text(x + bw / 2, y + bh / 2 + 6.5, s, 18, 600, INK, "middle"))
    xc, mc, yc = X[0] + bw / 2, M[1] + bh / 2, X[1] + bh / 2
    b.append(arrow(xc, X[1] - GAP, M[0] - GAP, mc, ACC, 1.25))                    # X → M
    b.append(arrow(M[0] + bw + GAP, mc, Y[0] + bw / 2, Y[1] - GAP, ACC, 1.25))     # M → Y
    b.append(arrow(X[0] + bw + GAP, yc, Y[0] - GAP, yc, INK, 1.25))               # X → Y
    beta = it("β")
    b.append(text(318, 248, "%s = 0.312***" % beta, 19, 500, INK, "end"))
    b.append(text(882, 248, "%s = 0.509***" % beta, 19, 500, INK, "start"))
    b.append(text(600, 300, "間接効果 %s = 0.159 [95%% CI 0.110, 0.207]" % beta, 16.5, 300, INK, "middle"))
    b.append(text(600, yc + 28, "直接効果", 16.5, 300, INK, "middle"))
    b.append(text(Y[0] + bw / 2, Y[1] + bh + 26, "%s² = 0.459" % it("R"), 15.5, 300, SEC, "middle"))
    # 総効果の内訳
    by, bhh, full = 468, 14, R - L
    wd = (full - 2) * 0.621
    b.append(text(L, by - 16, "総効果の内訳", 15.5, 300, SEC))
    b.append('<clipPath id="pc"><rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" rx="%s"/></clipPath>' % (L, by, full, bhh, bhh / 2))
    b.append('<g clip-path="url(#pc)">' + rect(L, by, wd, bhh, "none", NEUTRAL, 0)
             + rect(L + wd + 2, by, full - 2 - wd, bhh, "none", ACC, 0) + '</g>')
    b.append(text(L, by + bhh + 27, '直接効果 <tspan font-weight="600">62.1%</tspan>', 17))
    b.append(text(R, by + bhh + 27, '自己アイデンティティを経由する間接効果 <tspan font-weight="600">37.9%</tspan>', 17, 300, INK, "end"))
    b.append(text(L, 572, "*** %s &lt; .001。%s = 406（インドのデジタル市場の消費者）、5 週間隔の 2 波調査、PLS-SEM。調整変数 3 つの交互作用は有意でない。" % (it("p"), it("n")), 14.5, 300, SEC))
    return frame("AI ナッジの効果の 37.9% は、自己アイデンティティを経由する",
                 "AI によるライフスタイル・ナッジと持続可能な消費行動の、部分媒介モデルの推定結果",
                 "出典: Rajratna, “AI-Based Lifestyle Nudges and Sustainable Consumption in Digital Marketplaces” (2026) の要旨の数値から作図。",
                 "\n".join(b))


# ---------------------------------------------------------------- 図 3
def fig_event():
    y0, unit = 520, 66            # 値 0 の位置、1 倍あたりの高さ
    gx1, gx2 = 112, 668
    b = [text(L, 166, "事後の検索活動（ユーザー内プラセボ = 1）", 15.5, 300, SEC)]
    for v in range(0, 6):
        y = y0 - v * unit
        b.append(line(gx1, y, gx2, y, INK if v == 0 else HAIR, 1 if v == 0 else 0.75))
        b.append(text(gx1 - 12, y + 5.5, str(v), 15.5, 300, MUTED, "end"))
    b.append(line(gx1, y0 - unit, gx2, y0 - unit, SEC, 1, "4 4"))
    bars = [(224, 1.00, NEUTRAL, ["ユーザー内", "プラセボ"]),
            (390, 3.42, ACC, ["既知のヌル時刻", "（何も起こさない）"]),
            (556, 4.32, "#8793a3", ["実際のイベント", "（AI の応答）"])]
    bw = 84
    for cx, v, col, lab in bars:
        h = v * unit
        x, y = cx - bw / 2, y0 - h
        b.append('<path d="M%.2f,%.2f V%.2f Q%.2f,%.2f %.2f,%.2f H%.2f Q%.2f,%.2f %.2f,%.2f V%.2f Z" fill="%s"/>' % (
            x, y0 - 0.5, y + 10, x, y, x + 10, y, x + bw - 10, x + bw, y, x + bw, y + 10, y0 - 0.5, col))
        b.append(text(cx, y - 12, "%.2f 倍" % v, 19, 600, INK, "middle"))
        b.append(text(cx, y0 + 27, lab[0], 15.5, 500 if v == 3.42 else 300, INK, "middle"))
        b.append(text(cx, y0 + 49, lab[1], 15.5, 300, SEC, "middle"))
    nx = 724
    notes = [("既知のヌル時刻", ["何の作用も持たないと分かっている時刻。", "この時刻の後の増加は、効果ではなく、", "すでに続いていたタスクの継続を表す。"]),
             ("読み取り", ["実際のイベントの後は 4.32 倍。", "ただし、何も起こさない時刻の後でも", "3.42 倍になる。"]),
             ("対象", ["事前活動と washout の基準を満たす", "AI 応答（全体の 5.8%）。"])]
    y = 200
    for head, lines in notes:
        b.append(line(nx, y - 22, R, y - 22, HAIR, 0.75))
        b.append(text(nx, y + 4, head, 16.5, 600))
        for i, s in enumerate(lines):
            b.append(text(nx, y + 32 + i * 25, s, 15.5, 300, SEC))
        y += 32 + len(lines) * 25 + 34
    return frame("何も起こさない時刻でも、事後の検索活動は 3.42 倍になる",
                 "利用者が自分で選んだ時点（AI アシスタントを開く等）を起点にしたときの、事後の検索活動の比",
                 "出典: Iannelli &amp; Ai, “Event-Time Confounding Under Bursty Human Dynamics” (2026), arXiv:2608.21294 の要旨の数値から作図。",
                 "\n".join(b))


if __name__ == "__main__":
    for name, fn in (("01-security", fig_security), ("02-nudge", fig_nudge), ("03-event-time", fig_event)):
        with open(os.path.join(HERE, name + ".html"), "w", encoding="utf-8") as f:
            f.write(fn())
        print("wrote", name + ".html")
