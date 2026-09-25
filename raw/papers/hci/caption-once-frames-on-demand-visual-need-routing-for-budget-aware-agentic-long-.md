---
title: "Caption-once, Frames-on-Demand: Visual-Need Routing for Budget-Aware Agentic Long Video Understanding"
authors: "Weitong Cai, Hang Zhang, Yukai Huang, Yiqiao Xie, Shan Gao"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-09-12T06:05:06.909609"
arxiv_id: "http://arxiv.org/abs/2609.11899v1"
source_api: "arxiv"
categories: "cs.CV, cs.HC"
---

# Caption-once, Frames-on-Demand: Visual-Need Routing for Budget-Aware Agentic Long Video Understanding

**著者**: Weitong Cai, Hang Zhang, Yukai Huang, Yiqiao Xie, Shan Gao
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

Long-video understanding on edge devices must reason over hours of content under tight compute and bandwidth budgets. Subsampling visual tokens loses temporal structure, while text-only video memories lose fine-grained visual attributes. We observe a visual-textual duality: language memories carry long-range temporal structure better than dense frames, while pixels remain decisive for attribute-level perception. Building on this insight, we propose Caption-once, Frames-onDemand (CFD), a budget-aware edge-cloud agentic framework. The edge runs a single offline captioning pass that builds a dual-track narrative index, an event-level story skeleton plus a clip-level micro-log, cached and reused across queries without re-captioning. At query time, a cloud-side MLLM reasons over the index in a story-first loop centered on a lightweight Visual-Need Router: a per-query gating module that triggers bounded keyframe retrieval only for perceptual questions (appearance, on-screen text, attribute disambiguation) and keeps temporal-structural questions in language space. The router turns visual access into a first-class, query-conditioned cost, capping per-query frame consumption regardless of video length. Experiments on long-video benchmarks demonstrate strong accuracy-efficiency trade-offs while substantially reducing online visual processing.
