---
title: "Disclosure-Gated User Simulation for Companion-Agent Evaluation"
authors: "Yao Liu, Yu He"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-09-03T06:02:04.229150"
arxiv_id: "http://arxiv.org/abs/2609.00982v1"
source_api: "arxiv"
categories: "cs.CL, cs.AI, cs.HC"
---

# Disclosure-Gated User Simulation for Companion-Agent Evaluation

**著者**: Yao Liu, Yu He
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

Using a large language model to play the user is now standard in scalable evaluation. It has a repeatedly diagnosed failure: the simulated user is excessively cooperative, so a system under test can score by the sheer number of questions it asks rather than by making the user willing to speak. We answer with a disclosure gate conditioning information release on the companion agent's behaviour: its state is a ladder of five ordered gates, merged onto three observable depth layers. We specify, ablate, and audit it, and train a user simulator against that specification. Gating behaviour is learned from the training corpus's synthetic branch, while the real branch supplies how people speak and react; after training, the simulator need not be told at runtime which gate each item sits behind. The gate is a load-bearing component of the environment: on the English corpus of a published companion-agent benchmark (CompanionBench), once training no longer states per example which gate each item sits behind, the largest rank displacement across 12 systems under test exceeds the noise band set by re-running that environment under a new seed, while per-system scores show no detectable change. We state two acceptance criteria: a ranking must be order-preserving, and absolute scores must be scale-stable. Of the candidates we examine, only one passes both -- the simulator we release -- and its leaderboard correlates at 0.993 with the benchmark's original simulator. By contrast, prompting a frontier model as the simulator barely moves the ranking while shifting every score upward -- a shift invisible to anyone checking the ranking alone. The environment we specify is the one that benchmark already used. That publication describes the mechanism in about four hundred words, and we supply what it lacked: specification, ablations, human studies, negative controls, and downstream sensitivity analysis.
