---
title: "Explainable Embeddings with Distance Explainer"
authors: "Christiaan Meijer, Patrick Bos"
year: 2026
citations: 2
paper_type: "primary"
domain: "hci"
fetched: "2026-11-20T06:02:43.798630"
doi: "https://doi.org/10.1007/978-3-032-45470-6_20"
openalex_id: "https://openalex.org/W4415329046"
source_api: "openalex"
---

# Explainable Embeddings with Distance Explainer

**著者**: Christiaan Meijer, Patrick Bos
**年**: 2026 | **被引用数**: 2
**タイプ**: primary | **分野**: HCI

## Abstract

While eXplainable AI (XAI) has advanced significantly, few methods address interpretability in embedded vector spaces where dimensions represent complex abstractions. We introduce Distance Explainer, a novel method for generating local, post-hoc explanations of embedded spaces in machine learning models. Our approach adapts saliency-based techniques from RISE to explain the distance between two embedded data points by assigning attribution values through selective masking and distance-ranked mask filtering. We evaluate Distance Explainer on cross-modal embeddings (image-image and image-caption pairs) using established XAI metrics including Faithfulness, Sensitivity/Robustness, and Randomization. Experiments with ImageNet and CLIP models demonstrate that our method effectively identifies features contributing to similarity or dissimilarity between embedded data points while maintaining high robustness and consistency. We also explore how parameter tuning, particularly mask quantity and selection strategy, affects explanation quality. This work addresses a critical gap in XAI research and enhances transparency and trustworthiness in deep learning applications utilizing embedded spaces.
