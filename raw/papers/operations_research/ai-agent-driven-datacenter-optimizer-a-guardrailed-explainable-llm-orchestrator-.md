---
title: "AI Agent-Driven Datacenter Optimizer: A Guardrailed, Explainable LLM Orchestrator for Cloud Platform Management"
authors: "Jay Dighore, Vedant Gaidhane, Ayush Dumbhare, Kunal Kanchankar"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-10-23T08:10:51.798748"
doi: "https://doi.org/10.22214/ijraset.2026.85243"
openalex_id: "https://openalex.org/W7223177712"
source_api: "openalex"
---

# AI Agent-Driven Datacenter Optimizer: A Guardrailed, Explainable LLM Orchestrator for Cloud Platform Management

**著者**: Jay Dighore, Vedant Gaidhane, Ayush Dumbhare, Kunal Kanchankar
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Modern datacenters must balance three objectives that often conflict: keeping hardware within safe thermal limits, meeting latency expectations for high-priority work, and reducing the cost and carbon footprint of electricity. Traditional controllers handle these with fixed rules or heavily engineered optimization pipelines. This paper presents Grid Control, an autonomous datacenter orchestration system in which a large language model (LLM) acts as the decision-making agent. A simulated multi-region datacenter (5 regions, 15 servers, 60 chipsets) streams telemetry every second. Every decision interval the agent receives a frozen telemetry window and selects exactly one action from a small, closed vocabulary: shift_within_server, shift_within_region, migrate_region, or pass. A prioritized policy ranks overheating first, latency and load balance second, and cost and carbon third. Safety is enforced outside the model by a guardrail layer that routes high-criticality or administratorprohibited actions to a human approval queue. A feedback loop returns measured outcomes of past actions to the prompt as incontext learning signal, and a scope-restricted explainability module answers operator questions about the agent's behavior. Over 20 paired simulation runs, a deterministic stand-in for the agent's policy reduced time spent above the 68 °C threshold by about 24% and carbon-weighted load by about 9% relative to a no-agent baseline, with about 3% lower electricity cost. LLM-inthe-loop evaluation is left to future work. The contribution is an architecture and a reproducible testbed for studying safe, explainable, LLM-driven infrastructure control.
