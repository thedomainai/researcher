---
title: "Graph-Structured Persistent Memory for Efficient LLM-Based Computer Use Agents"
authors: ["Danylo Vorvul", "Andrii P. Musienko", "Iryna Galchenko", "Mykola Myroniuk", "Андрій Собчук"]
year: 2026
cited_by_count: 0
doi: "https://doi.org/10.3390/axioms15060415"
openalex_id: W7163133361
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# Graph-Structured Persistent Memory for Efficient LLM-Based Computer Use Agents

**Authors**: Danylo Vorvul, Andrii P. Musienko, Iryna Galchenko, Mykola Myroniuk, Андрій Собчук | **Year**: 2026 | **Cited by**: 0 | **Kind**: article | **Relevance**: agents: core

## Abstract

Large language model (LLM)-driven computer use agents (CUAs) automate graphical user interface (GUI) tasks but often re-solve previously encountered subtasks, increasing token use and latency. We address this limitation with a directed graph-based persistent memory in which nodes represent observable GUI states and edges encode executable action sequences. We formalize the memory-augmented agent as S=⟨A,Σ,G,δ,π,Φ⟩, define task reachability and memory-coverage conditions inspired by functional stability theory, and derive token-cost efficiency bounds. In control-theoretic terms, the Manager–Worker architecture can be interpreted as a closed-loop system where memory provides experience-based feedback; this interpretation is used as an analogy rather than a full model-reference adaptive control proof. Experiments on OSWorld show that the proposed agent cuts both the LLM token consumption and execution time by about 50% versus a memoryless baseline while preserving comparable success rates (≈36.9% on 15-step and ≈46.9% on 50-step tasks). The demonstrated contribution is therefore operational efficiency through reusable graph memory, not a claim of improved task success or classical Lyapunov stability.
