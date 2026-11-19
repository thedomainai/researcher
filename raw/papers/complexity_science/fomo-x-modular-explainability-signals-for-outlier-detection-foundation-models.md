---
title: "FoMo-X: Modular Explainability Signals for Outlier Detection Foundation Models"
authors: "Simon Klüttermann, Tim Katzke, Phuong Kim Thi Nguyen, Emmanuel Müller"
year: 2026
citations: 2
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-20T06:00:57.002095"
doi: "https://doi.org/10.1007/978-3-032-45470-6_23"
openalex_id: "https://openalex.org/W7138974851"
source_api: "openalex"
---

# FoMo-X: Modular Explainability Signals for Outlier Detection Foundation Models

**著者**: Simon Klüttermann, Tim Katzke, Phuong Kim Thi Nguyen, Emmanuel Müller
**年**: 2026 | **被引用数**: 2
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Tabular foundation models, specifically Prior-Data Fitted Networks (PFNs), have revolutionized outlier detection (OD) by enabling unsupervised zero-shot adaptation to new datasets without training. However, despite their predictive power, these models typically function as opaque black boxes, outputting scalar outlier scores that lack the operational context required for safety-critical decision-making. Existing post-hoc explanation methods are often computationally prohibitive for real-time deployment or fail to capture the epistemic uncertainty inherent in zero-shot inference. In this work, we introduce FoMo-X, a modular framework that equips OD foundation models with intrinsic, lightweight diagnostic capabilities. We leverage the insight that the frozen embeddings of a pretrained PFN backbone already encode rich, context-conditioned relational information. FoMo-X attaches auxiliary diagnostic heads to these embeddings, trained offline using the same generative simulator prior as the backbone. This allows us to distill computationally expensive properties, such as Monte Carlo dropout based epistemic uncertainty, into a deterministic, single-pass inference. We instantiate FoMo-X with two novel heads: a Severity Head that discretizes deviations into interpretable risk tiers, and an Uncertainty Head that provides calibrated confidence measures. Extensive evaluation on synthetic and real-world benchmarks (ADBench) demonstrates that FoMo-X recovers ground-truth diagnostic signals with high fidelity and negligible inference overhead. By bridging the gap between foundation model performance and operational explainability, FoMo-X offers a scalable path toward trustworthy, zero-shot outlier detection.
