---
title: "OptimAI: Optimization from Natural Language Using LLM-Powered AI Agents"
authors: "Raghav Thind, Youran Sun, Ling Liang, Haizhao Yang"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-30T06:03:26.935250"
doi: "https://doi.org/10.4208/jml.260208"
openalex_id: "https://openalex.org/W4417299421"
source_api: "openalex"
---

# OptimAI: Optimization from Natural Language Using LLM-Powered AI Agents

**著者**: Raghav Thind, Youran Sun, Ling Liang, Haizhao Yang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Optimization plays a vital role in scientific research and practical applications. However, translating a concrete optimization problem described in natural language into a mathematical formulation and selecting a suitable solver require substantial domain expertise. We introduce OptimAI, a framework for solving optimization problems described in natural language by leveraging LLM-powered AI agents, and achieve superior performance over current state-of-the-art methods. Our framework is built upon the following key roles: (1) a formulator that translates natural language problem descriptions into mathematical formulations; (2) a planner that constructs a high-level solution strategy prior to execution; and (3) a coder and a code critic capable of interacting with the environment and reflecting to refine future actions. Ablation studies confirm that all roles are essential; removing the planner or code critic results in $5.8\times$ and $3.1\times$ drops in productivity, respectively. Furthermore, we introduce UCB-based debug scheduling to dynamically switch between alternative plans, yielding an additional $3.3\times$ productivity gain. Our design emphasizes multi-agent collaboration, and our experiments confirm that combining diverse models leads to performance gains. The best OptimAI configurations attain 88.1% accuracy on the NLP4LP dataset and 82.3% on the Optibench dataset, reducing error rates by 58% and 52%, respectively, over prior best results.
