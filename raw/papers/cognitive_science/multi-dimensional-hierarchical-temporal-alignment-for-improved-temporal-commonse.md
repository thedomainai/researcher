---
title: "Multi-dimensional hierarchical temporal alignment for improved temporal commonsense reasoning in large language models"
authors: "Ge Yan, Hai-Tao Yu, Lei Chao"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-07-29T06:00:32.249593"
doi: ""
openalex_id: "https://openalex.org/W7168064881"
source_api: "openalex"
---

# Multi-dimensional hierarchical temporal alignment for improved temporal commonsense reasoning in large language models

**著者**: Ge Yan, Hai-Tao Yu, Lei Chao
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

Benefiting from recent advances in generative AI and large language models (LLMs), current LLM-driven AI systems are rapidly reshaping how we reason, plan, and make decisions. Yet endowing these systems with human-like temporal intelligence (e.g., understanding and comparing events across time) remains largely unresolved. To address this gap, we introduce a novel Multi-dimensional Hierarchical Temporal Alignment framework (denoted as MHTA), of which the core idea is to effectively ground the temporal alignment of an LLM in both event-specific and cross-event real-world temporal commonsense knowledge. Specifically, we first frame the temporal space as a multi-dimensional hierarchical space, where each dimension comprises its own set of temporal units. Building on this formulation, we curate an initial burn-in dataset in which annotations are constructed to reflect real-world human temporal commonsense in accordance with our defined temporal space. Based on the initial burn-in dataset, we propose two complementary fine-tuning objectives: (i) Grounding the temporal alignment in event-specific temporal commonsense knowledge, which is achieved through a novel hierarchy-preserving Wasserstein loss, and (ii) Grounding the temporal alignment in cross-event temporal commonsense knowledge, which is achieved via a margin-adaptive triplet loss. To evaluate the effectiveness of MHTA, we conduct extensive experiments on three representative benchmarks (MCTACO, DurationQA, and TimeDial). For example, on the MCTACO dataset, MHTA improves Mistral-7B by 6.0% in accuracy and 10.3% in exact match, and improves DeepSeek-LLM-7B by 5.4% in accuracy and 9.8% in exact match. Combined with different backbones, MHTA surpasses nearly all baselines across the three benchmarks and exceeds the performance of advanced models such as GPT-4o on MCTACO and DurationQA. These results demonstrate that MHTA provides consistent gains in temporal commonsense reasoning across diverse LLM backbones.
