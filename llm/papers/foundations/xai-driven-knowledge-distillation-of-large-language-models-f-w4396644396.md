---
title: "Xai-driven knowledge distillation of large language models for efficient deployment on low-resource devices"
authors: ["Riccardo Cantini", "Alessio Orsino", "Domenico Talia"]
year: 2024
cited_by_count: 30
doi: "https://doi.org/10.1186/s40537-024-00928-3"
openalex_id: W4396644396
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Xai-driven knowledge distillation of large language models for efficient deployment on low-resource devices

**Authors**: Riccardo Cantini, Alessio Orsino, Domenico Talia | **Year**: 2024 | **Cited by**: 30 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Abstract Large Language Models (LLMs) are characterized by their inherent memory inefficiency and compute-intensive nature, making them impractical to run on low-resource devices and hindering their applicability in edge AI contexts. To address this issue, Knowledge Distillation approaches have been adopted to transfer knowledge from a complex model, referred to as the teacher, to a more compact, computationally efficient one, known as the student. The aim is to retain the performance of the original model while substantially reducing computational requirements. However, traditional knowledge distillation methods may struggle to effectively transfer crucial explainable knowledge from an LLM teacher to the student, potentially leading to explanation inconsistencies and decreased performance. This paper presents DiXtill, a method based on a novel approach to distilling knowledge from LLMs into lightweight neural architectures. The main idea is to leverage local explanations provided by an eXplainable Artificial Intelligence (XAI) method to guide the cross-architecture distillation of a teacher LLM into a self-explainable student, specifically a bi-directional LSTM network.Experimental results show that our XAI-driven distillation method allows the teacher explanations to be effectively transferred to the student, resulting in better agreement compared to classical distillation methods,thus enhancing the student interpretability. Furthermore, it enables the student to achieve comparable performance to the teacher LLM while also delivering a significantly higher compression ratio and speedup compared to other techniques such as post-training quantization and pruning, which paves the way for more efficient and sustainable edge AI applications
