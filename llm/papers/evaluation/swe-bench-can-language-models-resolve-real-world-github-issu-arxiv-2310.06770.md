---
title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
authors: ["Carlos E. Jimenez", "John Yang", "Alexander Wettig", "Shun-Yu Yao", "Kexin Pei", "Ofir Press", "Karthik R. Narasimhan"]
year: 2023
cited_by_count: 4008
doi: null
openalex_id: arxiv-2310.06770
paper_type: article
evidence_kind: article
topics: ["evaluation"]
landmark: true
abstract_source: "semantic_scholar"
---

# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**Authors**: Carlos E. Jimenez, John Yang, Alexander Wettig, Shun-Yu Yao, Kexin Pei, Ofir Press, Karthik R. Narasimhan | **Year**: 2023 | **Cited by**: 4008 | **Kind**: article | **Relevance**: evaluation: core

## Abstract

Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities. We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models. To this end, we introduce SWE-bench, an evaluation framework consisting of $2,294$ software engineering problems drawn from real GitHub issues and corresponding pull requests across $12$ popular Python repositories. Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue. Resolving issues in SWE-bench frequently requires understanding and coordinating changes across multiple functions, classes, and even files simultaneously, calling for models to interact with execution environments, process extremely long contexts and perform complex reasoning that goes far beyond traditional code generation tasks. Our evaluations show that both state-of-the-art proprietary models and our fine-tuned model SWE-Llama can resolve only the simplest issues. The best-performing model, Claude 2, is able to solve a mere $1.96$% of the issues. Advances on SWE-bench represent steps towards LMs that are more practical, intelligent, and autonomous.
