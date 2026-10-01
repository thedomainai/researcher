---
title: "Effective Approaches to Attention-based Neural Machine Translation"
authors: ["Thang Luong", "Hieu T. T. L. Pham", "Christopher D. Manning"]
year: 2015
cited_by_count: 8624
doi: "https://doi.org/10.18653/v1/d15-1166"
openalex_id: W1902237438
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Effective Approaches to Attention-based Neural Machine Translation

**Authors**: Thang Luong, Hieu T. T. L. Pham, Christopher D. Manning | **Year**: 2015 | **Cited by**: 8624 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

An attentional mechanism has lately been used to improve neural machine translation (NMT) by selectively focusing on parts of the source sentence during translation.However, there has been little work exploring useful architectures for attention-based NMT.This paper examines two simple and effective classes of attentional mechanism: a global approach which always attends to all source words and a local one that only looks at a subset of source words at a time.We demonstrate the effectiveness of both approaches on the WMT translation tasks between English and German in both directions.With local attention, we achieve a significant gain of 5.0 BLEU points over non-attentional systems that already incorporate known techniques such as dropout.Our ensemble model using different attention architectures yields a new state-of-the-art result in the WMT'15 English to German translation task with 25.9 BLEU points, an improvement of 1.0 BLEU points over the existing best system backed by NMT and an n-gram reranker.1
