---
title: "GraphFAS: A Distributed System for Automated Graph Feature Generation and Selection in Industrial Transaction Networks"
authors: "Yice Luo, Yun Zhu, Xi Chen, Yongchao Liu, Xintan Zeng"
year: 2026
citations: 0
paper_type: "primary"
domain: "systems_engineering"
fetched: "2026-11-04T06:33:47.371803"
doi: "https://doi.org/10.1145/3799682.3840143"
openalex_id: "https://openalex.org/W7211989697"
source_api: "openalex"
---

# GraphFAS: A Distributed System for Automated Graph Feature Generation and Selection in Industrial Transaction Networks

**著者**: Yice Luo, Yun Zhu, Xi Chen, Yongchao Liu, Xintan Zeng
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: システム工学

## Abstract

Industrial fraud detection often relies on costly expert-crafted features that overlook graph-structured relational signals, while GNNs often do not meet the interpretability and deployment requirements of financial risk control. We propose GraphFAS (Graph Feature Automated Selection), a distributed feature selection procedure based on Boruta that bridges this gap through: (1) a non-parametric graph feature generation module that constructs explicit, interpretable structural features via multi-hop subgraph extraction and multi-scale aggregation without learned parameters; and (2) an automated distributed feature selection algorithm extending Boruta with median-based aggregation across partitions to robustly identify informative features at scale with minimal domain expertise. Compared with end-to-end GNN pipelines, GraphFAS decouples feature aggregation from model training, enabling direct integration with tabular models and direct compatibility with TreeSHAPbased explanations. Deployed in Alipay, GraphFAS delivers orderof-magnitude improvements in engineering efficiency while showing strong performance against expert-driven and graph-learning baselines on large-scale graphs.
