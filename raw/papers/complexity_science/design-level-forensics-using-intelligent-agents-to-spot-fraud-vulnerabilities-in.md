---
title: "DESIGN-LEVEL FORENSICS: USING INTELLIGENT AGENTS TO SPOT FRAUD VULNERABILITIES IN SAP CONFIGURATION"
authors: "Wolfgang Raeder, Jelena Demko-Rihter"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-10-18T13:16:00.306285"
doi: "https://doi.org/10.54318/czf.2026.wr.012"
openalex_id: "https://openalex.org/W7222740394"
source_api: "openalex"
---

# DESIGN-LEVEL FORENSICS: USING INTELLIGENT AGENTS TO SPOT FRAUD VULNERABILITIES IN SAP CONFIGURATION

**著者**: Wolfgang Raeder, Jelena Demko-Rihter
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Analyzing configurations extracted from enterprise IT systems such as SAP to identify design-level fraud risks and control weaknesses traditionally requires auditors and consultants with deep expertise in internal data structures and business logic. This dependency creates a bottleneck, particularly for less experienced practitioners. This practice-based design paper presents an approach, developed in cooperation with KPMG, that uses large language models (LLMs) to support and partially automate this forensic design analysis, thereby lowering the expertise threshold required for SAP configuration audits. The solution follows a two-stage architecture. First, raw configuration data extracted from SAP systems is processed by topic-specific evaluation routines that structure and pre-aggregate relevant information. Second, the compact results are combined with tailored prompts and transmitted via a REST interface to a language model, which identifies potential fraud vulnerabilities and configuration weaknesses and aggregates its granular responses into control-specific, audit-ready findings. An exploratory pilot in three real audits indicated time savings of about 20–30%, driven mainly by reduced documentation effort. Extending this architecture toward Agentic AI, the solution is embedded as a Model Context Protocol (MCP) server within an autonomous agent, which prepares the full workflow from data collection and analysis to the documentation of results, while approval and client communication remain with the auditor. The paper discusses the design, implementation, preliminary evaluation and professional safeguards of this approach and reflects on its implications for accessibility and scalability of designlevel forensics in SAP environments.
