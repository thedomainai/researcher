# -*- coding: utf-8 -*-
"""llm/index.jsonl から読書リスト llm/reading_list.md を生成する。

対象は「定番(landmark)かつ core」の論文。被引用数の多い順に並べる(全体)。
あわせて領域別の順位も出す。被引用数は OpenAlex、arXiv/S2 補完分は Semantic Scholar の値で、
出典が違うため厳密な比較には使えない(目安)。

    python3 tools/llm_reading_list.py
"""
import json
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LLM = os.path.join(BASE, "llm")
LABEL = {
    "foundations": "基盤", "post_training": "学習後の調整", "elicitation": "能力の引き出し",
    "evaluation": "評価", "safety_interp": "安全・解釈", "theory_cognition": "理論・認知",
    "applications": "応用", "agents": "エージェント",
}


def main():
    rows = [json.loads(l) for l in open(os.path.join(LLM, "index.jsonl"), encoding="utf-8") if l.strip()]
    sel = [r for r in rows if r["landmark"] and any(r["relevance"].get(t, {}).get("verdict") == "core" for t in r["topics"])]
    sel.sort(key=lambda r: -r["cited_by_count"])

    def clean(t):
        return re.sub(r"\s+", " ", t.replace("\\n", " ")).strip()

    def line(i, r):
        topics = "/".join(LABEL.get(t, t) for t in r["topics"])
        src = " ※S2" if r["openalex_id"].startswith(("arxiv-", "s2-")) else ""
        rel = os.path.relpath(os.path.join(BASE, r["file"]), LLM)
        flag = "" if r["has_abstract"] else " (抄録なし)"
        return "- [ ] %d. [%s](%s) — %s・%s・被引用 %s%s%s" % (
            i, clean(r["title"]).replace("[", "(").replace("]", ")"), rel, topics, r["year"], format(r["cited_by_count"], ","), src, flag)

    out = [
        "# LLM 読書リスト(定番の core・被引用順)", "",
        "対象: 定番(名指しで取得)かつ core の論文 %d 本。被引用数の多い順です。" % len(sel),
        "被引用数は OpenAlex の値です。※S2 は Semantic Scholar の値で、出典が違うため目安です。",
        "読んだら `- [ ]` を `- [x]` に直してください。", "", "## 全体", "",
    ]
    out += [line(i, r) for i, r in enumerate(sel, 1)]
    out += ["", "## 領域別(各領域の先頭 15 本)", ""]
    for t, lab in LABEL.items():
        sub = [r for r in sel if t in r["topics"]]
        out += ["### %s(%s・定番 core %d 本)" % (lab, t, len(sub)), ""]
        out += [line(i, r) for i, r in enumerate(sub[:15], 1)]
        out.append("")
    with open(os.path.join(LLM, "reading_list.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("定番 core %d 本 → llm/reading_list.md" % len(sel))


if __name__ == "__main__":
    main()
