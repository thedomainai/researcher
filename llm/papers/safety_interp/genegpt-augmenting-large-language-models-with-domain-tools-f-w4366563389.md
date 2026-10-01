---
title: "GeneGPT: augmenting large language models with domain tools for improved access to biomedical information"
authors: ["Qiao Jin", "Yifan Yang", "Qingyu Chen", "Zhiyong Lu"]
year: 2024
cited_by_count: 179
doi: "https://doi.org/10.1093/bioinformatics/btae075"
openalex_id: W4366563389
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# GeneGPT: augmenting large language models with domain tools for improved access to biomedical information

**Authors**: Qiao Jin, Yifan Yang, Qingyu Chen, Zhiyong Lu | **Year**: 2024 | **Cited by**: 179 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

MOTIVATION: While large language models (LLMs) have been successfully applied to various tasks, they still face challenges with hallucinations. Augmenting LLMs with domain-specific tools such as database utilities can facilitate easier and more precise access to specialized knowledge. In this article, we present GeneGPT, a novel method for teaching LLMs to use the Web APIs of the National Center for Biotechnology Information (NCBI) for answering genomics questions. Specifically, we prompt Codex to solve the GeneTuring tests with NCBI Web APIs by in-context learning and an augmented decoding algorithm that can detect and execute API calls. RESULTS: Experimental results show that GeneGPT achieves state-of-the-art performance on eight tasks in the GeneTuring benchmark with an average score of 0.83, largely surpassing retrieval-augmented LLMs such as the new Bing (0.44), biomedical LLMs such as BioMedLM (0.08) and BioGPT (0.04), as well as GPT-3 (0.16) and ChatGPT (0.12). Our further analyses suggest that: First, API demonstrations have good cross-task generalizability and are more useful than documentations for in-context learning; second, GeneGPT can generalize to longer chains of API calls and answer multi-hop questions in GeneHop, a novel dataset introduced in this work; finally, different types of errors are enriched in different tasks, providing valuable insights for future improvements. AVAILABILITY AND IMPLEMENTATION: The GeneGPT code and data are publicly available at https://github.com/ncbi/GeneGPT.
