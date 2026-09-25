---
title: "Toward Culturally-aware Multimodal Sentiment Analysis for Indonesian Social Media: Dataset Construction and Baseline Evaluation"
authors: "Ali Ibrahim, Dwi Fitri Brianna, Mariana Purba, Rizka Dhini Kurnia"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-08-31T06:03:09.864896"
doi: "https://doi.org/10.22266/ijies2026.0930.49"
openalex_id: "https://openalex.org/W7204646116"
source_api: "openalex"
---

# Toward Culturally-aware Multimodal Sentiment Analysis for Indonesian Social Media: Dataset Construction and Baseline Evaluation

**著者**: Ali Ibrahim, Dwi Fitri Brianna, Mariana Purba, Rizka Dhini Kurnia
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

Multimodal sentiment analysis on Indonesian social media faces unique challenges, including Indonesian-English code-switching, indirect communication governed by local politeness norms, and considerable formality variation across platforms.Existing English-centric models fail to capture these cultural dimensions.This study introduces IndoCHA-Fusion, an annotated multimodal dataset of 500 Indonesian-language samples collected from YouTube, TikTok, Instagram, and Twitter across six content domains, labelled along nine dimensions: (1) three-class sentiment, (2) fine-grained emotion, (3) intensity, (4) formality, (5) politeness, (6) code-switching marker, (7) implicitsentiment marker, (8) word count, and (9) timestamp.We further propose the IndoCHA-Fusion architecture, integrating IndoBERT with Morphological Attention, a Vision Transformer (ViT-Base/16), WavLM, and a Cultural Context Extractor via Cross-Modal Attention Fusion.On the held-out test set (75 samples via stratified 70/15/15 splitting), the model achieves 87.3% macro-accuracy (±0.6%) and 86.9% macro-F1 (±0.7%), with absolute gains of 5.2 and 8.1 percentage points in overall and implicit-sentiment accuracy over MISA (relative improvements: 6.33% and 11.08%).Ablation confirms the cultural-context module and code-switching handler as principal contributors.All headline metrics (accuracy, macro-F1) are macro-averages over five seed runs; 95% bootstrap confidence intervals are additionally reported for accuracy, macro-F1, and implicit-sentiment accuracy specifically, together with Wilcoxon signed-rank tests (p < 0.05).Inter-annotator agreement is κ̄ = 0.836.
