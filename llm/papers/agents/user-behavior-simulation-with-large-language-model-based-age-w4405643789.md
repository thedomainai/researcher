---
title: "User Behavior Simulation with Large Language Model-based Agents"
authors: ["Lei Wang", "Jingsen Zhang", "Hao Yang", "Zhi-Yuan Chen", "Jiakai Tang", "Zeyu Zhang", "Xu Chen", "Yankai Lin", "et al."]
year: 2024
cited_by_count: 54
doi: "https://doi.org/10.1145/3708985"
openalex_id: W4405643789
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# User Behavior Simulation with Large Language Model-based Agents

**Authors**: Lei Wang, Jingsen Zhang, Hao Yang, Zhi-Yuan Chen, Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, et al. | **Year**: 2024 | **Cited by**: 54 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

Simulating high quality user behavior data has always been a fundamental yet challenging problem in human-centered applications such as recommendation systems, social networks, among many others. The major difficulty of user behavior simulation originates from the intricate mechanism of human cognitive and decision processes. Recently, substantial evidence has suggested that by learning huge amounts of web knowledge, large language models (LLMs) can achieve human-like intelligence and generalization capabilities. Inspired by such capabilities, in this article, we take an initial step to study the potential of using LLMs for user behavior simulation in the recommendation domain. To make LLMs act like humans, we design profile, memory and action modules to equip them, building LLM-based agents to simulate real users. To enable interactions between different agents and observe their behavior patterns, we design a sandbox environment, where each agent can interact with the recommendation system, and different agents can converse with their friends via one-to-one chatting or one-to-many social broadcasting. In the experiments, we first demonstrate the believability of the agent-generated behaviors based on both subjective and objective evaluations. Then, to show the potential applications of our method, we simulate and study two social phenomena including (1) information cocoons and (2) user conformity behaviors. We find that controlling the personalization degree of recommendation algorithms and improving the heterogeneity of user social relations can be two effective strategies for alleviating the problem of information cocoon, and the conformity behaviors can be highly influenced by the amount of user social relations. To advance this direction, we have released our project at https://github.com/RUC-GSAI/YuLan-Rec .
