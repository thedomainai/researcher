---
title: "Transformer-XL: Attentive Language Models beyond a Fixed-Length Context"
authors: ["Zihang Dai", "Zhilin Yang", "Yiming Yang", "Jaime Carbonell", "Quoc Viet Le", "Ruslan Salakhutdinov"]
year: 2019
cited_by_count: 3220
doi: "https://doi.org/10.18653/v1/p19-1285"
openalex_id: W2964110616
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Transformer-XL: Attentive Language Models beyond a Fixed-Length Context

**Authors**: Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc Viet Le, Ruslan Salakhutdinov | **Year**: 2019 | **Cited by**: 3220 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Transformers have a potential of learning longer-term dependency, but are limited by a fixed-length context in the setting of language modeling.We propose a novel neural architecture Transformer-XL that enables learning dependency beyond a fixed length without disrupting temporal coherence.It consists of a segment-level recurrence mechanism and a novel positional encoding scheme.Our method not only enables capturing longer-term dependency, but also resolves the context fragmentation problem.As a result, Transformer-XL learns dependency that is 80% longer than RNNs and 450% longer than vanilla Transformers, achieves better performance on both short and long sequences, and is up to 1,800+ times faster than vanilla Transformers during evaluation.Notably, we improve the state-ofthe-art results of bpc/perplexity to 0.99 on en-wiki8, 1.08 on text8, 18.3 on WikiText-103, 21.8 on One Billion Word, and 54.5 on Penn Treebank (without finetuning).When trained only on WikiText-103, Transformer-XL manages to generate reasonably coherent, novel text articles with thousands of tokens.Our code, pretrained models, and hyperparameters are available in both Tensorflow and PyTorch 1 .
