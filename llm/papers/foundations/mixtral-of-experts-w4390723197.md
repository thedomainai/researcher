---
title: "Mixtral of Experts"
authors: ["Albert Qiaochu Jiang", "Alexandre Sablayrolles", "Antoine Roux", "Arthur Mensch", "Blanche Savary", "Chris Bamford", "Devendra Singh Chaplot", "Diego de Las Casas", "et al."]
year: 2024
cited_by_count: 143
doi: "https://doi.org/10.48550/arxiv.2401.04088"
openalex_id: W4390723197
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: true
abstract_source: "openalex"
---

# Mixtral of Experts

**Authors**: Albert Qiaochu Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de Las Casas, et al. | **Year**: 2024 | **Cited by**: 143 | **Kind**: article | **Relevance**: foundations: core

## Abstract

We introduce Mixtral 8x7B, a Sparse Mixture of Experts (SMoE) language model. Mixtral has the same architecture as Mistral 7B, with the difference that each layer is composed of 8 feedforward blocks (i.e. experts). For every token, at each layer, a router network selects two experts to process the current state and combine their outputs. Even though each token only sees two experts, the selected experts can be different at each timestep. As a result, each token has access to 47B parameters, but only uses 13B active parameters during inference. Mixtral was trained with a context size of 32k tokens and it outperforms or matches Llama 2 70B and GPT-3.5 across all evaluated benchmarks. In particular, Mixtral vastly outperforms Llama 2 70B on mathematics, code generation, and multilingual benchmarks. We also provide a model fine-tuned to follow instructions, Mixtral 8x7B - Instruct, that surpasses GPT-3.5 Turbo, Claude-2.1, Gemini Pro, and Llama 2 70B - chat model on human benchmarks. Both the base and instruct models are released under the Apache 2.0 license.
