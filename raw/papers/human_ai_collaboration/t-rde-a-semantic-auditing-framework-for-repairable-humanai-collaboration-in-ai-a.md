---
title: "T-RDE: A Semantic Auditing Framework for Repairable Human–AI Collaboration in AI-Assisted Software Engineering"
authors: "Tomoyuki Kano"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-05-29T06:06:22.621800"
doi: "https://doi.org/10.5281/zenodo.20419086"
openalex_id: "https://openalex.org/W7162503886"
source_api: "openalex"
---

# T-RDE: A Semantic Auditing Framework for Repairable Human–AI Collaboration in AI-Assisted Software Engineering

**著者**: Tomoyuki Kano
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

In AI-assisted software engineering, the fact that generated code compiles, passes tests, or appears to satisfy a task does not necessarily mean that the original human design intention has been preserved. Large language models can complete ambiguous requirements, introduce unsolicited features, suppress uncertainty, and transform provisional interpretations into apparently decisive implementations. In such situations, the central problem is not merely functional correctness. The deeper issue is whether the meaning changes introduced during generation are traceable, reviewable, and repairable. This paper proposes T-RDE, or Test-with-Resonant Deviation Evaluator, as a testingadjacent framework for auditing semantic change in AI-assisted software engineering. The name emphasizes that conventional tests remain necessary but insufficient: T-RDE supplements tests with an evaluator of resonant deviations between human design intent and AI-generated artifacts. T-RDE records the relationship between human design intent and AI-generated artifacts as a semantic map, classifies intent elements as preserved, transformed, deviated, or not implemented, and makes implicit additions introduced by AI systems explicit. It further models semantic change not as a single scalar defect score but as a set of ΔM components: ΔS for semantic content, ΔP for practical affordance, ΔR for relational configuration, ΔI for institutional arrangement, and ΔU for uncertainty handling. Among these, ΔU plays a special role as a precondition for quality gating, because hidden uncertainty can distort the evaluation of all other semantic changes. The paper uses Resonance Theory of Intelligence (RTI) not as a universal or exhaustive theory of intelligence, but as a relational lens for organizing four requirements central to human–AI coding collaboration: semantic alignment, uncertainty calibration, value coordination, and repairability. T-RDE does not aim to determine an objective final meaning, nor does it eliminate interpretive variance. Rather, it provides a structured framework for tracking, exposing, and reviewing meaning transformations, uncertainty handling, and shifts in responsibility during human–AI collaboration.
