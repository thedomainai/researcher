---
title: "PIU Smart Intelligence Agents: Design and Implementation of a Security-Aware Multi-Agent Architecture for Enterprise Intelligence"
authors: "Sujit Shibaprasad Maity"
year: 2026
citations: 0
paper_type: "primary"
domain: "information_systems"
fetched: "2026-10-23T08:10:41.579454"
doi: "https://doi.org/10.38124/ijisrt/26oct511"
openalex_id: "https://openalex.org/W7223170875"
source_api: "openalex"
---

# PIU Smart Intelligence Agents: Design and Implementation of a Security-Aware Multi-Agent Architecture for Enterprise Intelligence

**著者**: Sujit Shibaprasad Maity
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 情報システム

## Abstract

Enterprises increasingly rely on heterogeneous documents, relational databases, and analytical systems to support information retrieval and business decision-making. Integrating large language models (LLMs) with these sources introduces challenges in evidence reliability, analytical correctness, access control, and operational resilience. This paper presents PIU Smart Intelligence Agents, a security-aware multi-agent architecture designed to integrate enterprise document intelligence, retrieval-augmented generation (RAG), semantic search, document summarization, naturallanguage-to-SQL analytics, key performance indicator (KPI) generation, and conversational AI within a common application and governance framework. The proposed architecture organizes specialized AI capabilities around shared services for authentication, authorization, request validation, provider integration, observability, and controlled data access. Its document-processing workflow encompasses file validation, text extraction, optical character recognition for scanned documents, normalization, chunking, embedding generation, and vector-based indexing. The structured-analytics workflow separates schema-aware query generation from SQL validation, restricted database execution, and result interpretation. The architecture also addresses provider compatibility, timeout handling, failure recovery, document lifecycle management, and traceability of generated outputs. The source implementation reports 1,242 automated tests passed and two integration tests skipped. These results are reported implementation evidence and have not been independently reproduced. The available evidence does not establish comprehensive external RAG benchmark performance, quantitative correctness across all agents, independently validated security effectiveness, or production-scale performance and recovery guarantees. Accordingly, this study presents an integrated engineering architecture and identifies a reproducible evaluation framework for assessing its effectiveness. The principal contribution is the systematic integration of heterogeneous enterprise AI capabilities with explicit governance and validation requirements, rather than the introduction of a new learning or retrieval algorithm. Future work should prioritize agent-specific correctness testing, retrieval and answer-quality benchmarks, adversarial security evaluation, controlled load testing, and recovery verification.
