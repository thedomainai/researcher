---
title: "VILA: On Pre-training for Visual Language Models"
authors: ["Lin Ji", "Hongxu Yin", "Wei Ping", "Pavlo A. Molchanov", "Mohammad Shoeybi", "Song Han"]
year: 2024
cited_by_count: 224
doi: "https://doi.org/10.1109/cvpr52733.2024.02520"
openalex_id: W4402727885
paper_type: conference-paper
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# VILA: On Pre-training for Visual Language Models

**Authors**: Lin Ji, Hongxu Yin, Wei Ping, Pavlo A. Molchanov, Mohammad Shoeybi, Song Han | **Year**: 2024 | **Cited by**: 224 | **Kind**: article | **Relevance**: elicitation: supporting

## Abstract

Visual language models (VLMs) rapidly progressed with the recent success of large language models. There have been growing efforts on visual instruction tuning to extend the LLM with visual inputs, but lacks an in-depth study of the visual language pre-training process, where the model learns to perform joint modeling on both modalities. In this work, we examine the design options for VLM pre-training by augmenting LLM towards VLM through step-by-step controllable comparisons. We introduce three main findings: (1) freezing LLMs during pre-training can achieve decent zero-shot performance, but lack in-context learning capability, which requires unfreezing the LLM; (2) interleaved pre-training data is beneficial whereas image-text pairs alone are not optimal; (3) re-blending text-only instruction data to image-text data during instruction fine-tuning not only remedies the degradation of text-only tasks, but also boosts VLM task accuracy. With an enhanced pre-training recipe we build VILA, a Visual Language model family that consistently outperforms the state-of-the-art models, e.g., LLaVA-1.5, across main benchmarks without bells and whistles. Multi-modal pre-training also helps unveil appealing properties of VILA, including multi-image reasoning, enhanced in-context learning, and better world knowledge. VILA is also deployable on Jetson Orin for on-device VLM.
