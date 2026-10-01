---
title: "Self-Collaboration Code Generation via ChatGPT"
authors: ["Yihong Dong", "Xue Jiang", "Zhi Gang Jin", "Ge Li"]
year: 2024
cited_by_count: 219
doi: "https://doi.org/10.1145/3672459"
openalex_id: W4399557965
paper_type: article
evidence_kind: article
topics: ["applications", "agents"]
landmark: false
abstract_source: "openalex"
---

# Self-Collaboration Code Generation via ChatGPT

**Authors**: Yihong Dong, Xue Jiang, Zhi Gang Jin, Ge Li | **Year**: 2024 | **Cited by**: 219 | **Kind**: article | **Relevance**: applications: core; agents: core

## Abstract

Although large language models (LLMs) have demonstrated remarkable code-generation ability, they still struggle with complex tasks. In real-world software development, humans usually tackle complex tasks through collaborative teamwork, a strategy that significantly controls development complexity and enhances software quality. Inspired by this, we present a self-collaboration framework for code generation employing LLMs, exemplified by ChatGPT. Specifically, through role instructions, (1) Multiple LLM agents act as distinct “experts,” each responsible for a specific subtask within a complex task; (2) Specify the way to collaborate and interact, so that different roles form a virtual team to facilitate each other’s work, ultimately the virtual team addresses code generation tasks collaboratively without the need for human intervention. To effectively organize and manage this virtual team, we incorporate software-development methodology into the framework. Thus, we assemble an elementary team consisting of three LLM roles (i.e., analyst, coder, and tester) responsible for software development’s analysis, coding, and testing stages. We conduct comprehensive experiments on various code-generation benchmarks. Experimental results indicate that self-collaboration code generation relatively improves 29.9–47.1% Pass@1 compared to the base LLM agent. Moreover, we showcase that self-collaboration could potentially enable LLMs to efficiently handle complex repository-level tasks that are not readily solved by the single LLM agent.
