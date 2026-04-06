---
title: "DevMemory: A Structured Memory Management Architecture for Persistent Knowledge in AI Coding Agents"
authors: "Abhijeet Patil"
year: 2026
citations: 0
paper_type: "primary"
domain: "organization_science"
fetched: "2026-04-06T14:01:17.451353"
doi: "https://doi.org/10.5281/zenodo.19324351"
openalex_id: "https://openalex.org/W7143316772"
source_api: "openalex"
---

# DevMemory: A Structured Memory Management Architecture for Persistent Knowledge in AI Coding Agents

**著者**: Abhijeet Patil
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 組織科学

## Abstract

AI coding agents operate without persistent memory; useful outputs produced in one session are unavailable in the next, and information from one project never transfers to another. We present DevMemory, a structured memory management architecture that brings trust-scored, cross-scope knowledge retrieval to AI coding agents. Borrowing organizational categories from Tulving’s (1972) episodic-semantic-procedural taxonomy in cognitive psychology, DevMemory classifies stored information into three types across three hierarchical scopes (agent, project, organizational), governed by a formal trust scoring model with temporal decay, contradiction handling, and reinforcement-based promotion. The architecture introduces four key contributions: (1) a principled adaptation of cognitive memory categories to software development retrieval contexts, (2) a continuous trust function that computes information reliability as a product of provenance, recency, contradiction, and reinforcement signals, (3) a token-efficient retrieval pipeline that deduplicates and budget-packs results to maximize information density within context window constraints, and (4) a tool interface design that consolidates 17 operations into 5 LLM-optimized tools, reducing system prompt overhead by 33%. The system is implemented as an open-source MCP (Model Context Protocol) server, validated by 325 automated tests spanning unit, integration, efficacy, effectiveness benchmarks, and performance tests. An effectiveness benchmark on a 29-memory corpus with 8 evaluation queries demonstrates: 87.5% cross-session information reuse rate, Mean Reciprocal Rank of 0.875, trust-sorted retrieval improving average result quality by 8.6% over unsorted baselines, complete separation between verified and contradicted entries (0.78 trust gap), and 27-91% token savings under budget constraints while maintaining or improving result quality. We explicitly distinguish our engineering use of cognitive taxonomy labels from the phenomenological and mechanistic properties of biological memory systems, and discuss the implications of this gap.
