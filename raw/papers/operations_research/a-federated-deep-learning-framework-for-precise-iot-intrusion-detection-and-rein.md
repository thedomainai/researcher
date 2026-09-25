---
title: "A Federated Deep Learning Framework for Precise IoT Intrusion Detection and Reinforcement-based Automated Cyber Response"
authors: "Anaam Ghanim Hilal, Nawfal Turki Obeis"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-08-31T09:35:57.355626"
doi: "https://doi.org/10.22266/ijies2026.0930.32"
openalex_id: "https://openalex.org/W7204655255"
source_api: "openalex"
---

# A Federated Deep Learning Framework for Precise IoT Intrusion Detection and Reinforcement-based Automated Cyber Response

**著者**: Anaam Ghanim Hilal, Nawfal Turki Obeis
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

The rapid expansion of IoT deployments has created an attack surface that conventional intrusion detection systems are ill-equipped to defend.Centralized deep learning approaches compromise data privacy, while existing federated methods stop detection without addressing what the network should do next.This paper proposes a twostage framework that closes both gaps.In Stage 1, a federated CNN-BiLSTM-SGB model trained across eight non-IID clients produces a calibrated attack probability per flow, achieving a ROC-AUC of 0.9950 and an attack F1-score of 0.9924 on the CIC IoT Dataset 2023.In Stage 2, a dueling DDQN agent conditioned on that probability selects among six operational responses under the ATSR reward function, which weights penalties by attack severity and detection confidence.The agent reached a primary action accuracy of 97.73% and an attack-ALLOW rate of just 1.04%, with the highest accuracy recorded for the most dangerous threat categories.Together, the two stages demonstrate that federated data-local intrusion detection and severity-aware automated response can operate within a single coherent pipeline.
