---
title: "Diagnosing Algorithmic Bias: A Group Influence Framework for Fairness Auditing"
authors: "Olalekan J. Akintande, Amirreza Takhsha, Sune Holm, Aasa Feragen, Siavash Bigdeli"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-06-26T06:02:41.643533"
doi: "https://doi.org/10.1145/3805689.3806732"
openalex_id: "https://openalex.org/W7165641185"
source_api: "openalex"
---

# Diagnosing Algorithmic Bias: A Group Influence Framework for Fairness Auditing

**著者**: Olalekan J. Akintande, Amirreza Takhsha, Sune Holm, Aasa Feragen, Siavash Bigdeli
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Algorithmic fairness interventions often quantify and mitigate aggregate disparities but lack explanatory power for how these disparities arise during training. This work bridges the gap between outcome-based fairness auditing and training-data-centric interpretability by introducing a diagnostic framework grounded in group-level influence functions. We decompose the total influence on a demographic group's predictions into two novel components: self-influence (intra-group) and between-influence (inter-group). This decomposition reveals two critical failure modes: stereotyping, driven by disproportionate inter-group influence from advantaged groups, and under-learning, caused by insufficient intra-group influence within disadvantaged groups. Theoretically, we link these components to violations of standard group fairness criteria. Through experiments on COMPAS recidivism and ADULT income datasets, we demonstrate that severe fairness violations are frequently driven by strong intra-group influence, challenging conventional inter-group debiasing paradigms. Following influence-based diagnosis and targeted data reweighting, we employ SHAP to provide interpretable, feature-level explanations of residual bias. This end-to-end pipeline, from diagnosing disparity origins via self- and between-influence to targeted mitigation and explainable audit, moves beyond documenting what disparities exist to diagnosing how they emerge, enabling more precise and actionable bias interventions in high-stakes domains.
