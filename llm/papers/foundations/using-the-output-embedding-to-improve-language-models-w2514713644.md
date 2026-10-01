---
title: "Using the Output Embedding to Improve Language Models"
authors: ["Ofir Press", "Lior Wolf"]
year: 2017
cited_by_count: 652
doi: "https://doi.org/10.18653/v1/e17-2025"
openalex_id: W2514713644
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Using the Output Embedding to Improve Language Models

**Authors**: Ofir Press, Lior Wolf | **Year**: 2017 | **Cited by**: 652 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

We study the topmost weight matrix of neural network language models.We show that this matrix constitutes a valid word embedding.When training language models, we recommend tying the input embedding and this output embedding.We analyze the resulting update rules and show that the tied embedding evolves in a more similar way to the output embedding than to the input embedding in the untied model.We also offer a new method of regularizing the output embedding.Our methods lead to a significant reduction in perplexity, as we are able to show on a variety of neural network language models.Finally, we show that weight tying can reduce the size of neural translation models to less than half of their original size without harming their performance.
