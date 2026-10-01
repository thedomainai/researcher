---
title: "Beyond the Cloud: Edge Inference for Generative Large Language Models in Wireless Networks"
authors: ["Xinyuan Zhang", "Jiangtian Nie", "Yudong Huang", "Gaochang Xie", "Zehui Xiong", "Jiang Liu", "Dusit Tao Niyato", "Xuemin Shen"]
year: 2024
cited_by_count: 74
doi: "https://doi.org/10.1109/twc.2024.3497923"
openalex_id: W4404562740
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Beyond the Cloud: Edge Inference for Generative Large Language Models in Wireless Networks

**Authors**: Xinyuan Zhang, Jiangtian Nie, Yudong Huang, Gaochang Xie, Zehui Xiong, Jiang Liu, Dusit Tao Niyato, Xuemin Shen | **Year**: 2024 | **Cited by**: 74 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Generative Artificial Intelligenge (GAI) is revolutionizing the world with its unprecedented content creation ability. Large Language Model (LLM) is one of its most embraced branches. However, due to LLM’s substantial size and resource-intensive nature, it is cloud-hosted, raising concerns about privacy, usage limitations, and latency. In this paper, we propose to utilize ubiquitous distributed wireless edge computing resources for real-time LLM inference. Specifically, we introduce a novel LLM edge inference framework, incorporating batching and model quantization to ensure high throughput inference on resource-limited edge devices. Then, based on the architecture of transformer decoder-based LLMs, we formulate an edge inference optimization problem which is NP-hard, considering batch scheduling and joint allocation of communication and computation resources. The solution is the optimal throughput under edge resource constraints and heterogeneous user requirements on latency and accuracy. To solve this NP-hard problem, we develop an OT-GAH (Optimal Tree-search with Generalized Assignment Heuristics) algorithm with reasonable complexity and$\frac {1}{2}$-approximation ratio. We first design the OT algorithm with online tree-pruning for single-edge-node multi-user case, which navigates the inference request selection within the tree structure to miximize throughput. We then consider the multi-edge-node case and propose the GAH algorithm, which recrusively invokes the OT in each node’s inference scheduling iteration. Simulation results demonstrate the superiority of OT-GAH batching over other benchmarks, revealing an over 45% time complexity reduction compared to brute-force searching.
