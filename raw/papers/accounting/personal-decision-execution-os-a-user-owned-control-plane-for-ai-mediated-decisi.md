---
title: "Personal Decision & Execution OS: A User-Owned Control Plane for AI-Mediated Decision Continuity and Verified Execution (v0.2)"
authors: "유경 정"
year: 2026
citations: 0
paper_type: "primary"
domain: "accounting"
fetched: "2026-09-17T09:12:17.335241"
doi: "https://doi.org/10.5281/zenodo.22739425"
openalex_id: "https://openalex.org/W7212994727"
source_api: "openalex"
---

# Personal Decision & Execution OS: A User-Owned Control Plane for AI-Mediated Decision Continuity and Verified Execution (v0.2)

**著者**: 유경 정
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 会計学

## Abstract

Technical Design Report v0.2. September 14, 2026. Author: 정유경 (jung yugyoung). Public draft. Not peer reviewed. This report describes an operating architecture developed through repeated real-world use. It makes design claims and proposes measurable evaluation criteria; it does not claim controlled empirical validation. Abstract Long-term use of AI assistants creates a continuity problem: conversational memory, semantic retrieval, and agent execution can each recover useful context, but they do not by themselves guarantee that an assistant is acting on the current valid decision, within the correct authority boundary, using tools it actually possesses, or reporting execution truthfully. This report presents Personal Decision & Execution OS (PDE-OS), a user-owned control-plane architecture for AI-mediated decision continuity and verified execution. The system separates historical evidence from canonical state, resolves current decisions through explicit Decision/Correction records and supersession, gates continuity-dependent requests through canonical context retrieval, selects only success paths compatible with the current decision, checks present tool/account/permission capability before execution, and records verified evidence separately from configuration or intent. A risk-tiered governance rule ('Tight Core, Loose Edge') limits heavy verification to high-impact actions while keeping lightweight work fast. The architecture uses storage-provider revision identifiers and content hashes to detect changes before and after writes; this does not guarantee atomic conflict prevention when conditional writes are unavailable. An experimental Impact Scope model—Primary, Affected, Protected—is proposed to control cross-domain blast radius without building a large ontology. The report positions PDE-OS against contemporary stateful-agent, knowledge-management, workspace-agent, and durable-execution systems, and defines an evaluation agenda centered on stale-decision reuse, false completion, user intervention burden, scope errors, and concurrency conflicts. Revision note Version 0.2 updates the pre-publication draft with human-tolerant governance, Explore/Commit behavior, the three-part Impact Scope pilot, a bounded cross-model observation, and a staged evaluation plan. It also corrects capability-versus-completion wording and the limits of revision-based conflict detection. No new effectiveness benchmark or runtime-enforcement result is claimed. Evidence and AI assistance The operational description is based on the author's private SecondBrain policies, project context, and working records. These are not included in this public report; no independently reproducible effectiveness result is claimed. AI tools assisted with drafting, English wording, organization, and editorial review. The author is the named creator; AI systems are not listed as authors.
