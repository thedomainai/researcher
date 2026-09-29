---
title: "A non-destructive methodological framework for modernizing legacy clinical reporting systems for AI-driven pharmacoinformatics: a SAS case study"
authors: "Jaime Yan"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-09-29T06:01:25.800042"
doi: "https://doi.org/10.3389/fphar.2026.1876207"
openalex_id: "https://openalex.org/W7161326509"
source_api: "openalex"
---

# A non-destructive methodological framework for modernizing legacy clinical reporting systems for AI-driven pharmacoinformatics: a SAS case study

**著者**: Jaime Yan
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Legacy clinical reporting pipelines bottleneck drug development and pharmacovigilance: they encode regulatory-grade analytical logic but produce opaque output with no machine-readable intermediate layer, resisting integration with artificial intelligence (AI). Existing modernization approaches force a choice between full rewrites that abandon validated logic and incremental refactoring that preserves structural barriers to AI access. We present a non-destructive framework that achieves AI-driven pharmacoinformatics readiness without altering legacy source code. A metadata layer — a bridge map, a typed Intermediate Representation (IR), and an orchestrator — wraps existing reporting components, re-exposes their outputs as structured data consumable by large language models (LLMs), and enables optional incremental consolidation of selected components while the remainder operates unchanged. On a 558-component industrial SAS reporting library (373,000 lines of code), the framework demonstrated immediate AI readiness under coexistence mode with the legacy library unchanged. Where consolidation was elected, the modernized core achieved a 92% reduction in consolidated-core SAS lines of code (excluding the Python and YAML layers). Parity validation on 14 report types from an internal Phase III study cleared an 80% cell-level triage-admission gate on 11 of 14 reports (mean across all 14 report types 82.7%, best 99.2%); the three remaining reports differed in table-layout geometry rather than in computed values. A public benchmark on CDISC CDISCPilot01 data achieved 100% regression-consistency against frozen reference outputs across 5 reports (4,764 cells, 0 mismatches) — a reproducibility benchmark rather than independent validation. In a proof-of-concept study with a single large language model, the IR illustrated the feasibility of table summarization, adverse-event anomaly detection (a pharmacovigilance signal-detection example), and trial configuration generation — feasibility rather than validated performance. The framework offers a regulation-aware path to AI-integrated clinical trial reporting intended to reduce modernization overhead without interrupting ongoing regulatory submissions. Its regulatory-traceability features are design properties rather than validated compliance: no formal Installation/Operational/Performance Qualification (IQ/OQ/PQ) has been performed. All results derive from a single case study; the methodology is designed to be reusable across organizations and library scales, pending multi-site empirical validation.
