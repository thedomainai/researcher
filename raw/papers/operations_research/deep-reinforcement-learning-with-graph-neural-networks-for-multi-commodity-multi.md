---
title: "Deep Reinforcement Learning with Graph Neural Networks for Multi-Commodity Multi-Modal Network Flow Optimization in Humanitarian Logistics"
authors: "Bülent Soykan"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-10-23T08:10:53.488119"
doi: "https://doi.org/10.3233/nicsp260059"
openalex_id: "https://openalex.org/W7223171318"
source_api: "openalex"
---

# Deep Reinforcement Learning with Graph Neural Networks for Multi-Commodity Multi-Modal Network Flow Optimization in Humanitarian Logistics

**著者**: Bülent Soykan
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

This study aims to investigate the impact of deep reinforcement learning (DRL) augmented with graph attention networks (GAT) on the efficiency and equity of humanitarian logistics operations. It addresses a critical gap in the existing literature regarding the real-time scalability of multi-commodity, multi-modal network flow (MCMMNF) optimization under dynamic demand and infrastructure uncertainty. The research seeks new insights into balancing operational costs with equitable aid distribution, contributing to a deeper understanding of AI-driven decision support in crisis response. The study employs a quantitative simulation-based approach, utilizing a custom Gymnasium environment to model complex humanitarian logistics networks. The problem is formulated as a Markov Decision Process (MDP) on heterogeneous graphs. We propose a novel DRL framework using Proximal Policy Optimization (PPO) combined with an attention-based Graph Neural Network (GAT) encoder to capture dynamic network topologies. Data were generated across three distinct scenarios (disaster response, refugee crisis, and pandemic response) and analyzed against traditional heuristics (Greedy, BestFit) and random baselines using metrics such as total cost, demand satisfaction, and the Gini coefficient. The results reveal that the PPO-GAT agent significantly outperforms the best heuristic baselines, achieving a 30.5% reduction in operational costs in disaster response scenarios while maintaining near-perfect demand satisfaction (98%). Furthermore, the findings indicate that the learned policy naturally optimizes for equity, achieving a Gini coefficient of 0.12 compared to 0.28 for greedy approaches. These findings provide evidence that attention mechanisms effectively identify critical supply chain bottlenecks without manual feature engineering, offering significant implications for developing autonomous, real-time decision support systems for humanitarian organizations.
