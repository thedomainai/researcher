---
title: "Chain-of-LoRA: Enhancing the Instruction Fine-Tuning Performance of Low-Rank Adaptation on Diverse Instruction Set"
authors: ["Xihe Qiu", "Teqi Hao", "Shaojie Shi", "Xiaoyu Tan", "Yu-Jie Xiong"]
year: 2024
cited_by_count: 24
doi: "https://doi.org/10.1109/lsp.2024.3377590"
openalex_id: W4392796555
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Chain-of-LoRA: Enhancing the Instruction Fine-Tuning Performance of Low-Rank Adaptation on Diverse Instruction Set

**Authors**: Xihe Qiu, Teqi Hao, Shaojie Shi, Xiaoyu Tan, Yu-Jie Xiong | **Year**: 2024 | **Cited by**: 24 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Recently, large language models (LLMs) with conversational-style interaction, such as ChatGPT and Claude, have gained significant importance in the advancement of artificial general intelligence (AGI). However, the extensive resource requirements during pre-training, instruction fine-tuning (IF), and reinforcement learning through human feedback (RLHF) pose challenges, particularly for individuals and studios with limited resources. Moreover, sensitive data that cannot be deployed on remote training platforms or queried through APIs further exacerbates this issue. To address these limitations, researchers have introduced a parameter-efficient framework called low-rank adaptation (LoRA) for IF on LLMs. However, training individual LoRA networks faces capacity constraints and struggles to adapt to large domains with significant distributional shifts across different tasks. In this paper, we propose a novel framework called chain-of-LoRA to enhance the IF performance of LoRA. Our approach involves training a LoRA network to classify the instruction type and then utilizing task-specific LoRA networks to accomplish the respective tasks. By training multiple task-specific LoRA networks, we exploit a trade-off between performance and disk storage, leveraging the easily expandable and cost-effective nature of disk storage compared to precious graphical resources. Our experimental results demonstrate that our proposed framework achieves comparable performance to typical direct IF on LLMs.
