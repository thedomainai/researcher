---
title: "PMC-LLaMA: toward building open-source language models for medicine"
authors: ["Chaoyi Wu", "Weixiong Lin", "Xiaoman Zhang", "Ya Zhang", "Weidi Xie", "Yanfeng Wang"]
year: 2024
cited_by_count: 301
doi: "https://doi.org/10.1093/jamia/ocae045"
openalex_id: W4394782456
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# PMC-LLaMA: toward building open-source language models for medicine

**Authors**: Chaoyi Wu, Weixiong Lin, Xiaoman Zhang, Ya Zhang, Weidi Xie, Yanfeng Wang | **Year**: 2024 | **Cited by**: 301 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

OBJECTIVE: Recently, large language models (LLMs) have showcased remarkable capabilities in natural language understanding. While demonstrating proficiency in everyday conversations and question-answering (QA) situations, these models frequently struggle in domains that require precision, such as medical applications, due to their lack of domain-specific knowledge. In this article, we describe the procedure for building a powerful, open-source language model specifically designed for medicine applications, termed as PMC-LLaMA. MATERIALS AND METHODS: We adapt a general-purpose LLM toward the medical domain, involving data-centric knowledge injection through the integration of 4.8M biomedical academic papers and 30K medical textbooks, as well as comprehensive domain-specific instruction fine-tuning, encompassing medical QA, rationale for reasoning, and conversational dialogues with 202M tokens. RESULTS: While evaluating various public medical QA benchmarks and manual rating, our lightweight PMC-LLaMA, which consists of only 13B parameters, exhibits superior performance, even surpassing ChatGPT. All models, codes, and datasets for instruction tuning will be released to the research community. DISCUSSION: Our contributions are 3-fold: (1) we build up an open-source LLM toward the medical domain. We believe the proposed PMC-LLaMA model can promote further development of foundation models in medicine, serving as a medical trainable basic generative language backbone; (2) we conduct thorough ablation studies to demonstrate the effectiveness of each proposed component, demonstrating how different training data and model scales affect medical LLMs; (3) we contribute a large-scale, comprehensive dataset for instruction tuning. CONCLUSION: In this article, we systematically investigate the process of building up an open-source medical-specific LLM, PMC-LLaMA.
