---
title: "Computer Vision System and Transformer-Based Multimodal Fusion of Medical Images for Enhanced Diagnostic Decision Making"
authors: "soltan Abdullah, Kahlan F . Aljobory"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-10-01T06:00:11.320688"
doi: "https://doi.org/10.31185/wjcms.543"
openalex_id: "https://openalex.org/W7214706313"
source_api: "openalex"
---

# Computer Vision System and Transformer-Based Multimodal Fusion of Medical Images for Enhanced Diagnostic Decision Making

**著者**: soltan Abdullah, Kahlan F . Aljobory
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

The rise of artificial intelligence technologies and their increasing reliance in numerous fields, most notably medicine, is significant. AI plays a crucial role in assisting physicians with accurate patient diagnosis, enabling them to make informed decisions. This article presents a method for integrating computer vision technologies into the medical field, where multimodal medical imaging integrates structural and textual information to support clinical decision-making. However, most image fusion frameworks based on transformers remain narrowly designed for a single media combination and a single subsequent task. This paper proposes the Multimodal Adaptive Fusion Transformer (CMAFT), a unified architecture that combines Swin transformer encoders for each media with a Catalyst Cross Attention Fusion Module (GCAF) to dynamically weight each media's contribution based on its real-time reliability. CMAFT was evaluated against two structurally different multimodal reference standards: the BraTS 2021 dataset, in which four MRI sequences (T1, T1ce, T2, FLAIR) were combined to segment brain tumor volumes, and the MIMIC-CXR dataset, in which chest X-ray images were combined with duplex radiology report inclusions to classify multimodal pathology and generate reports. The proposed GCAF module provides a learnable reliability gateway that curbs degraded or lost data streams, while a multiscale hierarchical integration pyramid preserves both fine detail and overall semantic context. Experiments show that CMAFT achieves average Dice scores of 92.4%, 87.9%, and 84.6% for whole tumor, tumor nucleus, and enhanced tumor, respectively, on the BraTS 2021 dataset, and a multi-class average area under the curve (AUC) of 0.876 with an overall F1 value of 0.658 on the MIMIC-CXR dataset, outperforming modern hybrid CNN-Transformer models while using fewer parameters compared to similar dual-code baseline models. Resection studies confirm that both reliability gate and multi-scale integration contribute to measurable gains, and that CMAFT degrades smoothly when either an MRI sequence or radiology report is unavailable. These results suggest that a single adaptive mutual attention integration design can be generalized across volumetric and text-based multimodal diagnostic pathways.
