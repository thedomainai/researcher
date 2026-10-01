---
title: "Reducing Cost of LLM Agents with Trajectory Reduction"
authors: ["Yuan-an Xiao", "Pengfei Gao", "Chao Peng", "Yingfei Xiong"]
year: 2026
cited_by_count: 1
doi: "https://doi.org/10.1145/3797084"
openalex_id: W4415332588
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# Reducing Cost of LLM Agents with Trajectory Reduction

**Authors**: Yuan-an Xiao, Pengfei Gao, Chao Peng, Yingfei Xiong | **Year**: 2026 | **Cited by**: 1 | **Kind**: article | **Relevance**: agents: core

## Abstract

Multi-turn agent systems based on Large Language Models (LLMs) have become increasingly popular for software engineering tasks. While LLM agents demonstrate promising effectiveness, the high computational cost of input tokens due to ever-growing trajectories remains a significant efficiency concern. Efficiency has been largely overlooked in existing studies and agent products, and this paper addresses this gap by introducing an inference-time trajectory reduction approach that reduces computational costs. By analyzing existing agent trajectories, we demonstrate that useless, redundant, and expired information is widespread across trajectories. Such waste can be identified and reduced without compromising the agent's performance. We propose a simple yet effective trajectory reduction approach, AgentDiet, which automatically removes such waste during agent execution. We implement AgentDiet on a top-performing coding agent, and our evaluation on two LLMs and two benchmarks shows that AgentDiet can reduce input tokens by 39.9%-59.7% and the total computational cost by 21.1%-35.9%, while maintaining the same agent performance. These results indicate that inference-time trajectory reduction is a promising direction for agent systems.
