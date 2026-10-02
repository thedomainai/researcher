---
title: "Data Sherpa: An AI-Powered Assistant for Scientific Collaboration Knowledge Management"
authors: "Fabian Araneda Baltierra, F. Menanteau"
year: 2026
citations: 0
paper_type: "primary"
domain: "organization_science"
fetched: "2026-10-03T06:02:01.303984"
doi: "https://doi.org/10.5281/zenodo.22804319"
openalex_id: "https://openalex.org/W7213577181"
source_api: "openalex"
---

# Data Sherpa: An AI-Powered Assistant for Scientific Collaboration Knowledge Management

**著者**: Fabian Araneda Baltierra, F. Menanteau
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 組織科学

## Abstract

Large scientific collaborations face a persistent challenge: critical knowledge is scattered across hundreds of people, documents, datasets, and communication archives, creating steep learning curves and inefficiencies that disproportionately affect early-career researchers and newcomers. Senior scientists are repeatedly drawn away from high-impact research to answer the same operational questions, while valuable institutional knowledge risks being lost as collaborations sunset. Data Sherpa is an open-source, AI-powered assistant designed to address these challenges by providing researchers with fast, accurate, and context-aware access to collaboration-specific knowledge. The current proof-of-concept demonstrates retrieval-augmented generation (RAG) over Dark Energy Survey (DES) documentation, publications, and technical material, using vector embedding and semantic search with a PostgreSQL-based vector store (pgvector). Since submission, the project has shifted architecture: rather than continue building orchestration, multi-agent coordination, and model-serving infrastructure from scratch, we are migrating Data Sherpa onto Open WebUI, an actively maintained open-source platform providing local model deployment, containerized infrastructure, multi-agent workflows, and code generation. This migration runs on Jetstream2, allocated through NSF ACCESS, advancing our goal of full data sovereignty. The system's most distinguishing design goal, its ability to explicitly acknowledge uncertainty rather than produce a fluent but unsupported answer, is not yet implemented. Its conceptual design and an evaluation plan for measuring retrieval accuracy and abstention reliability are under active development, informed by the Open WebUI migration, and will be presented at the conference. Beyond the DES proof-of-concept, Data Sherpa has confirmed deployments planned with the South Pole Telescope (SPT) project, the Terahertz Intensity Mapper (TIM), and environmental and ecological datasets at the University of Illinois' Prairie Research Institute (PRI), demonstrating the framework's domain-agnostic design across projects within and beyond the Center for Astrophysical Surveys (CAPS) at NCSA.
