---
title: "Subkv: Quantizing Long Context KV Cache for Sub‐Billion Parameter Language Models on Edge Devices"
authors: ["Ziqian Zeng", "Tao Zhang", "Zhengdong Lu", "Wenjun Li", "Huiping Zhuang", "Hongen Shao", "Sin G. Teo", "Xiaofeng Zou"]
year: 2025
cited_by_count: 2
doi: "https://doi.org/10.1002/spe.3422"
openalex_id: W4409108393
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Subkv: Quantizing Long Context KV Cache for Sub‐Billion Parameter Language Models on Edge Devices

**Authors**: Ziqian Zeng, Tao Zhang, Zhengdong Lu, Wenjun Li, Huiping Zhuang, Hongen Shao, Sin G. Teo, Xiaofeng Zou | **Year**: 2025 | **Cited by**: 2 | **Kind**: article | **Relevance**: foundations: core

## Abstract

ABSTRACT Background Large Language Models (LLMs) have demonstrated remarkable capabilities across various tasks. However, their substantial computational and memory requirements present significant challenges for widespread deployment on edge devices. Motivation In long‐context scenarios, even sub‐billion parameter LLMs face unavoidable memory and performance bottlenecks due to inefficient KV Cache utilization. Existing quantization methods fail to address these challenges effectively. Method This paper addresses these challenges by introducing advanced quantization techniques tailored for sub‐billion parameter LLMs. It specifically targets reducing memory consumption through the conversion of the model's KV Cache to lower‐bit integers. We present SubKV, a quantization method specifically designed to optimize the KV Cache in sub‐billion parameter LLMs. Our analysis reveals distinct distributional differences in the magnitude of key and value caches. Leveraging this insight, we apply Per‐Channel Quantization to the key cache and Per‐Token Quantization to the value cache. Furthermore, we introduce the Dynamic Window Quantization method to enhance attention computations. To mitigate the extreme sensitivity of the first token, we also introduce Attention Sink‐Aware Quantization. Results Experimental results demonstrate that SubKV significantly reduces the KV Cache size during long context inference while maintaining model performance, offering superior results to existing KV Cache quantization methods.
