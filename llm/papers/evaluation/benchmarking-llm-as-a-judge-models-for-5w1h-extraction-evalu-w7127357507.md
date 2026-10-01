---
title: "Benchmarking LLM-as-a-Judge Models for 5W1H Extraction Evaluation"
authors: ["José Manuel Cassola-Bacallao", "José Morales-Donaire", "Paula Hernández-Montoya", "Brian Keith-Norambuena"]
year: 2026
cited_by_count: 1
doi: "https://doi.org/10.3390/electronics15030659"
openalex_id: W7127357507
paper_type: article
evidence_kind: article
topics: ["evaluation"]
landmark: false
abstract_source: "openalex"
---

# Benchmarking LLM-as-a-Judge Models for 5W1H Extraction Evaluation

**Authors**: José Manuel Cassola-Bacallao, José Morales-Donaire, Paula Hernández-Montoya, Brian Keith-Norambuena | **Year**: 2026 | **Cited by**: 1 | **Kind**: article | **Relevance**: evaluation: supporting

## Abstract

Evaluating 5W1H (Who, What, When, Where, Why, and How) information extraction systems remains challenging, as traditional information retrieval metrics like ROUGE and BLEU fail to capture semantic accuracy and narrative coherence. The LLM-as-a-Judge paradigm offers a promising alternative, yet systematic comparisons of judge models for this task are lacking. This study benchmarks multiple large language models, including state-of-the-art models such as GPT, Claude, and Gemini as evaluators of 5W1H extractions from Spanish news articles. We assess judge performance across six quality criteria: Factual Accuracy, Completeness, Relevance and Conciseness, Clarity and Readability, Faithfulness to Source, and Overall Coherence. Our analysis examines inter-judge agreement, score distribution patterns, criterion-level variance, and the relationship between evaluation quality and computational cost. Using two Spanish-language corpora (BASSE and FLARES), we identify which criteria exhibit consistent cross-model agreement and which prove most sensitive to judge selection. The main contribution of this work is providing the first systematic benchmark of LLM-as-a-Judge models for 5W1H extraction evaluation in Spanish, validated against expert journalistic judgment. Results reveal that all evaluated models achieve alignment levels above 90% across all metrics. Specifically, Claude Sonnet 4.5 emerges as the most accurate evaluator with a Global Judgment Acceptance Rate (JAR) of 99.79%. Furthermore, meta-evaluation with human experts demonstrates a substantial inter-annotator agreement of κ=0.6739. Finally, we provide recommendations for judge model selection based on task requirements and resource constraints, contributing practical guidance for researchers implementing LLM-based evaluation pipelines for information extraction tasks.
