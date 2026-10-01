---
title: "Agents4PLC: Automating Closed-Loop PLC Code Generation and Verification in Industrial Control Systems Using LLM-Based Agents"
authors: ["Zihan Liu", "Ruinan Zeng", "Dongxia Wang", "Gengyun Peng", "Xiaoxia Liu", "Qiang Liu", "Peiyu Liu", "Wenhai Wang", "et al."]
year: 2026
cited_by_count: 9
doi: "https://doi.org/10.1109/tse.2026.3667895"
openalex_id: W7131417432
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# Agents4PLC: Automating Closed-Loop PLC Code Generation and Verification in Industrial Control Systems Using LLM-Based Agents

**Authors**: Zihan Liu, Ruinan Zeng, Dongxia Wang, Gengyun Peng, Xiaoxia Liu, Qiang Liu, Peiyu Liu, Wenhai Wang, et al. | **Year**: 2026 | **Cited by**: 9 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

In industrial control systems, the generation and verification of Programmable Logic Controller (PLC) code are crucial for ensuring operational efficiency and safety. While Large Language Models (LLMs) have made strides in automated code generation, they fall short in providing correctness guarantees and specialized support for PLC programming (which has its own programming language and clear logical structures). To address these challenges, this paper introduces Agents4PLC, a novel framework that not only automates PLC code generation but also introduces code-level verification and repair built upon an LLM-based multi-agent system, which together is capable of directly producing operational PLC code without any human interaction. To comprehensively evaluate our framework, we first establish a new benchmark specially designed for the critical area ofverifiable PLC code generation, which includes hundreds of natural language requirements, human-written and verified formal specifications, and finally reference PLC code. Then, we carefully designed a multi-agent workflow combining a set of expert agents responsible for different code generation tasks including planning, coding, validation and debugging towards generating correct PLC code. For each agent, we also incorporate optimization strategies such as Retrieval-Augmented Generation (RAG), advanced prompt engineering techniques, and Chain-of-Thought strategies which are shown to be effective to enhance the ability of these expert ‘agents’. Evaluation against the benchmark demonstrates that Agents4PLC significantly outperforms existing methods, achieving superior results across a series of increasingly rigorous evaluation metrics. This research highlights the potential of LLM agent-based code generation in real-world industrial control systems and the importance of code-level verification in generating correct code with formal guarantees.
