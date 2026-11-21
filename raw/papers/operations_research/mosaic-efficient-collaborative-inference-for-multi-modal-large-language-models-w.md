---
title: "MOSAIC: Efficient Collaborative Inference for Multi-Modal Large Language Models with Distributed Edge Computing"
authors: "Kongyange Zhao, Zhixuan Liao, Shengyuan Ye, Tao Ouyang, Liekang Zeng"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-22T06:05:44.469929"
doi: "https://doi.org/10.1145/3842721.3849677"
openalex_id: "https://openalex.org/W7224918038"
source_api: "openalex"
---

# MOSAIC: Efficient Collaborative Inference for Multi-Modal Large Language Models with Distributed Edge Computing

**著者**: Kongyange Zhao, Zhixuan Liao, Shengyuan Ye, Tao Ouyang, Liekang Zeng
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Multi-modal large language models (MLLMs) enable natural language reasoning over heterogeneous sensory data, appealing to many edge AI scenarios, yet their deployment faces competing demands on latency, energy, and quality. We present MOSAIC, which adopts a component-level decomposition and distributed deployment paradigm for efficient MLLM inference at the edge, realizing three core ideas: parallel encoding, token pruning, and device-server collaboration. Specifically, for the offline stage, modality-specific encoders distilled from a unified foundation model are co-deployed with Q-Former projection on edge devices for parallel encoding, while LoRA instruction fine-tuning adapts the frozen LLM backbone to downstream tasks. For the online stage, we formulate a multi-objective optimization over latency and energy that jointly tunes token budgets, device frequencies, and quantization precision under long-term semantic accuracy constraints, achieving dynamic token pruning and device-server collaboration. We leverage Lagrangian relaxation to decompose the original problem into tractable per-slot subproblems and design an online algorithm with provable near-optimal performance and guaranteed constraint satisfaction. We implement a realistic testbed for extensive performance evaluation, which demonstrates that MOSAIC reduces latency by up to 49.8% and energy by up to 65.1% over advanced baselines while maintaining high semantic accuracy.
