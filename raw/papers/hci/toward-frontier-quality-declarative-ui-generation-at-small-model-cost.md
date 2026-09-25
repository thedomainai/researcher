---
title: "Toward Frontier-Quality Declarative UI Generation at Small-Model Cost"
authors: "Yingxiang Yang, Weihang Xiao, Ben Bullough, Tushar Deshpande, Niresh Agarwal"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-09-05T06:03:10.648829"
arxiv_id: "http://arxiv.org/abs/2609.04184v1"
source_api: "arxiv"
categories: "cs.HC"
---

# Toward Frontier-Quality Declarative UI Generation at Small-Model Cost

**著者**: Yingxiang Yang, Weihang Xiao, Ben Bullough, Tushar Deshpande, Niresh Agarwal
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

Declarative UI protocols such as A2UI let applications generate interactive UIs by selecting pre-built components from a catalog and binding their props to application data, rather than emitting frontend code from scratch. This contract is attractive for production systems because of safety and consistency. An open question is: can low-latency and low-cost small models achieve the required quality for A2UI-based UI generation? To answer this, we systematically study three controllable design choices for catalog-conditioned A2UI generation: supervised fine-tuning (SFT) data construction method, model size, and component-catalog size. Across two React/TypeScript domains and four base checkpoints spanning two model families (Qwen 3.5 0.8B/2B/4B; SmolLM 3B), we find: (i) a 4B fine-tuned student recovers ~98% of teacher semantic quality and ~97% of teacher visual quality at more than an order of magnitude lower cost than frontier API calls; (ii) both augmented strategies (Perturbed-catalog and Constrained-GT) Pareto-dominate the unaugmented Full-catalog baseline, while specializing on different axes; (iii) even small models can handle and benefit from relatively large component catalog size. We distill these results into practitioner-facing trade-offs and deployment recommendations across the three design choices.
