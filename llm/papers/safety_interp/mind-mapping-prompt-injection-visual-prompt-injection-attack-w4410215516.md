---
title: "Mind Mapping Prompt Injection: Visual Prompt Injection Attacks in Modern Large Language Models"
authors: ["S.G. Lee", "J.‐J. Kim", "Wooguil Pak"]
year: 2025
cited_by_count: 14
doi: "https://doi.org/10.3390/electronics14101907"
openalex_id: W4410215516
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Mind Mapping Prompt Injection: Visual Prompt Injection Attacks in Modern Large Language Models

**Authors**: S.G. Lee, J.‐J. Kim, Wooguil Pak | **Year**: 2025 | **Cited by**: 14 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Large language models (LLMs) have made significant strides in generating coherent and contextually relevant responses across diverse domains. However, these advancements have also led to an increase in adversarial attacks, such as prompt injection, where attackers embed malicious instructions within prompts to bypass security filters and manipulate LLM outputs. Various injection techniques, including masking and encoding sensitive words, have been employed to circumvent security measures. While LLMs continuously enhance their security protocols, they remain vulnerable, particularly in multimodal contexts. This study introduces a novel method for bypassing LLM security policies by embedding malicious instructions within a mind map image. The attack leverages the intentional incompleteness of the mind map structure, specifically the absence of explanatory details. When the LLM processes the image and fills in the missing sections, it inadvertently generates unauthorized outputs, violating its intended security constraints. This approach applies to any LLM capable of extracting and interpreting text from images. Compared to the best-performing baseline method, which achieved an ASR of 30.5%, our method reaches an ASR of 90%, yielding an approximately threefold-higher attack success. Understanding this vulnerability is crucial for strengthening security policies in state-of-the-art LLMs.
