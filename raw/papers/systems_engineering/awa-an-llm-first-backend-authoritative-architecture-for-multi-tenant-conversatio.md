---
title: "AWA: An LLM-First, Backend-Authoritative Architecture for Multi-Tenant Conversational Business Automation"
authors: "Hari R Chandran"
year: 2026
citations: 0
paper_type: "primary"
domain: "systems_engineering"
fetched: "2026-07-22T06:02:05.630293"
doi: "https://doi.org/10.5281/zenodo.21460621"
openalex_id: "https://openalex.org/W7169803243"
source_api: "openalex"
---

# AWA: An LLM-First, Backend-Authoritative Architecture for Multi-Tenant Conversational Business Automation

**著者**: Hari R Chandran
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: システム工学

## Abstract

AWA—Always Working Assistant is a multi-tenant conversational business automation platform designed to handle customer enquiries and structured workflows through browser-based chat and WhatsApp. The system supports business functions including appointment booking, product ordering, knowledge-based enquiries, lead capture, reminders, reviews, payments, and escalation to human operators. AWA follows an LLM-first, backend-authoritative architecture. Large language models are used to interpret natural customer messages, identify intent, extract multiple configured fields, manage conversational context, and generate user-facing responses. However, the language model is not allowed to directly modify business data. All business actions pass through deterministic backend validation, tenant-specific configuration, confirmation requirements, customer verification, authorization checks, idempotency controls, audit logging, and PostgreSQL persistence. The platform is implemented using FastAPI, React, PostgreSQL, Redis, background workers, and an abstraction layer supporting multiple LLM providers with fallback handling. The study presents the architecture, implementation, security model, workflow design, and practical evaluation of natural-language booking, ordering, multilingual interaction, contextual continuation, protected actions, and failure recovery. Evaluation results demonstrate successful natural multi-field extraction, complete booking and order workflows, OTP-protected confirmation, duplicate-execution prevention, provider fallback, and tenant-scoped business processing. The paper also documents current limitations involving certain contextual workflow transitions, multilingual catalogue interaction, and conversational edge cases. This record is a non-peer-reviewed research preprint based on the MCA project “AWA—Always Working Assistant,” developed at the Department of Computer Applications, Mar Thoma Institute of Information Technology, Ayur, Kerala, India.
