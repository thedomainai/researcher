---
title: "BioInstruct: instruction tuning of large language models for biomedical natural language processing"
authors: ["Hieu Tran", "Zhichao Yang", "Zonghai Yao", "Hong Yu"]
year: 2024
cited_by_count: 60
doi: "https://doi.org/10.1093/jamia/ocae122"
openalex_id: W4399326970
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# BioInstruct: instruction tuning of large language models for biomedical natural language processing

**Authors**: Hieu Tran, Zhichao Yang, Zonghai Yao, Hong Yu | **Year**: 2024 | **Cited by**: 60 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

OBJECTIVES: To enhance the performance of large language models (LLMs) in biomedical natural language processing (BioNLP) by introducing a domain-specific instruction dataset and examining its impact when combined with multi-task learning principles. MATERIALS AND METHODS: We created the BioInstruct, comprising 25 005 instructions to instruction-tune LLMs (LLaMA 1 and 2, 7B and 13B version). The instructions were created by prompting the GPT-4 language model with 3-seed samples randomly drawn from an 80 human curated instructions. We employed Low-Rank Adaptation (LoRA) for parameter-efficient fine-tuning. We then evaluated these instruction-tuned LLMs on several BioNLP tasks, which can be grouped into 3 major categories: question answering (QA), information extraction (IE), and text generation (GEN). We also examined whether categories (eg, QA, IE, and generation) of instructions impact model performance. RESULTS AND DISCUSSION: Comparing with LLMs without instruction-tuned, our instruction-tuned LLMs demonstrated marked performance gains: 17.3% in QA on average accuracy metric, 5.7% in IE on average F1 metric, and 96% in Generation tasks on average GPT-4 score metric. Our 7B-parameter instruction-tuned LLaMA 1 model was competitive or even surpassed other LLMs in the biomedical domain that were also fine-tuned from LLaMA 1 with vast domain-specific data or a variety of tasks. Our results also show that the performance gain is significantly higher when instruction fine-tuning is conducted with closely related tasks. Our findings align with the observations of multi-task learning, suggesting the synergies between 2 tasks. CONCLUSION: The BioInstruct dataset serves as a valuable resource and instruction tuned LLMs lead to the best performing BioNLP applications.
