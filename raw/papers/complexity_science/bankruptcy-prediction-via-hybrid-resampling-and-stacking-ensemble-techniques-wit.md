---
title: "Bankruptcy Prediction via Hybrid Resampling and Stacking Ensemble Techniques with Explainable Artificial Intelligence (XAI)-Driven Analysis"
authors: "Obu-Amoah Ampomah, Edmund Fosu Agyemang, Kofi Acheampong, Louis Agyekum, Enock Adu Bonsu"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-19T09:05:29.621436"
doi: "https://doi.org/10.21203/rs.3.rs-11545501/v1"
openalex_id: "https://openalex.org/W7204130993"
source_api: "openalex"
---

# Bankruptcy Prediction via Hybrid Resampling and Stacking Ensemble Techniques with Explainable Artificial Intelligence (XAI)-Driven Analysis

**著者**: Obu-Amoah Ampomah, Edmund Fosu Agyemang, Kofi Acheampong, Louis Agyekum, Enock Adu Bonsu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Abstract Reliable bankruptcy prediction is essential for creditors, investors, auditors, and regulators because delayed identification of financial distress can result in substantial economic losses. However, bankruptcy is a rare event, and severe class imbalance can produce high overall accuracy while concealing poor detection of distressed firms. This study develops an integrated bankruptcy prediction framework using the Taiwanese Bankruptcy Prediction dataset. Five boosting classifiers and five deep learning models were evaluated as standalone models. A two-stage stacking procedure subsequently used five-fold out-of-fold predictions from the boosting models as inputs to the deep learning meta-learners. The results show that resampling strategy materially shaped model behavior. SVM-SMOTE and SMOTE-Tomek favored accuracy and specificity, whereas SMOTE-ENN delivered stronger minority-class detection. Among standalone models, the RNN with SVM-SMOTE achieved the best overall predictive balance, with recall of 0.8235, G-mean of 0.8639, and ROC-AUC of 0.9417. Among stacking ensembles, SMOTE-ENN with (GB+XGB+HGB+LGBM+AB) + LSTM provided the best results with recall of 0.7255, G-mean of 0.8254, and ROC-AUC of 0.9270. SHAP analysis further showed that predicted bankruptcy risk was driven primarily by profitability, solvency and capital structure, debt-servicing burden, and operational efficiency and cost pressure. The findings demonstrate that no single resampling-model configuration universally dominates; therefore, model selection should reflect whether the operational priority is overall classification performance or the detection of bankrupt firms. The proposed framework provides an interpretable and leakage-controlled approach for aligning bankruptcy prediction with different financial risk-management objectives.
