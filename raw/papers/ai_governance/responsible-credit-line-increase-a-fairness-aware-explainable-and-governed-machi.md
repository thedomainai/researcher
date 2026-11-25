---
title: "Responsible Credit-Line Increase: A Fairness-Aware, Explainable, and Governed Machine-Learning Framework for Socio-Technical Lending Systems"
authors: "Akshay Sharma, Gaurav Sharma"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-10-31T12:02:31.541080"
doi: "https://doi.org/10.21203/rs.3.rs-11530197/v1"
openalex_id: "https://openalex.org/W7224551783"
source_api: "openalex"
abstract_source: "openalex"
---

# Responsible Credit-Line Increase: A Fairness-Aware, Explainable, and Governed Machine-Learning Framework for Socio-Technical Lending Systems

**著者**: Akshay Sharma, Gaurav Sharma
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Automated credit-line decisions shape access to liquidity for millions of consumers and are subject to fair-lending law. We study proactive credit-line increase (CLI) as a responsible-AI problem in which economic optimization, algorithmic fairness, explainability, and governance are designed together. We formalize CLI as incremental-profit maximization under a portfolio expected-loss budget and explicit fairness tolerances, and reduce it to a calibrated, auditable threshold policy with group-level recalibration that controls disparate impact without altering the validated model. Because account-level credit data cannot be shared, we evaluate on a released synthetic portfolio of 60,000 accounts. On a time-held-out fold, gradient boosting and a logistic baseline discriminate almost equally (AUC 0.762 vs. 0.758) and perform alike at a matched approval rate, while isotonic calibration of the boosted scores reduces expected calibration error from 0.194 to 0.006. The model is equally accurate across protected groups, yet a single threshold produces disparate impact (demographic-parity gap 0.084, disparate-impact ratio 0.85); group-wise recalibration under the same loss budget reduces the parity gap to 0.013 at a 0.6% cost in realized profit. A fairness-economics frontier shows that closing the parity gap by extending access to the disadvantaged group is profit-neutral to profit-positive in this portfolio, while a multi-period simulation shows that sustaining parity narrows the credit-access gap by 43% at a 0.6% cost in cumulative profit. On a real public credit benchmark the models again perform alike and the fairness controls transfer. We map each component to responsible-AI principles and model-risk governance, offering a reproducible reference design.
