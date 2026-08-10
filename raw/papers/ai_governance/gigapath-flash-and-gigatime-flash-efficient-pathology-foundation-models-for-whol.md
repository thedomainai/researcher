---
title: "GigaPath-Flash and GigaTIME-Flash: Efficient Pathology Foundation Models for Whole-Slide and Tumor Microenvironment Analysis"
authors: "Naoto Usuyama, Jeya Maria Jose Valanarasu, Sicong Yao, Hanwen Xu, Jaspreet Bagga"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-07-22T06:02:43.415766"
arxiv_id: "http://arxiv.org/abs/2607.18218v1"
source_api: "arxiv"
categories: "cs.CV, cs.AI"
---

# GigaPath-Flash and GigaTIME-Flash: Efficient Pathology Foundation Models for Whole-Slide and Tumor Microenvironment Analysis

**著者**: Naoto Usuyama, Jeya Maria Jose Valanarasu, Sicong Yao, Hanwen Xu, Jaspreet Bagga
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Foundation models have emerged as a driving force in computational pathology, with the potential to transform cancer diagnosis, prognosis, and treatment selection by learning transferable representations from large-scale histopathology data. A growing landscape of pathology foundation models now spans diverse data sources, architectures, and downstream applications. However, most pretrained models operate only at the image-tile level, use restrictive licenses, and remain computationally expensive, limiting large-scale slide-level clinical and research use.
  Here, we introduce GigaPath-Flash and GigaTIME-Flash, efficient models for whole-slide pathology AI and spatial proteomics prediction. GigaPath-Flash combines a 22M-parameter ViT-S tile encoder with a 21M-parameter LongNet slide encoder, both pretrained on large-scale real-world histopathology data. Its compact tile encoder is distilled from the billion-parameter GigaPath (ViT-g) teacher and shared by both models. GigaPath-Flash retains 97% of GigaPath's average slide-level performance with 50x less compute. GigaTIME-Flash extends this backbone to predict the tumor immune microenvironment directly from routine H&E images. It surpasses the original CNN-based GigaTIME in prediction quality while running 6x faster and using 8x less GPU memory.
  Together with GigaPath and GigaTIME, these models form an open-weight, Apache-2.0-licensed family pretrained on large-scale real-world clinical data. By releasing all models and weights, we provide accessible building blocks for computational pathology, immuno-oncology, and precision health.
