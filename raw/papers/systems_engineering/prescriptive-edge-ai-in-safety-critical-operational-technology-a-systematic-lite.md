---
title: "Prescriptive Edge AI in Safety-Critical Operational Technology: A Systematic Literature Review Protocol"
authors: "Breno Henrique Nascimento de Andrade, R.A.R. Oliveira, Charles T. B. Garrocho, Fernando A. M. Silva, Paulo Henrique Mariano"
year: 2026
citations: 0
paper_type: "systematic_review"
domain: "systems_engineering"
fetched: "2026-07-22T06:02:04.523002"
doi: "https://doi.org/10.17605/osf.io/qa3pv"
openalex_id: "https://openalex.org/W7169815538"
source_api: "openalex"
---

# Prescriptive Edge AI in Safety-Critical Operational Technology: A Systematic Literature Review Protocol

**著者**: Breno Henrique Nascimento de Andrade, R.A.R. Oliveira, Charles T. B. Garrocho, Fernando A. M. Silva, Paulo Henrique Mariano
**年**: 2026 | **被引用数**: 0
**タイプ**: systematic_review | **分野**: システム工学

## Abstract

1. Background and Rationale The integration of Artificial Intelligence in Operational Technology (OT) demands strict adherence to safety interlocks and deterministic latency. While Large Language Models (LLMs) offer advanced semantic reasoning, their cloud dependence and non-deterministic nature pose risks in safety-critical industrial environments, such as mining and heavy manufacturing. This systematic literature review investigates the deployment of Small Language Models (SLMs) and Agentic Frameworks at the extreme edge. The primary goal is to map how current literature transitions from descriptive AI applications to prescriptive, safety-aware control mechanisms that prevent modal collapse and hallucinations in offline edge hardware. 2. PICOC Framework Population: Edge computing devices (Extreme Edge / Far Edge) deployed in Operational Technology (OT) networks. Intervention: Deployment of Small Language Models (SLMs), Large Language Models (LLMs), or Agentic Frameworks for semantic reasoning and decision-making. Comparison: Cloud-based inference, purely reactive/heuristic control systems, or zero-shot inference without guardrails. Outcomes: Decision accuracy, inference latency, resilience against modal collapse, and adherence to deterministic safety interlocks. Context: Safety-critical industrial environments (e.g., mining, heavy manufacturing) with restricted or non-existent connectivity. 3. Research Questions (RQs) RQ1: What are the predominant architectures for deploying language models (LLMs/SLMs) at the operational edge in safety-critical environments? RQ2: How does the current literature resolve the trade-off between the semantic reasoning capabilities of SLMs and the need for deterministic latency in industrial OT networks? RQ3: Which guardrail mechanisms or admissibility filters are utilized to prevent hallucinations and modal collapse in generative AI-based decision-making at the process control level? 4. Search Strategy The review will cover peer-reviewed literature indexed in major engineering and computing databases, specifically Scopus and IEEE Xplore. The following search string will be applied to Title, Abstract, and Keywords: ("Edge Computing" OR "Edge AI" OR "Extreme Edge" OR "Far Edge") AND ("Language Model*" OR "LLM*" OR "SLM*" OR "Agent*") AND ("Safety-critical" OR "Operational Technology" OR "Industrial" OR "Mining") 5. Eligibility Criteria Inclusion Criteria (IC): IC1: Published between 2021 and 2026. IC2: Peer-reviewed studies (journals or highly ranked conference proceedings). IC3: Studies proposing, implementing, or evaluating generative AI/agentic models on resource-constrained hardware (Edge). Exclusion Criteria (EC): EC1: Review articles, surveys, or secondary studies. EC2: Studies focused exclusively on cloud-based LLM execution with no edge component. EC3: Applications outside the industrial/OT context (e.g., healthcare, finance, education). EC4: Non-peer-reviewed pre-prints (e.g., arXiv) to ensure theoretical rigor. 6. Screening and Data Extraction Strategy The PRISMA workflow will be applied. Following duplicate removal, an initial screening of titles and abstracts will be conducted to exclude irrelevant records based on the ECs. The remaining articles will undergo full-text screening. Data extraction will be performed systematically to address the proposed RQs.
