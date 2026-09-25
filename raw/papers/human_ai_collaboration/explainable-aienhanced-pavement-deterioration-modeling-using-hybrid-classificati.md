---
title: "Explainable AI–enhanced pavement deterioration modeling using hybrid classification–regression deep learning architecture"
authors: "Mohammad Sedighian-Fard, Amir Golroo, Mahdi Javanmardi, Alexandre Alahi, Hananeh Dehghan Tezerjani"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-02T08:56:36.882219"
doi: "https://doi.org/10.1038/s41598-026-67842-x"
openalex_id: "https://openalex.org/W7161948940"
source_api: "openalex"
---

# Explainable AI–enhanced pavement deterioration modeling using hybrid classification–regression deep learning architecture

**著者**: Mohammad Sedighian-Fard, Amir Golroo, Mahdi Javanmardi, Alexandre Alahi, Hananeh Dehghan Tezerjani
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Abstract Effective Pavement Management System (PMS) planning depends on the ability to anticipate both the severity and physical extent of multiple distress types under real-world data constraints. This work introduces an interpretable dual-stage Deep Learning (DL) framework that sequentially classifies distress severity and then predicts the corresponding crack lengths, alligator cracking areas, and pothole quantities. The first stage uses an Artificial Neural Network (ANN) optimized with Focal loss to overcome severe class imbalance, while the second employs an ANN with Huber loss and targeted non-zero weighting to counteract outlier dominance and the zero-inflation inherent in sparse distress records. Data scarcity is addressed through the Synthetic Minority Over-sampling Technique (SMOTE) and Gaussian noise augmentation. To ensure the learned relationships are not merely correlational, an Explainable Artificial Intelligence (XAI) framework combining Shapley Additive Explanations (SHAP), Partial Dependence Plots (PDP), and Individual Conditional Expectation (ICE) curves is integrated, verifying that the model's internal logic adheres to established Mechanistic-Empirical (M-E) pavement science—most notably by recovering high-severity alligator cracking as the dominant antecedent to pothole formation. Beyond prediction quality, the design is substantiated through systematic ablation experiments: a shared-backbone Multi-Task Learning (MTL) variant is shown to degrade regression accuracy due to gradient interference between conflicting loss objectives, while network capacity is empirically scaled, using a bottleneck regularization strategy for data-scarce targets such as pothole area and count, to prevent overfitting without compromising expressiveness. The framework achieves an F1-score of 0.982 for pothole severity, and R² values of 0.954 for alligator cracking area and 0.941 for linear crack length. Paired t-tests confirm the absence of systematic bias, establishing the architecture as a high-fidelity and trustworthy input for pavement maintenance planning within the Long-Term Pavement Performance (LTPP) context.
