---
title: "MATES: Learning Multi-Agent Interactions by Transforming Observations for Frozen Single-Agent Policies"
authors: "Elie Abboud, Oren Gal"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-24T06:01:03.418881"
arxiv_id: "http://arxiv.org/abs/2609.26010v1"
source_api: "arxiv"
categories: "cs.MA, cs.RO, eess.SY"
---

# MATES: Learning Multi-Agent Interactions by Transforming Observations for Frozen Single-Agent Policies

**著者**: Elie Abboud, Oren Gal
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Multi-agent reinforcement learning (MARL) commonly trains decentralized policies from scratch, requiring agents to acquire individual task competence and coordination simultaneously. Yet many multi-agent problems admit a compatible single-agent counterpart in which the underlying task can be learned in isolation. We introduce Multi-Agent Observation Transformation for Existing Single-Agent Policies (MATES), an input-side adaptation framework for tasks whose multi-agent observations preserve the solo-task information while exposing separately identifiable neighbor information. From multi-agent experience, MATES learns a small adapter that maps this observation into the format expected by a frozen single-agent policy, inducing actions suited to the shared environment without updating the single-agent policy itself. MATES leaves the pretrained policy's internal architecture unchanged and retains the objectives and update procedures of the underlying MARL algorithm. We evaluate MATES using both on- and off-policy algorithms on lifelong pathfinding, navigation, and cooperative discovery, spanning discrete and continuous observation and action spaces. Across all evaluated settings, MATES optimizes only 3.5-7.3% as many parameters as full-policy training while consistently outperforming MARL training from scratch. It approaches the performance of full fine-tuning, remains competitive overall with demonstration-based baselines, and retains strong task performance at team sizes not encountered during training. These results provide evidence that, under this observation structure, effective multi-agent behavior can be learned without modifying the policy that encodes individual competence.
