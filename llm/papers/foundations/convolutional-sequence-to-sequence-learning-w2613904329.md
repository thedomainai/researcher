---
title: "Convolutional Sequence to Sequence Learning"
authors: ["Jonas Gehring", "Michael Auli", "David Grangier", "Denis Yarats", "Yann Dauphin"]
year: 2017
cited_by_count: 2607
doi: "https://doi.org/10.48550/arxiv.1705.03122"
openalex_id: W2613904329
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Convolutional Sequence to Sequence Learning

**Authors**: Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, Yann Dauphin | **Year**: 2017 | **Cited by**: 2607 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

The prevalent approach to sequence to sequence learning maps an input sequence to a variable length output sequence via recurrent neural networks. We introduce an architecture based entirely on convolutional neural networks. Compared to recurrent models, computations over all elements can be fully parallelized during training and optimization is easier since the number of non-linearities is fixed and independent of the input length. Our use of gated linear units eases gradient propagation and we equip each decoder layer with a separate attention module. We outperform the accuracy of the deep LSTM setup of Wu et al. (2016) on both WMT'14 English-German and WMT'14 English-French translation at an order of magnitude faster speed, both on GPU and CPU.
