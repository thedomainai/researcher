---
title: "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting"
authors: ["Miles Turpin", "Julian Michael", "Ethan Perez", "Sam Bowman"]
year: 2023
cited_by_count: 1739
doi: null
openalex_id: arxiv-2305.04388
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: true
abstract_source: "semantic_scholar"
---

# Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting

**Authors**: Miles Turpin, Julian Michael, Ethan Perez, Sam Bowman | **Year**: 2023 | **Cited by**: 1739 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Large Language Models (LLMs) can achieve strong performance on many tasks by producing step-by-step reasoning before giving a final output, often referred to as chain-of-thought reasoning (CoT). It is tempting to interpret these CoT explanations as the LLM's process for solving a task. This level of transparency into LLMs' predictions would yield significant safety benefits. However, we find that CoT explanations can systematically misrepresent the true reason for a model's prediction. We demonstrate that CoT explanations can be heavily influenced by adding biasing features to model inputs--e.g., by reordering the multiple-choice options in a few-shot prompt to make the answer always"(A)"--which models systematically fail to mention in their explanations. When we bias models toward incorrect answers, they frequently generate CoT explanations rationalizing those answers. This causes accuracy to drop by as much as 36% on a suite of 13 tasks from BIG-Bench Hard, when testing with GPT-3.5 from OpenAI and Claude 1.0 from Anthropic. On a social-bias task, model explanations justify giving answers in line with stereotypes without mentioning the influence of these social biases. Our findings indicate that CoT explanations can be plausible yet misleading, which risks increasing our trust in LLMs without guaranteeing their safety. Building more transparent and explainable systems will require either improving CoT faithfulness through targeted efforts or abandoning CoT in favor of alternative methods.
