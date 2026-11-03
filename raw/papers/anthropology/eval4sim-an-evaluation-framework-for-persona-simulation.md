---
title: "Eval4Sim: An Evaluation Framework for Persona Simulation"
authors: "Eliseo Bao, Anxo Pérez, Javier Parapar, Xi Wang"
year: 2026
citations: 0
paper_type: "primary"
domain: "anthropology"
fetched: "2026-11-04T06:28:06.696808"
doi: "https://doi.org/10.1145/3799682.3840172"
openalex_id: "https://openalex.org/W7133487756"
source_api: "openalex"
---

# Eval4Sim: An Evaluation Framework for Persona Simulation

**著者**: Eliseo Bao, Anxo Pérez, Javier Parapar, Xi Wang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人類学

## Abstract

Large Language Model personas, explicit profiles specifying a user's attributes, preferences, and behavioural tendencies, are increasingly used to simulate human conversations for user modelling, social reasoning, and behavioural analysis. Evaluating whether such simulations faithfully reflect human conversational behaviour is critical, yet current practice often relies on LLM-as-a-judge approaches that provide limited grounding in observable behaviour and produce opaque scalar scores. We present Eval4Sim, an evaluation framework that measures alignment between simulated and human conversations across three dimensions: adherence, whether persona traits are recoverable from dialogue via dense retrieval; consistency, whether a persona maintains a distinguishable stylistic identity via authorship verification; and naturalness, whether conversations exhibit human-like turn-to-turn flow via dialogue NLI. Unlike optimization-oriented metrics, each dimension takes a human corpus as a reference baseline and penalizes deviations in both directions, distinguishing insufficient persona encoding from over-optimized, unnatural behaviour. The framework is corpus-agnostic: any persona-annotated conversational dataset can serve as the reference. Evaluated over ten simulation corpora, Eval4Sim surfaces systematic trade-offs invisible to single-score methods.
