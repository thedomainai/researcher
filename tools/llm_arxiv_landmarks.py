# -*- coding: utf-8 -*-
"""llm/ の定番文献のうち OpenAlex に無いもの(arXiv のみの論文など)を arXiv から補う。

  python3 tools/llm_arxiv_landmarks.py        # missing_landmarks.jsonl を arXiv で検索して取り込む
  (fetch_llm.py は実行後に merge_cached() を呼ぶ。全再構築で index が作り直されても復元される)

- 検索: arXiv API のタイトル検索。語の一致率 0.75 以上の候補から最良を採る(誤採用を避ける)
- 被引用数: Semantic Scholar の一括取得(arXiv ID 指定)。取れなければ 0
- 結果は llm/arxiv_landmarks.jsonl に残す(見つからなかったものも entry=null で残し、再検索しない)
- 索引の ID は "arxiv-<arXiv ID>"(openalex_id 項目を流用)。arxiv_id 項目に元の ID も持つ
"""
import json
import os
import re
import sys
import time
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import arxiv  # noqa: E402
import httpx  # noqa: E402
import fetch_llm  # noqa: F401,E402  (fetch_reference の保存先を llm/ に差し替える)
import fetch_reference as fr  # noqa: E402

CACHE_PATH = os.path.join(fr.REF_DIR, "arxiv_landmarks.jsonl")


def load_cache():
    rows = {}
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    rows[(r["topic"], r["title"])] = r
    return rows


def same_title(query_title, cand_title):
    """依頼タイトルの語が候補に 0.75 以上含まれ、かつ候補の語も 0.6 以上が依頼に含まれる。
    短い依頼タイトルが、語を含むだけの長い別タイトルに一致する誤採用を防ぐ。"""
    return (fr.title_overlap(query_title, cand_title) >= 0.75
            and fr.title_overlap(re.sub(r"[^\w\s]", " ", cand_title), query_title) >= 0.6)


def _query(client, query, title):
    """429 は待って再試行する。arXiv は連続アクセスに厳しい。"""
    for attempt in range(5):
        try:
            best, best_key = None, None
            for p in client.results(arxiv.Search(query=query, max_results=8)):
                ov = fr.title_overlap(title, p.title)
                if not same_title(title, p.title):
                    continue
                key = (round(ov, 2), -len(p.title))
                if best_key is None or key > best_key:
                    best, best_key = p, key
            return best
        except arxiv.HTTPError:
            time.sleep(20 * (attempt + 1))
    raise RuntimeError("arXiv の流量制限が解けませんでした")


def search_arxiv(title):
    # アポストロフィは空白でなく除く(Let's → Lets)。記号で割ると arXiv の語と合わなくなる
    plain = re.sub(r"[\u2019']", "", title)
    q = re.sub(r"\s+", " ", re.sub(r"[^A-Za-z0-9 ]+", " ", plain)).strip()
    client = arxiv.Client(delay_seconds=5, num_retries=0)
    best = _query(client, 'ti:"%s"' % q, title)
    if best is None:
        words = q.split()[:8]
        best = _query(client, " AND ".join("ti:%s" % w for w in words), title)
    return best


def search_s2(title):
    """Semantic Scholar のタイトル一致検索。引用数と抄録を一度に取る。見つからなければ None。"""
    plain = re.sub(r"[\u2019']", "", title)
    for attempt in range(4):
        time.sleep(4)
        try:
            r = httpx.get(fr.S2_BASE + "/paper/search/match", timeout=60, params={
                "query": plain, "fields": "title,abstract,year,authors,citationCount,externalIds"})
        except Exception:
            r = None
        if r is not None and r.status_code == 404:
            return None
        if r is not None and r.status_code == 200:
            for item in r.json().get("data", []):
                if same_title(title, item.get("title") or ""):
                    return item
            return None
        time.sleep(15 * (attempt + 1))
    raise RuntimeError("Semantic Scholar の流量制限が解けませんでした")


def s2_citations(arxiv_ids):
    out = {}
    for attempt in range(5):
        time.sleep(3)
        try:
            r = httpx.post(fr.S2_BASE + "/paper/batch", params={"fields": "citationCount"},
                           json={"ids": ["ARXIV:" + i for i in arxiv_ids]}, timeout=60)
        except Exception:
            r = None
        if r is not None and r.status_code == 200:
            for i, item in zip(arxiv_ids, r.json()):
                out[i] = (item or {}).get("citationCount") or 0
            return out
        time.sleep(15 * (attempt + 1))
    return out


def fetch_missing():
    cache = load_cache()
    todo = []
    with open(fr.MISSING_PATH, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                m = json.loads(line)
                if (m["topic"], m["title"]) not in cache:
                    todo.append(m)
    found = []
    for m in todo:
        rec = {"topic": m["topic"], "title": m["title"], "entry": None}
        item = search_s2(m["title"])
        p = None
        if item is not None:
            ids = item.get("externalIds") or {}
            aid = ids.get("ArXiv") or ("s2-" + item["paperId"] if item.get("paperId") else None)
            auth = [a.get("name", "") for a in (item.get("authors") or []) if a.get("name")]
            rec["entry"] = {
                "arxiv_id": aid or "", "title": re.sub(r"\s+", " ", item.get("title") or "").strip(),
                "authors": auth[:8] + (["et al."] if len(auth) > 8 else []),
                "year": item.get("year"), "abstract": re.sub(r"\s+", " ", item.get("abstract") or "").strip(),
                "cited_by_count": item.get("citationCount") or 0, "cites_fetched": True, "source": "semantic_scholar",
            }
            p = item
        if p is None:
            # 補助: arXiv のタイトル検索(流量制限中なら諦める)
            try:
                ap = search_arxiv(m["title"])
            except RuntimeError:
                ap = None
            if ap is not None:
                rec["entry"] = {
                    "arxiv_id": re.sub(r"v\d+$", "", ap.entry_id.rsplit("/abs/", 1)[-1]),
                    "title": re.sub(r"\s+", " ", ap.title).strip(),
                    "authors": [a.name for a in ap.authors[:8]] + (["et al."] if len(ap.authors) > 8 else []),
                    "year": ap.published.year, "abstract": re.sub(r"\s+", " ", ap.summary or "").strip(),
                    "cited_by_count": 0, "source": "arxiv",
                }
                p = ap
        if rec["entry"] is not None:
            found.append(rec)
        cache[(m["topic"], m["title"])] = rec
        os.makedirs(fr.REF_DIR, exist_ok=True)
        fr.write_jsonl(CACHE_PATH, list(cache.values()))  # 途中で落ちても進捗を失わない
        print("  %s: %s" % ("取得" if p is not None else "見つからず", m["title"][:70]), flush=True)
    pending = [r for r in cache.values() if r["entry"] and not r["entry"].get("cites_fetched")]
    if pending:
        cites = s2_citations(sorted({r["entry"]["arxiv_id"] for r in pending}))
        for r in pending:
            if r["entry"]["arxiv_id"] in cites:
                r["entry"]["cited_by_count"] = cites[r["entry"]["arxiv_id"]]
                r["entry"]["cites_fetched"] = True
        fr.write_jsonl(CACHE_PATH, list(cache.values()))
    return cache


def merge_cached():
    """キャッシュ済みの arXiv 定番を index.jsonl とファイルへ反映する(冪等・通信なし)。"""
    cache = load_cache()
    entries = fr.load_index()
    added = 0
    for rec in cache.values():
        e = rec["entry"]
        if not e or not e.get("arxiv_id"):
            continue
        oid = "arxiv-" + e["arxiv_id"]
        topic = rec["topic"]
        cur = entries.get(oid)
        if cur is None:
            cur = {
                "openalex_id": oid, "arxiv_id": e["arxiv_id"], "doi": None, "title": e["title"],
                "authors": e["authors"], "year": e["year"], "cited_by_count": e["cited_by_count"],
                "paper_type": "article", "evidence_kind": fr.classify_evidence("article", e["title"], e["abstract"]),
                "abstract": e["abstract"], "abstract_source": e.get("source", "arxiv"),
                "has_abstract": len(e["abstract"]) >= fr.MIN_ABSTRACT_CHARS,
                "oa_topic": None, "oa_field": None, "topics": [], "channels": {}, "relevance": {},
                "landmark": True, "file": "", "file_verified": False,
                "fetched_at": datetime.now().strftime("%Y-%m-%d"),
            }
            entries[oid] = cur
            added += 1
        if topic not in cur["topics"]:
            cur["topics"].append(topic)
        cur["channels"][topic] = ["landmark_arxiv"]
        cur["relevance"][topic] = {"verdict": "core", "reason": "定番文献(OpenAlex に無く arXiv から補完)"}
        cur["file"] = os.path.join(fr.CORPUS, "papers", cur["topics"][0],
                                   "%s-%s.md" % (fr.slugify(cur["title"]), re.sub(r"[^a-z0-9.]+", "-", oid.lower())))
        path = os.path.join(fr.BASE, cur["file"])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(fr.render_markdown(cur))
        cur["file_verified"] = os.path.isfile(path) and os.path.getsize(path) > 0
    order = list(fr.TOPICS)
    rows = sorted(entries.values(), key=lambda x: (order.index(x["topics"][0]), not x["landmark"], -x["cited_by_count"]))
    fr.write_jsonl(fr.INDEX_PATH, rows)
    return added, len(rows)


if __name__ == "__main__":
    fr_cache = fetch_missing()
    n_ok = sum(1 for r in fr_cache.values() if r["entry"])
    print("arXiv で見つかった定番: %d / %d" % (n_ok, len(fr_cache)))
    added, total = merge_cached()
    print("索引に追加 %d 件 → 合計 %d 件" % (added, total))
