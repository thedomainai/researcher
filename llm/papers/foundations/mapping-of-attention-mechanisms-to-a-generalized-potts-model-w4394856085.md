---
title: "Mapping of attention mechanisms to a generalized Potts model"
authors: ["Riccardo Rende", "Federica Gerace", "Alessandro Laio", "Sebastian Goldt"]
year: 2024
cited_by_count: 33
doi: "https://doi.org/10.1103/physrevresearch.6.023057"
openalex_id: W4394856085
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Mapping of attention mechanisms to a generalized Potts model

**Authors**: Riccardo Rende, Federica Gerace, Alessandro Laio, Sebastian Goldt | **Year**: 2024 | **Cited by**: 33 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Transformers are neural networks that revolutionized natural language processing and machine learning. They process sequences of inputs, like words, using a mechanism called self-attention, which is trained via masked language modeling (MLM). In MLM, a word is randomly masked in an input sequence, and the network is trained to predict the missing word. Despite the practical success of transformers, it remains unclear what type of data distribution self-attention can learn efficiently. Here, we show analytically that if one decouples the treatment of word positions and embeddings, a single layer of self-attention learns the conditionals of a generalized Potts model with interactions between sites and Potts colors. Moreover, we show that training this neural network is exactly equivalent to solving the inverse Potts problem by the so-called pseudolikelihood method, well known in statistical physics. Using this mapping, we compute the generalization error of self-attention in a model scenario analytically using the replica method. Published by the American Physical Society 2024
