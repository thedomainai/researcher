---
title: "STaR: Bootstrapping Reasoning With Reasoning"
authors: ["Eric Zelikman", "Yuhuai Wu", "Mu, Jesse", "Goodman, Noah D."]
year: 2022
cited_by_count: 114
doi: "https://doi.org/10.48550/arxiv.2203.14465"
openalex_id: W4226369848
paper_type: preprint
evidence_kind: article
topics: ["post_training"]
landmark: true
abstract_source: "openalex"
---

# STaR: Bootstrapping Reasoning With Reasoning

**Authors**: Eric Zelikman, Yuhuai Wu, Mu, Jesse, Goodman, Noah D. | **Year**: 2022 | **Cited by**: 114 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Generating step-by-step "chain-of-thought" rationales improves language model performance on complex reasoning tasks like mathematics or commonsense question-answering. However, inducing language model rationale generation currently requires either constructing massive rationale datasets or sacrificing accuracy by using only few-shot inference. We propose a technique to iteratively leverage a small number of rationale examples and a large dataset without rationales, to bootstrap the ability to perform successively more complex reasoning. This technique, the "Self-Taught Reasoner" (STaR), relies on a simple loop: generate rationales to answer many questions, prompted with a few rationale examples; if the generated answers are wrong, try again to generate a rationale given the correct answer; fine-tune on all the rationales that ultimately yielded correct answers; repeat. We show that STaR significantly improves performance on multiple datasets compared to a model fine-tuned to directly predict final answers, and performs comparably to fine-tuning a 30$\times$ larger state-of-the-art language model on CommensenseQA. Thus, STaR lets a model improve itself by learning from its own generated reasoning.
