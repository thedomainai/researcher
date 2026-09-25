---
title: "AICO: Feature significance tests for supervised learning"
authors: "Kay Giesecke, Enguerrand Horel, Chartsiri Jirachotkulthorn"
year: 2026
citations: 1
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-25T06:06:18.171587"
doi: "https://doi.org/10.1073/pnas.2530045123"
openalex_id: "https://openalex.org/W4416615353"
source_api: "openalex"
---

# AICO: Feature significance tests for supervised learning

**著者**: Kay Giesecke, Enguerrand Horel, Chartsiri Jirachotkulthorn
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Machine learning is central to modern science, industry, and policy, yet its predictive power often comes at the cost of transparency: We rarely know which input features drive a model’s predictions. Without such understanding, researchers cannot draw reliable conclusions, practitioners cannot ensure fairness or accountability, and policymakers cannot trust or govern model-based decisions. Existing tools for assessing feature influence are limited; most lack statistical guarantees, and many require costly retraining or surrogate modeling, making them impractical for large modern models. We introduce AICO (Add-In COvariates), a broadly applicable framework that turns model interpretability into an efficient statistical exercise. AICO tests whether each feature contributes to predictive performance by masking its information and measuring the resulting change. The method provides exact, finite-sample feature P -values and CIs for feature importance through a simple, nonasymptotic hypothesis testing procedure. It requires no retraining, surrogate modeling, or distributional assumptions, making it feasible for large-scale algorithms. In both controlled experiments and real applications, from credit scoring to mortgage-behavior prediction, AICO identifies variables that contribute to model behavior, providing a scalable and statistically principled path toward transparent and trustworthy machine learning.
