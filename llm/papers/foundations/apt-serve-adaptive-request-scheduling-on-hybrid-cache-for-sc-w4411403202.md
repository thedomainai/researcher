---
title: "Apt-Serve: Adaptive Request Scheduling on Hybrid Cache for Scalable LLM Inference Serving"
authors: ["Shihong Gao", "Xin Zhang", "Yanyan Shen", "Lei Chen"]
year: 2025
cited_by_count: 7
doi: "https://doi.org/10.1145/3725394"
openalex_id: W4411403202
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Apt-Serve: Adaptive Request Scheduling on Hybrid Cache for Scalable LLM Inference Serving

**Authors**: Shihong Gao, Xin Zhang, Yanyan Shen, Lei Chen | **Year**: 2025 | **Cited by**: 7 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Large language model (LLM) inference serving systems are essential to various LLM-based applications. As demand for LLM services continues to grow, scaling these systems to handle high request rates while meeting latency Service-Level Objectives (SLOs), referred to as effective throughput, becomes critical. However, existing systems often struggle to improve effective throughput, primarily due to a significant decline in Time To First Token (TTFT) SLO attainment. We identify two major causes of this bottleneck: (1) memory-intensive KV cache that limits batch size expansion under GPU memory constraints, and (2) rigid batch composition enforced by the default First-Come-First-Serve scheduling policy. In this paper, we introduce Apt-Serve, a scalable framework designed to enhance effective throughput in LLM inference serving. Apt-Serve features a new hybrid cache scheme that combines KV cache with a memory-efficient hidden cache for reusable input hidden state vectors, allowing large batch sizes and improving request concurrency. Based on the hybrid cache, Apt-Serve employs an adaptive runtime scheduling mechanism that dynamically optimizes batch composition. We formally define the adaptive scheduling optimization problem and propose an efficient algorithm with theoretical guarantees. Extensive evaluations on three real-world datasets and LLMs ranging from 13B to 66B parameters demonstrate that Apt-Serve achieves up to 8.8x improvement in effective throughput compared to the state-of-the-art inference serving systems.
