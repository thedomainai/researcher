---
title: "Cost-Sensitive Ensemble Models for Microcredit Risk Prediction: A Comparative Evaluation"
authors: "Reliya Indah Okta Limabri Reliya, Ari Muzakir"
year: 2026
citations: 0
paper_type: "primary"
domain: "accounting"
fetched: "2026-10-27T06:05:08.965845"
doi: "https://doi.org/10.63158/journalisi.v8i5.1902"
openalex_id: "https://openalex.org/W7223305203"
source_api: "openalex"
---

# Cost-Sensitive Ensemble Models for Microcredit Risk Prediction: A Comparative Evaluation

**著者**: Reliya Indah Okta Limabri Reliya, Ari Muzakir
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 会計学

## Abstract

Microcredit risk prediction is challenged by class imbalance and asymmetric misclassification costs. This study evaluates cost-sensitive ensemble models and examines model-selection stability across heterogeneous credit sources. Logistic Regression, Random Forest, XGBoost, and CatBoost were evaluated on one operational microcredit portfolio and three public credit datasets using development-only preprocessing, class-balanced fitting weights, and leakage controls. Model and threshold selection used validation data with a five-to-one false-negative cost ratio and minimum specificity of 0.70. XGBoost was selected for the operational, Credit Risk, and FIN ANA sources, while Logistic Regression was selected for German Credit. On the retrospectively held-out evaluation partitions, ROC-AUC values were 0.895, 0.940, 0.461, and 0.620, with recalls of 0.364, 0.839, 0.083, and 0.483, respectively. FIN ANA showed substantial degradation under broader distribution shift. The study jointly evaluates minority-class recall, asymmetric error costs, and validation-selected operating points, showing that cost-sensitive model selection is source-dependent and ROC-AUC alone is insufficient for practical risk detection. The operational analysis represents retrospective adverse-status screening rather than prospective default prediction because temporal feature snapshots and future outcome windows were unavailable.
