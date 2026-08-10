---
title: "DevoTG: Temporal Graph Neural Networks for Modeling C. elegans Developmental Connectomics"
authors: "Jayadratha Gayen, Bradly Alicea"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-06-26T06:00:24.936654"
arxiv_id: "http://arxiv.org/abs/2606.21940v1"
source_api: "arxiv"
categories: "cs.LG, q-bio.NC"
---

# DevoTG: Temporal Graph Neural Networks for Modeling C. elegans Developmental Connectomics

**著者**: Jayadratha Gayen, Bradly Alicea
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Understanding how a nervous system wires itself from birth to adulthood is a fundamental challenge in developmental neuroscience. We present DevoTG, a temporal graph framework that applies Temporal Graph Neural Networks (TGNs) to two complementary representations of C. elegans neural development: a Continuous-Time Dynamic Graph (CTDG) of cell division events derived from cell lineage data, and a Discrete-Time Dynamic Graph (DTDG) of the developing synaptic connectome spanning eight reconstructed electron-microscopy datasets. On the lineage prediction task, our TGN achieves a mean test AUC of 0.839 +/- 0.007 (5 seeds; validation AUC 0.937 +/- 0.001), outperforming a static GNN with the identical architecture by 26 AUC points (0.577 +/- 0.080), demonstrating that temporal memory is the decisive factor. Applied to the connectome DTDG, DevoTG identifies three connection stability classes (stable, developmental, and variable) across 225 neurons and 858 to 2,496 connections over development (L1 birth to adult), providing a temporal-graph-theoretic complement to the individual-variability classification of Witvliet et al. Analysis of hub command interneurons AVA, AVB, and AVE reveals their persistent centrality and how their integration roles are progressively reinforced across larval stages. Accompanying interactive visualizations (3D animated networks, centrality heatmaps, and a spatiotemporal lineage graph) make developmental dynamics accessible for biological hypothesis generation. DevoTG is open-source and designed for extension to other developing nervous systems. Code is publicly available at https://github.com/DevoLearn/DevoGraph/tree/main/DevoTG.
