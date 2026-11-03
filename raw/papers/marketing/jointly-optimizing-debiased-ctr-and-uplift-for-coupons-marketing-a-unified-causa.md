---
title: "Jointly Optimizing Debiased CTR and Uplift for Coupons Marketing: A Unified Causal Framework"
authors: "Siyun Yang, Shixiao Yang, Jian Wang, Di Fan, Kehe Cai"
year: 2026
citations: 0
paper_type: "primary"
domain: "marketing"
fetched: "2026-11-04T06:54:08.840147"
doi: "https://doi.org/10.1145/3799682.3840119"
openalex_id: "https://openalex.org/W7129091349"
source_api: "openalex"
---

# Jointly Optimizing Debiased CTR and Uplift for Coupons Marketing: A Unified Causal Framework

**著者**: Siyun Yang, Shixiao Yang, Jian Wang, Di Fan, Kehe Cai
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: マーケティング

## Abstract

In online advertising, marketing interventions such as coupons introduce significant confounding bias into Click-Through Rate (CTR) prediction. Observed clicks reflect a mixture of users' intrinsic preferences and the uplift induced by these interventions. This causes conventional models to miscalibrate base CTRs, which distorts downstream ranking and billing decisions. Furthermore, marketing interventions often operate as multi-valued treatments with varying magnitudes, introducing additional complexity to CTR prediction. To address these issues, we propose the Unified Multi-Valued Treatment Network (UniMVT). Specifically, UniMVT disentangles confounding factors from treatment-sensitive representations, enabling a full-space counterfactual inference module to jointly reconstruct the debiased base CTR and intensity-response curves. To handle the complexity of multi-valued treatments, UniMVT employs an auxiliary intensity estimation task to capture treatment propensities and devise a unit uplift objective that normalizes the intervention effect. This ensures comparable estimation across the continuous coupon-value spectrum. UniMVT simultaneously achieves debiased CTR prediction for accurate system calibration and precise uplift estimation for incentive allocation. Extensive experiments on synthetic and industrial datasets demonstrate UniMVT's superiority in both predictive accuracy and calibration. Furthermore, real-world A/B tests confirm that UniMVT significantly improves business metrics through more effective coupon distribution.
