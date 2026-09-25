---
title: "Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs"
authors: "Ravi Ranjan, Olivera Kotevska, Agoritsa Polyzou"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-09-11T06:03:46.665380"
arxiv_id: "http://arxiv.org/abs/2609.10439v1"
source_api: "arxiv"
categories: "cs.LG, cs.AI"
---

# Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs

**著者**: Ravi Ranjan, Olivera Kotevska, Agoritsa Polyzou
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Large Language Models (LLMs) can memorize and reproduce sensitive, copyrighted, or otherwise undesirable training content, creating privacy, safety, and regulatory concerns. Machine unlearning offers a practical alternative to full retraining, but many existing methods apply broad or fixed parameter updates that can degrade utility and remain brittle under deployment changes such as post-training quantization, where forgotten knowledge may partially re-emerge. We propose Forgetting Only What Matters via Unlearning Layers (FOM-UL), a layer-level unlearning framework that selects transformer layers using a forget-to-retain significance score. This score identifies layers with high influence on the forget set and low sensitivity to the retain set, allowing FOM-UL to concentrate updates where they are most effective while leaving most of the model unchanged. This targeted update strategy improves the forgetting-utility trade-off and provides an empirical path toward quantization-resilient unlearning by reducing the chance that small, diffuse updates are erased by low-bit rounding. Across TOFU, KnowUnDo, and MUSE-style evaluations, FOM-UL reduces residual memorization compared with strong GA, NPO, KLD, SURE, ReLearn, and LUNAR-based baselines while preserving retain-set utility close to the vanilla model. Under 8-bit and 4-bit post-training quantization, FOM-UL maintains stronger memorization suppression and utility preservation than competing methods, and adversarial prompt evaluations show lower recovery of forgotten content. Overall, FOM-UL provides an efficient unlearning strategy that improves targeted forgetting, utility preservation, and deployment robustness without claiming formal guarantees of erasure.
