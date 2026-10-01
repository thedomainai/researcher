---
title: "XLNet: Generalized Autoregressive Pretraining for Language Understanding"
authors: ["Zhilin Yang", "Dai, Zihang", "Yiming Yang", "Jaime Carbonell", "Ruslan Salakhutdinov", "Quoc Viet Le"]
year: 2019
cited_by_count: 1824
doi: "https://doi.org/10.48550/arxiv.1906.08237"
openalex_id: W2950813464
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# XLNet: Generalized Autoregressive Pretraining for Language Understanding

**Authors**: Zhilin Yang, Dai, Zihang, Yiming Yang, Jaime Carbonell, Ruslan Salakhutdinov, Quoc Viet Le | **Year**: 2019 | **Cited by**: 1824 | **Kind**: article | **Relevance**: foundations: core

## Abstract

With the capability of modeling bidirectional contexts, denoising autoencoding based pretraining like BERT achieves better performance than pretraining approaches based on autoregressive language modeling. However, relying on corrupting the input with masks, BERT neglects dependency between the masked positions and suffers from a pretrain-finetune discrepancy. In light of these pros and cons, we propose XLNet, a generalized autoregressive pretraining method that (1) enables learning bidirectional contexts by maximizing the expected likelihood over all permutations of the factorization order and (2) overcomes the limitations of BERT thanks to its autoregressive formulation. Furthermore, XLNet integrates ideas from Transformer-XL, the state-of-the-art autoregressive model, into pretraining. Empirically, under comparable experiment settings, XLNet outperforms BERT on 20 tasks, often by a large margin, including question answering, natural language inference, sentiment analysis, and document ranking.
