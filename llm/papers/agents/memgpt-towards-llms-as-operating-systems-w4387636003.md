---
title: "MemGPT: Towards LLMs as Operating Systems"
authors: ["Charles Packer", "Sarah Wooders", "Kevin Lin", "Vivian Fang", "Shishir G. Patil", "Stoica, Ion", "Joseph E. Gonzalez"]
year: 2023
cited_by_count: 58
doi: "https://doi.org/10.48550/arxiv.2310.08560"
openalex_id: W4387636003
paper_type: preprint
evidence_kind: article
topics: ["agents"]
landmark: true
abstract_source: "openalex"
---

# MemGPT: Towards LLMs as Operating Systems

**Authors**: Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Stoica, Ion, Joseph E. Gonzalez | **Year**: 2023 | **Cited by**: 58 | **Kind**: article | **Relevance**: agents: core

## Abstract

Large language models (LLMs) have revolutionized AI, but are constrained by limited context windows, hindering their utility in tasks like extended conversations and document analysis. To enable using context beyond limited context windows, we propose virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory. Using this technique, we introduce MemGPT (Memory-GPT), a system that intelligently manages different memory tiers in order to effectively provide extended context within the LLM's limited context window, and utilizes interrupts to manage control flow between itself and the user. We evaluate our OS-inspired design in two domains where the limited context windows of modern LLMs severely handicaps their performance: document analysis, where MemGPT is able to analyze large documents that far exceed the underlying LLM's context window, and multi-session chat, where MemGPT can create conversational agents that remember, reflect, and evolve dynamically through long-term interactions with their users. We release MemGPT code and data for our experiments at https://memgpt.ai.
