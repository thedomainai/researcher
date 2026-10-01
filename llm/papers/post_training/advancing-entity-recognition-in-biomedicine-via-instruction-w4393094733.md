---
title: "Advancing entity recognition in biomedicine via instruction tuning of large language models"
authors: ["Vipina K. Keloth", "Yan Hu", "Qianqian Xie", "Xueqing Peng", "Yan Wang", "Andrew Zheng", "Melih Selek", "Kalpana Raja", "et al."]
year: 2024
cited_by_count: 105
doi: "https://doi.org/10.1093/bioinformatics/btae163"
openalex_id: W4393094733
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Advancing entity recognition in biomedicine via instruction tuning of large language models

**Authors**: Vipina K. Keloth, Yan Hu, Qianqian Xie, Xueqing Peng, Yan Wang, Andrew Zheng, Melih Selek, Kalpana Raja, et al. | **Year**: 2024 | **Cited by**: 105 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

MOTIVATION: Large Language Models (LLMs) have the potential to revolutionize the field of Natural Language Processing, excelling not only in text generation and reasoning tasks but also in their ability for zero/few-shot learning, swiftly adapting to new tasks with minimal fine-tuning. LLMs have also demonstrated great promise in biomedical and healthcare applications. However, when it comes to Named Entity Recognition (NER), particularly within the biomedical domain, LLMs fall short of the effectiveness exhibited by fine-tuned domain-specific models. One key reason is that NER is typically conceptualized as a sequence labeling task, whereas LLMs are optimized for text generation and reasoning tasks. RESULTS: We developed an instruction-based learning paradigm that transforms biomedical NER from a sequence labeling task into a generation task. This paradigm is end-to-end and streamlines the training and evaluation process by automatically repurposing pre-existing biomedical NER datasets. We further developed BioNER-LLaMA using the proposed paradigm with LLaMA-7B as the foundational LLM. We conducted extensive testing on BioNER-LLaMA across three widely recognized biomedical NER datasets, consisting of entities related to diseases, chemicals, and genes. The results revealed that BioNER-LLaMA consistently achieved higher F1-scores ranging from 5% to 30% compared to the few-shot learning capabilities of GPT-4 on datasets with different biomedical entities. We show that a general-domain LLM can match the performance of rigorously fine-tuned PubMedBERT models and PMC-LLaMA, biomedical-specific language model. Our findings underscore the potential of our proposed paradigm in developing general-domain LLMs that can rival SOTA performances in multi-task, multi-domain scenarios in biomedical and health applications. AVAILABILITY AND IMPLEMENTATION: Datasets and other resources are available at https://github.com/BIDS-Xu-Lab/BioNER-LLaMA.
