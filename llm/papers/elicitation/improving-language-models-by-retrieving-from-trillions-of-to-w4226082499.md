---
title: "Improving language models by retrieving from trillions of tokens"
authors: ["Sebastian Borgeaud", "Arthur Mensch", "Jordan Hoffmann", "Trevor Y. Cai", "Eliza Rutherford", "Katie Millican", "George van den Driessche", "Jean-Baptiste Lespiau", "et al."]
year: 2021
cited_by_count: 298
doi: "https://doi.org/10.48550/arxiv.2112.04426"
openalex_id: W4226082499
paper_type: preprint
evidence_kind: article
topics: ["elicitation"]
landmark: true
abstract_source: "openalex"
---

# Improving language models by retrieving from trillions of tokens

**Authors**: Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, Trevor Y. Cai, Eliza Rutherford, Katie Millican, George van den Driessche, Jean-Baptiste Lespiau, et al. | **Year**: 2021 | **Cited by**: 298 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

We enhance auto-regressive language models by conditioning on document chunks retrieved from a large corpus, based on local similarity with preceding tokens. With a $2$ trillion token database, our Retrieval-Enhanced Transformer (RETRO) obtains comparable performance to GPT-3 and Jurassic-1 on the Pile, despite using 25$\times$ fewer parameters. After fine-tuning, RETRO performance translates to downstream knowledge-intensive tasks such as question answering. RETRO combines a frozen Bert retriever, a differentiable encoder and a chunked cross-attention mechanism to predict tokens based on an order of magnitude more data than what is typically consumed during training. We typically train RETRO from scratch, yet can also rapidly RETROfit pre-trained transformers with retrieval and still achieve good performance. Our work opens up new avenues for improving language models through explicit memory at unprecedented scale.
