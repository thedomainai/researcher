---
title: "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned"
authors: ["Elena Voita", "David Talbot", "Fedor Moiseev", "Rico Sennrich", "Ivan S. Titov"]
year: 2019
cited_by_count: 1097
doi: "https://doi.org/10.18653/v1/p19-1580"
openalex_id: W2946794439
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned

**Authors**: Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, Ivan S. Titov | **Year**: 2019 | **Cited by**: 1097 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Multi-head self-attention is a key component of the Transformer, a state-of-the-art architecture for neural machine translation.In this work we evaluate the contribution made by individual attention heads in the encoder to the overall performance of the model and analyze the roles played by them.We find that the most important and confident heads play consistent and often linguistically-interpretable roles.When pruning heads using a method based on stochastic gates and a differentiable relaxation of the L 0 penalty, we observe that specialized heads are last to be pruned.Our novel pruning method removes the vast majority of heads without seriously affecting performance.For example, on the English-Russian WMT dataset, pruning 38 out of 48 encoder heads results in a drop of only 0.15 BLEU. 1
