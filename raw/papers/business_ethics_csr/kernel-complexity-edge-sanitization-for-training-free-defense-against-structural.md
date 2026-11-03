---
title: "Kernel-Complexity Edge Sanitization for Training-Free Defense against Structural Graph Attacks"
authors: "Yaning Jia, Shenyang Deng, Yaoqing Yang, Chiyu Ma, Wenxuan Xu"
year: 2026
citations: 0
paper_type: "primary"
domain: "business_ethics_csr"
fetched: "2026-11-04T06:54:44.716446"
doi: "https://doi.org/10.1145/3799682.3841029"
openalex_id: "https://openalex.org/W7212151780"
source_api: "openalex"
---

# Kernel-Complexity Edge Sanitization for Training-Free Defense against Structural Graph Attacks

**著者**: Yaning Jia, Shenyang Deng, Yaoqing Yang, Chiyu Ma, Wenxuan Xu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 経営倫理・CSR

## Abstract

Graph Neural Networks (GNNs) have achieved remarkable success across diverse applications, yet they remain highly vulnerable to adversarial attacks that maliciously perturb graph structure. Existing defenses often lack rigorous theoretical grounding, rely on attack-specific heuristics, or require costly retraining procedures such as adversarial training. To address these limitations, we propose Kernel-Complexity Edge Sanitization (KCES), a training-free and model-agnostic framework for defending against structural attacks. KCES is built upon Graph Kernel Complexity (GKC), a principled metric derived from the graph Gram matrix that appears in a generalization upper bound on the GNN test error. From this bound, we define an edge-specific KC score that quantifies each edge's structural influence via its induced change in GKC. KCES then identifies and prunes high-KC edges, which are empirically enriched with adversarial perturbations under structural attacks, to mitigate their harmful impact. Computationally efficient and scalable, KCES operates as a lightweight preprocessing step without retraining and can be seamlessly integrated with existing defenses. Extensive experiments demonstrate that KCES consistently outperforms representative robust baselines across diverse attack settings and scales effectively to large graphs. Supported by theoretical analysis and extensive empirical validation, KCES provides a principled and efficient framework for securing GNNs. Our code is available at https://github.com/karpning/KCScore.
