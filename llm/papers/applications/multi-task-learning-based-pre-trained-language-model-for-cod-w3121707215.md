---
title: "Multi-task learning based pre-trained language model for code completion"
authors: ["Fang Liu", "Ge Li", "Yunfei Zhao", "Zhi Gang Jin"]
year: 2020
cited_by_count: 161
doi: "https://doi.org/10.1145/3324884.3416591"
openalex_id: W3121707215
paper_type: conference-paper
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# Multi-task learning based pre-trained language model for code completion

**Authors**: Fang Liu, Ge Li, Yunfei Zhao, Zhi Gang Jin | **Year**: 2020 | **Cited by**: 161 | **Kind**: article | **Relevance**: applications: supporting

## Abstract

Code completion is one of the most useful features in the Integrated Development Environments (IDEs), which can accelerate software development by suggesting the next probable token based on the contextual code in real-time. Recent studies have shown that statistical language modeling techniques can improve the performance of code completion tools through learning from large-scale software repositories. However, these models suffer from two major drawbacks: a) Existing research uses static embeddings, which map a word to the same vector regardless of its context. The differences in the meaning of a token in varying contexts are lost when each token is associated with a single representation; b) Existing language model based code completion models perform poor on completing identifiers, and the type information of the identifiers is ignored in most of these models. To address these challenges, in this paper, we develop a multi-task learning based pre-trained language model for code understanding and code generation with a Transformer-based neural architecture. We pre-train it with hybrid objective functions that incorporate both code understanding and code generation tasks. Then we fine-tune the pre-trained model on code completion. During the completion, our model does not directly predict the next token. Instead, we adopt multi-task learning to predict the token and its type jointly and utilize the predicted type to assist the token prediction. Experiments results on two real-world datasets demonstrate the effectiveness of our model when compared with state-of-the-art methods.
