---
title: "Developing meta-FM machine learning model with application for personalized language learning environment"
authors: "Qian Li, Y. Zhang"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-09-22T06:00:38.643535"
doi: "https://doi.org/10.1038/s41598-026-71932-1"
openalex_id: "https://openalex.org/W7213670956"
source_api: "openalex"
---

# Developing meta-FM machine learning model with application for personalized language learning environment

**著者**: Qian Li, Y. Zhang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

A meta-pretrained factorization machine (FM) framework, termed Meta-FM, is proposed to address the cold-start problem in personalized learning path generation for middle-school foreign language education. The framework further introduces a cross-modal feature augmentation module that integrates categorical metadata (e.g., learning style) with continuous interaction data (e.g., quiz performance) to enrich sparse representations for new learners. The method integrates meta-learning principles with a high-dimensional FM architecture, enabling rapid adaptation to new students from minimal initial data while preserving generalizability across diverse cohorts. The core innovation lies in a three-module system: a meta-pretrained FM backbone that captures feature interactions through latent factors, an adaptive fine-tuning mechanism that updates these factors via few-shot learning, and a cross-modal feature augmentation layer that enriches sparse inputs with structured metadata. Unlike conventional approaches that rely on heuristic rules or extensive per-learner data, the framework dynamically refines recommendations by combining behavioral metrics with cognitive and demographic indicators. The system interfaces with existing diagnostic and ranking modules, replacing one-hot encodings with dense feature representations and stochastic Plackett–Luce ranking for path generation. Implemented with mixed-precision quantization and Transformer-based feature encoding, the method achieves efficient memory usage and robust cold-start performance. Experiments on multilingual student interaction logs demonstrate significant improvements in personalization accuracy and adaptation speed compared with baseline methods. The results highlight the potential of meta-pretrained FMs to bridge the gap between interpretable feature interactions and rapid cold-start adaptation in educational recommendation systems.
