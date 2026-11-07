---
title: "A Deep Learning-Based Adversarial Attack Detection and Defense Method for Cybersecurity Protection in Power Systems"
authors: "Shuo Li, Xiangsen Xu, Pingzhou Li"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-08T06:15:44.553323"
doi: "https://doi.org/10.21203/rs.3.rs-11314898/v1"
openalex_id: "https://openalex.org/W7225415012"
source_api: "openalex"
---

# A Deep Learning-Based Adversarial Attack Detection and Defense Method for Cybersecurity Protection in Power Systems

**著者**: Shuo Li, Xiangsen Xu, Pingzhou Li
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Abstract Deep learning detectors are proposed to catch false data injection in power system state estimation, but they can themselves be attacked. We study an attacker who keeps the measurements physically consistent, so the residual test stays silent. It must also fake a minimum load change at a target bus. We propose PARRY, a two-layer detection and defence method. The first is a deep detector trained against this realisable attacker. The second is a far-bus witness that predicts each bus load from buses outside the attacker’s reach. We prove that the witness bounds the load change an undetected attack can fake, however it is optimised and however slowly it is applied. State re-estimation adds a small slack to this bound, which we measure. We evaluate on IEEE 14-bus and 118-bus systems with three years of real demand. Thresholds target a nominal 1% false alarm rate, and attacks are adaptive and white-box. On the 118-bus system a standard deep detector catches 19% of attacks that fake a 30% load change. Adversarial training with PGD or TRADES catches 36% or 32%. PARRY catches 75%, and 98% at a 50% change. No method detects 10% changes, which lie within natural load variation.
