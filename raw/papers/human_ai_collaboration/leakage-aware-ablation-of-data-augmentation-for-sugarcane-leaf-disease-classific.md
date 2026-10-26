---
title: "Leakage-Aware Ablation of Data Augmentation for Sugarcane Leaf Disease Classification: Operator- and Severity-Specific Effects"
authors: "Jarot Budiasto, Hasanudin Jayawardana, Tri Kustanti Rahayu, Yosefina Mangera"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-10-27T06:03:45.724863"
doi: "https://doi.org/10.63158/journalisi.v8i5.1896"
openalex_id: "https://openalex.org/W7223449483"
source_api: "openalex"
---

# Leakage-Aware Ablation of Data Augmentation for Sugarcane Leaf Disease Classification: Operator- and Severity-Specific Effects

**著者**: Jarot Budiasto, Hasanudin Jayawardana, Tri Kustanti Rahayu, Yosefina Mangera
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Conventional image augmentation is widely used to improve model generalization; however, its benefit in fine-grained plant disease classification can be overstated when duplicated or near-duplicated images cross the train–test boundary. This study tests whether conventional augmentation remains beneficial for sugarcane leaf disease classification after controlling duplicate leakage. The original Sugarcane Leaf Dataset contained 6,748 images and was audited using MD5, perceptual hash (pHash), and structural similarity index measure (SSIM), yielding 5,389 curated images. A leakage-aware stratified 70/15/15 train–validation–test split evaluated 13 augmentation configurations using ImageNet-pretrained MobileNetV2 across three random seeds, totaling 39 runs. Macro-F1 performance was assessed through paired stratified bootstrap analysis and an exact Page test. The baseline attained the highest mean Macro-F1 (0.9646 ± 0.0068), while photometric augmentation produced comparable performance (0.9643 ± 0.0079). Geometric policies generally reduced performance, and combined augmentation achieved the lowest Macro-F1 (0.8029). The Page test indicated an overall negative ordered trend, although the medium recipe outperformed the light recipe. These results demonstrate that augmentation policies must be validated by operator and severity level, rather than enabled by default in plant disease recognition.
