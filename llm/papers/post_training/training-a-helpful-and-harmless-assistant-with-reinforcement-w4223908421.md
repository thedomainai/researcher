---
title: "Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback"
authors: ["Yuntao Bai", "Jones, Andy", "Kamal Ndousse", "Amanda Askell", "Anna Chen", "Nova DasSarma", "Dawn Drain", "Stanislav Fort", "et al."]
year: 2022
cited_by_count: 389
doi: "https://doi.org/10.48550/arxiv.2204.05862"
openalex_id: W4223908421
paper_type: preprint
evidence_kind: article
topics: ["post_training"]
landmark: true
abstract_source: "openalex"
---

# Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

**Authors**: Yuntao Bai, Jones, Andy, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, et al. | **Year**: 2022 | **Cited by**: 389 | **Kind**: article | **Relevance**: post_training: core

## Abstract

We apply preference modeling and reinforcement learning from human feedback (RLHF) to finetune language models to act as helpful and harmless assistants. We find this alignment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data, efficiently improving our datasets and models. Finally, we investigate the robustness of RLHF training, and identify a roughly linear relation between the RL reward and the square root of the KL divergence between the policy and its initialization. Alongside our main results, we perform peripheral analyses on calibration, competing objectives, and the use of OOD detection, compare our models with human writers, and provide samples from our models using prompts appearing in recent related work.
