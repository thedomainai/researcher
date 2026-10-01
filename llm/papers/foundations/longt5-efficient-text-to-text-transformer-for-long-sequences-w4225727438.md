---
title: "LongT5: Efficient Text-To-Text Transformer for Long Sequences"
authors: ["Mandy Guo", "Joshua Ainslie", "David Uthus", "Santiago Ontañón", "Jianmo Ni", "Yun-Hsuan Sung", "Yinfei Yang"]
year: 2022
cited_by_count: 220
doi: "https://doi.org/10.18653/v1/2022.findings-naacl.55"
openalex_id: W4225727438
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# LongT5: Efficient Text-To-Text Transformer for Long Sequences

**Authors**: Mandy Guo, Joshua Ainslie, David Uthus, Santiago Ontañón, Jianmo Ni, Yun-Hsuan Sung, Yinfei Yang | **Year**: 2022 | **Cited by**: 220 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Recent work has shown that either (1) increasing the input length or (2) increasing model size can improve the performance of Transformer-based neural models.In this paper, we present LongT5, a new model that explores the effects of scaling both the input length and model size at the same time.Specifically, we integrate attention ideas from long-input transformers (ETC), and adopt pretraining strategies from summarization pretraining (PEGASUS) into the scalable T5 architecture.The result is a new attention mechanism we call Transient Global (TGlobal), which mimics ETC's local/global attention mechanism, but without requiring additional side-inputs.We are able to achieve state-ofthe-art results on several summarization and question answering tasks, as well as outperform the original T5 models on these tasks.We have open sourced our architecture and training code, as well as our pre-trained model checkpoints.
