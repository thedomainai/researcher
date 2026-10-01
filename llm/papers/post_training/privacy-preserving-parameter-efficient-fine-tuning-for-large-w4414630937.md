---
title: "Privacy-Preserving Parameter-Efficient Fine-Tuning for Large Language Model Services"
authors: ["Yansong Li", "Zhixing Tan", "Paula Branco", "Yang Liu"]
year: 2025
cited_by_count: 19
doi: "https://doi.org/10.1109/taslpro.2025.3612842"
openalex_id: W4414630937
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Privacy-Preserving Parameter-Efficient Fine-Tuning for Large Language Model Services

**Authors**: Yansong Li, Zhixing Tan, Paula Branco, Yang Liu | **Year**: 2025 | **Cited by**: 19 | **Kind**: article | **Relevance**: post_training: supporting

## Abstract

Parameter-Efficient Fine-Tuning (PEFT) provides a practical way for users to customize Large Language Models (LLMs) with their private data in LLM service scenarios. However, the inherently sensitive nature of private data demands robust privacy preservation measures during the customization of LLM services to ensure data security, maintain user trust, and comply with stringent regulatory standards. Based on PEFT, we propose Privacy-Preserving Parameter-Efficient Fine-Tuning (RAPT), a framework that offers privacy protection for LLM services. RAPT adopts a local privacy approach, enabling users to privatize their data locally using a text-to-text local differential privacy mechanism. Since PEFT performs poorly when directly trained on privatized data, we introduce a novel privatized token reconstruction task that is trained jointly with the downstream task, allowing LLMs to learn better task-dependent representations. Despite the simplicity of our framework, experiments show that RAPT achieves competitive performance across tasks while providing privacy guarantees against adversaries.
