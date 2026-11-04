---
title: "The Comparative Analysis of Hybrid Sampling, EasyEnsemble, and SVM-SMOTE Performance for Imbalanced Data Based on Bayesian Optimization"
authors: "Megawati Zein Waliulu, Kusman Sadik, Asep Saefuddin"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-05T08:16:35.794017"
doi: "https://doi.org/10.18860/cauchy.v11i2.42968"
openalex_id: "https://openalex.org/W7225075008"
source_api: "openalex"
---

# The Comparative Analysis of Hybrid Sampling, EasyEnsemble, and SVM-SMOTE Performance for Imbalanced Data Based on Bayesian Optimization

**著者**: Megawati Zein Waliulu, Kusman Sadik, Asep Saefuddin
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Imbalanced data represents a common challenge in classification modeling, as it can lead to prediction bias and reduce the models ability to correctly identify minority classes, which are often more critical. This study aims to compare the performance of three imbalance-handling techniquesHybrid Sampling, EasyEnsemble, and SVM-SMOTEapplied to the XGBoost classifier with hyperparameter tuning using Bayesian Optimization. A simulation study was conducted under a factorial completely randomized design involving three factors: class proportion (70:30, 80:20, 90:10), predictor variable types (10 categorical variables and a combination of 5 categorical and 5 numeric variables), and imbalance handling methods. Model performance was evaluated using balanced accuracy, sensitivity, and specificity. During the optimization process, 20 hyperparameter combinations were initially selected as prior evaluation points, followed by 20 additional optimization iterations to refine the search for the optimal hyperparameter configuration. The Bayesian Optimization process produced different optimal hyperparameter combinations for each simulation scenario, reflecting the distinct characteristics of the data under different experimental conditions. The analysis of variance revealed that both the main effects and the interactions among all factors significantly influenced classification performance. Among the evaluated methods, EasyEnsemble consistently achieved the best performance across all class imbalance scenarios. For all class proportions (70:30, 80:20, and 90:10), both in datasets consisting of 10 categorical predictor variables and in datasets comprising a combination of 5 categorical and 5 numerical predictor variables, EasyEnsemble achieved balanced accuracy, sensitivity, and specificity values consistently exceeding 0.90. Furthermore, Bayesian Optimization effectively enhanced the classification performance of XGBoost by efficiently identifying optimal hyperparameter configurations. Overall, the findings demonstrate that the combination of EasyEnsemble and Bayesian Optimization provides an effective approach for addressing class imbalance and improving classification performance.
