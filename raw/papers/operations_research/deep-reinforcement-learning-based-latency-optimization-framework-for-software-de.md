---
title: "Deep Reinforcement Learning-based Latency Optimization Framework for Software-defined Networks"
authors: "Yasser Jassem, Zainab Dhahir"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-08-31T09:35:57.354845"
doi: "https://doi.org/10.22266/ijies2026.0930.17"
openalex_id: "https://openalex.org/W7204652585"
source_api: "openalex"
---

# Deep Reinforcement Learning-based Latency Optimization Framework for Software-defined Networks

**著者**: Yasser Jassem, Zainab Dhahir
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Software-Defined Networking (SDN) enables centrally control.Conventional routing protocols are not able to cope with the extremely dynamic traffic conditions causing suboptimal Quality of Service (QoS).The proposed paper presents a routing framework (Deep Reinforcement Learning, DRL) of SDN based on Recurrent Proximal Policy Optimization (Recurrent PPO).The model uses Long Short-Term Memory (LSTM) to learn time-dependent relationships between network states to make routing decisions that are more flexible and context-sensitive.The routing decision process takes into account QoS metrics, such as latency, bandwidth, packet losses, and link utilization.A reward mechanism minimizes latency without compromising network stability.Evaluation relies on real multi-path routing scenarios derived from actual Mininet-based SDN simulations with genuine traffic patterns.Path selection occurs among five real candidate paths between source-destination pairs.Experimental results confirm that the proposed approach reaches 99.38% path selection accuracy across five candidate paths, with class-wise F1-scores exceeding 0.99 for all paths.The framework addresses practical SDN deployment aspects, including controller integration via OpenFlow rule translation, overhead analysis covering telemetry collection and inference latency, and benchmarking against traditional routing protocols such as Open Shortest Path First (OSPF) and deep reinforcement learning baselines including Deep Q-Network (DQN), Deep Deterministic Policy Gradient (DDPG), and Soft Actor-Critic (SAC).Performance improvements receive validation under dynamic network conditions across multiple topologies, namely Abilene, GEANT, and Fat-tree.
