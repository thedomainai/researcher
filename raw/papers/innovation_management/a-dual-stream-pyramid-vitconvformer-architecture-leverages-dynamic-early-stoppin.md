---
title: "A dual-stream Pyramid ViT–ConvFormer architecture leverages dynamic early stopping to classify diffuse large B-cell lymphoma"
authors: "Gei Ki Tang, CHEE CHIN LIM, FAEZAHTUL ARBAEYAH HUSSAIN, Qi Wei Oung, Aidy Irman Yajid"
year: 2026
citations: 0
paper_type: "primary"
domain: "innovation_management"
fetched: "2026-11-06T08:12:42.119981"
doi: "https://doi.org/10.1038/s41598-026-78343-2"
openalex_id: "https://openalex.org/W7202120736"
source_api: "openalex"
---

# A dual-stream Pyramid ViT–ConvFormer architecture leverages dynamic early stopping to classify diffuse large B-cell lymphoma

**著者**: Gei Ki Tang, CHEE CHIN LIM, FAEZAHTUL ARBAEYAH HUSSAIN, Qi Wei Oung, Aidy Irman Yajid
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: イノベーション管理

## Abstract

Abstract Purpose: Accurate stratification of Diffuse Large B-Cell Lymphoma (DLBCL) into MYC subtypes is crucial for determining therapeutic intensity. While Vision Transformers (ViTs) excel at capturing global tissue context, their quadratic computational complexity results in slow convergence. To address this, we developed PyConv, a dual-stream network designed to accelerate training while maintaining precise DLBCL classification. Methods: PyConv pairs local ConvFormer blocks with global Pyramid Vision Transformer (PVT) blocks, unifying cytological boundaries and macro-level tissue context via a Multi-Head Cross-Attention fusion layer. The architecture was evaluated using 180 whole-slide images (69,480 testing patches) against 13 state-of-the-art backbones. Results: PyConv achieved a multi-class accuracy and macro F1-score of 0.9962, an absolute decision boundary for benign cohorts, and a malignant stratification AUROC of 0.9999. It reached optimal generalization by epoch 20, an 83.5% reduction in convergence time over pure transformers. While pure hybrid models showed slightly higher raw throughput, DeLong’s testing confirmed performance variances were statistically non-significant. Grad-CAM, Integrated Gradient, and Attention Rollout verified that PyConv correctly prioritizes key cytological features like nuclear contours and prominent nucleoli. Conclusion: PyConv offers a highly accelerated, computationally balanced alternative for DLBCL stratification without sacrificing diagnostic accuracy or clinical interpretability.
