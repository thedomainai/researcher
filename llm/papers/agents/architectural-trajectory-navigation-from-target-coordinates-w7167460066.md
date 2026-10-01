---
title: "Architectural Trajectory Navigation: From Target Coordinates to Measurement Predicates"
authors: ["Volkan ER"]
year: 2026
cited_by_count: 5
doi: "https://doi.org/10.5281/zenodo.21207704"
openalex_id: W7167460066
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# Architectural Trajectory Navigation: From Target Coordinates to Measurement Predicates

**Authors**: Volkan ER | **Year**: 2026 | **Cited by**: 5 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

AI coding agents navigate software projects by reasoning toward a goal, but they typically formulate that goal as a target state to be reached — a coordinate, a patch, a desired measurement. This creates an epistemological hazard: if an agent can observe the target coordinate it is supposed to produce, its output is no longer an independent measurement of architectural health but a self-fulfilling projection. We present Architectural Trajectory Navigation, the dynamic extension of the Ontological Space Protocol (OSP), in which an agent's task is formulated not as a target coordinate but as a measurement predicate — a deterministic, engine-evaluated condition on the project's coordinate space (e.g., "coupling of module M ≤ 0.55"). The agent never observes the target coordinate; it observes only the predicate and a structural context (its focus node and current outgoing imports). A deterministic predicate gate (Q5.b) measures the agent's proposed structural delta against the predicate before any mutation reaches the project space, producing a typed AttemptOutcome (Completed / NotCompleted) and a mutation decision (Reject / AcceptAsProgress / AcceptAsCompleted). An adaptive control loop (maneuver limit + calibration feedback retry) bounds the agent's attempts and feeds gate rejections back as structured calibration messages rather than terminal failures. We evaluate the approach on an external corpus of three public repositories spanning three programming languages — chalk (JavaScript), click (Python), and cobra (Go) — using a real LLM (GPT-4o-mini) under a controlled structural harness. Across 24 external cells (3 repos × 2 task types × 2 policies × 2 feedback modes) plus 2 real-LLM synthetic-smoke cells, the agent achieved 26/26 Completed under first-attempt-dominant scenarios, at a mean cost of 1104 tokens per completed cell, with 0 axis regressions (no cell degraded a non-target architectural axis). Separately, a controlled synthetic fixture with scripted proposals isolates the RQ9 policy mechanism: progress-checkpoint accumulation completes under bounded attempts where strict rejection cannot. We report the external results as preliminary evidence that the structural-proposal pipeline works end-to-end on real analyzed repositories; we are explicit that this measures structural delta success (graph-level removed_edges), not source-code patch correctness, and that the first-attempt dominance suppresses the signals our controlled-mock experiment uses to distinguish feedback (RQ8) and policy (RQ9) conditions. The implementation (Rust workspace, type-level invariants INV-T1–T8) and raw evidence (JSON) are open-source; corpus repositories are cloneable. This is the second of three companion papers. Paper 1 established OSP's static conceptual space; Paper 3 extends the model to the genesis layer that produces bound work from human sentences.
