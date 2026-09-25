---
title: "DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research"
authors: "Linsen Zhu, Yi Shi"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-08-29T06:01:03.840740"
arxiv_id: "http://arxiv.org/abs/2608.26990v1"
source_api: "arxiv"
categories: "cs.AI, cs.MA"
---

# DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research

**著者**: Linsen Zhu, Yi Shi
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Large language models can summarize financial information, but an operational stock-research system must first assemble heterogeneous evidence, expose unavailable data and model capabilities, and control how generated opinions affect a final report. We present DSA, an evidence-aware orchestration framework for multi-market stock research with large language model (LLM) agents. DSA organizes the workflow into evidence acquisition, structured context construction, model-routed analysis, optional role and Strategy Skill reasoning, and report generation with selected context and diagnostics. A default report profile and an optional agentic profile share evidence and model-routing services but use profile-specific output validation and risk safeguards. In the agentic profile, core role outputs are processed by role-specific parsers, whereas Strategy Skill opinions undergo an additional signal-eligibility partition before synthesis; disagreement is supplied explicitly to the decision agent, followed by a conservative risk override. The reference implementation includes six regional market paths, fifteen bundled Strategy Skills, hosted and local model routes, and multiple execution and delivery surfaces. At a frozen software snapshot, a selected manifest of 1,457 portable offline backend contract tests passed; 596 cases were retrospectively mapped to six contract families central to the reported LLM-agent architecture. This evidence establishes implementation conformance for the tested software contracts, not superior report quality, forecasting accuracy, or investment returns.
