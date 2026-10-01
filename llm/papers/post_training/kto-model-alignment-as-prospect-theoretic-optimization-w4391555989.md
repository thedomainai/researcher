---
title: "KTO: Model Alignment as Prospect Theoretic Optimization"
authors: ["Kawin Ethayarajh", "Winnie Xu", "Niklas Muennighoff", "Dan Jurafsky", "Douwe Kiela"]
year: 2024
cited_by_count: 23
doi: "https://doi.org/10.48550/arxiv.2402.01306"
openalex_id: W4391555989
paper_type: preprint
evidence_kind: article
topics: ["post_training"]
landmark: true
abstract_source: "openalex"
---

# KTO: Model Alignment as Prospect Theoretic Optimization

**Authors**: Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, Douwe Kiela | **Year**: 2024 | **Cited by**: 23 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Kahneman & Tversky's $\textit{prospect theory}$ tells us that humans perceive random variables in a biased but well-defined manner (1992); for example, humans are famously loss-averse. We show that objectives for aligning LLMs with human feedback implicitly incorporate many of these biases -- the success of these objectives (e.g., DPO) over cross-entropy minimization can partly be ascribed to them belonging to a family of loss functions that we call $\textit{human-aware losses}$ (HALOs). However, the utility functions these methods attribute to humans still differ from those in the prospect theory literature. Using a Kahneman-Tversky model of human utility, we propose a HALO that directly maximizes the utility of generations instead of maximizing the log-likelihood of preferences, as current methods do. We call this approach KTO, and it matches or exceeds the performance of preference-based methods at scales from 1B to 30B, despite only learning from a binary signal of whether an output is desirable. More broadly, our work suggests that there is no one HALO that is universally superior; the best loss depends on the inductive biases most appropriate for a given setting, an oft-overlooked consideration.
