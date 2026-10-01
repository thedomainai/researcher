---
title: "ELT-Bench: An End-to-End Benchmark for Evaluating AI Agents on ELT Pipelines"
authors: ["Tengjun Jin", "Yuxuan Zhu", "Daniel D. Kang"]
year: 2025
cited_by_count: 5
doi: "https://doi.org/10.14778/3773749.3773750"
openalex_id: W7137814683
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# ELT-Bench: An End-to-End Benchmark for Evaluating AI Agents on ELT Pipelines

**Authors**: Tengjun Jin, Yuxuan Zhu, Daniel D. Kang | **Year**: 2025 | **Cited by**: 5 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

Practitioners are increasingly turning to Extract-Load-Transform (ELT) pipelines with the widespread adoption of cloud data warehouses. However, designing these pipelines often involves significant manual work to ensure correctness. Recent advances in AI-based methods, which have shown strong capabilities in data tasks, such as text-to-SQL, present an opportunity to alleviate manual efforts in developing ELT pipelines. Unfortunately, current benchmarks in data engineering only evaluate isolated tasks, such as using data tools and writing data transformation queries, leaving a significant gap in evaluating AI agents for generating end-to-end ELT pipelines. To fill this gap, we introduce ELT-Bench, an end-to-end benchmark designed to assess the capabilities of AI agents to build ELT pipelines. ELT-Bench consists of 100 pipelines, including 835 source tables and 203 data models across various domains. By simulating realistic scenarios involving the integration of diverse data sources and the use of popular data tools, ELT-Bench evaluates AI agents' abilities in handling complex data engineering workflows. AI agents must interact with databases and data tools, write code and SQL queries, and orchestrate every pipeline stage. We evaluate four representative code agents with six popular Large Language Models (LLMs) on ELT-Bench. The highest-performing agent, OpenHands CodeActAgent Claude-3.5-Sonnet, correctly generates only 11.3% of data models, with an average cost of $1.41 and 72.2 steps per pipeline. Our results demonstrate the challenges of ELT-Bench and highlight the need for a more advanced AI agent to reduce manual effort in ELT workflows.
