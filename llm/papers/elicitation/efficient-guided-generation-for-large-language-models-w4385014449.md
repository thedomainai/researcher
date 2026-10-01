---
title: "Efficient Guided Generation for Large Language Models"
authors: ["Brandon T. Willard", "Rémi Louf"]
year: 2023
cited_by_count: 20
doi: "https://doi.org/10.48550/arxiv.2307.09702"
openalex_id: W4385014449
paper_type: preprint
evidence_kind: article
topics: ["elicitation"]
landmark: true
abstract_source: "openalex"
---

# Efficient Guided Generation for Large Language Models

**Authors**: Brandon T. Willard, Rémi Louf | **Year**: 2023 | **Cited by**: 20 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

In this article we show how the problem of neural text generation can be constructively reformulated in terms of transitions between the states of a finite-state machine. This framework leads to an efficient approach to guiding text generation with regular expressions and context-free grammars by allowing the construction of an index over a language model's vocabulary. The approach is model agnostic, allows one to enforce domain-specific knowledge and constraints, and enables the construction of reliable interfaces by guaranteeing the structure of the generated text. It adds little overhead to the token sequence generation process and significantly outperforms existing solutions. An implementation is provided in the open source Python library Outlines
