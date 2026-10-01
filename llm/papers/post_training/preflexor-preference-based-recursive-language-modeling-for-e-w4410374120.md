---
title: "PRefLexOR: preference-based recursive language modeling for exploratory optimization of reasoning and agentic thinking"
authors: ["Markus J. Buehler"]
year: 2025
cited_by_count: 24
doi: "https://doi.org/10.1038/s44387-025-00003-z"
openalex_id: W4410374120
paper_type: article
evidence_kind: article
topics: ["post_training", "agents"]
landmark: false
abstract_source: "openalex"
---

# PRefLexOR: preference-based recursive language modeling for exploratory optimization of reasoning and agentic thinking

**Authors**: Markus J. Buehler | **Year**: 2025 | **Cited by**: 24 | **Kind**: article | **Relevance**: post_training: core; agents: supporting

## Abstract

We introduce PRefLexOR (Preference-based Recursive Language Modeling for Exploratory Optimization of Reasoning), a framework that integrates preference optimization with reinforcement learning (RL) concepts for self-improving scientific reasoning. PRefLexOR employs a recursive approach, refining intermediate steps before producing final outputs in training and inference. It optimizes log odds between preferred and non-preferred responses using an in-situ dataset generation algorithm. A dynamic knowledge graph contextualizes reasoning with retrieval-augmented data. Preference optimization enhances performance via rejection sampling, masking reasoning steps to focus on discovery. Recursive optimization, guided by feedback loops, refines reasoning. This process mirrors biological adaptation, enabling real-time learning. We find that even small models (3B parameters) self-teach deeper reasoning, solving open-domain problems effectively. Our method integrates into existing LLMs and demonstrates success in biological materials science, leveraging multi-agent self-improvement for enhanced reasoning depth and cross-domain adaptability, offering flexibility and integration into larger agentic systems.
