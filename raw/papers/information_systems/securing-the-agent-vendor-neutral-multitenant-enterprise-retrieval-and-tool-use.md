---
title: "Securing the Agent: Vendor-Neutral, Multitenant Enterprise Retrieval and Tool Use"
authors: "Francisco Javier Arceo, Varsha Prasad Narsing"
year: 2026
citations: 0
paper_type: "primary"
domain: "information_systems"
fetched: "2026-05-23T06:04:15.339424"
doi: "https://doi.org/10.1145/3786335.3813145"
openalex_id: "https://openalex.org/W7160692720"
source_api: "openalex"
---

# Securing the Agent: Vendor-Neutral, Multitenant Enterprise Retrieval and Tool Use

**著者**: Francisco Javier Arceo, Varsha Prasad Narsing
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 情報システム

## Abstract

Retrieval-Augmented Generation (RAG) and agentic AI systems are increasingly prevalent in enterprise AI deployments. However, real enterprise environments introduce challenges largely absent from academic treatments and consumer-facing APIs: multiple tenants with heterogeneous data, strict access-control requirements, regulatory compliance, and cost pressures that demand shared infrastructure. A fundamental problem underlies existing RAG architectures in these settings: retrieval systems rank documents by relevance--whether through semantic similarity, keyword matching, or hybrid approaches--not by authorization, so a query from one tenant can surface another tenant's confidential data simply because it scores highest. We formalize this gap and analyze additional shortcomings--including tool-mediated disclosure, context accumulation across turns, and client-side orchestration bypass--that arise when agentic systems conflate relevance with authorization. To address these challenges, we introduce a layered isolation architecture combining policy-aware ingestion, retrieval-time gating, and shared inference, enforced through server-side agentic orchestration. This approach centralizes security-critical operations--tool execution authorization, state isolation, and policy enforcement--on the server, creating natural enforcement points for multitenant isolation while allowing client-side frameworks to retain control over agent composition and latency-sensitive operations. We validate the proposed architecture through an open-source implementation in OGX, a vendor-neutral framework that implements an OpenAI-compatible, open-source Responses API with server-side multi-turn orchestration. We evaluate it empirically and show that ABAC gating eliminates cross-tenant leakage while introducing negligible overhead.
