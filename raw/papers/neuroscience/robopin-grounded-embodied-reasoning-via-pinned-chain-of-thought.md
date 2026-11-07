---
title: "RoboPIN: Grounded Embodied Reasoning via Pinned Chain-of-Thought"
authors: "Y Huang, Yifu Yuan, Linqi Han, Chengwen Li, Shuoheng Zhang"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-11-08T06:01:31.203111"
doi: "https://doi.org/10.1145/3767308.3835509"
openalex_id: "https://openalex.org/W7164894231"
source_api: "openalex"
---

# RoboPIN: Grounded Embodied Reasoning via Pinned Chain-of-Thought

**著者**: Y Huang, Yifu Yuan, Linqi Han, Chengwen Li, Shuoheng Zhang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Embodied reasoning requires models to perceive task-relevant objects and spaces in physical environments and maintain consistent visual grounding throughout multi-step reasoning. However, current vision-language models rely on text-only or coordinate-augmented chain-of-thought, where entity references remain implicit and ambiguous. This may cause the reasoning process to decouple from visual evidence, entity references to drift across steps, and a causal disconnection between the reasoning trajectory and the final answer, with these problems further amplified in multi-view scenarios due to cross-view appearance changes. To address these issues, we propose Pinned Chain-of-Thought (PinCoT), a structured reasoning paradigm that pins every reasoning step to visual evidence. PinCoT introduces the concept of reasoning anchor, which binds each task-relevant entity to a structured visual anchor with entity name, unique identity, view index, and spatial grounding, enabling consistent entity tracking across reasoning steps and views. We build a fully automated data generation pipeline to construct PIN-170K, a high-quality PinCoT-formatted reasoning dataset. We then train RoboPIN through three-stage post-training that progressively injects embodied knowledge, structured reasoning ability, and process-supervised alignment, with rewards that directly constrain both anchor localization and identity consistency during reasoning. On 14 benchmarks covering embodied spatial reasoning, multi-view reasoning, and pointing, RoboPIN with only 4B parameters surpasses 7B level open-source embodied models on average, achieving a 12% average improvement over the strongest 7B baseline, Mimo-Embodied. Further analysis shows that PinCoT improves grounding accuracy and cross-step identity consistency, validating the effectiveness of process supervision.
