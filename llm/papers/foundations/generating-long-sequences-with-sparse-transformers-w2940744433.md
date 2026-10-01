---
title: "Generating Long Sequences with Sparse Transformers"
authors: ["Rewon Child", "Scott Gray", "Alec Radford", "Ilya Sutskever"]
year: 2019
cited_by_count: 463
doi: "https://doi.org/10.48550/arxiv.1904.10509"
openalex_id: W2940744433
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Generating Long Sequences with Sparse Transformers

**Authors**: Rewon Child, Scott Gray, Alec Radford, Ilya Sutskever | **Year**: 2019 | **Cited by**: 463 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Transformers are powerful sequence models, but require time and memory that grows quadratically with the sequence length. In this paper we introduce sparse factorizations of the attention matrix which reduce this to $O(n \sqrt{n})$. We also introduce a) a variation on architecture and initialization to train deeper networks, b) the recomputation of attention matrices to save memory, and c) fast attention kernels for training. We call networks with these changes Sparse Transformers, and show they can model sequences tens of thousands of timesteps long using hundreds of layers. We use the same architecture to model images, audio, and text from raw bytes, setting a new state of the art for density modeling of Enwik8, CIFAR-10, and ImageNet-64. We generate unconditional samples that demonstrate global coherence and great diversity, and show it is possible in principle to use self-attention to model sequences of length one million or more.
