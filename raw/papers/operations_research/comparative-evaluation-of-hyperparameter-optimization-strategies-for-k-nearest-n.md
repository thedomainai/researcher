---
title: "Comparative Evaluation of Hyperparameter Optimization Strategies for k-Nearest Neighbors over Mixed Domain Search Spaces"
authors: "Meta Kallista, Ig. Prasetya Dwi Wibawa, Heni Widayani"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-29T06:05:42.425770"
doi: "https://doi.org/10.18860/cauchy.v11i2.42295"
openalex_id: "https://openalex.org/W7213548054"
source_api: "openalex"
---

# Comparative Evaluation of Hyperparameter Optimization Strategies for k-Nearest Neighbors over Mixed Domain Search Spaces

**著者**: Meta Kallista, Ig. Prasetya Dwi Wibawa, Heni Widayani
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

k-Nearest Neighbors (KNN) remains a strong baseline due to its simplicity, interpretability, and non-parametric structure; however, its predictive performance is highly sensitive to interacting hyperparameters. This paper studies search-constrained hyperparameter optimization for KNN over a mixed search space comprising an integer neighborhood size, a categorical distance metric, and a continuous Minkowski exponent. Seven tuning strategies are compared under a unified nested validation protocol with standardized preprocessing: grid search, random search, Bayesian optimization, genetic algorithm, surrogate optimization, particle swarm optimization, and grey wolf optimizer. Experiments on diverse public classification datasets from UCI, OpenML, and Kaggle evaluate predictive performance (accuracy, macro-AUC, cross-entropy), validation loss, and runtime. The results indicate that adaptive optimizers generally provide more favorable performancecost trade-offs than exhaustive grids under limited evaluations, while no single method is uniformly best across all datasets. Rank-based statistical comparisons using non-parametric tests further support the observed differences and motivate practical recommendations for selecting tuning strategies as a function of evaluation search and mixed-domain search-space characteristics.
