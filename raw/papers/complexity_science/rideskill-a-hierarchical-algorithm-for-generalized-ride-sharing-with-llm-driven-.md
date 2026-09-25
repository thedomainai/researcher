---
title: "RideSkill: A Hierarchical Algorithm for Generalized Ride Sharing with LLM-Driven Automatic Evolution"
authors: "Zijian Zhao, Sen Li, Xialiang Tong, Mingxuan Yuan"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-04T08:57:50.541440"
arxiv_id: "http://arxiv.org/abs/2609.02250v1"
source_api: "arxiv"
categories: "cs.MA, cs.CL, cs.ET, cs.LG"
---

# RideSkill: A Hierarchical Algorithm for Generalized Ride Sharing with LLM-Driven Automatic Evolution

**著者**: Zijian Zhao, Sen Li, Xialiang Tong, Mingxuan Yuan
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Ride-sharing, which allows multiple passengers with different origin-destination (OD) pairs to share a single vehicle, is a challenging operational problem, as it requires orders with different OD pairs to be efficiently bundled and assigned to vehicles under uncertain and varying scenarios. Although multi-agent reinforcement learning (MARL) solutions have achieved promising performance, they suffer from limited generalization (adapting to different environmental scenarios), low transferability (adapting to different platform objectives), and training difficulties in large-scale systems, such as the curse of dimensionality. Recently, motivated by the scaling of large language models (LLMs), several works have incorporated LLMs into ride-hailing systems, either by employing LLMs directly as decision-making agents or using them for automatic algorithm design. However, none of these approaches support vehicle sharing, which complicates the problem by expanding both the state and action spaces exponentially. Moreover, most of them require frequent LLM calls at inference time, making them infeasible for real-time deployment. To address these issues, we propose RideSkill, a hierarchical method for ride-sharing that leverages LLM-assisted automatic algorithmic design. RideSkill consists of a combiner that assigns appropriate skills to each vehicle from a learned skill repository, enabling adaptive dispatch under varying scenarios and objectives, and a repositioner that sequentially relocates idle vehicles to emerging regions, avoiding conflicts among vehicles. Crucially, the skill repository, combiner, and repositioner are all trained by an LLM-based automatic evolutionary method, eliminating the need for LLM calls during deployment and thus ensuring high real-time performance.
