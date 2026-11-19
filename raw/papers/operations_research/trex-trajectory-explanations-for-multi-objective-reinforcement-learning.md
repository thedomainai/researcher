---
title: "TREX: Trajectory Explanations for Multi-objective Reinforcement Learning"
authors: "Dilina Chandika Rajapakse, Juan C. Rosero, Ivana Dusparić"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-20T06:05:44.755955"
doi: "https://doi.org/10.1007/978-3-032-45470-6_11"
openalex_id: "https://openalex.org/W7140205654"
source_api: "openalex"
---

# TREX: Trajectory Explanations for Multi-objective Reinforcement Learning

**著者**: Dilina Chandika Rajapakse, Juan C. Rosero, Ivana Dusparić
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Reinforcement Learning (RL) has demonstrated its ability to solve complex decision-making problems in a variety of domains, by optimizing reward signals obtained through interaction with an environment. However, many real-world scenarios involve multiple, potentially conflicting objectives that cannot be easily represented by a single scalar reward. Multi-Objective Reinforcement Learning (MORL) addresses this limitation by enabling agents to optimize several objectives simultaneously, explicitly reasoning about trade-offs between them. However, the ``black box" nature of the RL models makes the decision process behind chosen objective trade-offs unclear. Current Explainable Reinforcement Learning (XRL) methods are typically designed for single scalar rewards and do not account for explanations with respect to distinct objectives or user preferences. To address this gap, in this paper we propose TREX, a Trajectory based Explainability framework to explain Multi-objective Reinforcement Learning policies, based on trajectory attribution. TREX generates trajectories directly from the learned expert policy, across different user preferences and clusters them into semantically meaningful temporal segments. We quantify the influence of these behavioural segments on the Pareto trade-off by training complementary policies that exclude specific clusters, measuring the resulting relative deviation on the observed rewards and actions compared to the original expert policy. Experiments on multi-objective MuJoCo environments - HalfCheetah, Ant and Swimmer, demonstrate the framework's ability to isolate and quantify the specific behavioural patterns.
