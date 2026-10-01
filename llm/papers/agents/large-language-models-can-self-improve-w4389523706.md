---
title: "Large Language Models Can Self-Improve"
authors: ["Jiaxin Huang", "Shixiang Gu", "Le Hou", "Yuexin Wu", "Xuezhi Wang", "Hongkun Yu", "Jiawei Han"]
year: 2023
cited_by_count: 196
doi: "https://doi.org/10.18653/v1/2023.emnlp-main.67"
openalex_id: W4389523706
paper_type: conference-paper
evidence_kind: article
topics: ["agents"]
landmark: true
abstract_source: "openalex"
---

# Large Language Models Can Self-Improve

**Authors**: Jiaxin Huang, Shixiang Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu, Jiawei Han | **Year**: 2023 | **Cited by**: 196 | **Kind**: article | **Relevance**: agents: core

## Abstract

Large Language Models (LLMs) have achieved excellent performances in various tasks.However, fine-tuning an LLM requires extensive supervision.Human, on the other hand, may improve their reasoning abilities by self-thinking without external inputs.In this work, we demonstrate that an LLM is also capable of self-improving with only unlabeled datasets.We use a pre-trained LLM to generate "highconfidence" rationale-augmented answers for unlabeled questions using Chain-of-Though (CoT) prompting and self-consistency, and finetune the LLM using those self-generated solutions as target outputs.We show that without any ground truth label, our approach significantly improves the general reasoning ability of PaLM 540B model (74.4%→82.1% on GSM8K, 90.0%→94.4% on OpenBookQA, and 63.4%→67.9% on ANLI-A3) and can also be adapted to extreme low-resource cases where even training questions and CoT prompts are limited.We conduct ablation studies and show that fine-tuning on diverse reasoning paths is critical for self-improvement.
