---
title: "Orthogonal Subspace Learning for Language Model Continual Learning"
authors: ["Xiao Wang", "Tianze Chen", "Qiming Ge", "Xia Han", "Rong Bao", "Rui Zheng", "Qi Zhang", "Tao Gui", "et al."]
year: 2023
cited_by_count: 71
doi: "https://doi.org/10.18653/v1/2023.findings-emnlp.715"
openalex_id: W4389520299
paper_type: conference-paper
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Orthogonal Subspace Learning for Language Model Continual Learning

**Authors**: Xiao Wang, Tianze Chen, Qiming Ge, Xia Han, Rong Bao, Rui Zheng, Qi Zhang, Tao Gui, et al. | **Year**: 2023 | **Cited by**: 71 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Benefiting from massive corpora and advanced hardware, large language models (LLMs) exhibit remarkable capabilities in language understanding and generation.However, their performance degrades in scenarios where multiple tasks are encountered sequentially, also known as catastrophic forgetting.In this paper, we propose orthogonal low-rank adaptation (O-LoRA), a simple and efficient approach for continual learning in language models, effectively mitigating catastrophic forgetting while learning new tasks.Specifically, O-LoRA learns tasks in different (low-rank) vector subspaces that are kept orthogonal to each other in order to minimize interference.Our method induces only marginal additional parameter costs and requires no user data storage for replay.Experimental results on continual learning benchmarks show that our method outperforms state-of-the-art methods.Furthermore, compared to previous approaches, our method excels in preserving the generalization ability of LLMs on unseen tasks.
