---
title: "SAD-ReID: Semantically-anchored dynamics for unsupervised vehicle re-identification"
authors: "Yun Jiang, Kunyi Zhu, Tao Sun"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-08-21T06:00:09.618705"
doi: "https://doi.org/10.1007/s44443-026-01119-1"
openalex_id: "https://openalex.org/W7160825884"
source_api: "openalex"
---

# SAD-ReID: Semantically-anchored dynamics for unsupervised vehicle re-identification

**著者**: Yun Jiang, Kunyi Zhu, Tao Sun
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

<title>Abstract</title> Unsupervised vehicle re-identification (Re-ID) is pivotal for scalable intelligent transportation systems but faces significant challenges from severe noise accumulation. Traditional clustering-based methods often suffer from error propagation during online training, as purely visual features are highly susceptible to intra-class viewpoint variations and inter-class similarities. To mitigate this fundamental limitation, we propose a novel Semantically-Anchored Dynamics (SAD-ReID) framework that exploits the viewpoint-invariant stability of text-induced semantic knowledge derived from Vision-Language Models. Specifically, we first introduce a Semantically-Guided Initialization strategy that fuses visual similarities with detailed textual descriptions generated automatically by Qwen-VL. This rectifies initial visual clusters to establish robust text-guided dual-prototype (visual and semantic) anchors. During the online learning phase, we propose a Reliability-Aware Dynamic Update (RADU) mechanism. By calculating a Cross-Modality Allegiance (CMA) score that measures the topological agreement between visual and textual spaces, RADU dynamically adjusts the memory update momentum. This efficiently accelerates learning from reliable samples while filtering out noisy pseudo-labels to prevent memory corruption. Furthermore, an Adaptive Granularity Attention Fusion (AGAF) module is designed to capture both global semantic attributes and fine-grained local discriminative details. Extensive experiments on the VeRi-776 and VehicleID benchmarks demonstrate the significant superiority of our approach over existing state-of-the-art methods, achieving an impressive Rank-1 accuracy of 90.0\% and 43.2\% mAP on VeRi-776. By enforcing text-visual semantic consistency throughout the evolutionary training process, SAD-ReID successfully prevents model drift and learns highly robust representations without any manual annotation.
