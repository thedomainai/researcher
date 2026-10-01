---
title: "GenCeption: Evaluate vision LLMs with unlabeled unimodal data"
authors: ["Lele Cao", "Valentin Buchner", "Zineb Senane", "Fangkai Yang"]
year: 2025
cited_by_count: 1
doi: "https://doi.org/10.1016/j.csl.2025.101785"
openalex_id: W4408050188
paper_type: article
evidence_kind: article
topics: ["evaluation"]
landmark: false
abstract_source: "semantic_scholar"
---

# GenCeption: Evaluate vision LLMs with unlabeled unimodal data

**Authors**: Lele Cao, Valentin Buchner, Zineb Senane, Fangkai Yang | **Year**: 2025 | **Cited by**: 1 | **Kind**: article | **Relevance**: evaluation: supporting

## Abstract

Multimodal Large Language Models (MLLMs) are typically assessed using expensive annotated multimodal benchmarks, which often lag behind the rapidly evolving demands of MLLM evaluation. This paper outlines and validates GenCeption, a novel, annotation-free evaluation method that requires only unimodal data to measure inter-modality semantic coherence and inversely assesses MLLMs' tendency to hallucinate. This approach eliminates the need for costly data annotation, minimizes the risk of training data contamination, is expected to result in slower benchmark saturation, and avoids the illusion of emerging abilities. Inspired by the DrawCeption game, GenCeption begins with a non-textual sample and proceeds through iterative description and generation steps. The semantic drift across iterations is quantified using the GC@T metric. While GenCeption is principally applicable to MLLMs across various modalities, this paper focuses on its implementation and validation for Vision LLMs (VLLMs). Based on the GenCeption method, we establish the MMECeption benchmark for evaluating VLLMs, and compare the performance of several popular VLLMs and human annotators. Our empirical results validate GenCeption's effectiveness, demonstrating strong correlations with established VLLM benchmarks. VLLMs still significantly lag behind human performance and struggle especially with text-intensive tasks.
