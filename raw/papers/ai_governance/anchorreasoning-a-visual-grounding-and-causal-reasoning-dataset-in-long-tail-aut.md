---
title: "AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios"
authors: "Zhipeng Bao, Wenjie Zhao, Tianle Zhu, Haohua Que, Chence Yang"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-09-25T06:04:12.358408"
arxiv_id: "http://arxiv.org/abs/2609.28366v1"
source_api: "arxiv"
categories: "cs.CV, cs.AI"
---

# AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios

**著者**: Zhipeng Bao, Wenjie Zhao, Tianle Zhu, Haohua Que, Chence Yang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Vision-language models (VLMs) offer a promising approach to long-tail autonomous driving, but existing driving datasets provide limited supervision for connecting decision-critical visual evidence with reasoning and planning. We introduce AnchorReasoning, a visually grounded reasoning dataset built on WOD-E2E, containing 416,119 annotated frames and 395,379 decision-critical elements across four major categories and 19 fine-grained types. Each frame is organized as a visually grounded chain-of-thought (VG-CoT) that links decision-critical element identification and localization, element attributes and implications, driving-action rationale, and action and trajectory planning. We further develop a curriculum supervised fine-tuning strategy that progressively learns these hierarchical capabilities, together with an object-size-aware grounding metric for evaluating localization quality. Experiments across eight general-purpose, embodied-AI, and AV-specific backbones show that VG-CoT supervision improves grounded reasoning and trajectory prediction. Across models, 5-s ADE and FDE decrease by 7.84 and 11.86, while RFS Frame and Cluster improve by 1.66 and 1.70. These gains are achieved with 18.5 fewer reasoning tokens and 0.32 s/frame lower inference latency on average, demonstrating the value of visually grounded, decision-focused supervision for VLM reasoning and planning in long-tail autonomous driving.
