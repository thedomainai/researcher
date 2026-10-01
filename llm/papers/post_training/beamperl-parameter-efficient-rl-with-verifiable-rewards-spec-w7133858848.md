---
title: "BeamPERL: parameter-efficient RL with verifiable rewards specializes compact LLMS for structured beam mechanics reasoning"
authors: ["Tarjei Paule Hage", "Markus J. Buehler"]
year: 2026
cited_by_count: 0
doi: "https://doi.org/10.1088/2632-2153/ae98e4"
openalex_id: W7133858848
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# BeamPERL: parameter-efficient RL with verifiable rewards specializes compact LLMS for structured beam mechanics reasoning

**Authors**: Tarjei Paule Hage, Markus J. Buehler | **Year**: 2026 | **Cited by**: 0 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Abstract Can reinforcement learning with hard, verifiable rewards teach a compact language model to reason about physics, or does it primarily learn to pattern-match toward correct answers? While recent RLVR and group relative policy optimization-based approaches have substantially advanced mathematical reasoning in compact language models, their application to structured engineering domains (where ground-truth solutions are analytically exact and symbolically verifiable) remains largely unexplored. We address this gap by training a 1.5B-parameter reasoning model on beam statics, a classic engineering problem, using parameter-efficient RLVR fine-tuning (PE-RLVR-FT) with binary correctness rewards from symbolic solvers, without teacher-generated reasoning traces. On a 123-sample, six-category evaluation set, the best BeamPERL checkpoint reaches 43.6 ± 0.5 % Pass@1 and 72.1 ± 0.5 % Pass@7 (mean ± standard deviation over three evaluation seeds), improving over the base model by 30.6 and 22.8 percentage points, respectively. However, the learned competence is anisotropic: the model generalizes compositionally (more loads, distributed loads, length scaling) but fails under topological shifts (moved supports) and applied moments that require the same equilibrium equations. Intermediate checkpoints yield the strongest reasoning, while continued optimization degrades robustness even as the training reward is maintained. These findings reveal a key limitation of outcome-level alignment: reinforcement learning with exact physics rewards induces procedural solution templates rather than internalization of governing equations. The precision of the reward signal—even when analytically exact—does not by itself guarantee transferable physical reasoning. Our results suggest that verifiable rewards may need to be paired with structured reasoning scaffolding to move beyond template matching toward robust scientific reasoning.
