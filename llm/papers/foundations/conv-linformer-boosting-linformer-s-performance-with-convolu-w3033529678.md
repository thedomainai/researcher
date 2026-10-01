---
title: "Conv-Linformer: Boosting Linformer's Performance with Convolution in Small-Scale Settings"
authors: ["Sinong Wang", "Belinda Z. Li", "Madian Khabsa", "Fang, Han", "Hao Ma"]
year: 2020
cited_by_count: 870
doi: "https://doi.org/10.48550/arxiv.2006.04768"
openalex_id: W3033529678
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Conv-Linformer: Boosting Linformer's Performance with Convolution in Small-Scale Settings

**Authors**: Sinong Wang, Belinda Z. Li, Madian Khabsa, Fang, Han, Hao Ma | **Year**: 2020 | **Cited by**: 870 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Large transformer models have shown extraordinary success in achieving state-of-the-art results in many natural language processing applications. However, training and deploying these models can be prohibitively costly for long sequences, as the standard self-attention mechanism of the Transformer uses $O(n^2)$ time and space with respect to sequence length. In this paper, we demonstrate that the self-attention mechanism can be approximated by a low-rank matrix. We further exploit this finding to propose a new self-attention mechanism, which reduces the overall self-attention complexity from $O(n^2)$ to $O(n)$ in both time and space. The resulting linear transformer, the \textit{Linformer}, performs on par with standard Transformer models, while being much more memory- and time-efficient.
