---
title: "An Explainable AI-Driven Multi-Objective Framework for Predictive Workforce Planning and Dynamic Resource Optimization"
authors: "Shraddha Srivastava, VEENA SINGH, Shobhit Sinha, Ankit Kumar Singh"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-21T09:16:37.708377"
doi: "https://doi.org/10.5281/zenodo.22842848"
openalex_id: "https://openalex.org/W7213672105"
source_api: "openalex"
---

# An Explainable AI-Driven Multi-Objective Framework for Predictive Workforce Planning and Dynamic Resource Optimization

**著者**: Shraddha Srivastava, VEENA SINGH, Shobhit Sinha, Ankit Kumar Singh
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Workforce planning increasingly relies on data-driven prediction, yet many organizations still lack an integrated, transparent pipeline that connects predictive risk modelling, explainability, and resource allocation into a single decision-support system. This study develops and empirically evaluates an explainable, prediction-informed multi-objective framework for workforce planning, built and tested end-to-end on the publicly available IBM HR Analytics Employee Attrition & Performance dataset (1,470 employee records; 30 usable predictor features after removing four constant or purely identifying columns). Because the dataset is cross-sectional rather than longitudinal, the framework is deliberately scoped to attrition and workforce-risk classification rather than time-series demand forecasting; this adaptation is stated explicitly rather than fabricating a temporal structure the data does not contain. Six classifiers — Logistic Regression, Support Vector Machine (RBF kernel), Random Forest, XGBoost, CatBoost, and a Multilayer Perceptron — were trained under a leakage-safe, stratified 70/15/15 train/validation/test split, with all hyperparameter tuning confined to training folds via 5-fold stratified cross-validation. The RBF-kernel SVM achieved the highest held-out test ROC-AUC (0.841; F1-score 0.552; Matthews Correlation Coefficient 0.508), but paired bootstrap resampling (2,000 iterations) showed this advantage over Logistic Regression, Random Forest, XGBoost, and CatBoost was not statistically significant (two-sided p > 0.15 in all four comparisons); only the comparison against the MLP baseline reached significance (p = 0.003). SHAP (SHapley Additive exPlanations) analysis of the selected model identified StockOptionLevel, DistanceFromHome, OverTime, Age, and JobSatisfaction as the dominant drivers of predicted attrition risk, with directions of effect consistent with established turnover theory. These real, model-derived risk scores were then embedded as one of four minimization objectives — cost, understaffing, skill mismatch, and residual workforce risk — in an NSGA-II multi-objective optimization of retention-resource allocation across the nine job-role cells actually present in the held-out test data. Cost, capacity, and criticality parameters that the dataset itself does not contain were derived through transparent, reproducible formulas from observable cell properties and are labeled throughout as scenario assumptions, not observed data. The resulting Pareto front (120 non-dominated solutions after 200 generations) Pareto-dominated both a blanket-intervention baseline and a SHAP-informed heuristic on every objective simultaneously, and sensitivity analysis showed the optimized outcomes respond monotonically and plausibly to changes in the assumed intervention effectiveness and available budget. A subgroup fairness audit revealed uneven recall across marital-status and age bands, underscoring that fairness risks in this pipeline require governance and human oversight rather than purely technical mitigation. The contribution is a fully reproducible demonstration — with every reported number traceable to saved experimental output — of how prediction, explanation, and optimization can be integrated into a single pipeline that supports, rather than replaces, accountable human workforce decisions.
