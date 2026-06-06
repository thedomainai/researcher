---
title: "Explaining sentiment in self-admitted technical debt: a comparative study of model-agnostic explainability methods"
authors: "Peiyu Chen, Xingguang Yang, Zhenyu Shu, G Z Wang, Zijie Huang"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-06-02T06:00:07.951763"
doi: "https://doi.org/10.1108/ijicc-01-2026-0066"
openalex_id: "https://openalex.org/W7162931983"
source_api: "openalex"
---

# Explaining sentiment in self-admitted technical debt: a comparative study of model-agnostic explainability methods

**著者**: Peiyu Chen, Xingguang Yang, Zhenyu Shu, G Z Wang, Zijie Huang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Purpose Self-Admitted Technical Debt (SATD) consists of source-code comments in which developers explicitly acknowledge suboptimal design or implementation decisions that require future improvement. These comments often convey emotional signals such as frustration, urgency, or concern, which may reflect the perceived severity and priority of technical debt. While sentiment analysis has been increasingly applied to SATD, little attention has been paid to the interpretability and reliability of sentiment predictions produced by modern deep learning models. This study aims to investigate how explainable artificial intelligence (XAI) techniques interpret SATD sentiment predictions and whether different model-agnostic explanation methods provide consistent or divergent explanations. Specifically, we examine the reliability, agreement, and limitations of popular post-hoc explainers when applied to BERT-based SATD sentiment classification. Design/methodology/approach We formulate SATD sentiment analysis as a binary classification task that distinguishes negative from non-negative comments and fine-tune a BERT model on a manually curated SATD sentiment dataset using ten-fold cross-validation. For all correctly predicted instances, we generate local token-level explanations using three model-agnostic XAI techniques: LIME, SHAP, and BreakDown. We quantitatively assess explanation behaviour and cross-method consistency using feature contribution distributions, top-k token overlap, semantic similarity based on BERT embeddings, and Spearman rank correlation. Findings The results reveal substantial divergence among the three explanation methods. LIME, SHAP, and BreakDown assign markedly different contribution magnitudes to influential tokens, exhibit near-zero overlap in top-k features, and frequently produce contradictory ranking orders and sentiment contribution directions. Statistical tests further confirm that these differences are systematic rather than random across both negative and non-negative sentiment categories. Originality/value Our findings demonstrate that model-agnostic explanation techniques cannot be used interchangeably for interpreting SATD sentiment predictions. Relying on a single explainer may lead to incomplete or misleading interpretations of developer intent. We therefore recommend multi-method triangulation and manual validation when explanation results are used to support technical debt prioritisation, code review, or maintenance decision-making. This study provides a comprehensive and reproducible empirical analysis of explanation reliability and divergence for SATD sentiment analysis, contributing a foundation for trustworthy and interpretable SATD analytics.
