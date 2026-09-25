---
title: "AI Transparency in Network Intrusion Detection"
authors: "Dawlat Mustafa Sulaiman"
year: 2026
citations: 0
paper_type: "primary"
domain: "sociology"
fetched: "2026-09-03T06:03:50.765376"
doi: "https://doi.org/10.65542/djei.v2i3.87"
openalex_id: "https://openalex.org/W7204770610"
source_api: "openalex"
---

# AI Transparency in Network Intrusion Detection

**著者**: Dawlat Mustafa Sulaiman
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 社会学

## Abstract

Machine-learning intrusion detectors often report near-perfect performance on familiar benchmarks, yet their generalization and decision transparency remain uncertain. This study evaluates a reproducible and explainable binary network-intrusion-detection workflow using the NSL-KDD KDDTrain+_20Percent file (25,192 records and 41 input features). Six classifiers were compared: Random Forest (RF), Logistic Regression, Decision Tree (DT), Support Vector Machine, k-Nearest Neighbors, and Gaussian Naive Bayes. The protocol used a stratified 70:30 hold-out split, five-fold stratified cross-validation, training-only preprocessing, a fixed random seed, and independent evaluation on KDDTest+. On the internal hold-out set, RF achieved 99.64% accuracy, 99.40% attack recall, 99.85% specificity, and a ROC-AUC of 0.99994; its five-fold mean accuracy was 99.74% with a standard deviation of 0.16%. On KDDTest+, RF accuracy decreased to 77.82%, whereas DT achieved the highest independent accuracy of 81.53%. Global and case-based SHAP analyses identified influential network features and explained correct, false-positive, and false-negative predictions. These findings show that near-perfect internal NSL-KDD performance does not establish deployment readiness without independent testing and transparent error analysis.
