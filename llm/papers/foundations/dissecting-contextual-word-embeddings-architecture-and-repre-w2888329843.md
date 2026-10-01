---
title: "Dissecting Contextual Word Embeddings: Architecture and Representation"
authors: ["Matthew E. Peters", "Mark Neumann", "Luke Zettlemoyer", "Wen-tau Yih"]
year: 2018
cited_by_count: 445
doi: "https://doi.org/10.18653/v1/d18-1179"
openalex_id: W2888329843
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Dissecting Contextual Word Embeddings: Architecture and Representation

**Authors**: Matthew E. Peters, Mark Neumann, Luke Zettlemoyer, Wen-tau Yih | **Year**: 2018 | **Cited by**: 445 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Contextual word representations derived from pre-trained bidirectional language models (biLMs) have recently been shown to provide significant improvements to the state of the art for a wide range of NLP tasks.However, many questions remain as to how and why these models are so effective.In this paper, we present a detailed empirical study of how the choice of neural architecture (e.g.LSTM, CNN, or self attention) influences both end task accuracy and qualitative properties of the representations that are learned.We show there is a tradeoff between speed and accuracy, but all architectures learn high quality contextual representations that outperform word embeddings for four challenging NLP tasks.Additionally, all architectures learn representations that vary with network depth, from exclusively morphological based at the word embedding layer through local syntax based in the lower contextual layers to longer range semantics such coreference at the upper layers.Together, these results suggest that unsupervised biLMs, independent of architecture, are learning much more about the structure of language than previously appreciated.
