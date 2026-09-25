---
title: "Adaptive Multimodal Biometric Identification: A Lightweight CNN Approach with Confidence-based Score Fusion"
authors: "Ahmed Al-Safi, Yaghoub Farjami"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-08-31T06:01:13.128600"
doi: "https://doi.org/10.22266/ijies2026.0930.43"
openalex_id: "https://openalex.org/W7204624082"
source_api: "openalex"
---

# Adaptive Multimodal Biometric Identification: A Lightweight CNN Approach with Confidence-based Score Fusion

**著者**: Ahmed Al-Safi, Yaghoub Farjami
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Getting a biometric system to be both accurate and fast is harder than it looksmost designs sacrifice one for the other.The standard workaround is to run all modalities every timeeffective, but wasteful.We pair face and hand recognition on the MULBv1 dataset, with face going first every time.The hand model enters only when the facial confidence score drops below a fixed threshold of 0.95in practice, 95.84 % of cases never reach that point, with hand verification triggered in just 4.16% of attempts.Both modalities use the same compact Convolutional Neural Network (CNN) architecture we designed from scratch -592,776 parameters (~2.26 MiB) eachtrained independently as separate face and hand models.Face images pass through Multi-task Cascaded Convolutional Networks (MTCNN) for detection and alignment, while hand images are pre-processed with Otsu thresholding and morphological filtering.Tested on MULBv1, the system achieves 99.41% Rank-1 accuracy with a 47.92% reduction in total model invocationsefficiency and accuracy prove more compatible than most designs assume.
