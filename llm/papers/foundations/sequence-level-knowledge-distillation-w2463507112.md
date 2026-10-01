---
title: "Sequence-Level Knowledge Distillation"
authors: ["Yoon Kim", "Alexander M. Rush"]
year: 2016
cited_by_count: 110
doi: "https://doi.org/10.48550/arxiv.1606.07947"
openalex_id: W2463507112
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Sequence-Level Knowledge Distillation

**Authors**: Yoon Kim, Alexander M. Rush | **Year**: 2016 | **Cited by**: 110 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Neural machine translation (NMT) offers a novel alternative formulation of translation that is potentially simpler than statistical approaches. However to reach competitive performance, NMT models need to be exceedingly large. In this paper we consider applying knowledge distillation approaches (Bucila et al., 2006; Hinton et al., 2015) that have proven successful for reducing the size of neural models in other domains to the problem of NMT. We demonstrate that standard knowledge distillation applied to word-level prediction can be effective for NMT, and also introduce two novel sequence-level versions of knowledge distillation that further improve performance, and somewhat surprisingly, seem to eliminate the need for beam search (even when applied on the original teacher model). Our best student model runs 10 times faster than its state-of-the-art teacher with little loss in performance. It is also significantly better than a baseline model trained without knowledge distillation: by 4.2/1.7 BLEU with greedy decoding/beam search. Applying weight pruning on top of knowledge distillation results in a student model that has 13 times fewer parameters than the original teacher model, with a decrease of 0.4 BLEU.
