---
title: "MKG-CARE: Case-Aware Reasoning with Multimodal Knowledge Graphs for Explainable Medical Image Diagnosis"
authors: "Yiming Xu, Yixuan Liu, Yuhang Zhang, Ling Zheng, Yihan Wang"
year: 2026
citations: 0
paper_type: "primary"
domain: "history_of_technology"
fetched: "2026-11-04T06:39:04.638559"
doi: "https://doi.org/10.1145/3799682.3840673"
openalex_id: "https://openalex.org/W7162073525"
source_api: "openalex"
---

# MKG-CARE: Case-Aware Reasoning with Multimodal Knowledge Graphs for Explainable Medical Image Diagnosis

**著者**: Yiming Xu, Yixuan Liu, Yuhang Zhang, Ling Zheng, Yihan Wang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 技術史

## Abstract

Medical image diagnosis has achieved significant progress with deep learning, yet existing methods often rely on isolated visual evidence and lack the ability to effectively leverage similar cases and external knowledge. In clinical practice, diagnosis is typically supported by similar historical cases and their associated symptoms. To explicitly model this evidence-based diagnostic process, we propose MKG-CARE, a framework that performs case-aware reasoning using multimodal knowledge graphs for explainable medical image diagnosis. Specifically, we construct a case-aware multimodal knowledge graph as a structured diagnostic memory, where diseases, images, and symptoms are hierarchically organized. Given an input image, MKG-CARE adaptively retrieves similar cases from this memory and extracts their corresponding case-centered subgraphs. We further introduce a knowledge propagation and injection mechanism, where an image-centric Graph Attention Network aggregates heterogeneous semantics within the retrieved case subgraphs, followed by bidirectional cross-modal attention to align and inject the aggregated case knowledge into visual representations. To mitigate retrieval noise, we design a confidence-calibrated decision refinement scheme that estimates each retrieved case's reliability from prediction confidence and sample similarity, and reweights its contribution to the final prediction for interpretable case-level evidence attribution. Extensive experiments on multiple medical imaging datasets demonstrate consistent improvements over strong baselines, while ablation and qualitative analyses validate the effectiveness and interpretability of our method. The code is available at https://github.com/lyxuan1022/MKG-CARE.
