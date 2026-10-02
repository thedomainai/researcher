#!/usr/bin/env python3
"""X アカウントのアイコン・ヘッダー画像と、プロフィール文・固定ポストの文面を config/x_accounts.yaml から作る。

出力:
  config/site_assets/x/avatar-<cluster>.png   400x400(領域色の円 + 領域の 2 字 + 「論文解説」)
  config/site_assets/x/header-<cluster>.png   1500x500
標準出力: アカウントごとの表示名・ハンドル・プロフィール文・固定ポスト(文字数の検査つき)

使い方: python3 tools/build_x_assets.py [--text-only]
"""

import argparse
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent
ACCOUNTS = BASE / "config" / "x_accounts.yaml"
SITE = BASE / "config" / "site.yaml"
OUT = BASE / "config" / "site_assets" / "x"

PAPER = (244, 240, 232)
INK = (22, 21, 15)
INK2 = (76, 72, 62)
COLORS = {
    "cognition": (79, 99, 216), "economics": (185, 130, 28), "organization": (213, 64, 42),
    "society": (63, 133, 82), "systems": (18, 143, 150), "ai": (141, 79, 199),
}
FONT_BOLD = "/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc"
FONT_REG = "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"
BIO_LIMIT = 160
POST_LIMIT = 280
URL_LENGTH = 23


def weighted_len(text):
    return sum(2 if ord(ch) > 0x2E7F else 1 for ch in text)


def texts(spec, site_url):
    defaults = spec["defaults"]
    rows = []
    for account in spec["accounts"]:
        others = " ".join("@" + a["handle"] for a in spec["accounts"] if a["cluster"] != account["cluster"])
        bio = defaults["bio_template"].format(label=account["label"], scope=account["scope"])
        pinned = defaults["pinned_template"].format(label=account["label"], others=others, url=site_url + "/guide/")
        shown = pinned.replace(site_url + "/guide/", "x" * URL_LENGTH)
        rows.append({"account": account, "bio": bio, "pinned": pinned,
                     "bio_len": len(bio), "pinned_len": weighted_len(shown)})
    return rows


def avatar(account, path):
    from PIL import Image, ImageDraw, ImageFont
    size = 400
    color = COLORS[account["cluster"]]
    image = Image.new("RGB", (size, size), color)
    draw = ImageDraw.Draw(image)
    big = ImageFont.truetype(FONT_BOLD, 150)
    small = ImageFont.truetype(FONT_BOLD, 46)
    draw.text((size / 2, 175), account["avatar_text"], font=big, fill=PAPER, anchor="mm")
    draw.line([(130, 262), (270, 262)], fill=PAPER, width=4)
    draw.text((size / 2, 312), "論文解説", font=small, fill=PAPER, anchor="mm")
    image.save(path)


def header(account, accounts, path):
    from PIL import Image, ImageDraw, ImageFont
    w, h = 1500, 500
    color = COLORS[account["cluster"]]
    image = Image.new("RGB", (w, h), PAPER)
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, w, 16], fill=color)
    x = 430   # 左下にアイコンが重なるので、本文は右へ寄せる
    heading = "%s｜論文解説" % account["label"]
    size = 112
    title = ImageFont.truetype(FONT_BOLD, size)
    while draw.textlength(heading, font=title) > w - x - 60 and size > 60:
        size -= 4
        title = ImageFont.truetype(FONT_BOLD, size)
    sub = ImageFont.truetype(FONT_BOLD, 40)
    note = ImageFont.truetype(FONT_REG, 32)
    chip = ImageFont.truetype(FONT_BOLD, 30)
    draw.text((x, 70 + (112 - size) // 2), heading, font=title, fill=INK)
    draw.text((x, 220), "論文をもとに、AI が概念を日本語で解説", font=sub, fill=INK2)
    draw.text((x, 282), "毎日 2 本 · 出典つき · 人による査読なし", font=note, fill=INK2)
    # 全 6 領域の並び。自分の領域だけ色で塗る
    cx, cy = x, 372
    for other in accounts:
        label = other["label"]
        width = int(draw.textlength(label, font=chip)) + 36
        if other["cluster"] == account["cluster"]:
            draw.rounded_rectangle([cx, cy, cx + width, cy + 54], radius=27, fill=color)
            draw.text((cx + width / 2, cy + 27), label, font=chip, fill=PAPER, anchor="mm")
        else:
            draw.rounded_rectangle([cx, cy, cx + width, cy + 54], radius=27, outline=INK2, width=2)
            draw.text((cx + width / 2, cy + 27), label, font=chip, fill=INK2, anchor="mm")
        cx += width + 12
    image.save(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text-only", action="store_true", help="画像を作らず、文面と文字数の検査だけ行う")
    args = parser.parse_args()
    spec = yaml.safe_load(ACCOUNTS.read_text(encoding="utf-8"))
    site_url = yaml.safe_load(SITE.read_text(encoding="utf-8"))["site"]["url"]
    failed = False
    for row in texts(spec, site_url):
        account = row["account"]
        print("[%s] %s  @%s" % (account["cluster"], account["display_name"], account["handle"]))
        print("  プロフィール(%d 字 / %d): %s" % (row["bio_len"], BIO_LIMIT, row["bio"]))
        print("  固定ポスト(換算 %d / %d): %s" % (row["pinned_len"], POST_LIMIT, row["pinned"]))
        if row["bio_len"] > BIO_LIMIT or row["pinned_len"] > POST_LIMIT or len(account["handle"]) > 15:
            failed = True
            print("  !! 上限超過", file=sys.stderr)
        if not args.text_only:
            OUT.mkdir(parents=True, exist_ok=True)
            avatar(account, OUT / ("avatar-%s.png" % account["cluster"]))
            header(account, spec["accounts"], OUT / ("header-%s.png" % account["cluster"]))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
