---
title: "How far are we to GPT-4V? Closing the gap to commercial multimodal models with open-source suites"
authors: ["Zhe Chen", "Weiyun Wang", "Weiyun Wang", "Hao Tian", "Shenglong Ye", "Zhangwei Gao", "Erfei Cui", "Wenwen Tong", "et al."]
year: 2024
cited_by_count: 293
doi: "https://doi.org/10.1007/s11432-024-4231-5"
openalex_id: W4405595839
paper_type: article
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "semantic_scholar"
---

# How far are we to GPT-4V? Closing the gap to commercial multimodal models with open-source suites

**Authors**: Zhe Chen, Weiyun Wang, Weiyun Wang, Hao Tian, Shenglong Ye, Zhangwei Gao, Erfei Cui, Wenwen Tong, et al. | **Year**: 2024 | **Cited by**: 293 | **Kind**: article | **Relevance**: elicitation: supporting

## Abstract

In this paper, we introduce InternVL 1.5, an open-source multimodal large language model (MLLM) to bridge the capability gap between open-source and proprietary commercial models in multimodal understanding. We introduce three simple improvements. (1) Strong vision encoder: we explored a continuous learning strategy for the large-scale vision foundation model — InternViT-6B, boosting its visual understanding capabilities, and making it can be transferred and reused in different LLMs. (2) Dynamic high-resolution: we divide images into tiles ranging from 1 to 40 of 448×448 pixels according to the aspect ratio and resolution of the input images, which supports up to 4K resolution input. (3) High-quality bilingual dataset: we carefully collected a high-quality bilingual dataset that covers common scenes, document images, and annotated them with English and Chinese question-answer pairs, significantly enhancing performance in optical character recognition (OCR) and Chinese-related tasks. We evaluate InternVL 1.5 through a series of benchmarks and comparative studies. Compared to both open-source and proprietary commercial models, InternVL 1.5 shows competitive performance, achieving state-of-the-art results in 8 of 18 multimodal benchmarks. Code and models are available at https://github.com/OpenGVLab/InternVL.
