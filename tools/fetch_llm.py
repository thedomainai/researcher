#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LLM 専門家向けコーパス llm/ の取得。fetch_reference.py の仕組みをそのまま使う。

違いは保存先(llm/)、トピック(tools/llm_topics.py の 8 領域)、
直近年の重点取得(recent_queries。2024 年以降を被引用順・関連度順で追加)の 3 点。
raw/ と wiki/ には書かない。日次パイプライン・Tier 分類の対象外。手動実行専用。

使い方(fetch_reference.py と同じ引数):
    python3 tools/fetch_llm.py --dry-run
    python3 tools/fetch_llm.py --topic agents --dump-candidates   # 候補を集めて未判定を書き出す
    python3 tools/fetch_llm.py --apply-judgments <jsonl>          # セッション内の判定を取り込む
    python3 tools/fetch_llm.py --topic agents --no-gate           # キャッシュ済みの判定だけで保存
    python3 tools/fetch_llm.py --verify
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch_reference as fr  # noqa: E402
import llm_topics  # noqa: E402

fr.CORPUS = "llm"
fr.REF_DIR = os.path.join(fr.BASE, fr.CORPUS)
fr.PAPERS_DIR = os.path.join(fr.REF_DIR, "papers")
fr.INDEX_PATH = os.path.join(fr.REF_DIR, "index.jsonl")
fr.EXCLUDED_PATH = os.path.join(fr.REF_DIR, "excluded.jsonl")
fr.MISSING_PATH = os.path.join(fr.REF_DIR, "missing_landmarks.jsonl")
fr.CACHE_DIR = os.path.join(fr.REF_DIR, ".cache")
fr.TOPICS = llm_topics.TOPICS
fr.GATE_SYSTEM = llm_topics.GATE_SYSTEM
fr.GATE_USER = llm_topics.GATE_USER

if __name__ == "__main__":
    rc = fr.main()
    # 全再構築で index が作り直されても、arXiv から補った定番を戻す(通信なし・冪等)
    if rc == 0 and os.path.exists(fr.INDEX_PATH) and not any(
            a in sys.argv for a in ("--dry-run", "--verify", "--dump-candidates", "--apply-judgments")):
        import llm_arxiv_landmarks
        added, total = llm_arxiv_landmarks.merge_cached()
        print("arXiv 定番の反映: 新規 %d 件 / 索引合計 %d 件" % (added, total))
    sys.exit(rc)
