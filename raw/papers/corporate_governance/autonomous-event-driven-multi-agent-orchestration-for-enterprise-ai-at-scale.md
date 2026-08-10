---
title: "Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale"
authors: "Harsh Rao Dhanyamraju, Leonidas Raghav, Aaron Lee"
year: 2026
citations: 0
paper_type: "primary"
domain: "corporate_governance"
fetched: "2026-06-26T06:03:07.167334"
doi: ""
openalex_id: "https://openalex.org/W7165423792"
source_api: "openalex"
---

# Autonomous Event-Driven Multi-Agent Orchestration for Enterprise AI at Scale

**著者**: Harsh Rao Dhanyamraju, Leonidas Raghav, Aaron Lee
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: コーポレートガバナンス

## Abstract

Enterprise AI aims to move toward continuous event monitoring, detection, and action across specialist agents, yet existing multi-agent systems largely assume discrete request-response workflows and remain underexplored at enterprise scale. We evaluate DAG Plan and Execute and ReAct across 208 production-derived enterprise scenarios spanning Persona (<10 agents), Department (20-80), and Enterprise (200) scales, and introduce a Task Manager for continuous operation via priority inference, related-event merging, and preemption. Results show that scale, not task complexity, dominates orchestration performance: both architectures perform well at small scale but degrade at enterprise scale as agent discovery noise becomes the primary bottleneck, with simple tasks degrading more sharply than complex ones. DAG Plan and Execute offers higher precision and structured parallelization at smaller scales, but its higher overhead worsens at enterprise scale; ReAct is more robust by handling failures incrementally. The Task Manager reduces high-priority queue latency by 14-75% and improves related-event correctness by over 20 percentage points at enterprise scale.
