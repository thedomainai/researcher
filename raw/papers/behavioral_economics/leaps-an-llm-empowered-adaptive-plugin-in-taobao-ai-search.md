---
title: "LEAPS: An LLM-Empowered Adaptive Plugin in Taobao AI Search"
authors: "Lei Wang, Jinhang Wu, Zhibin Wang, Biye Li"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-11-04T06:27:29.188950"
doi: "https://doi.org/10.1145/3799682.3840100"
openalex_id: "https://openalex.org/W7123283912"
source_api: "openalex"
---

# LEAPS: An LLM-Empowered Adaptive Plugin in Taobao AI Search

**著者**: Lei Wang, Jinhang Wu, Zhibin Wang, Biye Li
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

The rapid rise of large language models has shifted user search behavior from discrete keywords to natural-language, multi-constraint queries--a shift existing e-commerce search architectures struggle to accommodate. Users face a dilemma: precise natural-language queries often trigger zero-result scenarios, while forced simplification yields noisy, generic results that overwhelm decision-making. To address this, we propose LEAPS (LLM-Empowered Adaptive Plugin in Taobao AI Search), which upgrades traditional search pipelines via a "Broaden-and-Refine" paradigm by attaching plugins at both ends. (1) Upstream, a Query Expander generates adaptive, complementary query combinations to maximize the candidate set, trained via a three-stage strategy of inverse data augmentation, posterior-knowledge supervised fine-tuning, and diversity-aware reinforcement learning. (2) Downstream, a Relevance Verifier filters noise by synthesizing multi-source signals (e.g., OCR text, reviews) with chain-of-thought reasoning. Extensive offline experiments and online A/B testing show that LEAPS significantly enhances the conversational shopping experience, while its non-intrusive architecture preserves established short-text retrieval performance and enables low-cost integration with diverse back-ends. Fully deployed on Taobao AI Search since August 2025, LEAPS serves hundreds of millions of users monthly.
