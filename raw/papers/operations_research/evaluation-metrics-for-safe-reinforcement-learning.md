---
title: "Evaluation Metrics for Safe Reinforcement Learning"
authors: "Lindsay Spoor, Aske Plaat, Thomas Moerland"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-18T09:14:04.674571"
doi: ""
openalex_id: "https://openalex.org/W7213372353"
source_api: "openalex"
---

# Evaluation Metrics for Safe Reinforcement Learning

**著者**: Lindsay Spoor, Aske Plaat, Thomas Moerland
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Safe reinforcement learning (RL) is commonly formalized as a Constrained Markov Decision Process (CMDP), in which an agent maximizes expected reward while keeping its expected cumulative cost below a specified safety bound. Existing safe RL benchmarks predominantly report whether an algorithm is safe on average, following this expectation-based guarantee. We argue that this convention is insufficient to reliably characterize an algorithm's true safety: it fails to capture how often and how severely the safety bound is violated, whether this holds consistently across tasks and safety bounds, and whether training-time behavior is representative of behavior of the final converged policy. Therefore, we introduce (i) evaluation metrics for safe RL that address each of these concerns and in addition allow for aggregation across tasks and safety bounds. We furthermore define (ii) a safety tier system to systematically categorize and compare algorithms in terms of safety and reliability at both training and for a final policy. Using this framework, we provide (iii) an empirical safety evaluation across multiple safety navigation tasks. Our results show that aggregate metrics, distributional reporting, and task- and safety bound-specific results each reveal information the other metrics cannot. We therefore recommend reporting all three jointly, rather than compressing this information into a single value, as is common practice. We provide SafeRLEval, an open-source evaluation suite to support the reliable characterization of safety in future safe RL research.
