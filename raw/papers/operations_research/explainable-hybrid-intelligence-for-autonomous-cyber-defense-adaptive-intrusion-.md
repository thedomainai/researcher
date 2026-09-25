---
title: "Explainable Hybrid Intelligence for Autonomous Cyber Defense: Adaptive Intrusion Detection and Real-time Firewall Enforcement Using Reinforcement Learning"
authors: "Magi Hossameldin Mahfouz, Raghda Essam Ali, Ayat Mahmoud"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-21T09:16:40.626000"
doi: "https://doi.org/10.22266/ijies2026.1031.75"
openalex_id: "https://openalex.org/W7213646413"
source_api: "openalex"
---

# Explainable Hybrid Intelligence for Autonomous Cyber Defense: Adaptive Intrusion Detection and Real-time Firewall Enforcement Using Reinforcement Learning

**著者**: Magi Hossameldin Mahfouz, Raghda Essam Ali, Ayat Mahmoud
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Conventional rule-based firewalls rely on static signatures, limiting adaptability to unseen attacks, while AI-enabled commercial tools remain proprietary and lack transparency.This paper presents Net-Knight, an explainable hybrid intelligence framework integrating supervised intrusion detection, unsupervised anomaly detection, reinforcement learning (RL)-based mitigation, and Linux nftables enforcement.A LightGBM classifier trained on 22 engineered NetFlow features from NF-UQ-NIDS-v2 performs intrusion detection, while an autoencoder ensemble supplies complementary anomaly evidence.These signals form a 28-dimensional state used by a MaskablePPO agent to select among five mitigation actions.The IDS achieves 96.82% accuracy and a 0.9681 macro F1-score across nine classes; the RL agent attains a 96.9% rule-match rate; and the integrated decision pipeline reaches 96.3% end-to-end decision accuracy at 8.7 ms mean processing latency in the controlled evaluation.A proposed Hierarchical Confusion-Aware Disambiguation (HCAD) extension is evaluated separately through Monte Carlo sensitivity analysis; its projected gains are not treated as experimentally measured performance.
