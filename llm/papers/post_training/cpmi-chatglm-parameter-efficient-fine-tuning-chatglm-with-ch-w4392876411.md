---
title: "CPMI-ChatGLM: parameter-efficient fine-tuning ChatGLM with Chinese patent medicine instructions"
authors: ["Can Liu", "Kaijie Sun", "Qingqing Zhou", "Yuchen Duan", "Jianhua Shu", "Hongxing Kan", "Zongyun Gu", "Jili Hu"]
year: 2024
cited_by_count: 49
doi: "https://doi.org/10.1038/s41598-024-56874-w"
openalex_id: W4392876411
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# CPMI-ChatGLM: parameter-efficient fine-tuning ChatGLM with Chinese patent medicine instructions

**Authors**: Can Liu, Kaijie Sun, Qingqing Zhou, Yuchen Duan, Jianhua Shu, Hongxing Kan, Zongyun Gu, Jili Hu | **Year**: 2024 | **Cited by**: 49 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Chinese patent medicine (CPM) is a typical type of traditional Chinese medicine (TCM) preparation that uses Chinese herbs as raw materials and is an important means of treating diseases in TCM. Chinese patent medicine instructions (CPMI) serve as a guide for patients to use drugs safely and effectively. In this study, we apply a pre-trained language model to the domain of CPM. We have meticulously assembled, processed, and released the first CPMI dataset and fine-tuned the ChatGLM-6B base model, resulting in the development of CPMI-ChatGLM. We employed consumer-grade graphics cards for parameter-efficient fine-tuning and investigated the impact of LoRA and P-Tuning v2, as well as different data scales and instruction data settings on model performance. We evaluated CPMI-ChatGLM using BLEU, ROUGE, and BARTScore metrics. Our model achieved scores of 0.7641, 0.8188, 0.7738, 0.8107, and - 2.4786 on the BLEU-4, ROUGE-1, ROUGE-2, ROUGE-L and BARTScore metrics, respectively. In comparison experiments and human evaluation with four large language models of similar parameter scales, CPMI-ChatGLM demonstrated state-of-the-art performance. CPMI-ChatGLM demonstrates commendable proficiency in CPM recommendations, making it a promising tool for auxiliary diagnosis and treatment. Furthermore, the various attributes in the CPMI dataset can be used for data mining and analysis, providing practical application value and research significance.
