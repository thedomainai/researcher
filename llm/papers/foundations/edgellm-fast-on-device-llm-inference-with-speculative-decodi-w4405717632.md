---
title: "EdgeLLM: Fast On-Device LLM Inference With Speculative Decoding"
authors: ["Daliang Xu", "Wangsong Yin", "Hao Zhang", "Xin Jin", "Ying Zhang", "Shiyun Wei", "Mengwei Xu", "Xuanzhe Liu"]
year: 2024
cited_by_count: 47
doi: "https://doi.org/10.1109/tmc.2024.3513457"
openalex_id: W4405717632
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# EdgeLLM: Fast On-Device LLM Inference With Speculative Decoding

**Authors**: Daliang Xu, Wangsong Yin, Hao Zhang, Xin Jin, Ying Zhang, Shiyun Wei, Mengwei Xu, Xuanzhe Liu | **Year**: 2024 | **Cited by**: 47 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Generative tasks, such as text generation and question answering, are essential for mobile applications. Given their inherent privacy sensitivity, executing them on devices is demanded. Nowadays, the execution of these generative tasks heavily relies on the Large Language Models (LLMs). However, the scarce device memory severely hinders the scalability of these models. We presentEdgeLLM, an efficient on-device LLM inference system for models whose sizes exceed the device's memory capacity.EdgeLLMis built atop speculative decoding, which delegates most tokens to a smaller, memory-resident (draft) LLM.EdgeLLMintegrates three novel techniques: (1) Instead of generating a fixed width and depth token tree,EdgeLLMproposes compute-efficient branch navigation and verification to pace the progress of different branches according to their accepted probability to prevent the wasteful allocation of computing resources to the wrong branch and to verify them all at once efficiently. (2) It uses a self-adaptive fallback strategy that promptly initiates the verification process when the smaller LLM generates an incorrect token. (3) To not block the generation,EdgeLLMproposes speculatively generating tokens during large LLM verification with the compute-IO pipeline. Through extensive experiments,EdgeLLMexhibits impressive token generation speed which is up to 9.3× faster than existing engines.
