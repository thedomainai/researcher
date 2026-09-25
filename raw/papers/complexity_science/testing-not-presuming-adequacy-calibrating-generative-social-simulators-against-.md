---
title: "Testing, not presuming, adequacy: calibrating generative social simulators against emergent network structure"
authors: "Tengfei Shao, Chao Li, Xu Wang, Masayuki Goto"
year: 2026
citations: 0
paper_type: "meta_analysis"
domain: "complexity_science"
fetched: "2026-09-23T06:02:04.517713"
arxiv_id: "http://arxiv.org/abs/2609.24012v1"
source_api: "arxiv"
categories: "cs.AI, cs.MA, cs.SI"
---

# Testing, not presuming, adequacy: calibrating generative social simulators against emergent network structure

**著者**: Tengfei Shao, Chao Li, Xu Wang, Masayuki Goto
**年**: 2026 | **被引用数**: 0
**タイプ**: meta_analysis | **分野**: 複雑系科学

## Abstract

Validation of generative social simulators often stops at face validity: emergent network structure is compared descriptively, without quantified parameter uncertainty or an adequacy check. We present an adequacy-aware calibration protocol that couples amortized posterior estimation with a synthetic identifiability assessment, a matched-sample-size adequacy check (prior-predictive reachability plus per-statistic posterior-predictive localization), a diagnosis-guided repair, and a statistic-held-out audit. We demonstrate it on a real second-hand luxury resale market with four channel-by-residency cells, each a bipartite buyer-brand network, using a forward model built from persona profiles elicited once, offline, by a language model. The behavioural parameters are recoverable in all four cells, though calibration is approximate and overconfident for one parameter. The observed summary falls outside the simulator's reachability reference in every cell, with the mean purchased tier as the pervasive discrepancy. The repair meets the value-block criterion in two of four cells but does not restore adequacy, and the held-out audit surfaces a buyer-breadth-dispersion miss no earlier diagnostic detected. A profile-source ablation finds the language-model profiles beat a flat rule baseline in all four cells, yet within-category brand relabelling causes no consistent degradation, so the profiles are a partially validated input whose value rests on structure, not brand identity. Making no causal claim, we conclude that an independent-aggregation account, without agent interaction or a buyer-breadth mechanism, cannot jointly reproduce the market's purchased-tier level, head-brand concentration, community structure and buyer-breadth heterogeneity.
