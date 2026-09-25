---
title: "Everything in Moderation: Per-Domain Coverage Optima and Alignment-Resistant Domain Gaps in Multi-Domain Mid-Training"
authors: "Yunpeng Xu, Kun Zheng"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-09-10T06:03:52.898900"
arxiv_id: "http://arxiv.org/abs/2609.09081v1"
source_api: "arxiv"
categories: "cs.AI"
---

# Everything in Moderation: Per-Domain Coverage Optima and Alignment-Resistant Domain Gaps in Multi-Domain Mid-Training

**著者**: Yunpeng Xu, Kun Zheng
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Mid-training, the stage between pre-training and alignment, is where a model's per-domain data composition is typically set by data availability rather than principled design. We ask what that decision buys, and whether a later alignment pass can undo it. In a controlled logical-reasoning setting (Qwen3-8B-Base, with a 4B replication; five semantically rule-disjoint KOR-Bench domains) we train 30 allocations spanning the five-domain simplex, 24 sweep configurations plus six withheld from the fit, at five seeds each. Three findings emerge. First, every domain has an interior coverage optimum: the moderate band ($10\%$-$40\%$) is best for all five domains, and a calibrated permutation test for quadratic interiority gives $P\approx0.010$; the fitted mid-training-only curves, with 8B peaks between $9.9\%$ and $35.1\%$, reproduce for curve shape but not peak location. Second, the gaps survive a fixed-budget alignment pass: compensatory SFT raises 116/120 cells (mean $+4.32\%$) yet bridges $0/240$ pairs at a $5\%$ threshold and $30/240$ at a $10\%$ ratio, an equal-budget uniform control behaves almost identically, and a permutation null would bridge $13.8\pm3.3$ and $77.9\pm8.5$ pairs ($P<0.001$). Third, zero coverage collapses mid-training-only accuracy, though a FineWeb-Edu-only control shows the collapse is commingled with generic drift. An exploratory $θ^*$ allocation attains the largest full-pipeline gain ($+4.36\%$ vs. $+0.80\%$/$+0.64\%$\,pp) but is marginal under Welch test.
