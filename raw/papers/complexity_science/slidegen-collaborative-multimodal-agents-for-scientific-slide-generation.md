---
title: "SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation"
authors: "Xin Liang, Zhilin Zhang, Xiang Zhang, Haoran Su, Yiwei Xu"
year: 2026
citations: 35
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-08T06:15:40.733421"
doi: "https://doi.org/10.1145/3767308.3835435"
openalex_id: "https://openalex.org/W7109032245"
source_api: "openalex"
---

# SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation

**著者**: Xin Liang, Zhilin Zhang, Xiang Zhang, Haoran Su, Yiwei Xu
**年**: 2026 | **被引用数**: 35
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Creating presentation slides from scientific papers is not simply a matter of summarizing paragraphs. A presenter is required to decide what story to tell, which figures and equations to highlight, and how to arrange them into pages that are visually clear rather than crowded or repetitive. The need to jointly reason over long contexts and layout-sensitive design makes paper-to-slide generation a uniquely challenging multimodal task. Most existing approaches, however, focus mainly on textual content selection, producing slides that often lack visual balance, narrative flow, or coherent integration of multimodal evidence. In this work, we introduce SlideGen, a collaborative vision-language multi-agent framework that coordinates narrative planning, multimodal grounding, and layout composition. SlideGen assigns specialized agents to outline the presentation structure, align supporting figures and tables with key claims, generate speaker notes, and compose editable PPTX slides through a diverse layout library. By refining layouts at the deck level, the system produces slide decks that are both faithful to the source paper and effective as presentations. To evaluate slide generation beyond text fidelity, we propose geometry-aware density (GAD), a metric that captures visual clutter, sparsity, and fragmentation, and shows strong agreement with human judgments. Evaluated across four complementary dimensions on our 200-paper benchmark, SlideGen consistently and significantly improves layout balance, content coverage, and text coherence, outperforming competitive baselines in paper-to-slide generation. Our findings suggest that effective slide generation requires multimodal design reasoning, and that agent collaboration offers a principled bridge between document understanding and scientific communication.
