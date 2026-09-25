#!/usr/bin/env python3
"""単発の参照文献取得: 臨床・行動科学の根拠を OpenAlex から引いて reference/ に保存する。

日次パイプラインとは独立した、手動実行専用のスクリプトである。
  - raw/ と wiki/ には書かない。保存先は reference/ のみ。
  - Tier分類・compile_wiki・launchd の対象外。
  - 公開日の制限なし。関連度順で総説(type:review)と被引用50以上の一般論文を別々に取り、
    定番の文献はタイトル指定(LANDMARKS)で個別に取る。被引用数の降順だけでは無関係な文献が混ざるため。
  - 保存したファイルは、書いた直後に実在確認する。index.jsonl の file は実在するパスのみ。

使い方:
    python3 tools/fetch_reference.py --dry-run          # 予算と件数の見積りのみ
    python3 tools/fetch_reference.py                    # 全トピックを取得
    python3 tools/fetch_reference.py --topic sleep      # 1トピックだけ
    python3 tools/fetch_reference.py --verify           # 既存 index の実在確認のみ

OpenAlex の API キー(OPENALEX_API_KEY)が必須。キー無しの無料枠は1日約100検索で足りない。
1回の実行は最大 MAX_REQUESTS 回に制限し、課金枠(前払い)を使わない。
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime

import httpx

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF_DIR = os.path.join(BASE, "reference")
PAPERS_DIR = os.path.join(REF_DIR, "papers")
INDEX_PATH = os.path.join(REF_DIR, "index.jsonl")
NO_ABSTRACT_PATH = os.path.join(REF_DIR, "no_abstract.jsonl")  # 被引用200以上でアブストラクトが無い文献の書誌のみ
NO_ABSTRACT_MIN_CITED = 200

OA_WORKS = "https://api.openalex.org/works"
OA_RATE = "https://api.openalex.org/rate-limit"
SELECT = ",".join(
    [
        "id", "doi", "title", "publication_year", "cited_by_count", "type",
        "is_retracted", "authorships", "abstract_inverted_index", "primary_location",
    ]
)
REVIEW_PER_QUERY = 8      # 総説(type:review)を被引用数順に取る件数
ARTICLE_PER_QUERY = 5     # 一般論文を被引用数順に取る件数(被引用 ARTICLE_MIN_CITED 以上)
ARTICLE_MIN_CITED = 50
MAX_REQUESTS = 120        # 1回の実行の上限。1検索=10クレジット、無料枠は1日1,000検索
MIN_ABSTRACT_CHARS = 200  # これより短いアブストラクトは根拠として使えないので保存しない

# トピックごとのクエリ。OpenAlex の title_and_abstract.search 構文(AND / OR / 引用符 / 括弧)。
TOPICS = {
    "bipolar": {
        "label": "双極性障害・薬物療法・副作用",
        "queries": [
            "bipolar AND (mania OR hypomania) AND (episode OR relapse)",
            'bipolar AND ("mood stabilizer" OR lithium OR valproate OR lamotrigine)',
            "bipolar AND antipsychotic AND (\"side effect\" OR adverse OR sedation OR akathisia)",
            'bipolar AND antidepressant AND (switch OR "manic switch" OR efficacy)',
            "akathisia AND (suicide OR suicidal)",
            "akathisia AND (antipsychotic OR aripiprazole OR treatment)",
        ],
    },
    "cognition": {
        "label": "抑うつ・双極性の認知機能障害、自伝的記憶",
        "queries": [
            '(bipolar OR depression) AND ("cognitive impairment" OR "cognitive dysfunction" OR neurocognitive)',
            '"overgeneral autobiographical memory" AND depression',
            '(bipolar OR depression) AND ("executive function" OR "cognitive function") AND (remission OR euthymic)',
        ],
    },
    "sleep": {
        "label": "睡眠・概日リズム",
        "queries": [
            '"delayed sleep phase" AND (disorder OR chronotype)',
            'circadian AND (rhythm OR misalignment) AND (mood OR depression OR bipolar)',
            '"sleep deprivation" AND (cognition OR attention OR performance)',
            '"sleep deprivation" AND (mood OR emotion OR impulsivity)',
            '("social jetlag" OR eveningness) AND depression',
            'sleep AND bipolar AND (relapse OR "social rhythm")',
        ],
    },
    "reward": {
        "label": "報酬系・衝動性・嗜癖",
        "queries": [
            'dopamine AND "prediction error" AND reward',
            '"gaming disorder" OR "internet gaming disorder"',
            '"gambling disorder" AND (dopamine OR reward OR impulsivity)',
            '(buying OR spending) AND (compulsive OR impulsive) AND disorder',
            '"reward sensitivity" AND (bipolar OR mania)',
        ],
    },
    "avoidance": {
        "label": "経験の回避・思考抑制・ACT",
        "queries": [
            '"experiential avoidance" AND (psychopathology OR depression)',
            '"thought suppression" AND (rebound OR ironic)',
            '"acceptance and commitment therapy" AND (efficacy OR meta-analysis)',
            '"psychological flexibility" AND ("well-being" OR depression)',
        ],
    },
    "hedonic": {
        "label": "快楽適応・成功後の幸福",
        "queries": [
            '"hedonic adaptation" OR "hedonic treadmill"',
            '"lottery winners" AND ("accident victims" OR happiness)',
            '("hedonic adaptation" OR "hedonic treadmill" OR "set point") AND ("well-being" OR happiness)',
            '"affective forecasting" AND ("impact bias" OR "durability bias")',
        ],
    },
    "mastery": {
        "label": "熟達・運と実力",
        "queries": [
            '"deliberate practice" AND (expertise OR performance)',
            '"deliberate practice" AND (meta-analysis OR domains)',
            'luck AND (success OR career) AND (skill OR talent OR merit)',
            '"expert performance" AND (acquisition OR expertise)',
        ],
    },
    "scarcity": {
        "label": "希少性と認知・再現性",
        "queries": [
            'scarcity AND poverty AND (cognition OR "cognitive function" OR bandwidth OR "decision making")',
            '"scarcity mindset" OR "psychology of scarcity" OR "scarcity theory"',
            'poverty AND "cognitive function" AND (replication OR "failed to replicate" OR reanalysis OR "meta-analysis")',
        ],
    },
    "suicide": {
        "label": "自殺念慮・安全計画",
        "queries": [
            '"passive suicidal ideation" OR "passive ideation"',
            '"safety planning" AND (suicide OR suicidal)',
            '"suicidal ideation" AND (passive OR active OR severity) AND (assessment OR "risk factor")',
            'suicidal AND (bipolar) AND ("risk factors" OR prevention)',
        ],
    },
}


# 定番の文献。タイトルで検索し、被引用数が最大の1件を取る(取得後にタイトルを目視確認する)。
LANDMARKS = [
    ("scarcity", "Poverty impedes cognitive function"),
    ("scarcity", "Some consequences of having too little"),
    ("hedonic", "Experienced well-being rises with income, even above $75,000 per year"),
    ("hedonic", "Income and emotional well-being: A conflict resolved"),
    ("hedonic", "Hedonic adaptation"),
    ("mastery", "The role of deliberate practice in the acquisition of expert performance"),
    ("mastery", "Deliberate practice and performance in music, games, sports, education, and professions: a meta-analysis"),
    ("mastery", "Talent versus luck: the role of randomness in success and failure"),
    ("suicide", "Safety Planning Intervention: A Brief Intervention to Mitigate Suicide Risk"),
    ("suicide", "Comparison of the Safety Planning Intervention With Follow-up vs Usual Care of Suicidal Patients"),
    ("avoidance", "Ironic processes of mental control"),
    ("avoidance", "Experiential avoidance and behavioral disorders: a functional dimensional approach to diagnosis and treatment"),
    ("reward", "A neural substrate of prediction and reward"),
    ("bipolar", "Suicide attempts associated with akathisia"),
]


def load_dotenv(path):
    """`export KEY=VALUE` / `KEY=VALUE` を読む。値は表示しない。"""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[7:].lstrip()
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            if key and key not in os.environ:
                os.environ[key] = value.strip().strip("\"'")


def restore_abstract(inverted):
    """OpenAlex の abstract_inverted_index(単語→位置の配列)を本文に復元する。"""
    if not inverted:
        return ""
    slots = {}
    for word, positions in inverted.items():
        for pos in positions:
            slots[pos] = word
    return " ".join(slots[i] for i in sorted(slots)).strip()


def slugify(text, limit=60):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (slug[:limit].rstrip("-")) or "untitled"


def classify_evidence(work, abstract):
    """根拠の種類を推定する。タイトルとアブストラクトの語句による近似であり、確定ではない。"""
    text = ((work.get("title") or "") + " " + abstract).lower()
    if "meta-analy" in text or "metaanaly" in text:
        return "meta_analysis"
    if "systematic review" in text:
        return "systematic_review"
    if work.get("type") == "review":
        return "review"
    if "randomi" in text and ("trial" in text or "controlled" in text):
        return "rct"
    return "article"


class Client:
    def __init__(self, key):
        self.key = key
        self.requests = 0
        self.http = httpx.Client(timeout=30, headers={"Authorization": "Bearer " + key})

    def rate_limit(self):
        r = self.http.get(OA_RATE)
        r.raise_for_status()
        return r.json()["rate_limit"]

    def works(self, filt, per_page, search=None, sort=None):
        if self.requests >= MAX_REQUESTS:
            raise RuntimeError("1回の上限 %d リクエストに達しました" % MAX_REQUESTS)
        params = {"filter": filt, "per_page": per_page, "select": SELECT}
        if search:
            params["search"] = search  # 関連度順(既定)
        if sort:
            params["sort"] = sort
        last = None
        for attempt in range(3):
            self.requests += 1
            time.sleep(1.0)
            try:
                r = self.http.get(OA_WORKS, params=params)
                if r.status_code == 200:
                    return r.json().get("results", [])
                last = "HTTP %s" % r.status_code
            except Exception as e:  # ネットワーク障害
                last = str(e)
            time.sleep(5 * (attempt + 1))
        raise RuntimeError("OpenAlex 失敗: %s" % last)


def load_index():
    entries = {}
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    e = json.loads(line)
                    entries[e["openalex_id"]] = e
    return entries


def write_index(entries):
    os.makedirs(REF_DIR, exist_ok=True)
    tmp = INDEX_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for e in sorted(entries.values(), key=lambda x: (x["topics"][0], -x["cited_by_count"])):
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    os.replace(tmp, INDEX_PATH)


def render_markdown(e):
    authors = ", ".join(e["authors"]) or "(unknown)"
    front = [
        "---",
        "title: %s" % json.dumps(e["title"], ensure_ascii=False),
        "authors: %s" % json.dumps(e["authors"], ensure_ascii=False),
        "year: %s" % (e["year"] if e["year"] else "null"),
        "cited_by_count: %d" % e["cited_by_count"],
        "doi: %s" % json.dumps(e["doi"]),
        "openalex_id: %s" % e["openalex_id"],
        "paper_type: %s" % e["paper_type"],
        "evidence_kind: %s" % e["evidence_kind"],
        "topics: %s" % json.dumps(e["topics"], ensure_ascii=False),
        "---",
        "",
        "# %s" % e["title"],
        "",
        "**Authors**: %s | **Year**: %s | **Cited by**: %d | **Kind**: %s"
        % (authors, e["year"], e["cited_by_count"], e["evidence_kind"]),
        "",
        "## Abstract",
        "",
        e["abstract"],
        "",
    ]
    return "\n".join(front)


def verify_entries(entries):
    """index の file が実在し、中身に OpenAlex ID とアブストラクト冒頭が含まれるかを確認する。"""
    missing, mismatch = [], []
    for e in entries.values():
        path = os.path.join(BASE, e["file"])
        if not os.path.isfile(path):
            missing.append(e["file"])
            continue
        with open(path, encoding="utf-8") as f:
            body = f.read()
        if e["openalex_id"] not in body or e["abstract"][:80] not in body:
            mismatch.append(e["file"])
    return missing, mismatch


def to_entry(work, abstract, topic, query, rank):
    authors = [
        (a.get("author") or {}).get("display_name", "")
        for a in (work.get("authorships") or [])
    ]
    authors = [a for a in authors if a]
    oa_id = work["id"].rsplit("/", 1)[-1]
    year = work.get("publication_year")
    title = (work.get("title") or "").replace("\n", " ").strip()
    rel = os.path.join(
        "reference", "papers", topic, "%s-%s.md" % (slugify(title), oa_id.lower())
    )
    return {
        "openalex_id": oa_id,
        "doi": work.get("doi"),
        "title": title,
        "authors": authors[:8] + (["et al."] if len(authors) > 8 else []),
        "year": year,
        "cited_by_count": work.get("cited_by_count") or 0,
        "paper_type": work.get("type"),
        "evidence_kind": classify_evidence(work, abstract),
        "abstract": abstract,
        "topics": [topic],
        "queries": [query],
        "file": rel,
        "file_verified": False,
        "fetched_at": datetime.now().strftime("%Y-%m-%d"),
    }


def load_no_abstract():
    out = {}
    if os.path.exists(NO_ABSTRACT_PATH):
        with open(NO_ABSTRACT_PATH, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    e = json.loads(line)
                    out[e["openalex_id"]] = e
    return out


def write_no_abstract(no_abs):
    if not no_abs:
        return
    os.makedirs(REF_DIR, exist_ok=True)
    with open(NO_ABSTRACT_PATH, "w", encoding="utf-8") as f:
        for e in sorted(no_abs.values(), key=lambda x: -x["cited_by_count"]):
            f.write(json.dumps(e, ensure_ascii=False) + "\n")


def save_work(work, topic, query, rank, entries, no_abs, landmark=False):
    """1件を保存し index に載せる。結果は {added, noabs, retracted} の件数で返す。"""
    res = {"added": 0, "noabs": 0, "retracted": 0}
    if work.get("is_retracted"):
        res["retracted"] = 1
        return res
    abstract = restore_abstract(work.get("abstract_inverted_index"))
    title = (work.get("title") or "").strip()
    if not title:
        return res
    if len(abstract) < MIN_ABSTRACT_CHARS:
        res["noabs"] = 1
        cited = work.get("cited_by_count") or 0
        if cited >= NO_ABSTRACT_MIN_CITED:
            oa_id = work["id"].rsplit("/", 1)[-1]
            no_abs.setdefault(oa_id, {
                "openalex_id": oa_id, "doi": work.get("doi"), "title": title,
                "year": work.get("publication_year"), "cited_by_count": cited,
                "paper_type": work.get("type"), "topics": [topic],
                "note": "OpenAlex にアブストラクトが無いため本文は保存していない(書誌のみ)",
            })
            if topic not in no_abs[oa_id]["topics"]:
                no_abs[oa_id]["topics"].append(topic)
        return res
    entry = to_entry(work, abstract, topic, query, rank)
    entry["landmark"] = landmark
    existing = entries.get(entry["openalex_id"])
    if existing:
        if topic not in existing["topics"]:
            existing["topics"].append(topic)
        if query not in existing["queries"]:
            existing["queries"].append(query)
        if landmark:
            existing["landmark"] = True
        return res
    path = os.path.join(BASE, entry["file"])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_markdown(entry))
    # 書いた直後に実在確認する。確認できないものは index に載せない。
    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        print("  ! 保存に失敗: %s" % entry["file"])
        return res
    entry["file_verified"] = True
    entries[entry["openalex_id"]] = entry
    res["added"] = 1
    return res


def main():
    parser = argparse.ArgumentParser(description="臨床・行動科学の参照文献を単発で取得する")
    parser.add_argument("--topic", help="トピックを1つに限定 (%s)" % ", ".join(TOPICS))
    parser.add_argument("--dry-run", action="store_true", help="予算と見積りのみ表示し、取得しない")
    parser.add_argument("--verify", action="store_true", help="既存 index の実在確認のみ")
    args = parser.parse_args()

    if args.verify:
        entries = load_index()
        missing, mismatch = verify_entries(entries)
        print("index %d 件 / 欠落 %d / 内容不一致 %d" % (len(entries), len(missing), len(mismatch)))
        for p in missing + mismatch:
            print("  NG:", p)
        return 1 if (missing or mismatch) else 0

    load_dotenv(os.path.join(BASE, ".env"))
    key = os.environ.get("OPENALEX_API_KEY", "")
    if not key:
        print("OPENALEX_API_KEY が設定されていません。キー無しの無料枠(約100検索/日)では不足します。")
        return 1

    topics = {args.topic: TOPICS[args.topic]} if args.topic else TOPICS
    if args.topic and args.topic not in TOPICS:
        print("不明なトピック: %s (%s)" % (args.topic, ", ".join(TOPICS)))
        return 2
    n_queries = sum(len(t["queries"]) for t in topics.values())
    needed = n_queries * 2 + (0 if args.topic else len(LANDMARKS))

    client = Client(key)
    limits = client.rate_limit()
    remaining = limits["credits_remaining"]
    cost = limits["credit_costs"]["search"]
    print("クエリ %d 本 → 最大 %d リクエスト(%d クレジット)。残り %d クレジット、前払い残 %s ドル"
          % (n_queries, needed, needed * cost, remaining, limits["prepaid_remaining_usd"]))
    if needed > MAX_REQUESTS:
        print("1回の上限 %d を超えます。--topic で分けてください。" % MAX_REQUESTS)
        return 1
    if needed * cost > remaining:
        print("無料枠の残りを超えるため中止します(課金は発生させません)。")
        return 1
    if args.dry_run:
        return 0

    entries = load_index()
    no_abs = load_no_abstract()
    counts = {}
    skipped_noabs = skipped_retracted = 0
    for topic, cfg in topics.items():
        print("\n[%s] %s" % (topic, cfg["label"]))
        topic_new = 0
        for query in cfg["queries"]:
            found = client.works("type:review", REVIEW_PER_QUERY, search=query)
            found += client.works(
                "type:article,cited_by_count:>%d" % ARTICLE_MIN_CITED,
                ARTICLE_PER_QUERY, search=query,
            )
            kept = 0
            for rank, work in enumerate(found, 1):
                n = save_work(work, topic, query, rank, entries, no_abs)
                kept += n["added"]
                skipped_noabs += n["noabs"]
                skipped_retracted += n["retracted"]
            topic_new += kept
            print("  %3d 件追加 | %s" % (kept, query[:70]))
        counts[topic] = topic_new

    if not args.topic:
        print("\n[landmarks] 定番文献をタイトルで取得")
        for topic, title in LANDMARKS:
            found = client.works(
                "title.search:%s" % title.replace(",", " "), 1, sort="cited_by_count:desc"
            )
            if not found:
                print("  - 見つからず | %s" % title[:70])
                continue
            n = save_work(found[0], topic, "landmark: " + title, 0, entries, no_abs, landmark=True)
            counts[topic] = counts.get(topic, 0) + n["added"]
            skipped_noabs += n["noabs"]
            skipped_retracted += n["retracted"]
            flag = "追加" if n["added"] else ("既存" if not n["noabs"] else "アブストラクト無し")
            print("  %s | %s => %s (%s, %d)" % (
                flag, title[:45], (found[0].get("title") or "")[:55],
                found[0].get("publication_year"), found[0].get("cited_by_count") or 0))

    write_index(entries)
    write_no_abstract(no_abs)
    missing, mismatch = verify_entries(entries)

    print("\n" + "=" * 60)
    print("取得結果(新規追加、トピック別)")
    for topic, n in counts.items():
        print("  %-10s %d" % (topic, n))
    print("index 合計 %d 件 | アブストラクト欠落で除外 %d(うち被引用%d以上の書誌を no_abstract.jsonl に %d 件) | 撤回論文を除外 %d"
          % (len(entries), skipped_noabs, NO_ABSTRACT_MIN_CITED, len(no_abs), skipped_retracted))
    print("リクエスト数 %d(%d クレジット)" % (client.requests, client.requests * cost))
    print("実在確認: 欠落 %d / 内容不一致 %d" % (len(missing), len(mismatch)))
    print("=" * 60)
    return 1 if (missing or mismatch) else 0


if __name__ == "__main__":
    sys.exit(main())
