---
title: "AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration"
authors: ["Ji Lin", "Jiaming Tang", "Haotian Tang", "Shang Wen Yang", "Guangxuan Xiao", "Song Han"]
year: 2025
cited_by_count: 227
doi: "https://doi.org/10.1145/3714983.3714987"
openalex_id: W4406650295
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: true
abstract_source: "openalex"
---

# AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration

**Authors**: Ji Lin, Jiaming Tang, Haotian Tang, Shang Wen Yang, Guangxuan Xiao, Song Han | **Year**: 2025 | **Cited by**: 227 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Large language models (LLMs) have transformed numerous AI applications. On-device LLM is becoming increasingly important: running LLMs locally on edge devices can reduce cloud computing costs and protect users' privacy. However, the astronomical model size and the limited hardware resources pose significant deployment challenges. To solve these issues, we propose Activation-aware Weight Quantization (AWQ) and TinyChat, an algorithm-system full-stack solution for efficient on-device LLM deployment. AWQ is a novel quantization method that identifies and protects salient weights based on activation distribution, significantly reducing model size while preserving performance. TinyChat, an optimized inference framework, translates AWQ's theoretical memory savings into practical speedups through techniques such as on-the-fly dequantization, SIMD-aware weight packing, and kernel fusion. Together, they enable 4x model size reduction and 3-4x acceleration across various edge platforms, from high-end desktop GPUs to resource-constrained IoT devices. This solution democratizes on-device LLM deployment, offering privacy-preserving, low-latency AI capabilities across a wide range of applications.
