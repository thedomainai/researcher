---
title: "Generating Wikipedia by Summarizing Long Sequences"
authors: ["Peter J. Liu", "Saleh, Mohammad", "Etienne Pot", "Ben Goodrich", "Ryan Sepassi", "Łukasz Kaiser", "Noam Shazeer"]
year: 2018
cited_by_count: 74
doi: "https://doi.org/10.48550/arxiv.1801.10198"
openalex_id: W2787214294
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Generating Wikipedia by Summarizing Long Sequences

**Authors**: Peter J. Liu, Saleh, Mohammad, Etienne Pot, Ben Goodrich, Ryan Sepassi, Łukasz Kaiser, Noam Shazeer | **Year**: 2018 | **Cited by**: 74 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

We show that generating English Wikipedia articles can be approached as a multi- document summarization of source documents. We use extractive summarization to coarsely identify salient information and a neural abstractive model to generate the article. For the abstractive model, we introduce a decoder-only architecture that can scalably attend to very long sequences, much longer than typical encoder- decoder architectures used in sequence transduction. We show that this model can generate fluent, coherent multi-sentence paragraphs and even whole Wikipedia articles. When given reference documents, we show it can extract relevant factual information as reflected in perplexity, ROUGE scores and human evaluations.
