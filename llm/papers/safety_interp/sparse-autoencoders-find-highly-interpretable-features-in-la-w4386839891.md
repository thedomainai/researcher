---
title: "Sparse Autoencoders Find Highly Interpretable Features in Language Models"
authors: ["Hoagy Cunningham", "Aidan Ewart", "Logan Riggs", "Huben, Robert", "Lee Sharkey"]
year: 2023
cited_by_count: 53
doi: "https://doi.org/10.48550/arxiv.2309.08600"
openalex_id: W4386839891
paper_type: preprint
evidence_kind: article
topics: ["safety_interp"]
landmark: true
abstract_source: "openalex"
---

# Sparse Autoencoders Find Highly Interpretable Features in Language Models

**Authors**: Hoagy Cunningham, Aidan Ewart, Logan Riggs, Huben, Robert, Lee Sharkey | **Year**: 2023 | **Cited by**: 53 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

One of the roadblocks to a better understanding of neural networks' internals is \textit{polysemanticity}, where neurons appear to activate in multiple, semantically distinct contexts. Polysemanticity prevents us from identifying concise, human-understandable explanations for what neural networks are doing internally. One hypothesised cause of polysemanticity is \textit{superposition}, where neural networks represent more features than they have neurons by assigning features to an overcomplete set of directions in activation space, rather than to individual neurons. Here, we attempt to identify those directions, using sparse autoencoders to reconstruct the internal activations of a language model. These autoencoders learn sets of sparsely activating features that are more interpretable and monosemantic than directions identified by alternative approaches, where interpretability is measured by automated methods. Moreover, we show that with our learned set of features, we can pinpoint the features that are causally responsible for counterfactual behaviour on the indirect object identification task \citep{wang2022interpretability} to a finer degree than previous decompositions. This work indicates that it is possible to resolve superposition in language models using a scalable, unsupervised method. Our method may serve as a foundation for future mechanistic interpretability work, which we hope will enable greater model transparency and steerability.
