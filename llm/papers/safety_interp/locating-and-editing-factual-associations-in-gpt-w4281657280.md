---
title: "Locating and Editing Factual Associations in GPT"
authors: ["Meng, Kevin", "David Anthony Bau", "Alex Andonian", "Yonatan Belinkov"]
year: 2022
cited_by_count: 173
doi: "https://doi.org/10.48550/arxiv.2202.05262"
openalex_id: W4281657280
paper_type: preprint
evidence_kind: article
topics: ["safety_interp"]
landmark: true
abstract_source: "openalex"
---

# Locating and Editing Factual Associations in GPT

**Authors**: Meng, Kevin, David Anthony Bau, Alex Andonian, Yonatan Belinkov | **Year**: 2022 | **Cited by**: 173 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

We analyze the storage and recall of factual associations in autoregressive transformer language models, finding evidence that these associations correspond to localized, directly-editable computations. We first develop a causal intervention for identifying neuron activations that are decisive in a model's factual predictions. This reveals a distinct set of steps in middle-layer feed-forward modules that mediate factual predictions while processing subject tokens. To test our hypothesis that these computations correspond to factual association recall, we modify feed-forward weights to update specific factual associations using Rank-One Model Editing (ROME). We find that ROME is effective on a standard zero-shot relation extraction (zsRE) model-editing task, comparable to existing methods. To perform a more sensitive evaluation, we also evaluate ROME on a new dataset of counterfactual assertions, on which it simultaneously maintains both specificity and generalization, whereas other methods sacrifice one or another. Our results confirm an important role for mid-layer feed-forward modules in storing factual associations and suggest that direct manipulation of computational mechanisms may be a feasible approach for model editing. The code, dataset, visualizations, and an interactive demo notebook are available at https://rome.baulab.info/
