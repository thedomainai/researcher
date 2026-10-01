---
title: "Reasoning Models and Test Time Compute Scaling: A Review"
authors: ["Kochumol Abraham"]
year: 2026
cited_by_count: 0
doi: "https://doi.org/10.5281/zenodo.22895592"
openalex_id: W7214012446
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Reasoning Models and Test Time Compute Scaling: A Review

**Authors**: Kochumol Abraham | **Year**: 2026 | **Cited by**: 0 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Language model quality was long treated as a function of parameters and training data, with inference cost fixed. That assumption no longer holds. This review examines the shift towards spending variable computation at query time. It traces four stages: prompted intermediate reasoning, bootstrapped training on self-generated traces, critique and revision loops, and reinforcement learning against outcome signals that produces extended reasoning as a trained behaviour. The strategies for spending an inference budget are organised into longer single traces, repeated sampling with aggregation, search over partial solutions, and refinement, each characterised by its parallelism and its characteristic failure mode. The review then examines the limits of the approach. Unlike training-time scaling, inference-time returns are instance-dependent, admit no smooth law, and can turn negative, with published analysis reporting accuracy declining as reasoning length grows. Domain evaluations in software security and medicine are surveyed alongside evidence that the reinforcement learning recipe generalises to graph, web-agent and multimodal settings. Open problems are identified in difficulty estimation, verification signals, compute-aware reporting, and the unresolved relationship between a visible reasoning trace and the answer it precedes.
