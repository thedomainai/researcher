---
title: "A unified architecture for natural language processing"
authors: ["Ronan Collobert", "Jason Weston"]
year: 2008
cited_by_count: 5241
doi: "https://doi.org/10.1145/1390156.1390177"
openalex_id: W2117130368
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# A unified architecture for natural language processing

**Authors**: Ronan Collobert, Jason Weston | **Year**: 2008 | **Cited by**: 5241 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

We describe a single convolutional neural network architecture that, given a sentence, outputs a host of language processing predictions: part-of-speech tags, chunks, named entity tags, semantic roles, semantically similar words and the likelihood that the sentence makes sense (grammatically and semantically) using a language model. The entire network is trained jointly on all these tasks using weight-sharing, an instance of multitask learning. All the tasks use labeled data except the language model which is learnt from unlabeled text and represents a novel form of semi-supervised learning for the shared tasks. We show how both multitask learning and semi-supervised learning improve the generalization of the shared tasks, resulting in state-of-the-art-performance.
