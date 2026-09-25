---
title: "Cyber-Financial Contagion: Modeling the Propagation of an AI Vendor Compromise Through the Banking System"
authors: "Alex Leytes"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-09-11T06:03:42.584012"
arxiv_id: "http://arxiv.org/abs/2609.10350v1"
source_api: "arxiv"
categories: "cs.AI, cs.CY, cs.LG"
---

# Cyber-Financial Contagion: Modeling the Propagation of an AI Vendor Compromise Through the Banking System

**著者**: Alex Leytes
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

The banking system now depends on a small set of shared artificial intelligence vendors for fraud screening, credit decisioning, anti-money-laundering triage, customer analytics, and internal decision support. This paper studies how a compromise inside one of those vendors can propagate along a chain of operational, informational, and financial linkages until it triggers losses that look, from the outside, like a classical banking crisis. We build a four-layer heterogeneous network that couples AI vendors, financial institutions, interbank exposures, and customer accounts, and we propose CFC-Prop, a stochastic epidemic-and-clearing model that runs on that network. On a synthetic dataset with 60 vendors, 220 banks, roughly 2,500 vendor-bank service edges, and 1,400 interbank exposures, CFC-Prop reproduces the heavy-tailed loss distributions and the sharp dependence on patch latency that are consistent with prior cyber-financial evidence. We also train an early-warning model, CFC-GNN, that uses vendor-side incident telemetry and graph structure to flag high-cascade-risk vendors before impact. Across four baselines the proposed model reaches AUROC 0.82 and AUPRC 0.60 while keeping calibration errors bounded. We release the full code, synthetic data, and reproducible scripts. The results argue that cyber concentration among AI vendors is a first-order financial-stability problem and give supervisors a concrete quantitative tool for reasoning about it.
