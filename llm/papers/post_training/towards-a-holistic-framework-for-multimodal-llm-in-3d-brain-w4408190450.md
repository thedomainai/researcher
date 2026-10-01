---
title: "Towards a holistic framework for multimodal LLM in 3D brain CT radiology report generation"
authors: ["Cheng-Yi Li", "Kao-Jung Chang", "Cheng-Fu Yang", "Hsin‐Yu Wu", "Wenting Chen", "Hritik Bansal", "Ling Chen", "Yi‐Ping Yang", "et al."]
year: 2025
cited_by_count: 70
doi: "https://doi.org/10.1038/s41467-025-57426-0"
openalex_id: W4408190450
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Towards a holistic framework for multimodal LLM in 3D brain CT radiology report generation

**Authors**: Cheng-Yi Li, Kao-Jung Chang, Cheng-Fu Yang, Hsin‐Yu Wu, Wenting Chen, Hritik Bansal, Ling Chen, Yi‐Ping Yang, et al. | **Year**: 2025 | **Cited by**: 70 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Multi-modal large language models (MLLMs) have transformed the landscape of modern healthcare, with automated radiology report generation (RRG) emerging as a cutting-edge application. While 2D MLLM-based RRG has been well established, its utility for 3D medical images remains largely unexplored. In this regard, we curate the 3D-BrainCT dataset (18,885 text-scan pairs) and develop BrainGPT, a clinically visual instruction-tuned (CVIT) model designed for 3D CT RRG. While we notice that the traditional LLM metrics failed to gauge the diagnostic quality of the RRG, we propose feature-oriented radiology task evaluation (FORTE), an evaluation scheme that captures the clinical essence of the generated reports. Here we show that BrainGPT achieves an average FORTE F1-score of 0.71 (degree = 0.661; landmark = 0.706; feature = 0.693, and impression = 0.779) and 74% of BrainGPT-generated reports were indistinguishable from human-written ground truth in a Turing-like test. Together, our work establishes a comprehensive framework encompassing dataset curation, anatomy-aware model fine-tuning, and the development of robust evaluation metrics for the RRG. By sharing our experience in 3D MLLM-based RRG, we aim to accelerate the expedition in human-machine collaboration for next-generation healthcare. Multimodal large language models (MLLMs) hold promise for a range of medical applications. Here, the authors use MLLMs for 3D brain CT radiology report generation, demonstrating that combining anatomy-aware model fine-tuning with robust evaluation metrics establishes a comprehensive and effective framework.
