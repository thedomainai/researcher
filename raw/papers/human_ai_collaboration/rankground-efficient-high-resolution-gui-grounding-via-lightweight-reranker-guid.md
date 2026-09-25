---
title: "RankGround: Efficient High-Resolution GUI Grounding via Lightweight Reranker-Guided Crop Selection"
authors: "Liyang Fan, Xinping Bi, Yitai Li, Shuaimin Li, Hui Li"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-18T06:03:25.940955"
arxiv_id: "http://arxiv.org/abs/2609.18690v1"
source_api: "arxiv"
categories: "cs.CV, cs.CL, cs.HC"
---

# RankGround: Efficient High-Resolution GUI Grounding via Lightweight Reranker-Guided Crop Selection

**著者**: Liyang Fan, Xinping Bi, Yitai Li, Shuaimin Li, Hui Li
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Graphical User Interface (GUI) grounding is a fundamental perception task for multimodal agents, enabling them to interpret natural language instructions and interact with digital interfaces. Existing methods face a fundamental trade-off between accuracy and efficiency: direct full-image inference often fails to capture small or visually similar UI elements, while multi-crop strategies improve localization at the cost of multiple expensive Vision-Language Model (VLM) calls per query.
  To address this challenge, we propose RankGround, a two-stage framework that achieves accurate GUI grounding with a single VLM call per query. Central to our approach is GroundRanker, a lightweight multimodal reranker that identifies the most promising crop from a dense candidate set. Because no off-the-shelf ranking dataset is available, we construct ranking supervision data from existing grounding datasets. A strict containment criterion and boundary-aware positive augmentation improve alignment and spatial coverage in cluttered layouts. GroundRanker is then trained with a two-stage curriculum: a pointwise objective first learns coarse containment, and a listwise objective refines subtle semantic and spatial distinctions among visually similar crops.
  Experimental results show that RankGround consistently outperforms strong baselines while reducing computational cost. It achieves 1.4 times faster inference and improves localization accuracy by 5.5% on average over the second-best method across all backbones and screen scales, establishing a new state of the art in both efficiency and precision for GUI grounding.
