---
title: "FunnelCausalNet: Funnel-aware Joint Conversion-Revenue Uplift for Multi-tier Coupon Allocation"
authors: "Yu Zhang, Zhihan Wang, Guanlin Chen, Min Jiang, Shuai Li"
year: 2026
citations: 0
paper_type: "primary"
domain: "marketing"
fetched: "2026-11-04T06:54:13.919582"
doi: "https://doi.org/10.1145/3799682.3840815"
openalex_id: "https://openalex.org/W7202347999"
source_api: "openalex"
---

# FunnelCausalNet: Funnel-aware Joint Conversion-Revenue Uplift for Multi-tier Coupon Allocation

**著者**: Yu Zhang, Zhihan Wang, Guanlin Chen, Min Jiang, Shuai Li
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: マーケティング

## Abstract

Coupon campaigns seek to lift both conversion and revenue, but gross merchandise value (GMV) follows a deterministic funnel from conversion to conditional order value and is zero-inflated and heavy-tailed. We propose FunnelCausalNet, an uplift estimator coupling a binary conversion head with a nonnegative conditional-value head through $μ_{\mathrm{gmv}}=μ_{\mathrm{conv}}μ_{\mathrm{val}}$. Under explicit RCT, support, rate-gap, and cross-head covariance-control assumptions, an idealized leading-order MSE comparison identifies a regime in which funnel composition can reduce pointwise variance; this is a heuristic, not a guarantee for the shared-representation neural model. The estimator is paired with marginal split-conformal CATE summaries, combined through a Bonferroni union as audit bands, and a Lagrangian budgeted allocator using RCT-anchored estimates for subsidy-aware ROI accounting. On semi-synthetic multi-tier Criteo-MT7, FunnelCausalNet's mean AUUC_GMV is within one seed standard deviation of the leading feature-interaction baseline among eleven baselines, while a controlled ablation reduces GMV effect error versus direct GMV regression by 18--48% across tested zero-inflation regimes. On de-identified industrial Hotel-Coupon RCT logs with about 4.9 million hold-out exposure records per seed, expected-outcome evaluation sweeps full LP frontiers; FunnelCausalNet has the best seed-averaged mean DeltaROI at all seven correlated anchors from 10% to 60%, which we treat as descriptive frontier consistency rather than independent significance. On sparse binary-spend public benchmarks, revenue-focused rankers can dominate uplift-curve proxies, defining an explicit regime boundary.
