---
title: "Entropy Regularization in Deep Reinforcement Learning: A Structured Review Across Classical Control, Generative Policies, and Reasoning Language Models"
authors: ["Giorgio Taricco"]
year: 2026
cited_by_count: 0
doi: "https://doi.org/10.3390/e28070811"
openalex_id: W7169567789
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Entropy Regularization in Deep Reinforcement Learning: A Structured Review Across Classical Control, Generative Policies, and Reasoning Language Models

**Authors**: Giorgio Taricco | **Year**: 2026 | **Cited by**: 0 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Entropy regularization is a recurring mechanism in reinforcement learning (RL), but its meaning changes across algorithmic settings. In classical online RL, entropy encourages exploration and smooths policy improvement; in inverse RL and imitation learning, maximum-entropy resolves ambiguity among expert-consistent behaviors; in offline RL, entropy must be balanced against data support; in generative policies, entropy becomes a tractability problem; and in reinforcement learning with verifiable rewards (RLVR) for large language models (LLMs), token entropy is tied to reasoning diversity, calibration, and collapse. This review organizes these developments into a unified taxonomy. We first summarize the mathematical foundations of maximum-entropy RL, soft Bellman equations, policy-gradient entropy dynamics, and Kullback-Leibler (KL)-constrained mirror descent. We then review entropy in imitation learning, offline RL, intrinsic motivation, diffusion and flow-based policy classes, and RLVR. Particular attention is given to recent work on entropy collapse in reasoning LLMs, entropy-based advantage shaping, covariance-based control, positive-advantage reweighting, and ordinary differential equation (ODE)-based flow-matching policies with tractable entropy. The review emphasizes that entropy is not universally beneficial: useful exploration, support preservation, multimodality, calibration, and reasoning diversity require different entropy objects and different control mechanisms.
