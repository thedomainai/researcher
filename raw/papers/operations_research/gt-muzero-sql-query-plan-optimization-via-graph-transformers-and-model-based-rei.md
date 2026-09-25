---
title: "GT-Muzero: SQL Query Plan Optimization via Graph Transformers and Model-Based Reinforcement Learning"
authors: "Fuming Ye, Wenting Li, Qiong Zhou, Jie Ye, Mengzhu Liu"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-22T09:24:06.210927"
doi: "https://doi.org/10.31449/inf.v50i15.13987"
openalex_id: "https://openalex.org/W7213663463"
source_api: "openalex"
---

# GT-Muzero: SQL Query Plan Optimization via Graph Transformers and Model-Based Reinforcement Learning

**著者**: Fuming Ye, Wenting Li, Qiong Zhou, Jie Ye, Mengzhu Liu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Learning-based Structured Query Language (SQL) optimizers often face low sample efficiency and high training costs. To address these challenges, this study proposes a query optimization framework, GT- MuZero, which integrates a Graph Transformer (GT) with the model-based reinforcement learning (RL) algorithm MuZero. The framework converts SQL queries into heterogeneous graphs containing tables, predicates, and join operators. Structural encoding is performed via Laplacian feature vectors. GT’s global self-attention mechanism effectively overcomes the over-smoothing problem encountered by traditional Graph Neural Networks (GNNs) when processing deep execution trees. MuZero reduces reliance on costly real-database interactions by performing virtual forward planning in a learned latent space. Experiments on a high-performance server equipped with NVIDIA A100 GPUs, using the 100 GB TPC-DS benchmark datasets, demonstrated exceptional sample efficiency: GT-MuZero achieved 96.73% policy consistency with only 10,000 real training samples, whereas conventional methods such as GCN- PPO required more than 50,000 samples. Quantitative evaluation showed a geometric mean performance ratio (GMPR) of 2.81. Compared with the PostgreSQL baseline, latency for complex queries was reduced by more than 3.8 times. Although the average inference latency of 155 ms exhibits diminishing returns for minimal queries, the framework’s high sample efficiency and closed-loop robustness under large-scale, complex analytical workloads demonstrate its practical effectiveness and scientific value for building high-performance, adaptive intelligent database systems.
