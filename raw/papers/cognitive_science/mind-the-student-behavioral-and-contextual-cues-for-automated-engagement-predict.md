---
title: "Mind the Student: Behavioral and Contextual Cues for Automated Engagement Prediction in Online Learning"
authors: "Alperen Kantarci, Visvanathan Ramesh, Gemma Roig"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-08-29T06:00:45.489039"
arxiv_id: "http://arxiv.org/abs/2608.24340v1"
source_api: "arxiv"
categories: "cs.CV, cs.AI, cs.HC, cs.LG"
---

# Mind the Student: Behavioral and Contextual Cues for Automated Engagement Prediction in Online Learning

**著者**: Alperen Kantarci, Visvanathan Ramesh, Gemma Roig
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

The prediction of student engagement from the online tutoring videos is difficult because engagement is a multidimensional construct comprising distinct behavioral, emotional, and cognitive states. A reliable prediction requires bringing together different types of behavioral signals as well as expressive cues. Through our analysis of the CASED dataset, it is clear that engagement prediction gets even harder due to the high inter-person variability as well as the subjectivity of the engagement annotation. To tackle these challenges, we develop a multimodal framework that integrates the implicit spatiotemporal features extracted from pretrained video, audio, and image encoders along with structured behavioral modalities like head pose, gaze, facial action units, emotion, and wavelet-based audio features. We integrate these modalities via a Perceiver IO latent bottleneck. Moreover, student and instructor personalities are modeled as variational posteriors over learnable embeddings to enable partial pooling across participants. We employ evidential regression and spectral-normalized Gaussian process classification heads for uncertainty-aware prediction to further improve robustness and calibration. Benchmark on the CASED challenge test set shows that all participating methods converge near random-chance performance, revealing the difficulty of the dataset. In this highly ambiguous regime, our framework achieves competitive performance while uniquely offering well-calibrated uncertainty metrics, demonstrating that reliable risk-quantification is an essential prerequisite for deploying engagement models in real-world educational tools.
