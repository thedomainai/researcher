---
title: "An empirical study of LLaMA3 quantization: from LLMs to MLLMs"
authors: ["Wei Huang", "Xingyu Zheng", "Xudong Ma", "Haotong Qin", "Chengtao Lv", "Hong Chen", "Jie Luo", "Xiaojuan Qi", "et al."]
year: 2024
cited_by_count: 41
doi: "https://doi.org/10.1007/s44267-024-00070-x"
openalex_id: W4405887239
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# An empirical study of LLaMA3 quantization: from LLMs to MLLMs

**Authors**: Wei Huang, Xingyu Zheng, Xudong Ma, Haotong Qin, Chengtao Lv, Hong Chen, Jie Luo, Xiaojuan Qi, et al. | **Year**: 2024 | **Cited by**: 41 | **Kind**: article | **Relevance**: foundations: core

## Abstract

The LLaMA family, a collection of foundation language models ranging from 7B to 65B parameters, has become one of the most powerful open-source large language models (LLMs) and the popular LLM backbone of multi-modal large language models (MLLMs), widely used in computer vision and natural language understanding tasks. In particular, LLaMA3 models have recently been released and have achieved impressive performance in various domains with super-large scale pre-training on over 15T tokens of data. Given the wide application of low-bit quantization for LLMs in resource-constrained scenarios, we explore LLaMA3's capabilities when quantized to low bit-width. This exploration can potentially provide new insights and challenges for the low-bit quantization of LLaMA3 and other future LLMs, especially in addressing performance degradation issues that suffer in LLM compression. Specifically, we comprehensively evaluate the 10 existing post-training quantization and LoRA fine-tuning (LoRA-FT) methods of LLaMA3 on 1-8 bits and various datasets to reveal the low-bit quantization performance of LLaMA3. To uncover the capabilities of low-bit quantized MLLM, we assessed the performance of the LLaMA3-based LLaVA-Next-8B model under 2-4 ultra-low bits with post-training quantization methods. Our experimental results indicate that LLaMA3 still suffers from non-negligible degradation in linguistic and visual contexts, particularly under ultra-low bit widths. This highlights the significant performance gap at low bit-width that needs to be addressed in future developments. We expect that this empirical study will prove valuable in advancing future models, driving LLMs and MLLMs to achieve higher accuracy at lower bit to enhance practicality.
