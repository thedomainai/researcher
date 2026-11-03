---
title: "CG-Probes: Recovering Guardrail Directions from Patient Query Embeddings"
authors: "Marko Řeháček, Vitezslav Dusek, Martin Rusinko, Vít Nováček"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_resource_management"
fetched: "2026-11-04T06:54:21.084407"
doi: "https://doi.org/10.1145/3799682.3840044"
openalex_id: "https://openalex.org/W7214658580"
source_api: "openalex"
---

# CG-Probes: Recovering Guardrail Directions from Patient Query Embeddings

**著者**: Marko Řeháček, Vitezslav Dusek, Martin Rusinko, Vít Nováček
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人的資源管理

## Abstract

Patient-facing AI assistants promise valuable support to patients, but incoming queries can pose medical risks. To create guardrails, we work with oncologists to define three ordinal risk axes: Medical Urgency, Psychological Urgency, and Topic Sensitivity. We propose Clinical Guardrail Probes (CG-Probes) to measure the risks from query embeddings. We probe for each axis in the normalized embedding space of frozen embedders via the difference-in-means method, treating each axis as a potential linear direction. To train the probes, we cluster 79,658 Czech oncology search queries with BERTopic and use these clusters to generate pairs of queries with contrastive risk levels via few-shot prompting. We evaluate the approach on 200 queries (90 real, 110 synthetic), each graded by two oncologists, against two open-weight LLMs and a frontier LLM. We find that urgency-based axes are recoverable as linear directions, and the probes are competitive with open-weight LLMs (no significant differences in quadratic-weighted kappa) at a fraction of the latency. Each axis yields a scalar score that clinicians can inspect and use to set escalation thresholds. The pipeline requires only search logs, axis definitions, and black-box access to the embedding model, suggesting transferability across healthcare domains. Robust validation on new queries and axes remains future work.
