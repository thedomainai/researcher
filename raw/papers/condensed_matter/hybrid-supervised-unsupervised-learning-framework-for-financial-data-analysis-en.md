---
title: "Hybrid Supervised-unsupervised Learning Framework for Financial Data Analysis Enhanced by Quantum-inspired Computing"
authors: "Praneeth Reddy Amudala Puchakayala, Poonam Ghule, Vijay Vaswani, Jeevith S H"
year: 2026
citations: 0
paper_type: "primary"
domain: "condensed_matter"
fetched: "2026-11-27T06:08:09.032092"
doi: "https://doi.org/10.22266/ijies2026.1130.81"
openalex_id: "https://openalex.org/W7222536905"
source_api: "openalex"
---

# Hybrid Supervised-unsupervised Learning Framework for Financial Data Analysis Enhanced by Quantum-inspired Computing

**著者**: Praneeth Reddy Amudala Puchakayala, Poonam Ghule, Vijay Vaswani, Jeevith S H
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 物性物理

## Abstract

Financial time-series analysis poses some difficulties, due to the non-stationarity of data, its distribution is heavy-tailed, the regime structure in financial time-series is latent, and there are few labelled training signals available.These models are highly sensitive to unexpected trade-offs and limited out-of-distribution generalisation, and unsupervised models, on their own, are unable to directly inform tradeable decisions.This paper proposes a framework named Quantum-Inspired Hybrid Supervised-Unsupervised Learning (QIHSL) consisting of three tightly-integrated modules: (1) Quantum-Inspired Feature Transformation (QFT) module that maps the financial features into amplitudeand phase-encoded qubit-state analogues, and generates the cross-feature interaction terms inspired by entanglement;(2) Quantum-Inspired K-Means (QI-KMeans) clustering module that uses the quantum fidelity based distance metric to learn the regime (bull, bear, sideways) of the data in an unsupervised manner; and (3) a Quantum-Inspired Support Vector Machine (QI-SVM) regime-gated ensemble for robust and regime-aware return-direction prediction with QI-SVMs that specialise in predicting the return direction in different market regimes.The experiments on a comprehensive benchmark dataset of 4,950 synthetic daily observations from the S&P 500 index, used to capture the statistical properties of equity markets, namely Student-t distributed returns (ν = 5), three-state regime switching and nineteen technical indicators, show that QIHSL achieves an accuracy of 0.4913, a precision of 0.5538, a recall of 0.2588, an F1-score of 0.3527 and an AUC of 0.5029 on the hold-out test set, outperforming the baseline SVM by 5.92 percentage points in precision.It represents the best of all six comparison methods (Table 2) and for all the architectures in the matched-condition comparison (Table 7) is an advantage (not a finding) of precision for two instances of the simulation and does not necessarily mean that they are more likely to forecast than others.The controlled ablation study (Table 3) also shows that a component-level benefit for quantum-inspired feature enrichment can be measured by the QFT module's accuracy of +2.0 pp and F1-score of +11.9 pp over the SVM baseline (A2 vs. A1).Five-fold stratified cross validation gives a stability of AUC = 0.4987 ± 0.0095.An ablation study shows that the QFT module contributes the largest single-step accuracy gain (+2.0 pp) and F1-score gain (+11.9 pp over A1); adding regime gating further improves accuracy (+0.95 pp) but reduces F1 (-0.0786) and AUC (-0.0123) relative to QFT alone.The reported AUC (around 0.5) is at chance level, and no pairwise McNemar comparison is significant at alpha = 0.05 (the smallest p = 0.2433), which is consistent with the almost efficient nature of the synthetic benchmark.Combined, results show no statistically relevant predictive value for the synthetic benchmark.The most interesting aspect of QIHSL is its highest precision (0.5538) of all methods compared, which could have some relevance to conservative trading, but not to proven practical forecast effectiveness.
