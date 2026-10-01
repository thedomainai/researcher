---
title: "Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving"
authors: ["Ruoyu Qin", "Zheming Li", "Weiran He", "Jialei Cui", "Heyi Tang", "Feng Ren", "Teng Ma", "Shangming Cai", "et al."]
year: 2025
cited_by_count: 15
doi: "https://doi.org/10.1145/3773772"
openalex_id: W4416249188
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving

**Authors**: Ruoyu Qin, Zheming Li, Weiran He, Jialei Cui, Heyi Tang, Feng Ren, Teng Ma, Shangming Cai, et al. | **Year**: 2025 | **Cited by**: 15 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Mooncake is the serving platform for Kimi, an LLM chatbot service developed by Moonshot AI. This platform features a KVCache-centric disaggregated architecture that not only separates prefill and decoding clusters but also efficiently utilizes the underexploited CPU, DRAM, SSD and NIC resources of the GPU cluster to establish a disaggregated KVCache. At the core of Mooncake is its KVCache-centric global cache and a scheduler designed to maximize throughput while adhering to stringent latency-related Service Level Objectives (SLOs). Our experiments demonstrate that Mooncake excels in scenarios involving long-context inputs. In tests using real traces, Mooncake increases the effective request capacity by 59%∼498% when compared to baseline methods, all while complying with SLOs. Currently, Mooncake is operational across thousands of nodes, processing over 100 billion tokens daily. In practical deployments, Mooncake ’s innovative architecture enables Kimi to handle 115% and 107% more requests on NVIDIA A800 and H800 clusters, respectively, compared to previous systems.
