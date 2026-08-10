---
title: "High-quality generation of dynamic game content via small language models: A proof of concept"
authors: "Morten I. K. Munk, Arturo Valdivia, Paolo Burelli"
year: 2026
citations: 0
paper_type: "primary"
domain: "strategic_management"
fetched: "2026-07-31T06:07:13.034574"
doi: "https://doi.org/10.1145/3815598.3815605"
openalex_id: "https://openalex.org/W7162004637"
source_api: "openalex"
---

# High-quality generation of dynamic game content via small language models: A proof of concept

**著者**: Morten I. K. Munk, Arturo Valdivia, Paolo Burelli
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 経営戦略

## Abstract

Large language models (LLMs) offer promise for dynamic game content generation, but they face critical barriers, including narrative incoherence and high operational costs. Due to their large size, they are often accessed in the cloud, limiting their application in offline games. Many of these practical issues are solved by pivoting to small language models (SLMs), but existing studies using SLMs have resulted in poor output quality. We propose a strategy of achieving high-quality SLM generation through aggressive fine-tuning on deliberately scoped tasks with narrow context, constrained structure, or both. In short, more difficult tasks require narrower scope and higher specialization to the training corpus. Training data is synthetically generated via a DAG-based approach, grounding models in the specific game world. Such models can form the basis for agentic networks designed around the narratological framework at hand, representing a more practical and robust solution than cloud-dependent LLMs. To validate this approach, we present a proof-of-concept focusing on a single specialized SLM as the fundamental building block. We introduce a minimal RPG loop revolving around rhetorical battles of reputations, powered by this model. We demonstrate that a simple retry-until-success strategy reaches adequate quality (as defined by an LLM-as-a-judge scheme) with predictable latency suitable for real-time generation. While local quality assessment remains an open question, our results demonstrate feasibility for real-time generation under typical game engine constraints.
