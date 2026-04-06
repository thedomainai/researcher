---
title: "SentinelAgent: Intent-Verified Delegation Chains for Securing Federal Multi-Agent AI Systems"
authors: "KrishnaSaiReddy Patil"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-04-06T13:19:32.276681"
arxiv_id: "http://arxiv.org/abs/2604.02767v1"
source_api: "arxiv"
categories: "cs.CR, cs.AI, cs.MA"
---

# SentinelAgent: Intent-Verified Delegation Chains for Securing Federal Multi-Agent AI Systems

**著者**: KrishnaSaiReddy Patil
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

When Agent A delegates to Agent B, which invokes Tool C on behalf of User X, no existing framework can answer: whose authorization chain led to this action, and where did it violate policy? This paper introduces SentinelAgent, a formal framework for verifiable delegation chains in federal multi-agent AI systems. The Delegation Chain Calculus (DCC) defines seven properties - six deterministic (authority narrowing, policy preservation, forensic reconstructibility, cascade containment, scope-action conformance, output schema conformance) and one probabilistic (intent preservation) - with four meta-theorems and one proposition establishing the practical infeasibility of deterministic intent verification. The Intent-Preserving Delegation Protocol (IPDP) enforces all seven properties at runtime through a non-LLM Delegation Authority Service. A three-point verification lifecycle achieves 100% combined TPR at 0% FPR on DelegationBench v4 (516 scenarios, 10 attack categories, 13 federal domains). Under black-box adversarial conditions, the DAS blocks 30/30 attacks with 0 false positives. Deterministic properties are unbreakable under adversarial stress testing; intent verification degrades to 13% against sophisticated paraphrasing. Fine-tuning the NLI model on 190 government delegation examples improves P2 from 1.7% to 88.3% TPR (5-fold cross-validated, F1=82.1%). Properties P1, P3-P7 are mechanically verified via TLA+ model checking across 2.7 million states with zero violations. Even when intent verification is evaded, the remaining six properties constrain the adversary to permitted API calls, conformant outputs, traceable actions, bounded cascades, and compliant behavior.
