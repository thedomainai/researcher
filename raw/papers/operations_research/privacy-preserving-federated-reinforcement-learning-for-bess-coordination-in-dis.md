---
title: "Privacy-preserving federated reinforcement learning for BESS coordination in distribution networks with voltage regulation"
authors: "Xiaotian Zhou, Y. Liu, Wenjie Xu, Hao Liang, Sara Rouhani"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-08-20T12:31:46.609225"
doi: "https://doi.org/10.1016/j.apenergy.2026.128681"
openalex_id: "https://openalex.org/W7117676031"
source_api: "openalex"
---

# Privacy-preserving federated reinforcement learning for BESS coordination in distribution networks with voltage regulation

**著者**: Xiaotian Zhou, Y. Liu, Wenjie Xu, Hao Liang, Sara Rouhani
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

The increasing integration of distributed energy resources (DERs) in distribution networks, particularly battery energy storage systems (BESSs), enables energy trading and operational cost reduction but also introduces challenges for coordinated energy management. Effective coordination of distributed BESSs requires access to residential data, raising significant data privacy concerns. In recent years, federated reinforcement learning (FRL) has emerged as a promising AI approach for privacy-preserving BESS energy management. However, the application of FRL in distribution networks is limited by several challenges, including coordination under voltage constraints caused by coupled BESS interactions, privacy leakage from intermediate result sharing, and scalability issues under high BESS penetration.To address these challenges, this paper proposes a privacy-preserving federated reinforcement learning scheme for BESS coordination with voltage regulation (PPFRL-BC). The BESS energy management problem is formulated under (ε,δ)-differential privacy constraints, within which privacy-preserving reward functions jointly capture system-level rewards and voltage regulation requirements. Building on this formulation, the proposed PPFRL-BC scheme enables coordinated BESS operation without direct sharing of raw residential data, while a BESS-oriented Gaussian noise mechanism is incorporated to mitigate privacy leakage associated with intermediate result sharing. To further improve scalability, an approximate action branching method is introduced to reduce computational complexity in large-scale distribution networks.Case studies on the IEEE 33-bus and 123-bus test feeders demonstrate that the proposed PPFRL-BC scheme effectively coordinates distributed BESS operations, maintains voltage regulation under network constraints and preserves data privacy, while achieving performance comparable to the centralized scheme and outperforming both decentralized and conventional horizontal FRL schemes.
