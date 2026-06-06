"""
問いに対して関連概念を検索し、推論の記録（inquiry）を保存する

Usage:
    python tools/inquire.py search "問いのテキスト" [--top N]
    python tools/inquire.py save --question "問い" --file synthesis.md [--slug custom-slug]

search: concepts.json + 過去の inquiry を横断検索し、関連度の高い概念を返す
save:   合成結果を wiki/inquiries/ に YAML frontmatter 付きで保存する
"""
import argparse
import datetime
import json
import os
import re
import sys

BASE = "/Users/yuta/workspace/projects/researcher"
WIKI_META = os.path.join(BASE, "wiki", "_meta")
WIKI_CONCEPTS = os.path.join(BASE, "wiki", "concepts")
WIKI_INQUIRIES = os.path.join(BASE, "wiki", "inquiries")
CONCEPTS_PATH = os.path.join(WIKI_META, "concepts.json")

os.makedirs(WIKI_INQUIRIES, exist_ok=True)


# ============================================================
# 検索エンジン
# ============================================================

def load_concepts():
    """concepts.json を読み込む"""
    with open(CONCEPTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_past_inquiries():
    """過去の inquiry ファイルから frontmatter を読み込む"""
    inquiries = []
    if not os.path.isdir(WIKI_INQUIRIES):
        return inquiries
    for fname in os.listdir(WIKI_INQUIRIES):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(WIKI_INQUIRIES, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        # YAML frontmatter を簡易パース
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = parts[1].strip()
                question = ""
                domains = []
                mechanisms = []
                for line in fm.split("\n"):
                    if line.startswith("question:"):
                        question = line.split(":", 1)[1].strip().strip('"').strip("'")
                    elif line.startswith("domains:"):
                        domains = _parse_yaml_list(line.split(":", 1)[1])
                    elif line.startswith("mechanisms:"):
                        mechanisms = _parse_yaml_list(line.split(":", 1)[1])
                inquiries.append({
                    "file": fname,
                    "question": question,
                    "domains": domains,
                    "mechanisms": mechanisms,
                })
    return inquiries


def _parse_yaml_list(value):
    """簡易的な YAML インラインリストのパース: [a, b, c] → ['a', 'b', 'c']"""
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1]
        return [v.strip().strip('"').strip("'") for v in inner.split(",") if v.strip()]
    return []


def tokenize_query(query):
    """日本語の問いをトークンに分割する（簡易）"""
    # 助詞・記号で分割し、短すぎるトークンを除外
    particles = r'[のはがをにでともかへやらけどてたなりますですするいうある、。？?・\s]+'
    tokens = re.split(particles, query)
    # 1文字以下のトークンは除外（ただし漢字1文字は残す）
    tokens = [t for t in tokens if len(t) > 1 or (len(t) == 1 and '\u4e00' <= t <= '\u9fff')]
    return tokens


def score_concept(concept, tokens, query):
    """概念エントリのスコアを計算する"""
    score = 0.0

    # 検索対象フィールドとその重み
    fields = {
        "title_ja": 3.0,
        "title_en": 2.0,
        "description": 2.0,
        "mechanisms": 5.0,  # メカニズムマッチは最重要
        "invariant_constraints": 3.0,
        "core_questions": 4.0,
    }

    for field, weight in fields.items():
        value = concept.get(field, "")
        if isinstance(value, list):
            value = " ".join(value)
        if not value:
            continue

        value_lower = value.lower()
        for token in tokens:
            if token.lower() in value_lower:
                score += weight

    # query 全体がフィールドに含まれる場合のボーナス
    for field in ["description", "title_ja"]:
        value = concept.get(field, "")
        if value and query in value:
            score += 5.0

    return score


def search_concepts(query, top_n=20):
    """問いに対して関連概念を検索する"""
    concepts = load_concepts()
    tokens = tokenize_query(query)

    if not tokens:
        print(f"  有効なトークンが抽出できませんでした: {query}", file=sys.stderr)
        return []

    scored = []
    for concept in concepts:
        s = score_concept(concept, tokens, query)
        if s > 0:
            scored.append((s, concept))

    scored.sort(key=lambda x: -x[0])
    return scored[:top_n]


def search_inquiries(query, tokens):
    """過去の inquiry から関連するものを検索する"""
    inquiries = load_past_inquiries()
    results = []
    for inq in inquiries:
        score = 0.0
        searchable = inq["question"] + " " + " ".join(inq["domains"]) + " " + " ".join(inq["mechanisms"])
        for token in tokens:
            if token.lower() in searchable.lower():
                score += 2.0
        if score > 0:
            results.append((score, inq))
    results.sort(key=lambda x: -x[0])
    return results


def print_search_results(query, top_n):
    """検索結果を整形して出力する"""
    tokens = tokenize_query(query)
    print(f"問い: {query}")
    print(f"検索トークン: {tokens}")
    print()

    # 概念検索
    results = search_concepts(query, top_n)
    print(f"--- 関連概念 ({len(results)}件) ---")
    print()
    for i, (score, c) in enumerate(results):
        mechanisms = ", ".join(c.get("mechanisms", []))
        constraints = ", ".join(c.get("invariant_constraints", []))
        core_qs = ", ".join(c.get("core_questions", []))
        domains = ", ".join(c.get("related_domains", []))
        tier = c.get("tier", "?")

        print(f"  {i+1}. [{score:.1f}] {c['slug']}")
        print(f"     {c.get('title_ja', '')} (Tier {tier})")
        print(f"     {c.get('description', '')}")
        if mechanisms:
            print(f"     mechanisms: {mechanisms}")
        if constraints:
            print(f"     constraints: {constraints}")
        if core_qs:
            print(f"     core_questions: {core_qs}")
        if domains:
            print(f"     domains: {domains}")
        print()

    # 過去の inquiry 検索
    inq_results = search_inquiries(query, tokens)
    if inq_results:
        print(f"--- 関連する過去の inquiry ({len(inq_results)}件) ---")
        print()
        for score, inq in inq_results:
            print(f"  [{score:.1f}] {inq['file']}")
            print(f"     問い: {inq['question']}")
            print()


# ============================================================
# Inquiry 保存
# ============================================================

def save_inquiry(question, source_file, slug=None):
    """inquiry ドキュメントを wiki/inquiries/ に保存する"""
    today = datetime.date.today().isoformat()

    if slug is None:
        # question から slug を生成（英数字+ハイフンに変換）
        slug = re.sub(r'[^a-zA-Z0-9\s-]', '', question.lower())
        slug = re.sub(r'\s+', '-', slug.strip())
        slug = slug[:60] if slug else "inquiry"

    filename = f"{today}-{slug}.md"
    filepath = os.path.join(WIKI_INQUIRIES, filename)

    # ソースファイルの内容を読み込み
    if not os.path.exists(source_file):
        print(f"エラー: ファイルが見つかりません: {source_file}", file=sys.stderr)
        sys.exit(1)

    with open(source_file, "r", encoding="utf-8") as f:
        body = f.read()

    # frontmatter が既にある場合はそのまま使用
    if body.startswith("---"):
        content = body
    else:
        # frontmatter を付与
        content = f"""---
question: "{question}"
date: {today}
status: draft
domains: []
mechanisms: []
---

{body}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"保存: {filepath}")
    return filepath


# ============================================================
# CLI エントリポイント
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="問いに対する関連概念検索と inquiry 保存"
    )
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    # search サブコマンド
    sp_search = subparsers.add_parser("search", help="関連概念を検索")
    sp_search.add_argument("query", help="検索する問い")
    sp_search.add_argument("--top", type=int, default=20, help="返す概念数（デフォルト: 20）")

    # save サブコマンド
    sp_save = subparsers.add_parser("save", help="inquiry を保存")
    sp_save.add_argument("--question", required=True, help="問いのテキスト")
    sp_save.add_argument("--file", required=True, help="合成結果のファイルパス")
    sp_save.add_argument("--slug", default=None, help="カスタムスラグ（省略時は自動生成）")

    # list サブコマンド
    sp_list = subparsers.add_parser("list", help="過去の inquiry を一覧")

    # stats サブコマンド
    sp_stats = subparsers.add_parser("stats", help="concepts.json のエンリッチ状況")

    parsed = parser.parse_args()

    if parsed.command == "search":
        print_search_results(parsed.query, parsed.top)

    elif parsed.command == "save":
        save_inquiry(parsed.question, parsed.file, parsed.slug)

    elif parsed.command == "list":
        inquiries = load_past_inquiries()
        if not inquiries:
            print("過去の inquiry はありません。")
        else:
            print(f"過去の inquiry ({len(inquiries)}件):")
            for inq in inquiries:
                print(f"  {inq['file']}")
                print(f"    問い: {inq['question']}")
                if inq['domains']:
                    print(f"    domains: {', '.join(inq['domains'])}")
                print()

    elif parsed.command == "stats":
        concepts = load_concepts()
        total = len(concepts)
        with_mechanisms = sum(1 for c in concepts if c.get("mechanisms"))
        with_constraints = sum(1 for c in concepts if c.get("invariant_constraints"))
        with_core_qs = sum(1 for c in concepts if c.get("core_questions"))
        with_all = sum(
            1 for c in concepts
            if c.get("mechanisms") and c.get("invariant_constraints") and c.get("core_questions")
        )

        print(f"concepts.json エンリッチ状況:")
        print(f"  全エントリ数:          {total}")
        print(f"  mechanisms あり:       {with_mechanisms} ({100*with_mechanisms//total}%)")
        print(f"  invariant_constraints: {with_constraints} ({100*with_constraints//total}%)")
        print(f"  core_questions あり:   {with_core_qs} ({100*with_core_qs//total}%)")
        print(f"  全フィールド揃い:      {with_all} ({100*with_all//total}%)")

        # メカニズムの頻度集計
        if with_mechanisms > 0:
            mech_counts = {}
            for c in concepts:
                for m in c.get("mechanisms", []):
                    mech_counts[m] = mech_counts.get(m, 0) + 1
            print(f"\n  メカニズム頻度 (上位20):")
            for m, count in sorted(mech_counts.items(), key=lambda x: -x[1])[:20]:
                print(f"    {m}: {count}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
