---
title: "Semi-supervised Sequence Learning"
authors: ["Andrew M. Dai", "Quoc Viet Le"]
year: 2015
cited_by_count: 473
doi: "https://doi.org/10.48550/arxiv.1511.01432"
openalex_id: W2170973209
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Semi-supervised Sequence Learning

**Authors**: Andrew M. Dai, Quoc Viet Le | **Year**: 2015 | **Cited by**: 473 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

We present two approaches that use unlabeled data to improve sequence learning with recurrent networks. The first approach is to predict what comes next in a sequence, which is a conventional language model in natural language processing. The second approach is to use a sequence autoencoder, which reads the input sequence into a vector and predicts the input sequence again. These two algorithms can be used as a "pretraining" step for a later supervised sequence learning algorithm. In other words, the parameters obtained from the unsupervised step can be used as a starting point for other supervised training models. In our experiments, we find that long short term memory recurrent networks after being pretrained with the two approaches are more stable and generalize better. With pretraining, we are able to train long short term memory recurrent networks up to a few hundred timesteps, thereby achieving strong performance in many text classification tasks, such as IMDB, DBpedia and 20 Newsgroups.
