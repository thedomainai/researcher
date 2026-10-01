---
title: "OFQ-LLM: Outlier-Flexing Quantization for Efficient Low-Bit Large Language Model Acceleration"
authors: ["Gang Wang", "Siqi Cai", "Wenjie Li", "Dongxu Lyu", "Guanghui He"]
year: 2025
cited_by_count: 7
doi: "https://doi.org/10.1109/tcsi.2025.3547732"
openalex_id: W4408399636
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# OFQ-LLM: Outlier-Flexing Quantization for Efficient Low-Bit Large Language Model Acceleration

**Authors**: Gang Wang, Siqi Cai, Wenjie Li, Dongxu Lyu, Guanghui He | **Year**: 2025 | **Cited by**: 7 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Large Language Models (LLMs) have achieved significant success in various Natural Language Processing (NLP) tasks, becoming essential to modern intelligent computing. Their large memory footprint and high computational cost hinder efficient deployment. Post-Training Quantization (PTQ) is a promising technique to alleviate this issue and accelerate LLM inference. However, the presence of outliers impedes the advancement of LLM quantization to lower bit levels. In this paper, we introduce OFQ-LLM, an algorithm-hardware co-design solution that adopts outlier-flexing quantization to efficiently accelerate LLM at low-bit levels. The key insight of OFQ-LLM is that normal data can be efficiently quantized in a slightly reduced data encoding space, while the rest encoding space can be used for flexible outlier values. During quantization, we use rescale-based clipping (RBC) to optimize accuracy for normal data and group outlier clustering (GOC) to flexibly represent outlier values. At the hardware level, we introduce a memory-aligned outlier-flexing encoding scheme to encode activations and weights in LLMs at a low bit level. The outlier-normal mixed hardware architecture is devised to leverage the encoding scheme and accelerate LLMs with high speed and high energy efficiency. Our experiments show that OFQ-LLM achieves better accuracy compared to state-of-the-art (SOTA) low-bit LLM PTQ works. OFQ-LLM-based accelerator surpasses the SOTA outlier-aware accelerators by up to$2.69\times $core energy efficiency, up to$3.83\times $speed up and$2.44\times $energy reduction in LLM prefilling phase, and up to$2.01\times $speed up and$2.88\times $energy reduction in LLM decoding phase, with superior accuracy.
