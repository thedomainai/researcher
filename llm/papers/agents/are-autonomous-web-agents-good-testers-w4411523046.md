---
title: "Are Autonomous Web Agents Good Testers?"
authors: ["Antoine Chevrot", "Alexandre Vernotte", "Jean‐Rémy Falleri", "Xavier Blanc", "Bruno Legeard", "Aymeric Cretin"]
year: 2025
cited_by_count: 10
doi: "https://doi.org/10.1145/3728879"
openalex_id: W4411523046
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# Are Autonomous Web Agents Good Testers?

**Authors**: Antoine Chevrot, Alexandre Vernotte, Jean‐Rémy Falleri, Xavier Blanc, Bruno Legeard, Aymeric Cretin | **Year**: 2025 | **Cited by**: 10 | **Kind**: article | **Relevance**: agents: core

## Abstract

Despite advances in automated testing, manual testing remains prevalent due to the high maintenance demands associated with test script fragility—scripts often break with minor changes in application structure. Recent developments in Large Language Models (LLMs) offer a potential alternative by powering Autonomous Web Agents (AWAs) that can autonomously interact with applications. These agents may serve as Autonomous Test Agents (ATAs), potentially reducing the need for maintenance-heavy automated scripts by utilising natural language instructions similar to those used by human testers. This paper investigates the feasibility of adapting AWAs for natural language test case execution and how to evaluate them. We contribute with (1) a benchmark of three offline web applications, and a suite of 113 manual test cases, split between passing and failing cases, to evaluate and compare ATAs performance, (2) SeeAct-ATA and pinATA, two open-source ATA implementations capable of executing test steps, verifying assertions and giving verdicts, and (3) comparative experiments using our benchmark that quantifies our ATAs effectiveness. Finally we also proceed to a qualitative evaluation to identify the limitations of PinATA, our best performing implementation. Our findings reveal that our simple implementation, SeeAct-ATA, does not perform well compared to our more advanced PinATA implementation when executing test cases (50% performance improvement). However, while PinATA obtains around 60% of correct verdict and up to a promising 94% specificity, we identify several limitations that need to be addressed to develop more resilient and reliable ATAs, paving the way for robust, low maintenance test automation.
