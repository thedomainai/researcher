---
title: "Optimization of the SCL-90 scale using machine learning: a novel approach to mental health assessment"
authors: "Meng Li, Cheng Liu, Gang Shao"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-11-14T06:11:18.170943"
doi: "https://doi.org/10.3389/fpsyg.2026.2018014"
openalex_id: "https://openalex.org/W7225892616"
source_api: "openalex"
---

# Optimization of the SCL-90 scale using machine learning: a novel approach to mental health assessment

**著者**: Meng Li, Cheng Liu, Gang Shao
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

Background Mental health assessment is critical for early intervention and treatment, yet traditional tools like the Symptom Checklist-90 (SCL-90) suffer from redundancy and high respondent burden. This study aims to optimize the SCL-90 using machine learning to enhance assessment efficiency while maintaining agreement with the full-scale SCL-90 screening classification. Methods Nine machine learning algorithms were evaluated via 10-fold cross-validation. SHapley Additive exPlanations (SHAP) was used to rank item importance, and the optimal item count was determined experimentally by a pre-specified one-standard-error rule, yielding a 44-item subset; hyperparameters were tuned with metaheuristic optimization algorithms. All feature-selection and tuning steps were evaluated under a leakage-free nested cross-validation protocol, complemented by a stratified hold-out evaluation, head-to-head comparison with established SCL-90 short forms, and psychometric analyses. Performance metrics included accuracy, precision, recall, and f1 score. Results The baseline LGBM model achieved the highest F1 score of 0.9413. Under the original full-data evaluation protocol, the GWO-optimized SHAP-XGB model reached an F1 of 0.9501. Upon re-evaluation under the leakage-free nested protocol, the tuned 44-item model yielded an F1 of 0.9233, which was statistically indistinguishable from the untuned full-feature baseline. Moreover, the 44-item form outperformed four established short forms reconstructed on the same dataset. SHAP analysis identified key predictors that were closely associated with depressive tendencies, anxiety–stress coping, and somatic symptoms. Depressive symptoms constituted the primary dimension, and the largest observed interaction occurred between anxiety and depression, which is reported as an exploratory, model-specific pattern. Conclusion This study presents a data-driven, proof-of-concept optimization of the SCL-90, reducing item count by 51% (from 90 to 44 items) while maintaining agreement with the full-scale SCL-90 screening classification. SHAP analysis played a pivotal role in enhancing model interpretability by quantifying feature contributions and revealing symptom interaction patterns. However, the generalizability and clinical utility of the optimized 44-item scale require rigorous external validation before any practical application.
