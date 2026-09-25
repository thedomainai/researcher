---
title: "An Integrated Machine Learning Framework for Multi-task Retail Decision Support with Explainable AI"
authors: "Eman Taher, Doaa S. Elzanfaly, Wessam H. El-Behaidy"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-09-21T06:00:39.844441"
doi: "https://doi.org/10.22266/ijies2026.1031.71"
openalex_id: "https://openalex.org/W7213629713"
source_api: "openalex"
---

# An Integrated Machine Learning Framework for Multi-task Retail Decision Support with Explainable AI

**著者**: Eman Taher, Doaa S. Elzanfaly, Wessam H. El-Behaidy
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

Modern Retail companies must understand their customers, optimize their products, and forecast revenue accurately to remain competitive, yet most organizations lack integrated systems capable of translating transactional data into concrete business decisions.These are not data problems but intelligence problems: the absence of systems that extract the right insight at the right time.Machine learning (ML) addresses this gap by automatically generating customer profiles, product suggestions, and revenue forecasts from historical data.However, Artificial Intelligence (AI) alone is insufficient; managers will not act on predictions they cannot understand.Explainable Artificial Intelligence (XAI) solves this final barrier by making every model transparent and justifiable, ensuring AI-driven recommendations carry the trust required for real operational adoption.This paper proposes a unified, intelligent decision-support framework integrating four ML modules: Customer Segmentation, Product Recommendation, Product-Level Sales Prediction, and Daily Sales Forecasting, with XAI applied to the segmentation, product-level prediction, and forecasting modules, and a Large Language Model (LLM) based automated reporting with the LLaMA model, evaluated on the Global Superstore dataset.The LRFMV (Length, Recency, Frequency, Monetary, Volume) model with K-Means (K=3) yields three interpretable segments: At-Risk (16%), Regular (51.3%),VIP Active (32.7%), validated at 93% classification accuracy with SHapley Additive exPlanations (SHAP) Fidelity=1.00 and Local Interpretable Model-Agnostic Explanations (LIME) Stability=0.99 for the segmentation surrogate classifier.User-User Collaborative Filtering (CF) achieves the best recommendation F1-Score = 0.31 and Recall=0.98;XGBoost achieves Test R²=0.95 for product-level prediction, and Linear Regression outperforms all ensemble models for daily forecasting (R²=0.9876,Mean Absolute Error=$198), with 7-day Exponential Moving Average (EMA) confirmed as the dominant feature across all three models.LLM layer synthesizes all outputs into structured business intelligence reports.The results demonstrate that accuracy, interpretability, and actionability are mutually reinforced rather than competing objectives, providing a replicable blueprint for deploying responsible, human-centered AI in retail decisionmaking.
