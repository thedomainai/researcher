---
title: "PRIME: Plasticity Recovery in Multi-Agent Environments for UAV-Assisted Emergency Communication Networks"
authors: "Wen Qiu, Zhiqiang He, Wei Zhao, Hiroshi Masui"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-07-22T06:00:55.921704"
arxiv_id: "http://arxiv.org/abs/2607.17922v1"
source_api: "arxiv"
categories: "cs.MA, cs.LG, cs.NI"
---

# PRIME: Plasticity Recovery in Multi-Agent Environments for UAV-Assisted Emergency Communication Networks

**著者**: Wen Qiu, Zhiqiang He, Wei Zhao, Hiroshi Masui
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Most reinforcement learning controllers for these networks assume stationary conditions, and the few that handle change react to the external environment while leaving the network's internal state unexamined. We show that sustained non-stationarity damages this internal state directly: as objectives shift, neurons progressively fall dormant and the shared policy loses the capacity to learn. The obvious remedy, resetting dormant neurons, is unsafe under shared-parameter multi-agent training: many neurons that appear inactive are still receiving strong training gradients, and whether a neuron appears dormant depends on which agent's observations it processes. PRIME (Plasticity Recovery In Multi-agent Environments) therefore verifies both directions before intervening. Extending the bidirectional Silent Neuron framework to cooperative multi-agent reinforcement learning, it aggregates activation and gradient statistics over the full team batch, reads the backward signal from the gradient the training loss has already deposited , not from a hand-crafted proxy, and reinitializes only neurons that are simultaneously activation-dormant and gradient-silent. Useful representations are preserved while learning capacity is restored. On a phase-switching UAV emergency communication simulator, PRIME improves interquartile mean return by 24.9\% over MAPPO and holds dormant neuron fractions at 10--20\% versus 40--45\%; ablations attribute the gains to the gradient signal and team-level aggregation rather than to the specific reset operator. A dynamic regret bound shows that the perturbation cost scales with the small silent-subspace dimension rather than the full parameter count.
