---
title: "Architecture and Production Deployment of an AI-Driven Enterprise Audit Evidence Management and Compliance Automation Platform"
authors: "Varsha Shah"
year: 2026
citations: 0
paper_type: "primary"
domain: "psychology"
fetched: "2026-08-21T06:01:11.759667"
doi: "https://doi.org/10.5281/zenodo.22000469"
openalex_id: "https://openalex.org/W7203682375"
source_api: "openalex"
---

# Architecture and Production Deployment of an AI-Driven Enterprise Audit Evidence Management and Compliance Automation Platform

**著者**: Varsha Shah
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 心理学

## Abstract

Enterprise audit functions face mounting pressure to process increasing volumes of digital evidence, satisfy multi-jurisdictional compliance obligations, and demonstrate decision traceability under regulatory frameworks governing automated processing. This paper presents the architecture and production deployment design of a cloud-native, AI-driven platform for enterprise audit evidence management and compliance automation. The platform integrates a five-layer microservices architecture — evidence ingestion, ML-based anomaly detection, LLM-driven compliance classification, zero-trust access control, and automated regulatory reporting — deployed on Kubernetes with Apache Kafka as the event backbone. A hybrid ML and large language model pipeline classifies audit evidence against structured compliance checklists and natural language regulatory requirements, with SHAP-based attribution providing decision-level explainability for auditor review. Building on this architecture, the paper formalizes evidence processing into an explainable Hybrid Evidence Intelligence Framework: an ML anomaly score, an LLM compliance score, and a SHAP-derived explainability score are combined into a single, auditable confidence measure that governs human-review routing, together with a complementary audit risk score for prioritizing reviewer attention across concurrent evidence items. Role-based access control enforces a five-tier privilege hierarchy across the audit lifecycle, and zero-trust security principles govern all inter-service communication. The platform addresses four structural failure modes prevalent in legacy audit systems: manual evidence triage, siloed compliance verification, opaque automated decisions, and fragmented regulatory reporting. Design decisions are grounded in published literature across audit automation, regulatory natural language processing, enterprise ML deployment, and security architecture.
