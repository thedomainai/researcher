---
title: "Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping"
authors: ["Jesse Dodge", "Gabriel Ilharco", "Roy Schwartz", "Ali Farhadi", "Hannaneh Hajishirzi", "Noah A. Smith"]
year: 2020
cited_by_count: 209
doi: "https://doi.org/10.48550/arxiv.2002.06305"
openalex_id: W3005700362
paper_type: preprint
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping

**Authors**: Jesse Dodge, Gabriel Ilharco, Roy Schwartz, Ali Farhadi, Hannaneh Hajishirzi, Noah A. Smith | **Year**: 2020 | **Cited by**: 209 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Fine-tuning pretrained contextual word embedding models to supervised downstream tasks has become commonplace in natural language processing. This process, however, is often brittle: even with the same hyperparameter values, distinct random seeds can lead to substantially different results. To better understand this phenomenon, we experiment with four datasets from the GLUE benchmark, fine-tuning BERT hundreds of times on each while varying only the random seeds. We find substantial performance increases compared to previously reported results, and we quantify how the performance of the best-found model varies as a function of the number of fine-tuning trials. Further, we examine two factors influenced by the choice of random seed: weight initialization and training data order. We find that both contribute comparably to the variance of out-of-sample performance, and that some weight initializations perform well across all tasks explored. On small datasets, we observe that many fine-tuning trials diverge part of the way through training, and we offer best practices for practitioners to stop training less promising runs early. We publicly release all of our experimental data, including training and validation scores for 2,100 trials, to encourage further analysis of training dynamics during fine-tuning.
