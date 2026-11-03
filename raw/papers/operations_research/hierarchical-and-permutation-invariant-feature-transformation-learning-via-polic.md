---
title: "Hierarchical and Permutation-Invariant Feature Transformation Learning via Policy-Guided Embedding Search"
authors: "Rui Liu, Tao Zhe, Yanyong Huang, Sankha Narayan Guria, Xiao Luo"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-04T06:55:00.141382"
doi: "https://doi.org/10.1145/3799682.3840882"
openalex_id: "https://openalex.org/W7212144472"
source_api: "openalex"
---

# Hierarchical and Permutation-Invariant Feature Transformation Learning via Policy-Guided Embedding Search

**著者**: Rui Liu, Tao Zhe, Yanyong Huang, Sankha Narayan Guria, Xiao Luo
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Feature transformation improves predictive performance on tabular data by constructing informative abstractions from raw features. Recent generative approaches encode transformation knowledge into continuous embedding spaces for efficient exploration of candidate strategies, but face three key limitations: (1) overlooking hierarchical relationships between low-level features, operations, and high-level abstractions; (2) enforcing order-sensitive embeddings on inherently permutation-invariant transformation sequences, thereby introducing systematic bias; and (3) relying on gradient-based search, which is ill-suited to non-convex transformation spaces. We propose a framework with two complementary components. First, a permutation-invariant hierarchical module captures interactions across features, operations, and abstraction levels, with a self-attention pooling mechanism that maps semantically equivalent structures to consistent embeddings aligned with downstream performance. Second, a policy-guided multi-objective reinforcement learning strategy initializes the search from empirically strong seeds and jointly optimizes predictive accuracy and transformation efficiency. Extensive experiments on diverse tabular benchmarks demonstrate the effectiveness and robustness of our framework against strong baselines. Our code and data are publicly available at: https://github.com/RayLiu1103/PHER.
