---
title: "Decoupled Weight Decay Regularization"
authors: ["Ilya Loshchilov", "Frank Hutter"]
year: 2017
cited_by_count: 9419
doi: "https://doi.org/10.48550/arxiv.1711.05101"
openalex_id: W2908510526
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# Decoupled Weight Decay Regularization

**Authors**: Ilya Loshchilov, Frank Hutter | **Year**: 2017 | **Cited by**: 9419 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

L$_2$ regularization and weight decay regularization are equivalent for standard stochastic gradient descent (when rescaled by the learning rate), but as we demonstrate this is \emph{not} the case for adaptive gradient algorithms, such as Adam. While common implementations of these algorithms employ L$_2$ regularization (often calling it "weight decay" in what may be misleading due to the inequivalence we expose), we propose a simple modification to recover the original formulation of weight decay regularization by \emph{decoupling} the weight decay from the optimization steps taken w.r.t. the loss function. We provide empirical evidence that our proposed modification (i) decouples the optimal choice of weight decay factor from the setting of the learning rate for both standard SGD and Adam and (ii) substantially improves Adam's generalization performance, allowing it to compete with SGD with momentum on image classification datasets (on which it was previously typically outperformed by the latter). Our proposed decoupled weight decay has already been adopted by many researchers, and the community has implemented it in TensorFlow and PyTorch; the complete source code for our experiments is available at https://github.com/loshchil/AdamW-and-SGDW
