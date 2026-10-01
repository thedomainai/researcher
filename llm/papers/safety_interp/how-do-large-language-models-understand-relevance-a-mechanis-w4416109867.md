---
title: "How Do Large Language Models Understand Relevance? A Mechanistic Interpretability Perspective"
authors: ["Qi Liu", "Haozhe Duan", "Jiaxin Mao", "Ji-Rong Wen"]
year: 2025
cited_by_count: 3
doi: "https://doi.org/10.1145/3774942"
openalex_id: W4416109867
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# How Do Large Language Models Understand Relevance? A Mechanistic Interpretability Perspective

**Authors**: Qi Liu, Haozhe Duan, Jiaxin Mao, Ji-Rong Wen | **Year**: 2025 | **Cited by**: 3 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Recent studies have shown that large language models (LLMs) can assess relevance and support information retrieval (IR) tasks such as document ranking and relevance judgment generation. However, the internal mechanisms by which off-the-shelf LLMs understand and operationalize relevance remain largely unexplored. In this article, we systematically investigate how different LLM modules contribute to relevance judgment through the lens of mechanistic interpretability. Using activation patching techniques, we analyze the roles of various model components and identify a multi-stage, progressive process in generating either pointwise or pairwise relevance judgment. Specifically, LLMs first extract query and document information in the early layers, then process relevance information according to instructions in the middle layers, and finally utilize specific attention heads in the later layers to generate relevance judgments in the required format. Our findings provide insights into the mechanisms underlying relevance assessment in LLMs, offering valuable implications for future research on leveraging LLMs for IR tasks.
