---
title: "EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games"
authors: "Tristan Maidment, JB Lanier, Chase McDonald, Nathan Tsang, Eugene Vinitsky"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-06-26T06:00:59.694221"
arxiv_id: "http://arxiv.org/abs/2606.23995v1"
source_api: "arxiv"
categories: "cs.LG, cs.AI, cs.GT, cs.MA"
---

# EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games

**著者**: Tristan Maidment, JB Lanier, Chase McDonald, Nathan Tsang, Eugene Vinitsky
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Recent work has established that regularized policy gradient methods such as PPO, when used in self-play, can match or exceed specialized game-theoretic algorithms for solving two-player zero-sum imperfect-information games. The uniform distribution has emerged as a strong policy regularization target for this purpose, but it regularizes equally toward all actions regardless of their viability. We introduce EMAgnet, which instead regularizes toward an exponential moving average (EMA) of the last-iterate policy's parameters, providing an adaptive regularization target that evolves with the agent's improving strategy. We evaluate EMAgnet on both standard two-player zero-sum benchmarks and modified benchmarks with exploration challenges and large numbers of strictly dominated strategies. Relative to PPO self-play with uniform-magnet regularization under both linear and power-law annealing schedules, EMAgnet achieves lower exploitability in the majority of tested environments, with consistent performance gains across games containing strictly dominated strategies.
