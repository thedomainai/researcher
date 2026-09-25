---
title: "A machine learning framework for privacy preserving personalized multimodal emotion recognition"
authors: "Sanjay Agal"
year: 2026
citations: 0
paper_type: "meta_analysis"
domain: "cognitive_science"
fetched: "2026-09-02T08:53:51.985403"
doi: "https://doi.org/10.1038/s41598-026-69233-8"
openalex_id: "https://openalex.org/W7204803478"
source_api: "openalex"
---

# A machine learning framework for privacy preserving personalized multimodal emotion recognition

**著者**: Sanjay Agal
**年**: 2026 | **被引用数**: 0
**タイプ**: meta_analysis | **分野**: 認知科学

## Abstract

This paper presents a novel machine learning framework, Privacy-Preserving Personalized Multimodal Emotion Recognition (P3MER), that simultaneously addresses three fundamental challenges in affective computing: achieving state-of-the-art recognition accuracy, ensuring robust privacy protection, and enabling effective personalization to individual users. The framework integrates hierarchical multimodal fusion with federated learning and differential privacy to enable collaborative model training without centralized data collection, thereby preserving the confidentiality of sensitive biometric data such as facial expressions, speech recordings, and physiological signals. A key innovation is the incorporation of federated meta-learning that allows rapid personalization of global models to individual expression patterns with minimal local data, while maintaining formal privacy guarantees. Extensive experimental evaluation across three benchmark datasets (CMU-MOSEI, DEAP, and MAHNOB-HCI) demonstrates that P3MER achieves an average improvement of 4.1% in recognition accuracy over state-of-the-art centralized models, while providing formal \((\epsilon , \delta )\) -differential privacy guarantees. At a privacy budget of \(\epsilon = 3.0\) , the framework maintains 95.8% of the non-private federated performance, significantly outperforming conventional differentially private federated learning approaches. The meta-learning personalization mechanism yields an average personalization gain of 14.7% with only five adaptation steps, effectively addressing the inherent heterogeneity in emotional expression across individuals. Furthermore, the framework demonstrates exceptional robustness to real-world challenges, including extreme data heterogeneity (39% reduction in performance variance compared to existing personalized federated approaches), modality incompleteness (maintaining 86.3% of full-modality performance when physiological signals are unavailable), and few-shot learning scenarios (achieving 78% of maximum personalization gain with only 20-50 local samples). These results collectively validate that P3MER successfully reconciles the competing objectives of accuracy, privacy, and personalization in multimodal emotion recognition, offering a practical pathway toward deployable, ethical affective computing systems that respect user privacy while maintaining adaptive intelligence. The proposed framework establishes new standards for privacy-preserving affective computing and provides both theoretical foundations and practical implementations for developing emotion-aware technologies that earn user trust through their technical capability and ethical design. By demonstrating that privacy protection and personalization need not come at the expense of recognition accuracy, this work advances the field toward human-centered AI systems that are simultaneously intelligent, adaptive, and respectful of fundamental privacy rights.
