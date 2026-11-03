---
title: "LSF-SR: Latent Semantic Fusion for Sequential Recommendation via Flow-based Conditional Variational Autoencoders"
authors: "Shih-Hong Chen, Josh Jia-Ching Ying, Vincent Shin-Mu Tseng"
year: 2026
citations: 0
paper_type: "primary"
domain: "strategic_management"
fetched: "2026-11-04T06:53:17.765206"
doi: "https://doi.org/10.1145/3799682.3841099"
openalex_id: "https://openalex.org/W7214389273"
source_api: "openalex"
---

# LSF-SR: Latent Semantic Fusion for Sequential Recommendation via Flow-based Conditional Variational Autoencoders

**著者**: Shih-Hong Chen, Josh Jia-Ching Ying, Vincent Shin-Mu Tseng
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 経営戦略

## Abstract

Sequential recommendation aims to predict users' future interests from their historical interactions. Although Large Language Models (LLMs) capture rich item semantics, existing methods often struggle to align collaborative signals with textual semantic knowledge. As a result, the learned item representations fail to capture the complementary strengths of both signals, leading to suboptimal recommendation quality. To address this limitation, we propose Latent Semantic Fusion for Sequential Recommendation via Flow-based Conditional Variational Autoencoders (LSF-SR), a novel framework that uses a Conditional Variational Autoencoder (CVAE) with Normalizing Flows to fuse item ID embeddings and LLM-generated semantic signals. At the core of LSF-SR is a conditional fusion module augmented with planar or radial flows. This module learns a flexible latent space that encourages items with similar semantic profiles to cluster together within the latent manifold. Through extensive experiments on five public benchmark datasets, we demonstrate that LSF-SR consistently outperforms state-of-the-art baselines, achieving gains of up to 12.98% and 14.13% in Recall@20 and NDCG@20, respectively.
