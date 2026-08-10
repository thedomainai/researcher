---
title: "A Taxonomy of AI Governance Approaches: Distinguishing Visibility, Alignment, and Authorization"
authors: "Edward Meyman"
year: 2026
citations: 17
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-06-26T06:02:40.290085"
doi: "https://doi.org/10.5281/zenodo.18275969"
openalex_id: "https://openalex.org/W7124536980"
source_api: "openalex"
---

# A Taxonomy of AI Governance Approaches: Distinguishing Visibility, Alignment, and Authorization

**著者**: Edward Meyman
**年**: 2026 | **被引用数**: 17
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

The term “AI governance” has become semantically overloaded, applied indiscriminately to logging, guardrails, model alignment, dashboards, and policy workflows. This paper introduces a formal taxonomy that distinguishes three fundamentally different governance problems—visibility (what happened), alignment (is the system generally safe), and authorization (was this specific action permitted under policy at execution time)—and maps common vendor “governance” claims to the problems they actually solve. The taxonomy defines deterministic AI governance as a pre-execution authorization layer in which identical governed state yields identical governance verdicts and the system emits cryptographically verifiable decision artifacts sufficient for independent third-party offline replay. It specifies the normative structure of governed state, the Minimum Evidence Package (Normative), an enforcement triad (ALLOW / DENY / ABSTAIN), and disqualifying evaluation methods, including anti-laundering checks designed to prevent trust-based or vendor-dependent imitation of governance. Version 1.5.1 clarifies the doctrinal boundary between observability and enforcement. Observability governs accounts of action; authorization governs permission to act. SDLC controls constrain deployment but do not constrain individual runtime decisions once deployed. Signed artifacts protect history; signed authorizations govern the future. Authorization governance is present only when a non-bypassable runtime gate binds each action to governed state and policy version and fails closed when governance conditions fail or required evidence is missing. This work is intentionally testable and disqualifying rather than aspirational. It provides enterprise buyers, regulators, auditors, and researchers with a shared vocabulary and concrete conformance criteria for evaluating AI governance claims in high-stakes, regulated deployments. The framework is architecture-agnostic and may be applied to any AI governance solution. Update (June 2026, v1.6): Version 1.6 aligns the taxonomy package with the Four Tests Standard (Stop, Ownership, Replay, Escalation), the Authorization Artifact Test, and FERZ Technical Advisory TA-2026-01, which names the artifact gap: the evidentiary condition that arises when observability is relied upon to satisfy an ex-ante authorization requirement. The companion evaluation kit is updated accordingly, and the Evidence Package Examples add an agentic tool-use example in which an external data transfer is blocked before dispatch. The three-problem taxonomy, the deterministic governance definition, and the conformance methodology are unchanged from v1.5.1. Update (Jan 2026): Released a companion evaluation kit including an Executive Summary (board/C-suite orientation), a Vendor Evaluation Supplement with decision logic for determining when authorization-layer governance is required, and Evidence Package Examples demonstrating independently replayable ALLOW, DENY, and ABSTAIN verdicts conformant with the Minimum Evidence Package requirements.
