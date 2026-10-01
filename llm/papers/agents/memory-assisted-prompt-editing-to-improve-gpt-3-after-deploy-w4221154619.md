---
title: "Memory-assisted prompt editing to improve GPT-3 after deployment"
authors: ["Aman Madaan", "Niket Tandon", "Peter A. Clark", "Yiming Yang"]
year: 2022
cited_by_count: 59
doi: "https://doi.org/10.18653/v1/2022.emnlp-main.183"
openalex_id: W4221154619
paper_type: conference-paper
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# Memory-assisted prompt editing to improve GPT-3 after deployment

**Authors**: Aman Madaan, Niket Tandon, Peter A. Clark, Yiming Yang | **Year**: 2022 | **Cited by**: 59 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

Large LMs such as GPT-3 are powerful, but can commit mistakes that are obvious to humans.For example, GPT-3 would mistakenly interpret "What word is similar to good?" to mean a homophone, while the user intended a synonym.Our goal is to effectively correct such errors via user interactions with the system but without retraining, which will be prohibitively costly.We pair GPT-3 with a growing memory of recorded cases where the model misunderstood the user's intents, along with user feedback for clarification.Such a memory allows our system to produce enhanced prompts for any new query based on the user feedback for error correction on similar cases in the past.On four tasks (two lexical tasks, two advanced ethical reasoning tasks), we show how a (simulated) user can interactively teach a deployed GPT-3, substantially increasing its accuracy over the queries with different kinds of misunderstandings by the GPT-3.Our approach is a step towards the low-cost utility enhancement for very large pre-trained LMs. 1 * Equal Contribution 1 Code, data, and instructions to implement MemPrompt for a new task at https://www.memprompt.com/
