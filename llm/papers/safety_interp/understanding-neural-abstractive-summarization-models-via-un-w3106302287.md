---
title: "Understanding Neural Abstractive Summarization Models via Uncertainty"
authors: ["Jiacheng Xu", "Shrey Desai", "Greg Durrett"]
year: 2020
cited_by_count: 38
doi: "https://doi.org/10.18653/v1/2020.emnlp-main.508"
openalex_id: W3106302287
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Understanding Neural Abstractive Summarization Models via Uncertainty

**Authors**: Jiacheng Xu, Shrey Desai, Greg Durrett | **Year**: 2020 | **Cited by**: 38 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

An advantage of seq2seq abstractive summarization models is that they generate text in a free-form manner, but this flexibility makes it difficult to interpret model behavior.In this work, we analyze summarization decoders in both blackbox and whitebox ways by studying on the entropy, or uncertainty, of the model's token-level predictions.For two strong pretrained models, PEGASUS (Zhang et al., 2020) and BART (Lewis et al., 2020) on two summarization datasets, we find a strong correlation between low prediction entropy and where the model copies tokens rather than generating novel text.The decoder's uncertainty also connects to factors like sentence position and syntactic distance between adjacent pairs of tokens, giving a sense of what factors make a context particularly selective for the model's next output token.Finally, we study the relationship of decoder uncertainty and attention behavior to understand how attention gives rise to these observed effects in the model.We show that uncertainty is a useful perspective for analyzing summarization and text generation models more broadly.1
