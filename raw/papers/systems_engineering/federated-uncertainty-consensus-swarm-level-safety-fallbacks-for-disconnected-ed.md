---
title: "Federated Uncertainty Consensus: Swarm-Level Safety Fallbacks for Disconnected Edge AI"
authors: "Chidiebere Christopher"
year: 2026
citations: 0
paper_type: "primary"
domain: "systems_engineering"
fetched: "2026-09-03T06:05:24.000742"
doi: "https://doi.org/10.5281/zenodo.22235052"
openalex_id: "https://openalex.org/W7204905101"
source_api: "openalex"
---

# Federated Uncertainty Consensus: Swarm-Level Safety Fallbacks for Disconnected Edge AI

**著者**: Chidiebere Christopher
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: システム工学

## Abstract

Edge Artificial Intelligence (AI) is increasingly deployed in latency-critical and highly dynamic environments, such as autonomous Unmanned Aerial Vehicle (UAV) swarms and disaster response robotics [3, 9]. A critical vulnerability in these systems is data drift—where the operational environment deviates from the training distribution, leading to silent model degradation [1, 2]. Current safety fallback mechanisms rely on hierarchical cloud architectures, where an edge device defers ambiguous inferences to a central server [4]. However, this is structurally impossible in disconnected, cloud-denied, or strictly localized ad-hoc networks. In this paper, we propose Federated Uncertainty Consensus (FUC), a novel technical AI safety protocol. Rather than defaulting to a centralized cloud, an edge node utilizes local Uncertainty Quantification (UQ) via Conformal Prediction [5]. Upon detecting out-of-distribution (OOD) anomalies, the node broadcasts a lightweight peer-to-peer query to the local swarm. The swarm mathematically aggregates its confidence, achieving a "safety fallback consensus" to override the degraded node. We outline the decentralized architecture, provide empirical latency metrics from a simulated ad-hoc swarm, and demonstrate that FUC maintains real-time safety thresholds without reliance on cloud infrastructure [7, 8].
