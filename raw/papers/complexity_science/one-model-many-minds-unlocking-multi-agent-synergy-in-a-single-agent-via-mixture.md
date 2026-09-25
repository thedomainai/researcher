---
title: "One Model, Many Minds: Unlocking Multi-Agent Synergy in a Single Agent via Mixture of Roles"
authors: "Zhichen Zeng, Huiyuan Chen, Jingru Cheng, Juan Zha, Ming Liu"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-08-29T06:01:03.839745"
arxiv_id: "http://arxiv.org/abs/2608.27338v1"
source_api: "arxiv"
categories: "cs.MA"
---

# One Model, Many Minds: Unlocking Multi-Agent Synergy in a Single Agent via Mixture of Roles

**著者**: Zhichen Zeng, Huiyuan Chen, Jingru Cheng, Juan Zha, Ming Liu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Specializing Large Language Models (LLMs) toward distinct abilities underpins successes ranging from personalized assistants to multi-agent systems (MAS). Single-agent paradigms rely on pre-defined personas or steering vectors to induce specialization, yet they impose a single fixed specialization that fails to adapt to diverse queries. Conversely, MAS achieves dynamic multi-perspective problem solving by orchestrating agents with distinct text-based roles, but fusing these specializations requires multi-turn interactions that inflate context length and inference cost. To address these limitations, we propose Mixture of Roles (MoRe), which adaptively composes multiple specializations into a single steering vector for single-turn inference. Specifically, MoRe learns a diversified codeboox of steering vectors, each of which encodes a latent role. A query-aware router dynamically fuses the codebook into a steering vector that encompasses multiple roles. By steering the backbone LLM with the composed vector, MoRe enables multi-perspective specialization in a single-agent, single-turn inference process. The proposed MoRe can be efficiently trained via a three-stage SFT curriculum and GRPO post-training, while the backbone LLM remains frozen. Experiments across reasoning and personality benchmarks show that MoRe outperforms single-agent baselines by 2.2% on average, and achieves performance on par with MAS while reducing token cost by 20x.
