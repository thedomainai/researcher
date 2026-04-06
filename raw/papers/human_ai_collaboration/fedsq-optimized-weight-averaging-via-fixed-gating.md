---
title: "FedSQ: Optimized Weight Averaging via Fixed Gating"
authors: "Cristian Pérez-Corral, Jose I. Mestre, Alberto Fernández-Hernández, Manuel F. Dolz, José Duato"
year: 2026
citations: 0
paper_type: "meta_analysis"
domain: "human_ai_collaboration"
fetched: "2026-04-06T13:21:07.595152"
arxiv_id: "http://arxiv.org/abs/2604.02990v1"
source_api: "arxiv"
categories: "cs.LG, cs.AI, cs.DC"
---

# FedSQ: Optimized Weight Averaging via Fixed Gating

**著者**: Cristian Pérez-Corral, Jose I. Mestre, Alberto Fernández-Hernández, Manuel F. Dolz, José Duato
**年**: 2026 | **被引用数**: 0
**タイプ**: meta_analysis | **分野**: 人間-AI協働

## Abstract

Federated learning (FL) enables collaborative training across organizations without sharing raw data, but it is hindered by statistical heterogeneity (non-i.i.d.\ client data) and by instability of naive weight averaging under client drift. In many cross-silo deployments, FL is warm-started from a strong pretrained backbone (e.g., ImageNet-1K) and then adapted to local domains. Motivated by recent evidence that ReLU-like gating regimes (structural knowledge) stabilize earlier than the remaining parameter values (quantitative knowledge), we propose FedSQ (Federated Structural-Quantitative learning), a transfer-initialized neural federated procedure based on a DualCopy, piecewise-linear view of deep networks. FedSQ freezes a structural copy of the pretrained model to induce fixed binary gating masks during federated fine-tuning, while only a quantitative copy is optimized locally and aggregated across rounds. Fixing the gating reduces learning to within-regime affine refinements, which stabilizes aggregation under heterogeneous partitions. Experiments on two convolutional neural network backbones under i.i.d.\ and Dirichlet splits show that FedSQ improves robustness and can reduce rounds-to-best validation performance relative to standard baselines while preserving accuracy in the transfer setting.
