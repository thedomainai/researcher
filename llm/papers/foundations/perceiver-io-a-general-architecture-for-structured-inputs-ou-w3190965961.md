---
title: "Perceiver IO: A General Architecture for Structured Inputs & Outputs"
authors: ["Andrew Jaegle", "Sebastian Borgeaud", "Jean-Baptiste Alayrac", "Carl Doersch", "Catalin Ionescu", "Xin David Ding", "Skanda Koppula", "Daniel Zoran", "et al."]
year: 2021
cited_by_count: 205
doi: "https://doi.org/10.48550/arxiv.2107.14795"
openalex_id: W3190965961
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Perceiver IO: A General Architecture for Structured Inputs & Outputs

**Authors**: Andrew Jaegle, Sebastian Borgeaud, Jean-Baptiste Alayrac, Carl Doersch, Catalin Ionescu, Xin David Ding, Skanda Koppula, Daniel Zoran, et al. | **Year**: 2021 | **Cited by**: 205 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

A central goal of machine learning is the development of systems that can solve many problems in as many data domains as possible. Current architectures, however, cannot be applied beyond a small set of stereotyped settings, as they bake in domain & task assumptions or scale poorly to large inputs or outputs. In this work, we propose Perceiver IO, a general-purpose architecture that handles data from arbitrary settings while scaling linearly with the size of inputs and outputs. Our model augments the Perceiver with a flexible querying mechanism that enables outputs of various sizes and semantics, doing away with the need for task-specific architecture engineering. The same architecture achieves strong results on tasks spanning natural language and visual understanding, multi-task and multi-modal reasoning, and StarCraft II. As highlights, Perceiver IO outperforms a Transformer-based BERT baseline on the GLUE language benchmark despite removing input tokenization and achieves state-of-the-art performance on Sintel optical flow estimation with no explicit mechanisms for multiscale correspondence.
