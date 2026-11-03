---
title: "TabClaw: An Interactive and Self-Evolving Agent for Spreadsheet Manipulation and Table Reasoning"
authors: "Mingyue Cheng, Shuo Yu, Daoyu Wang, Qingchuan Li, Xiaoyu Tao"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-11-04T06:39:11.951860"
doi: "https://doi.org/10.1145/3799682.3840274"
openalex_id: "https://openalex.org/W7164135767"
source_api: "openalex"
---

# TabClaw: An Interactive and Self-Evolving Agent for Spreadsheet Manipulation and Table Reasoning

**著者**: Mingyue Cheng, Shuo Yu, Daoyu Wang, Qingchuan Li, Xiaoyu Tao
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Spreadsheets and tables are widely used representations for structured data analysis, but effective analysis still requires substantial manual effort and domain expertise. Recent large language model (LLM) agents can automate parts of this process, but they often provide limited transparency into intermediate decisions, rely on implicit assumptions, struggle with multi-table comparison, and repeat similar workflows without adapting to a user's preferences. This paper presents TabClaw, an open-source interactive AI agent for spreadsheet manipulation and table reasoning. Users upload CSV or Excel files and issue natural-language requests; TabClaw clarifies ambiguous intent, exposes an editable execution plan, streams a ReAct-style tool-using analysis loop, dispatches specialist agents for parallel multi-table reasoning, and synthesizes findings with explicit consensus and uncertainty markers. Beyond one-off analysis, TabClaw records completed workflows, extracts persistent user memory, distills reusable skills from repeated tool-use patterns, supports package-style skill import, and upgrades skills from negative feedback. Experiments on spreadsheet manipulation and table reasoning benchmarks show that TabClaw improves executable task completion and reasoning performance while preserving an inspectable user workflow. This paper shows how TabClaw turns spreadsheets and tables into inspectable analytical workflows while gradually personalizing itself to recurring data-analysis tasks. Our code is available.
