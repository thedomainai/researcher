---
title: "Fifty Years of Specification Completeness: What Aviation Certification Tells AI Governance About Epoch Limits, Proof Surfaces, and the Structural Gap"
authors: "Christo Zietsman"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-06-26T06:02:50.732149"
arxiv_id: "http://arxiv.org/abs/2606.25120v1"
source_api: "arxiv"
categories: "cs.SE, cs.CY"
---

# Fifty Years of Specification Completeness: What Aviation Certification Tells AI Governance About Epoch Limits, Proof Surfaces, and the Structural Gap

**著者**: Christo Zietsman
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Aviation software certification has operationalised three structural requirements for governed software systems since 1992: structured governance linkage between governing specifications and operational evidence, context-bounded validity that triggers revalidation when operational context changes, and an objective evidence architecture that defines what proof means and what makes it sufficient. These requirements appear in DO-178C and DO-330 and are enforced through FAA and EASA certification.
  No existing framework requires these structural properties as intrinsic properties of individual AI governance documents. A system prompt, an AGENTS.md file, a governance policy, or a task envelope can be deployed without satisfying any of the three requirements aviation has enforced for three decades. Aviation is the most technically rigorous instance: its standard-setting bodies have acknowledged that their frameworks break down for AI systems, yet none requires these properties of individual governance documents.
  Aviation's structural requirements break down at the system level because AI systems are non-deterministic, but remain transferable at the document level: the governance artifact is a static artifact whose structural properties can be evaluated independently of the stochastic system it governs.
  The paper maps DO-178C's traceability architecture, DO-330's requalification triggers, and DO-178C's objective evidence requirements onto three structural findings: epoch limits on governance document validity, proof surfaces as the revalidation feedback mechanism, and the absence of structural completeness requirements in AI governance instruments. An empirical companion (arXiv:2604.21090) found that 37% of AI governance documents fall below the structural quality threshold. PromptQ's seven-principle framework operationalises these requirements at the governance document layer.
