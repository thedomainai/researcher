---
title: "SIMPLE SPECTRAL GRAPH CONVOLUTION"
authors: "Hao Zhu, Piotr Koniusz"
year: 2026
citations: 81
paper_type: "primary"
domain: "operations_research"
fetched: "2026-08-24T18:51:04.003576"
doi: "https://doi.org/10.26190/unsworks/32608"
openalex_id: "https://openalex.org/W3124006607"
source_api: "openalex"
---

# SIMPLE SPECTRAL GRAPH CONVOLUTION

**著者**: Hao Zhu, Piotr Koniusz
**年**: 2026 | **被引用数**: 81
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Graph Convolutional Networks (GCNs) are leading methods for learning graph representations. However, without specially designed architectures, the performance of GCNs degrades quickly with increased depth. As the aggregated neighborhood size and neural network depth are two completely orthogonal aspects of graph representation, several methods focus on summarizing the neighborhood by aggregating K-hop neighborhoods of nodes while using shallow neural networks. However, these methods still encounter oversmoothing, and suffer from high computation and storage costs. In this paper, we use a modified Markov Diffusion Kernel to derive a variant of GCN called Simple Spectral Graph Convolution (S2GC). Our spectral analysis shows that our simple spectral graph convolution used in S2GC is a trade-off of low- and high-pass filter bands which capture the global and local contexts of each node. We provide two theoretical claims which demonstrate that we can aggregate over a sequence of increasingly larger neighborhoods compared to competitors while limiting severe oversmoothing. Our experimental evaluations show that S2GC with a linear learner is competitive in text and node classification tasks. Moreover, S2GC is comparable to other state-of-the-art methods for node clustering and community prediction tasks.
