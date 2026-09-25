---
title: "CogEvol: Towards Efficient and Reliable Learning Environment Generation"
authors: "Shangqing Tu, Daniel Zhang-Li, Yucheng Wang, Shiyu Gan, Yanpeng Wang"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-02T08:56:45.470175"
arxiv_id: "http://arxiv.org/abs/2608.30968v1"
source_api: "arxiv"
categories: "cs.CL, cs.AI"
---

# CogEvol: Towards Efficient and Reliable Learning Environment Generation

**著者**: Shangqing Tu, Daniel Zhang-Li, Yucheng Wang, Shiyu Gan, Yanpeng Wang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

We present CogEvol, a family of models trained specifically for Learning Environment Generation: turning a course brief into a finished learning artifact (structured-JSON slides or self-contained interactive HTML pages) in a single pass. Across 220k production requests, CogEvol completes a slide in a median of 17 seconds and an interactive page in 59, replacing minutes-long multi-turn agent scaffolding. Reliability is enforced rather than hoped for: a production-grounded data pipeline turns real failures into 53,687 verified SFT samples, and a hybrid rule-plus-VLM reward drives GRPO-based RL, hardened after we caught and fixed a reward-hacking episode that produced visually convincing but unplayable games. CogEvol-27B scores 83.7 on slide quality and 63.7 on a 500-case interactive-HTML benchmark with 26.9x fewer parameters than flagship coding models, and, in collaboration with the OpenMAIC team, serves their live production traffic. CogEvol-4B is released openly under the Apache 2.0 license at https://github.com/CogEvol/CogEvol-4B; external flagships are measured on the same suites under the identical harness. Scaffold editing cuts interactive-page generation cost by a further ~76%, and the full stack runs on domestic Ascend accelerators at application-level parity with A800 GPUs, lowering the unit cost of AI-native education at scale.
