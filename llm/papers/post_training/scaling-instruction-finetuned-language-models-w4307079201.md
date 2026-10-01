---
title: "Scaling Instruction-Finetuned Language Models"
authors: ["Hyung Won Chung", "Le Hou", "Shayne Longpre", "Barret Zoph", "Yi Hong Tay", "William Fedus", "Li, Yunxuan", "Xuezhi Wang", "et al."]
year: 2022
cited_by_count: 1174
doi: "https://doi.org/10.48550/arxiv.2210.11416"
openalex_id: W4307079201
paper_type: preprint
evidence_kind: article
topics: ["post_training"]
landmark: true
abstract_source: "openalex"
---

# Scaling Instruction-Finetuned Language Models

**Authors**: Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Hong Tay, William Fedus, Li, Yunxuan, Xuezhi Wang, et al. | **Year**: 2022 | **Cited by**: 1174 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Finetuning language models on a collection of datasets phrased as instructions has been shown to improve model performance and generalization to unseen tasks. In this paper we explore instruction finetuning with a particular focus on (1) scaling the number of tasks, (2) scaling the model size, and (3) finetuning on chain-of-thought data. We find that instruction finetuning with the above aspects dramatically improves performance on a variety of model classes (PaLM, T5, U-PaLM), prompting setups (zero-shot, few-shot, CoT), and evaluation benchmarks (MMLU, BBH, TyDiQA, MGSM, open-ended generation). For instance, Flan-PaLM 540B instruction-finetuned on 1.8K tasks outperforms PALM 540B by a large margin (+9.4% on average). Flan-PaLM 540B achieves state-of-the-art performance on several benchmarks, such as 75.2% on five-shot MMLU. We also publicly release Flan-T5 checkpoints, which achieve strong few-shot performance even compared to much larger models, such as PaLM 62B. Overall, instruction finetuning is a general method for improving the performance and usability of pretrained language models.
