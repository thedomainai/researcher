---
title: "STRAPSim: A Portfolio Similarity Metric for ETF Alignment and Portfolio Trades"
authors: "Mingshu Li, Dhruv Desai, Jerinsh Jeyapaulraj, Philip Sommer, Riya Jain"
year: 2026
citations: 0
paper_type: "primary"
domain: "finance_corporate"
fetched: "2026-11-15T06:55:01.352293"
doi: "https://doi.org/10.1145/3858063.3858885"
openalex_id: "https://openalex.org/W4415336009"
source_api: "openalex"
---

# STRAPSim: A Portfolio Similarity Metric for ETF Alignment and Portfolio Trades

**著者**: Mingshu Li, Dhruv Desai, Jerinsh Jeyapaulraj, Philip Sommer, Riya Jain
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: コーポレートファイナンス

## Abstract

Accurately measuring portfolio similarity is critical for a wide range of financial applications, including Exchange-traded Fund (ETF) recommendation, portfolio trading, and risk alignment. Existing similarity measures often rely on exact asset overlap or static distance metrics, which fail to capture similarities among the constituents (e.g., securities within the portfolio) as well as nuanced relationships between partially overlapping portfolios with heterogeneous weights. We introduce STRAPSim (Semantic, Two-level, Residual-Aware Portfolio Similarity), a novel method that computes portfolio similarity by matching constituents based on semantic similarity, weighting them according to their portfolio share, and aggregating results via residual-aware greedy alignment. We benchmark our approach against Jaccard, weighted Jaccard, as well as BERTScore-inspired variants across public classification, regression, and recommendation tasks, as well as on corporate bond ETF datasets. Empirical results show that our method consistently outperforms baselines in predictive accuracy and ranking alignment, achieving the highest Spearman correlation with return-based similarity. By leveraging constituent-aware matching and dynamic reweighting, portfolio similarity offers a scalable, interpretable framework for comparing structured asset baskets, demonstrating its utility in ETF benchmarking, portfolio construction, and systematic execution.
