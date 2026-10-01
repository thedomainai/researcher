---
title: "RoFormer: Enhanced transformer with Rotary Position Embedding"
authors: ["Jianlin Su", "Murtadha Ahmed", "Yu Lu", "Shengfeng Pan", "Bo Wen", "Yunfeng Liu"]
year: 2023
cited_by_count: 1682
doi: "https://doi.org/10.1016/j.neucom.2023.127063"
openalex_id: W4388979610
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: true
abstract_source: "semantic_scholar"
---

# RoFormer: Enhanced transformer with Rotary Position Embedding

**Authors**: Jianlin Su, Murtadha Ahmed, Yu Lu, Shengfeng Pan, Bo Wen, Yunfeng Liu | **Year**: 2023 | **Cited by**: 1682 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Position encoding recently has shown effective in the transformer architecture. It enables valuable supervision for dependency modeling between elements at different positions of the sequence. In this paper, we first investigate various methods to integrate positional information into the learning process of transformer-based language models. Then, we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information. Specifically, the proposed RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. Notably, RoPE enables valuable properties, including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding. Finally, we evaluate the enhanced transformer with rotary position embedding, also called RoFormer, on various long text classification benchmark datasets. Our experiments show that it consistently overcomes its alternatives. Furthermore, we provide a theoretical analysis to explain some experimental results. RoFormer is already integrated into Huggingface: \url{https://huggingface.co/docs/transformers/model_doc/roformer}.
