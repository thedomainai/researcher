---
title: "GraphMind: From Operational Traces to Self-Evolving Workflow Automation"
authors: "Yiwen Zhu, Joyce Cahoon, Anna Pavlenko, Qiushi Bai, Nima Shahbazi"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-04T06:22:07.036780"
doi: "https://doi.org/10.1145/3799682.3840085"
openalex_id: "https://openalex.org/W7161729938"
source_api: "openalex"
---

# GraphMind: From Operational Traces to Self-Evolving Workflow Automation

**著者**: Yiwen Zhu, Joyce Cahoon, Anna Pavlenko, Qiushi Bai, Nima Shahbazi
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Complex operational workflows coordinating personnel, tools, and information are central to system operations, yet end-to-end automation remains challenging due to extensive human input requirements and limited ability to adapt over time. We present GraphMind, a system that constructs, executes, and evolves action-centric workflow graphs with minimal human effort. The system operates in three phases. First, a scalable offline pipeline extracts structured workflow graphs from large volumes of human resolution traces, capturing problems, actions, and their causal relationships. Second, an online multi-agent traversal engine navigates the graph to dynamically construct and execute workflows, combining graph-guided retrieval with LLM-driven reasoning at each step. Third, Adaptive Traversal Reinforcement (ATR) reinforces successful traversal paths, enabling execution-informed graph adaptation. GraphMind has been deployed across four production cloud database services for incident investigation. Evaluated on 93 held-out incidents and validated via blind expert review, the system outperforms an Agentic Summary-RAG baseline in mitigation reach, hallucination rate, and diagnostic throughput while requiring 8x less retrieval context. The ATR layer reduces hallucination rate by 26%, demonstrating that workflow graphs can learn from execution feedback. A 12-week field study confirms practical value: 97% of scored conversations yield actionable results within interactive latency.
