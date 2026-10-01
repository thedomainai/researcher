---
title: "Adapting Language Models for Zero-shot Learning by Meta-tuning on Dataset and Prompt Collections"
authors: ["Ruiqi Zhong", "Kristy Lee", "Zheng Zhang", "Dan Klein"]
year: 2021
cited_by_count: 102
doi: "https://doi.org/10.18653/v1/2021.findings-emnlp.244"
openalex_id: W3194309076
paper_type: conference-paper
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Adapting Language Models for Zero-shot Learning by Meta-tuning on Dataset and Prompt Collections

**Authors**: Ruiqi Zhong, Kristy Lee, Zheng Zhang, Dan Klein | **Year**: 2021 | **Cited by**: 102 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Large pre-trained language models (LMs) such as GPT-3 have acquired a surprising ability to perform zero-shot learning.For example, to classify sentiment without any training examples, we can "prompt" the LM with the review and the label description "Does the user like this movie?",and ask whether the next word is "Yes" or "No".However, the next word prediction training objective is still misaligned with the target zero-shot learning objective.To address this weakness, we propose meta-tuning, which directly optimizes the zero-shot learning objective by finetuning pre-trained language models on a collection of datasets.We focus on classification tasks, and construct the meta-dataset by aggregating 43 existing datasets and annotating 441 label descriptions in a question-answering (QA) format.When evaluated on unseen tasks, meta-tuned models outperform a samesized QA model and the previous SOTA zeroshot learning system based on natural language inference.Additionally, increasing parameter count from 220M to 770M improves AUC-ROC scores by 6.3%, and we forecast that even larger models would perform better.Therefore, measuring zero-shot learning performance on language models out-of-thebox might underestimate their true potential, and community-wide efforts on aggregating datasets and unifying their formats can help build models that answer prompts better.
