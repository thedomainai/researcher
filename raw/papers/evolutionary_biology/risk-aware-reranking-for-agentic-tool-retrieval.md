---
title: "Risk-Aware Reranking for Agentic Tool Retrieval"
authors: "Qinfei Li, Xiaoxuan Dong, Jin Zhang, 玉徳 许, Wenhao Deng"
year: 2026
citations: 0
paper_type: "primary"
domain: "evolutionary_biology"
fetched: "2026-11-04T06:27:34.497122"
doi: "https://doi.org/10.1145/3799682.3840706"
openalex_id: "https://openalex.org/W7204192955"
source_api: "openalex"
---

# Risk-Aware Reranking for Agentic Tool Retrieval

**著者**: Qinfei Li, Xiaoxuan Dong, Jin Zhang, 玉徳 许, Wenhao Deng
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 進化生物学・文化進化

## Abstract

Tool retrieval determines which external tools are exposed to an LLM agent for a user query or task, making retrieval a critical pre-execution safety boundary. Unlike document retrieval, tool retrieval exposes executable actions: a tool that is useful for one task may be unnecessary or risky for another. However, existing tool-retrieval methods primarily optimize semantic relevance, and safety evaluations often focus on failures after tool execution rather than risks introduced during retrieval. We study risk-aware tool retrieval, where the goal is to retrieve useful tools while reducing exposure to higher-risk tools. We propose a lightweight reranking framework on top of a frozen first-stage retriever. The framework models query-conditioned relevance and tool-level exposure risk separately, combines them through an explicit parameter controlling the tradeoff between safety and utility, smooths scores over a ToolGraph, and optionally applies rule-based safety constraints. To support retrieval-time safety evaluation, we annotate 6,108 tools across UltraTool and Seal-Tools with five ordinal risk levels and define metrics that measure risky-tool exposure in the top-$k$ results. Experiments on UltraTool and Seal-Tools show that our approach improves the relevance--safety tradeoff over relevance-only retrievers and reranking baselines, with the rule-filtered variant providing a conservative operating point for safety-critical deployments. These findings indicate that retrieval-stage filtering can reduce the candidate action space exposed to agents before execution, complementing downstream tool-use safeguards. The code and supplementary materials are available at: https://github.com/qli447/risk-aware-tool-retrieval-release.
