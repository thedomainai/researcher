---
title: "Longformer: The Long-Document Transformer"
authors: ["Iz Beltagy", "Matthew E. Peters", "Arman Cohan"]
year: 2020
cited_by_count: 2182
doi: "https://doi.org/10.48550/arxiv.2004.05150"
openalex_id: W3015468748
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Longformer: The Long-Document Transformer

**Authors**: Iz Beltagy, Matthew E. Peters, Arman Cohan | **Year**: 2020 | **Cited by**: 2182 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

The quadratic complexity of standard attention (O(N²)) remains the dominant bottleneck for training and deploying large language models on long sequences. We introduce Murmurative Attention, a novel attention mechanism that replaces pairwise token-token interactions with token-to-slot interactions over a fixed-size learnable memory pool of M slots, achieving O(N·M) complexity with M ≪ N. The mechanism operates in four phases per round: (1) select — each token hard-selects the top-k relevant slots via dot-product similarity; (2) attend — tokens compute a standard softmax over their selected slots and aggregate their value vectors; (3) update — tokens write back to slots via an exponential moving average; and (4) diffuse — slots exchange information with their neighbors through a tridiagonal discrete Laplace stencil, enabling global information propagation across rounds. We prove that with M = 256 slots and R = 3 rounds, Murmurative Attention achieves identical language modeling perplexity to standard multi-head attention while consuming 4.4× fewer attention FLOPs at N=512 tokens, 10.1× fewer at N=4,096, and 20.2× fewer at N=8,192 — a gap that widens asymptotically. We implement efficient CUDA kernels including a WMMA tensor-core path, fuse the select-attend and update-diffuse operations into single GPU launches, and provide a full training benchmark comparing wall-clock time, memory, and perplexity-per-FLOP efficiency against standard attention and FlashAttention. Our results show that sub-quadratic attention can match the representational quality of full attention while dramatically reducing the computational cost of long-context training.
