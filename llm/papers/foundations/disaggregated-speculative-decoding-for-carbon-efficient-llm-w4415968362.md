---
title: "Disaggregated Speculative Decoding for Carbon-Efficient LLM Serving"
authors: ["Tianyao Shi", "Yanran Wu", "Sihang Liu", "Yi Ding"]
year: 2025
cited_by_count: 3
doi: "https://doi.org/10.1109/lca.2025.3630094"
openalex_id: W4415968362
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Disaggregated Speculative Decoding for Carbon-Efficient LLM Serving

**Authors**: Tianyao Shi, Yanran Wu, Sihang Liu, Yi Ding | **Year**: 2025 | **Cited by**: 3 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Large language models (LLMs) are increasingly deployed in practice but incur significant computational costs and environmental impacts. Disaggregated serving techniques, particularly decoupling prefill and decoding (DPD) across GPUs, have been introduced to improve performance and reduce carbon emissions. However, DPD suffers from high bandwidth overhead due to frequent large KV cache transfers. To address this, we present disaggregated speculative decoding (DSD), which leverages speculative decoding by assigning draft models to older GPUs and target models to newer GPUs, requiring only token and probability distribution transfers. Building on this insight, we introduce GreenLLM, an SLO- and bandwidth- aware framework that unifies DPD and DSD, profiles workload characteristics, and dynamically selects the most carbon-efficient configuration. Across diverse benchmarks, GreenLLM reduces carbon emissions by up to 40.6% while meeting latency SLOs.
