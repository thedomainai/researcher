---
title: "VFR-Audit: Verdict-Level Reliability for Fairness Audits in Hospital Length-of-Stay Prediction"
authors: "Md Jannatul Rakib Joy, Viet Vo, Caslon Chua"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-11-04T06:48:06.308091"
doi: "https://doi.org/10.1145/3799682.3840827"
openalex_id: "https://openalex.org/W7204905129"
source_api: "openalex"
---

# VFR-Audit: Verdict-Level Reliability for Fairness Audits in Hospital Length-of-Stay Prediction

**著者**: Md Jannatul Rakib Joy, Viet Vo, Caslon Chua
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Fairness audits in clinical Artificial Intelligence convert continuous fairness metrics into binary pass-or-fail verdicts against operational thresholds, where hospital governance boards, payers, and regulators act on the resulting verdicts. Such audits are repeated over time and across hospital sites, thus the same verdict can flip between pass and fail across audits. Existing uncertainty methods such as Bayesian posteriors, bootstrap confidence intervals, and permutation tests address verdict instability only at the continuous-metric level. Converting metric-level uncertainty into a verdict-stability claim remains a manual step that scales poorly across the (model, metric, attribute) cells an audit covers. Existing uncertainty methods also leave open whether bias-mitigation steps, such as reweighing or per-group threshold shifts, yield a stable passing verdict at the cost of model discrimination measured as AUROC or AUPRC.To address this verdict-stability gap, we propose VFR-Audit, a framework built around the Verdict Flip Rate (VFR), a scalar bounded between 0 and 0.5 that measures the probability of verdict reversal under stratified bootstrap resampling. VFR-Audit reports VFR alongside three reliability axes, namely within-cohort resampling stability, audit-size sensitivity, and cross-hospital verdict agreement via Fleiss' kappa.
