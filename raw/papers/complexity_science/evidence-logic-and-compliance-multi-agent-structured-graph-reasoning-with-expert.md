---
title: "Evidence, Logic, and Compliance: Multi-Agent Structured Graph Reasoning with Expert Arbitration for Medical Referral"
authors: "Qi Peng, Yi Cai, Jialin Cui, Tong Zhu, Yujuan Ding"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-02T08:54:18.987025"
arxiv_id: "http://arxiv.org/abs/2608.30938v1"
source_api: "arxiv"
categories: "cs.MA"
---

# Evidence, Logic, and Compliance: Multi-Agent Structured Graph Reasoning with Expert Arbitration for Medical Referral

**著者**: Qi Peng, Yi Cai, Jialin Cui, Tong Zhu, Yujuan Ding
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Medical referral (directing patients to the appropriate hospital department) is a complex decision-making process requiring the synthesis of multimodal data, including patient narratives, laboratory indicators, and radiology imaging. While Large Language Models (LLMs) have advanced medical dialogue systems, they struggle with real-world referral tasks due to two primary limitations: (1) Information Overload, where models fixate on high-frequency disease terms while overlooking subtle but critical urgency indicators; and (2) Unstructured Collaboration, where existing multi-agent frameworks rely on loose dialogue that leads to semantic drift and confirmation bias. To address these challenges, we introduce MASGR (Multi-Agent Structured Graph Reasoning), a framework that treats referral not as a classification task but as a structured graph construction problem. MASGR deploys specialized agents to extract evidence from distinct modalities and coordinates them through a clinical reasoning graph. This graph forces agents to establish explicit logical connections between conflicting evidence. Furthermore, we integrate a knowledge-guided arbitration mechanism that prioritizes patient safety rules over standard diagnostic classification. Extensive experiments on real-world medical records demonstrate that MASGR significantly outperforms state-of-the-art LLMs and existing multi-agent systems, particularly in complex cases requiring the balancing of chronic disease management and emergency intervention. The AI contribution lies in the Multi-Agent Structured Graph Reasoning framework that transforms unstructured multi-agent dialogue into a verifiable logical graph construction. The engineering application is demonstrated through its deployment in a complex healthcare decision-making system to optimize the precision of complex medical referrals.
