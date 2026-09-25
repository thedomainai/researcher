---
title: "From Monitoring to Authorization: The Structural Shift in Agentic AI Governance"
authors: "Edward Meyman"
year: 2026
citations: 19
paper_type: "primary"
domain: "information_systems"
fetched: "2026-08-29T09:03:06.605776"
doi: "https://doi.org/10.5281/zenodo.18743974"
openalex_id: "https://openalex.org/W7131107050"
source_api: "openalex"
---

# From Monitoring to Authorization: The Structural Shift in Agentic AI Governance

**著者**: Edward Meyman
**年**: 2026 | **被引用数**: 19
**タイプ**: primary | **分野**: 情報システム

## Abstract

As AI systems transition from content generation to autonomous execution (writing to databases, initiating transactions, modifying infrastructure), the governance problem shifts from observing behavior to authorizing action. Monitoring-based architectures document what occurred; they do not determine whether a specific action was permitted before execution. This paper analyzes a recurring structural ambiguity across recent cross-jurisdiction regulatory frameworks: the under-specification of the enforcement primitive at the decision boundary where AI intent becomes real-world effect. Drawing on comparative analysis of EU, U.S., and Asia-Pacific governance frameworks, it distinguishes observability from authorization and argues that monitoring alone cannot satisfy enforcement-grade requirements in high-impact agentic deployments. The paper defines the architectural properties of an authorization boundary (non-bypassable runtime gating, deterministic verdict semantics resolving to ALLOW, DENY, or ABSTAIN, definitional fail-closed behavior, and policy-state binding) and locates the completeness questions across the corpus instruments: the Authorization Artifact Test as the threshold, the Authorization Boundary Integrity Model separating Output, Input, and Replay Integrity, the Five Tests Standard (5TS) as the normative test vocabulary, the ABIM Evidence Requirements as the evidence standard, and the Composition Test for authorization-infrastructure claims. Verdicts must be reconstructable by an independent third party from the authorization artifact and its bound materials under a declared replay mode (State-Replay or Protocol-Replay). The argument is structural rather than empirical. It derives governance requirements from engineering constraints inherent to autonomous systems and from the regulatory trajectory toward decision-level, independently reconstructable evidence. The paper positions authorization infrastructure as a necessary layer beneath existing monitoring and compliance stacks in regulated, high-consequence AI environments, and serves as an accessible entry point to the FERZ authorization architecture corpus. Version 1.2.0 (August 2026) makes fail-closed behavior definitional rather than a default, replaces verdict reproduction with independent reconstruction under a declared replay mode, states human override as material consumption of authority-bound input by the runtime authorization boundary, retires the Minimum Authorization Boundary Contract (MABC) in favor of the instrument structure above with an express continuity note, retains the canonical provenance principle with a provenance-versus-admissibility clarification, and updates regulatory references, including the AI Omnibus amendments to the EU AI Act (Annex III application from 2 December 2027, Annex I from 2 August 2028), the Article 43 conformity-assessment correction, and NIST AI 200-2 (TEVV-Athlon, initial public draft).
