---
title: "TALM: Tool Augmented Language Models"
authors: ["Aaron Parisi", "Yao Zhao", "Noah Fiedel"]
year: 2022
cited_by_count: 32
doi: "https://doi.org/10.48550/arxiv.2205.12255"
openalex_id: W4281557623
paper_type: preprint
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# TALM: Tool Augmented Language Models

**Authors**: Aaron Parisi, Yao Zhao, Noah Fiedel | **Year**: 2022 | **Cited by**: 32 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

Transformer based language models (LMs) demonstrate increasing performance with scale across a wide variety of tasks. Scale alone however cannot enable models to solve tasks that require access to ephemeral, changing, or private data that was unavailable at training time. Many useful tasks may also benefit from LMs being able to access APIs that read or modify state. In this work, we present Tool Augmented Language Models (TALM), combining a text-only approach to augment language models with non-differentiable tools, and an iterative "self-play" technique to bootstrap performance starting from few tool demonstrations. TALM exhibits strong performance on both a knowledge-heavy QA task and a reasoning oriented math task with simple tools. At a given model scale, TALM significantly outperforms non-augmented LMs. We further demonstrate that TALM successfully performs out-of-distribution inferences on both QA and math tasks, where non-augmented LMs fail. Our results suggest that Tool Augmented Language Models are a promising direction to enrich LMs' capabilities, with less dependence on scale.
