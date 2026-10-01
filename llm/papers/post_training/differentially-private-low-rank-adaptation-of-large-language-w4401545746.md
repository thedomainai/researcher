---
title: "Differentially Private Low-Rank Adaptation of Large Language Model Using Federated Learning"
authors: ["Xiao-Yang Liu", "Rongyi Zhu", "Daochen Zha", "Jiechao Gao", "Shan Zhong", "Matt White", "Meikang Qiu"]
year: 2024
cited_by_count: 64
doi: "https://doi.org/10.1145/3682068"
openalex_id: W4401545746
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Differentially Private Low-Rank Adaptation of Large Language Model Using Federated Learning

**Authors**: Xiao-Yang Liu, Rongyi Zhu, Daochen Zha, Jiechao Gao, Shan Zhong, Matt White, Meikang Qiu | **Year**: 2024 | **Cited by**: 64 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

The surge in interest and application of large language models (LLMs) has sparked a drive to fine-tune these models to suit specific applications, such as finance and medical science. However, concerns regarding data privacy have emerged, especially when multiple stakeholders aim to collaboratively enhance LLMs using sensitive data. In this scenario, federated learning becomes a natural choice, allowing decentralized fine-tuning without exposing raw data to central servers. Motivated by this, we investigate how data privacy can be ensured in LLM fine-tuning through practical federated learning approaches, enabling secure contributions from multiple parties to enhance LLMs. Yet, challenges arise: (1) despite avoiding raw data exposure, there is a risk of inferring sensitive information from model outputs, and (2) federated learning for LLMs incurs notable communication overhead. To address these challenges, this article introduces DP-LoRA, a novel federated learning algorithm tailored for LLMs. DP-LoRA preserves data privacy by employing a Gaussian mechanism that adds noise in weight updates, maintaining individual data privacy while facilitating collaborative model training. Moreover, DP-LoRA optimizes communication efficiency via low-rank adaptation, minimizing the transmission of updated weights during distributed training. The experimental results across medical, financial, and general datasets using various LLMs demonstrate that DP-LoRA effectively ensures strict privacy constraints while minimizing communication overhead.
