---
title: "Entity-Based Knowledge Conflicts in Question Answering"
authors: ["Shayne Longpre", "Kartik Perisetla", "Anthony Chen", "Nikhil Ramesh", "Chris DuBois", "Sameer Kumar Singh"]
year: 2021
cited_by_count: 94
doi: "https://doi.org/10.18653/v1/2021.emnlp-main.565"
openalex_id: W3199011812
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Entity-Based Knowledge Conflicts in Question Answering

**Authors**: Shayne Longpre, Kartik Perisetla, Anthony Chen, Nikhil Ramesh, Chris DuBois, Sameer Kumar Singh | **Year**: 2021 | **Cited by**: 94 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Knowledge-dependent tasks typically use two sources of knowledge: parametric, learned at training time, and contextual, given as a passage at inference time.To understand how models use these sources together, we formalize the problem of knowledge conflicts, where the contextual information contradicts the learned information.Analyzing the behaviour of popular models, we measure their over-reliance on memorized information (the cause of hallucinations), and uncover important factors that exacerbate this behaviour.Lastly, we propose a simple method to mitigate over-reliance on parametric knowledge which minimizes hallucination and improves out-of-distribution generalization by 4% -7%.Our findings demonstrate the importance for practitioners to evaluate model tendency to hallucinate rather than read, and show that our mitigation strategy encourages generalization to evolving information (i.e., time-dependent queries).To encourage these practices, we have released our framework for generating knowledge conflicts.1
