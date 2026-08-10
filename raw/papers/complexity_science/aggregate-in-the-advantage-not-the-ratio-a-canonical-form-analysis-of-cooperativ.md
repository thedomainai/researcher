---
title: "Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization"
authors: "Zijian Zhao, Sen Li"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-07-22T06:00:51.593292"
arxiv_id: "http://arxiv.org/abs/2607.17924v1"
source_api: "arxiv"
categories: "cs.MA, cs.LG"
---

# Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization

**著者**: Zijian Zhao, Sen Li
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Multi-agent policy optimization, exemplified by PPO-based methods, is a key branch of cooperative Multi-Agent Reinforcement Learning (MARL). A central design question is how many neighboring agents\footnote{In this paper, "neighbors" refer not only to physical proximity but also to agents whose actions influence one another.} to aggregate in order to effectively utilize global information for cooperation. This decision must be made along two dimensions: in the advantage (which agents' rewards contribute to the credit signal) and in the ratio (which agents' likelihood ratios form the clipped importance weight). Existing methods occupy scattered, underexplored points on these two axes: IPPO treats both separately; MAPPO pairs a team-level advantage with per-agent ratios; HAPPO employs sequential ratios with per-agent advantages; and single-agent reductions operating on factorized joint policies aggregate both into fully joint products. We formalize these two design choices as support matrices $\SA$ and $\SR$, and prove a canonical structure: the expected multi-agent policy optimization objective depends on the pair $(\SA,\SR)$ only through their matrix product $\tS=\SR\SA$. This yields two key consequences: (i) Redundancy: the two support matrices are interchangeable with respect to the signal, meaning neither aggregation pattern is inherently superior.(ii) Variance Ordering: the advantage aggregates rewards as a sum (additive variance with an interior bias-variance optimum at the coupling neighborhood), whereas the ratio aggregates likelihood ratios as a product (multiplicative variance that grows exponentially with support size, with no accompanying bias reduction). The resulting design principle is unambiguous: aggregate neighbors in the advantage, sized to the coupling neighborhood, and keep the ratio per-agent.
