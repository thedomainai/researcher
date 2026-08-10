---
title: "Harness Engineering for LLM-Driven GPU Kernel Generation"
authors: "Yue Shui, Chenyu Ma, Hangfei Xu, Shengzhao Wen, Yanpeng Wang"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-07-22T06:02:24.956896"
arxiv_id: "http://arxiv.org/abs/2607.17979v1"
source_api: "arxiv"
categories: "cs.LG, cs.AI"
---

# Harness Engineering for LLM-Driven GPU Kernel Generation

**著者**: Yue Shui, Chenyu Ma, Hangfei Xu, Shengzhao Wen, Yanpeng Wang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Large language models (LLMs) can assist GPU kernel generation, but their practical effectiveness depends on whether generated code can be reliably constrained, validated, profiled, and selected. This paper presents a harness-centered system for LLM-driven GPU kernel optimization in the MLSys 2026 FlashInfer AI Kernel Generation Contest on NVIDIA Blackwell B200 GPUs. The system separates an evaluation harness from a profile-backed optimization controller: the harness enforces compilation, correctness, official-aligned timing, and artifact archival, while the controller turns profiler and workload evidence into bounded candidate-generation decisions. Human-authored skills capture operator constraints, references, profiling procedures, and promotion rules, while Codex and Claude Code agents generate candidate kernels inside those constraints. Across five operator definitions, the retained official-aligned artifacts achieved mean-latency speedups over supplied FlashInfer baselines of 1.62x, 18.05x, 29.68x, 1.12x, and 13.70x. The Agent-Assisted kernels outperform the Full-Agent artifacts across the evaluated definitions, indicating that expert-provided optimization directions, high-quality references, and workload context remain critical for reliable AI-driven kernel optimization.
