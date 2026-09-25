---
title: "VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning"
authors: "Junxiang Xu, Ruisi Wang, Fanyi Pu, Maijunxian Wang, Ran Ji"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-08-28T09:14:46.066989"
arxiv_id: "http://arxiv.org/abs/2608.26105v1"
source_api: "arxiv"
categories: "cs.CV, cs.AI, cs.LG, cs.MM, cs.RO"
---

# VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning

**著者**: Junxiang Xu, Ruisi Wang, Fanyi Pu, Maijunxian Wang, Ran Ji
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Native visual reasoning treats visual generation as the medium of reasoning itself: visual states (i.e. images and videos) are not merely inputs to be understood or outputs to be rendered, but first-class substrates for problem solving beyond language. Yet progress remains bottlenecked by the lack of scalable training tasks, reliable feedback, and controlled comparisons across generative substrates. In this work, we introduce VBVR-Pro, a closed-loop testbed that makes native visual reasoning through generation trainable, verifiable, optimizable, and experimentally controllable. 1) Task scaling. VBVR-Pro turns visual reasoning into a controlled task space of 300 procedurally generated tasks. Models trained on VBVR-Pro show strong transfer beyond the proposed suite across seven external visual reasoning benchmarks such as RISE-Video, MME-CoF-Pro, and BabyVision. 2) Verifiable rewards. VBVR-Pro provides verifiable reward scorers for task-grounded evaluation. Through a systematic study of leading MLLMs as judges, we identify recurring failure modes of the prevalent VLM-as-a-judge paradigm. In contrast, the proposed scorers are grounded in deterministic, task-specific rules, achieve fine-grained alignment with human judgments. Importantly, they serve as reliable reward signals for large-scale multi-task reinforcement learning and demonstrate stronger post-RL performance across visual reasoning tasks. 3) Mechanism study. VBVR-Pro enables controlled modality studies across more than 30 image, video, and interleaved generators. Our analysis shows that video generation remains strongest for tasks requiring persistent spatiotemporal state tracking, while interleaved generation provides a compute-efficient alternative. Critically, ablations and probing suggest the presence of vision-native trajectories that are crucial to visual reasoning. We release all data, models, scorers, and code.
