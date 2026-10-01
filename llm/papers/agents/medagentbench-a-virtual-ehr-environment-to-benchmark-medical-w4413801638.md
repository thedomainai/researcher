---
title: "MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents"
authors: ["Yixing Jiang", "Kameron Collin Black", "Gloria Geng", "Danny Park", "James Zou", "Andrew Y. Ng", "Jonathan H. Chen"]
year: 2025
cited_by_count: 60
doi: "https://doi.org/10.1056/aidbp2500144"
openalex_id: W4413801638
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents

**Authors**: Yixing Jiang, Kameron Collin Black, Gloria Geng, Danny Park, James Zou, Andrew Y. Ng, Jonathan H. Chen | **Year**: 2025 | **Cited by**: 60 | **Kind**: article | **Relevance**: agents: core

## Abstract

BACKGROUND Recent large language models (LLMs) have demonstrated significant advancements, particularly in their ability to serve as agents, thereby surpassing their traditional role as chatbots.These agents can leverage their planning and tool utilization capabilities to address tasks specified at a high level.This suggests new potential to reduce the burden of administrative tasks and address current health care staff shortages.However, a standardized dataset to benchmark the agent capabilities of LLMs in medical applications is currently lacking, making it difficult to evaluate their performance on complex tasks in interactive health care environments. METHODSTo address this gap in the deployment of agentic artificial intelligence (AI) in health care, we introduce MedAgentBench, a broad evaluation suite designed to assess the agent capabilities of LLMs within medical records contexts.MedAgentBench encompasses 300 patient-specific clinically derived tasks from 10 categories written by human physicians, realistic profiles of 100 patients with over 700,000 data elements, a Fast Healthcare Interoperability Resources-compliant interactive environment, and an accompanying codebase.The environment uses standard application programming interfaces and communication infrastructure used in modern electronic health record (EHR) systems so that it can be easily migrated into live EHR systems. RESULTSMedAgentBench presents an unsaturated agent-oriented benchmark at which current state-of-the-art LLMs exhibit some ability to succeed.The best model (Claude 3.5 Sonnet v2) achieves a success rate of 69.67%.However, there is still substantial room for improvement, which gives the community a clear direction for future optimization efforts.Furthermore, there is significant variation in performance across task categories.CONCLUSIONS Agent-based task frameworks and benchmarks are the necessary next step to advance the potential and capabilities for effectively improving and integrating AI systems into clinical workflows.MedAgentBench establishes this and is publicly available at https://github .com /stanfordmlgroup /MedAgentBench, offering a valuable framework for model developers to track progress and drive continuous improvements in the agent capabilities of LLMs within the medical domain.
