---
title: "Finetuned Language Models Are Zero-Shot Learners"
authors: ["Jason Wei", "Maarten Bosma", "Vincent Y. Zhao", "Kelvin Guu", "Adams Wei Yu", "Lester, Brian", "Nan Du", "Andrew M. Dai", "et al."]
year: 2021
cited_by_count: 69
doi: "https://doi.org/10.48550/arxiv.2109.01652"
openalex_id: W3198002980
paper_type: preprint
evidence_kind: article
topics: ["post_training"]
landmark: true
abstract_source: "openalex"
---

# Finetuned Language Models Are Zero-Shot Learners

**Authors**: Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Lester, Brian, Nan Du, Andrew M. Dai, et al. | **Year**: 2021 | **Cited by**: 69 | **Kind**: article | **Relevance**: post_training: core

## Abstract

This paper explores a simple method for improving the zero-shot learning abilities of language models. We show that instruction tuning -- finetuning language models on a collection of tasks described via instructions -- substantially improves zero-shot performance on unseen tasks. We take a 137B parameter pretrained language model and instruction-tune it on over 60 NLP tasks verbalized via natural language instruction templates. We evaluate this instruction-tuned model, which we call FLAN, on unseen task types. FLAN substantially improves the performance of its unmodified counterpart and surpasses zero-shot 175B GPT-3 on 20 of 25 tasks that we evaluate. FLAN even outperforms few-shot GPT-3 by a large margin on ANLI, RTE, BoolQ, AI2-ARC, OpenbookQA, and StoryCloze. Ablation studies reveal that number of finetuning datasets, model scale, and natural language instructions are key to the success of instruction tuning.
