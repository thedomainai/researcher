---
title: "Fully Byzantine-Resilient Distributed Multi-Agent Q-Learning"
authors: "Haejoon Lee, Dimitra Panagou"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-04-06T13:19:32.276372"
arxiv_id: "http://arxiv.org/abs/2604.02791v1"
source_api: "arxiv"
categories: "cs.MA, eess.SY"
---

# Fully Byzantine-Resilient Distributed Multi-Agent Q-Learning

**著者**: Haejoon Lee, Dimitra Panagou
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

We study Byzantine-resilient distributed multi-agent reinforcement learning (MARL), where agents must collaboratively learn optimal value functions over a compromised communication network. Existing resilient MARL approaches typically guarantee almost sure convergence only to near-optimal value functions, or require restrictive assumptions to ensure convergence to optimal solution. As a result, agents may fail to learn the optimal policies under these methods. To address this, we propose a novel distributed Q-learning algorithm, under which all agents' value functions converge almost surely to the optimal value functions despite Byzantine edge attacks. The key idea is a redundancy-based filtering mechanism that leverages two-hop neighbor information to validate incoming messages, while preserving bidirectional information flow. We then introduce a new topological condition for the convergence of our algorithm, present a systematic method to construct such networks, and prove that this condition can be verified in polynomial time. We validate our results through simulations, showing that our method converges to the optimal solutions, whereas prior methods fail under Byzantine edge attacks.
