---
title: "A deep learning and TOPSIS framework for predictive maintenance scheduling in smart manufacturing: an Industry 4.0 approach"
authors: "Md Mohsin Uddin Fahim, Amit J. Lopes"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_management"
fetched: "2026-11-18T07:30:59.197689"
doi: "https://doi.org/10.1007/s00170-026-19478-4"
openalex_id: "https://openalex.org/W7201884732"
source_api: "openalex"
---

# A deep learning and TOPSIS framework for predictive maintenance scheduling in smart manufacturing: an Industry 4.0 approach

**著者**: Md Mohsin Uddin Fahim, Amit J. Lopes
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーション管理

## Abstract

Abstract Despite significant advances in deep learning-based failure prognosis, existing predictive maintenance frameworks consistently terminate at the prediction step, leaving the critical operational challenge of prioritising maintenance resources across heterogeneous asset fleets unresolved. This paper addresses this gap by proposing an integrated framework that couples Long Short-Term Memory network-based Remaining Useful Life prediction with the Technique for Order of Preference by Similarity to Ideal Solution for data-driven multi-criteria maintenance scheduling, validated on the NASA C-MAPSS FD001 turbofan degradation benchmark. The framework dynamically synthesises predicted health indicators with operational criteria encompassing machine criticality, maintenance cost, and production downtime impact to generate a ranked intervention schedule whose quality is evaluated through a rigorous, assumption-free protocol comprising precision-recall analysis, area under the precision-recall curve, Spearman rank correlation, and a scheduling efficiency ratio against a random baseline. A five-seed ablation study comparing Long Short-Term Memory, Bidirectional Long Short-Term Memory, and Gated Recurrent Unit architectures, with Wilcoxon signed-rank validation, establishes statistically equivalent prediction accuracy, confirming the architecture-agnostic nature of the scheduling design. The scheduling evaluation demonstrates near-perfect discrimination, capturing all failure-proximate assets by targeting less than one-third of the fleet, with a 3.70-fold efficiency improvement over random allocation, an AUPRC of 0.9923, and tier discrimination significant at p < 10⁻¹¹. Cross-domain validation on CWRU Bearing Fault rotating machinery confirms perfect discrimination (AUPRC = 1.000) and a Spearman correlation of ρ = 0.803 between the closeness coefficient and physical fault severity, thereby supporting physically grounded scheduling without explicit severity supervision. These findings establish that coupling accurate deep-learning-based prognosis with principled multi-criteria decision-making yields high-confidence intervention decisions and quantifiable gains in resource efficiency in Industry 4.0 smart manufacturing environments.
