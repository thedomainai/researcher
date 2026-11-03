---
title: "Mind2Report: Expert-Level Commercial Report Synthesis via Cognitive Deep Research Agent"
authors: "Mingyue Cheng, Daoyu Wang, Qi Liu, Shuo Yu, Xiaoyu Tao"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-04T06:22:03.384024"
doi: "https://doi.org/10.1145/3799682.3840672"
openalex_id: "https://openalex.org/W7119689058"
source_api: "openalex"
---

# Mind2Report: Expert-Level Commercial Report Synthesis via Cognitive Deep Research Agent

**著者**: Mingyue Cheng, Daoyu Wang, Qi Liu, Shuo Yu, Xiaoyu Tao
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Synthesizing informative commercial reports from massive and noisy web sources is critical for high-stakes business decisions. Although recent deep research agents (DRAs) achieve notable progress, their reports remain limited in quality, reliability, and coverage. These mainly stem from ambiguous intents that cause search drift, retrieved web content that rapidly saturates the context window, and single-pass synthesis that limits report comprehensiveness. In this work, we propose Mind2Report, a cognitive deep research agent that emulates commercial analysts to synthesize expert-level reports. Mind2Report first probes fine-grained commercial intent to establish a structured outline, then recursively explores web sources and distills validated evidence into research memory to preserve context efficiency. Meanwhile, the research memory and outline continuously co-evolve, refining the report structure to avoid rigid initial planning. Finally, Mind2Report iteratively synthesizes the report based on the evolving outline and accumulated evidence. Together, these designs enable reliable and context-efficient long-horizon commercial deep research. To rigorously evaluate commercial DRAs, we further construct QRC-Eval, comprising 200 real-world commercial tasks and a holistic evaluation framework covering report quality, reliability, and coverage. Extensive experiments demonstrate that Mind2Report consistently outperforms leading proprietary and open-source DRAs, while ablations verify the effectiveness of each module and further analyze the challenges they address. We expect this work to advance the development of commercial deep research agents.
