---
title: "GradeSQL: Outcome reward models for intelligent Text-to-SQL generation from LLMs"
authors: ["Mattia Tritto", "Giuseppe Farano", "Dario Di Palma", "Gaetano Rossiello", "Dharmashankar Subramanian", "Fedelucio Narducci", "Tommaso Di Noia"]
year: 2026
cited_by_count: 1
doi: "https://doi.org/10.1007/s10844-026-01071-6"
openalex_id: W7167627726
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# GradeSQL: Outcome reward models for intelligent Text-to-SQL generation from LLMs

**Authors**: Mattia Tritto, Giuseppe Farano, Dario Di Palma, Gaetano Rossiello, Dharmashankar Subramanian, Fedelucio Narducci, Tommaso Di Noia | **Year**: 2026 | **Cited by**: 1 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Abstract As Large Language Models (LLMs) become foundational to next-generation Intelligent Information Systems, the bridge between natural language interfaces and structured database systems remains a critical bottleneck. While Text-to-SQL generation enables cooperative support for complex query formulation, ensuring the reliability of these generated queries at inference time is a central challenge. Conventional methods rely on coarse execution-based signals, which may limit their ability to capture the nuanced semantic alignment required for high-stakes database environments. In this work, we propose the use of Outcome Reward Models (ORMs) as a fine-grained, probabilistic feedback mechanism for test-time verification in Text-to-SQL tasks. We introduce GradeSQL, a framework for training task-specific ORMs that assign scalar utility scores to candidate SQL queries based on their semantic correctness and alignment with database schema. Our approach is evaluated on the BIRD and Spider benchmarks across multiple open-source LLM families. Experimental results demonstrate that ORM-based verification consistently outperforms traditional execution-based heuristics.
