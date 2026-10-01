---
title: "Parameter-efficient fine-tuning of large language models using semantic knowledge tuning"
authors: ["Nusrat Jahan Prottasha", "Asif Mahmud", "Md. Shohanur Islam Sobuj", "Prakash Bhat", "Md. Kowsher", "Niloofar Yousefi", "Özlem Özmen Garibay"]
year: 2024
cited_by_count: 21
doi: "https://doi.org/10.1038/s41598-024-75599-4"
openalex_id: W4405842131
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Parameter-efficient fine-tuning of large language models using semantic knowledge tuning

**Authors**: Nusrat Jahan Prottasha, Asif Mahmud, Md. Shohanur Islam Sobuj, Prakash Bhat, Md. Kowsher, Niloofar Yousefi, Özlem Özmen Garibay | **Year**: 2024 | **Cited by**: 21 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Large Language Models (LLMs) are gaining significant popularity in recent years for specialized tasks using prompts due to their low computational cost. Standard methods like prefix tuning utilize special, modifiable tokens that lack semantic meaning and require extensive training for best performance, often falling short. In this context, we propose a novel method called Semantic Knowledge Tuning (SK-Tuning) for prompt and prefix tuning that employs meaningful words instead of random tokens. This method involves using a fixed LLM to understand and process the semantic content of the prompt through zero-shot capabilities. Following this, it integrates the processed prompt with the input text to improve the model's performance on particular tasks. Our experimental results show that SK-Tuning exhibits faster training times, fewer parameters, and superior performance on tasks such as text classification and understanding compared to other tuning methods. This approach offers a promising method for optimizing the efficiency and effectiveness of LLMs in processing language tasks.
