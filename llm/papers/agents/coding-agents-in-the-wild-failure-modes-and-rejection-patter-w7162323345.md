---
title: "Coding Agents in the Wild: Failure Modes and Rejection Patterns of AI-Generated Pull Requests"
authors: ["Mahd Hindi", "Yasir Mahmood", "Linda Mohammed", "Salah Bouktif", "Mohammed Mediani"]
year: 2026
cited_by_count: 1
doi: "https://doi.org/10.1109/access.2026.3696573"
openalex_id: W7162323345
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# Coding Agents in the Wild: Failure Modes and Rejection Patterns of AI-Generated Pull Requests

**Authors**: Mahd Hindi, Yasir Mahmood, Linda Mohammed, Salah Bouktif, Mohammed Mediani | **Year**: 2026 | **Cited by**: 1 | **Kind**: article | **Relevance**: agents: core

## Abstract

Autonomous coding agents increasingly submit pull requests (PRs) to real software repositories, making it important to evaluate their behavior under actual review, testing, and governance workflows rather than only through synthetic benchmarks. This paper investigates how agent-generated pull request (APR) rejection evolves over time, which visible failure modes most often explain rejected APRs (RAPRs), and how these findings inform more effective coding-agent deployment and design. We follow a three-phase methodology. First, we construct an APR cohort from the AIDev-POP subset of the AIDev dataset, covering 12,433 APRs from 1,495 popular repositories and five coding agents. Second, we develop a socio-technical taxonomy of rejection reasons and validate a large language model (LLM)-based classifier on a manually labeled ground-truth subset of commented RAPRs, achieving 85.5% accuracy in identifying the main bucket reasons of the rejection. Third, we model temporal rejection patterns and conduct stratified analyses across agents, deployment settings, and reviewer types. Observational results show a significant decline in APR rejection odds over time after accounting for differences in change size, documentation and test updates, and agent type. This decline is not limited to a single agent in particular. Empirical results show that documentation co-changes are associated with lower rejection odds, whereas test-touch and patch size provide weaker differentiation. Most RAPRs are silent, with 84.2% closed without inline reviewer feedback. Among commented RAPRs, functional failures are the dominant visible rejection pattern, especially specification mismatch and logic defects. Overall, APR outcomes reflect interactions among agent behavior, repository guardrails, and developer practices. We translate these findings into evidence-informed design principles and advocate reflexive coding agent as a new design pattern that emphasizes context acquisition, local validation, and closer alignment with repository expectations. Our replication package is available at: https://github.com/mahdhindi/coding-agents-wild.
