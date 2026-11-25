---
title: "Knowledge Graph-Enhanced Deep Reinforcement Learning for Optimal Dispatch of Microgrids"
authors: "張基玉, Kehe Wu, Wenchao Cui, Fangfang Dang, Xiaoliang Zhang"
year: 2027
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-26T06:05:55.152179"
doi: "https://doi.org/10.32604/cmc.2026.089295"
openalex_id: "https://openalex.org/W7221769406"
source_api: "openalex"
---

# Knowledge Graph-Enhanced Deep Reinforcement Learning for Optimal Dispatch of Microgrids

**著者**: 張基玉, Kehe Wu, Wenchao Cui, Fangfang Dang, Xiaoliang Zhang
**年**: 2027 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

To address the challenges of incomplete state representation, hard-to-guarantee safety constraints, and slow convergence driven by sparse rewards in microgrid dispatch, a knowledge graph-enhanced deep reinforcement learning (DRL) optimization method is proposed. Based on the Soft Actor-Critic (SAC) framework, the approach integrates both static dispatch regulation and event knowledge graphs. Specifically, a Relational Graph Convolutional Network (R-GCN) is deployed to encode the static graph into the state space, thereby enhancing structural and semantic awareness of the system. To enhance operational safety, rule reasoning over the static knowledge graph formulates a safe action feasible region, where projection operators ensure strict satisfaction of device-level box constraints, while coupled constraints are addressed via reward penalties. Furthermore, event graph similarity retrieval is leveraged to construct potential-based reward shaping and adaptive behavioral regularization, which are combined with a knowledge-credibility-weighted experience replay mechanism to accelerate convergence. Simulation results on a modified IEEE 33-bus system across four distinct scenarios demonstrate that, compared to the baseline SAC algorithm in conventional settings, the proposed method reduces daily operational costs by 7.8%, lowers constraint violation rates by 81.3%, and decreases convergence episodes by 33.6% on this benchmark. Moreover, it exhibits superior robustness and performance across all metrics under complex perturbation scenarios.
