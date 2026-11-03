---
title: "GroupSegment-SHAP: Shapley Value Explanations with Group-Segment Players for Multivariate Time Series"
authors: "Jinwoong Kim, Sangjin Park"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-04T06:22:07.038356"
doi: "https://doi.org/10.1145/3799682.3840928"
openalex_id: "https://openalex.org/W7123808958"
source_api: "openalex"
---

# GroupSegment-SHAP: Shapley Value Explanations with Group-Segment Players for Multivariate Time Series

**著者**: Jinwoong Kim, Sangjin Park
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Multivariate time-series models achieve strong predictive performance in healthcare, industry, energy, and finance, but how they combine cross-variable interactions with temporal dynamics remains unclear. SHapley Additive exPlanations (SHAP) are widely used for interpretation. However, existing time-series variants typically treat the feature and time axes independently, fragmenting structural signals formed jointly by multiple variables over specific intervals. We propose GroupSegment SHAP (GS-SHAP), which constructs explanatory units as group-segment players based on cross-variable dependence and distribution shifts over time, and then quantifies each unit's contribution via Shapley attribution. We evaluate GS-SHAP across four real-world domains: human activity recognition, power-system forecasting, medical signal analysis, and financial time series, and compare it with KernelSHAP, TimeSHAP, SequenceSHAP, WindowSHAP, and TSHAP. GS-SHAP improves deletion-based faithfulness (DeltaAUC) by about 1.7x on average over time-series SHAP baselines, while reducing wall-clock runtime by about 40 percent on average under matched perturbation budgets. A financial case study shows that GS-SHAP identifies interpretable multivariate-temporal interactions among key market variables during high-volatility regimes.
