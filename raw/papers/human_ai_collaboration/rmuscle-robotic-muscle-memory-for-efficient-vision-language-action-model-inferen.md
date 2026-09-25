---
title: "rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model Inference"
authors: "Kaijun Zhou, Zhiyang Li, Le Chen, Jinyu Gu"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-18T06:03:21.547901"
arxiv_id: "http://arxiv.org/abs/2609.19104v1"
source_api: "arxiv"
categories: "cs.RO, cs.AI"
---

# rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model Inference

**著者**: Kaijun Zhou, Zhiyang Li, Le Chen, Jinyu Gu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Factory work is a promising early scenario for embodied AI: assigning repetitive manual jobs to robots has clear economic payoff, and a structured station keeps the jobs tractable for current policies. Vision-Language-Action (VLA) models now dominate as the policy paradigm for these robots. The inference latency of VLA models directly affects robot responsiveness and motion smoothness. However, existing VLA inference frameworks do not fully exploit the characteristics of embodied workloads or account for the distinct bottlenecks across different stages of VLA inference.
  In this paper, we first characterize embodied workloads and identify substantial task similarity across repeated robot executions. We further find that such similarity extends beyond observations and action trajectories to internal model states. Drawing on these observations, we present rMuscle, a real-time VLA inference framework inspired by human muscle memory. It exploits cross-execution similarity through a dual-phase muscle-memory cache. The Context Cache reuses visual-token outputs to reduce computation, while the Action Cache reuses neuron activation patterns to reduce weight accesses. We keep both the cache memory footprint and access overhead low through online cache recomputation, sliding-window cache retrieval, and mask sharing across consecutive denoising steps. rMuscle achieves 1.29-1.42X speedup on RTX 4090 and Jetson Thor across LIBERO, RoboTwin, and physical manipulation tasks, while maintaining the original success rates on real-world robots.
