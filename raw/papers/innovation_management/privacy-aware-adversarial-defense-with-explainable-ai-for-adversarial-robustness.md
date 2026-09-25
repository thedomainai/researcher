---
title: "Privacy-aware adversarial defense with explainable AI for adversarial robustness in AI model"
authors: "Bilal Sardar, Shareeful Islam, Stefano Silvestri, Spyridon Papastergiou"
year: 2026
citations: 0
paper_type: "primary"
domain: "innovation_management"
fetched: "2026-09-17T09:11:53.841735"
doi: "https://doi.org/10.1007/s40860-026-00273-7"
openalex_id: "https://openalex.org/W7213234829"
source_api: "openalex"
---

# Privacy-aware adversarial defense with explainable AI for adversarial robustness in AI model

**著者**: Bilal Sardar, Shareeful Islam, Stefano Silvestri, Spyridon Papastergiou
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: イノベーション管理

## Abstract

Abstract AI models in critical sectors such as healthcare and finance must provide both data privacy and adversarial robustness. Differential Privacy (DP) protects training data by injecting noise, but this noise smooths decision boundaries and leaves models open to adversarial evasion, a tension known as the Privacy-Robustness Trade-off. Although this trade-off is well documented, its internal mechanism remains underexplored: prior work does not reveal how the noise reshapes a model’s reasoning or which features become vulnerable. To close this gap, we propose a Privacy-Aware Adversarial Defense grounded in Explainable AI. Specifically, we introduce the Attention Concentration Score (ACS), which measures how DP training shifts Transformer attention away from task-critical features toward non-functional ones. This attention drift correlates with adversarial vulnerability, providing a mechanistic explanation of the trade-off. Building on this insight, we develop a Manifold-Aligned Semantic Attack that targets the most drifted features, and a TrustScore defense that fuses embedding-level anomaly detection with attention-level consistency checks. We validate across two datasets (Adult Census, MIMIC-IV), two architectures (DeBERTa-V3-Large, LLaMA−3.1-8B), and seven experiments benchmarking five attacks against six defenses. Within the recommended range ( $$\epsilon \in [5, 10]$$ ϵ ∈ [ 5 , 10 ] ), models retain 84.2% accuracy (96.2% of baseline), while TrustScore reaches an Area Under the ROC Curve (AUC) of 0.87-−0.94, outperforming Isolation Forest (0.65) and supervised detection (0.58). Moreover, these conclusions hold under feature-categorization variants (attribution- and PCA-based); privacy noise disproportionately destabilizes the minority class; the consistency signal adds sub-millisecond overhead; and a surrogate-attention variant preserves detection under black-box deployment, establishing the approach’s dependability for reliable intelligent environments.
