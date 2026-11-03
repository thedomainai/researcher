---
title: "When Is Shallow Enough? Adaptive Split Federated Learning with Client-Specific Sufficiency Estimation"
authors: "Wenhao Yuan, Chenchen Lin, Wenhao Hu, Jian Chen, Jinfeng Xu"
year: 2026
citations: 0
paper_type: "meta_analysis"
domain: "neuroscience"
fetched: "2026-11-04T06:01:27.999194"
doi: "https://doi.org/10.1145/3799682.3840747"
openalex_id: "https://openalex.org/W7203666835"
source_api: "openalex"
---

# When Is Shallow Enough? Adaptive Split Federated Learning with Client-Specific Sufficiency Estimation

**著者**: Wenhao Yuan, Chenchen Lin, Wenhao Hu, Jian Chen, Jinfeng Xu
**年**: 2026 | **被引用数**: 0
**タイプ**: meta_analysis | **分野**: 脳科学

## Abstract

\textit{Split Federated Learning} (SFL) enables distributed model training by splitting networks between the server and clients. However, under client heterogeneity, the conventional static split strategy may be suboptimal because clients can differ in data distributions, adaptation dynamics, and representation learning progress, making a single split point insufficient to accommodate client-specific training states. In this paper, we propose \textsc{FedSGA}, a \textbf{S}ufficiency-\textbf{G}uided \textbf{A}daptive split \textbf{Fed}erated learning framework that addresses this question through client-specific shallow sufficiency estimation. First, we introduce a client-specific adaptation channel based on private prompt tokens, which tracks local adaptation dynamics separately from the shared backbone and provides a lightweight signal for detecting whether client adaptation remains active. To further avoid repeated online probing over multiple candidate depths, we design a shallow sufficiency estimator that combines cross-client semantic alignment, temporal interface stability, and prompt-state variation to estimate whether the shallowest split is already sufficient. Finally, we introduce a split-compatible interface harmonization module that projects activations from different split depths into a shared semantic space, improving the comparability of heterogeneous client interfaces before server-side prediction. Extensive experiments on multiple heterogeneous benchmarks demonstrate the effectiveness of \textsc{FedSGA} in improving model performance compared with state-of-the-art methods while reducing unnecessary client-side computation.
