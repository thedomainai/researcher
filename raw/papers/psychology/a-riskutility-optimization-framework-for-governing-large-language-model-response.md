---
title: "A Risk–Utility Optimization Framework for Governing Large Language Model Responses"
authors: "Jinghao Chang"
year: 2026
citations: 0
paper_type: "primary"
domain: "psychology"
fetched: "2026-04-06T14:00:52.795882"
doi: "https://doi.org/10.17613/tzvgm-j2e56"
openalex_id: "https://openalex.org/W7134120560"
source_api: "openalex"
---

# A Risk–Utility Optimization Framework for Governing Large Language Model Responses

**著者**: Jinghao Chang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 心理学

## Abstract

Large language models (LLMs) are increasingly deployed in enterprise, public-sector, and consumer-facing settings where organizations must simultaneously pursue utility and constrain multiple categories of risk. In practice, governance choices rarely reduce to a binary distinction between "ship" and "do not ship." Instead, operators decide whether a response should be delivered automatically, escalated to human review, routed through layered review, or refused and transferred to a nonLLM channel. This paper develops a theory-first optimization framework for that governance problem. We model response governance as the selection of an action from a finite menu under joint constraints on hallucination risk, severe-output risk, latency, token expenditure, and human-review cost. The framework yields a constrained optimization problem whose Lagrangian interpretation provides a practical policy calculus: governance becomes a query-level action rule that maximizes expected net value after pricing residual harms and operational burdens. Under mild monotone single-crossing assumptions, the optimal policy admits a simple threshold structure in an estimated task-risk score. This recovers four governance regimes that matter in practice-fully automatic service, threshold-triggered human review, layered review, and refusal/transfer in extremerisk regions-as special cases of the same model. We derive comparative-statics results showing when review thresholds fall, when layered review strictly dominates one-stage review, and when refusal is preferable to further automated assistance. The contribution is not a new prediction algorithm but a formal decision framework that connects responsible AI governance, epistemic risk, and operational optimization in a tractable way that is suitable for organizational design, auditability, and regulatory interpretation.
