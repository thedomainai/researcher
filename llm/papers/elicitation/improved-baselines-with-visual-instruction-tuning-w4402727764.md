---
title: "Improved Baselines with Visual Instruction Tuning"
authors: ["Haotian Liu", "Chunyuan Li", "Yuheng Li", "Yong Jae Lee"]
year: 2024
cited_by_count: 1490
doi: "https://doi.org/10.1109/cvpr52733.2024.02484"
openalex_id: W4402727764
paper_type: conference-paper
evidence_kind: article
topics: ["elicitation"]
landmark: true
abstract_source: "openalex"
---

# Improved Baselines with Visual Instruction Tuning

**Authors**: Haotian Liu, Chunyuan Li, Yuheng Li, Yong Jae Lee | **Year**: 2024 | **Cited by**: 1490 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

Large multimodal models (LMM) have recently shown encouraging progress with visual instruction tuning. In this paper, we present the first systematic study to investigate the design choices of LMMs in a controlled setting under the LLaVA framework. We show that the fully-connected vision-language connector in LLaVA is surprisingly power-ful and data-efficient. With simple modifications to LLa VA, namely, using CLIP- ViT-L-336px with an MLP projection and adding academic-task-oriented VQA data with response formatting prompts, we establish stronger baselines that achieve state-of-the-art across 11 benchmarks. Our final 13B checkpoint uses merely 1.2M publicly available data, and finishes full training in ~ 1 day on a single 8-AI00 node. Furthermore, we present some early exploration of open problems in LMMs, including scaling to higher resolution inputs, compositional capabilities, and model hallucination, etc. We hope this makes state-of-the-art LMM research more accessible. Code and model will be publicly available.
