---
title: "Bounded Autonomy: A Budget-Constrained Framework for AI Agent Operations Toward Safety-Critical Process Environments"
authors: "M. I. Khan, M. Khanna, A. Shivkumar, T. Sharma, A. Sakala"
year: 2026
citations: 0
paper_type: "primary"
domain: "systems_engineering"
fetched: "2026-11-03T06:44:11.695665"
doi: "https://doi.org/10.2118/236401-ms"
openalex_id: "https://openalex.org/W7225042327"
source_api: "openalex"
---

# Bounded Autonomy: A Budget-Constrained Framework for AI Agent Operations Toward Safety-Critical Process Environments

**著者**: M. I. Khan, M. Khanna, A. Shivkumar, T. Sharma, A. Sakala
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: システム工学

## Abstract

Abstract Tight autonomy budgets improve safety for AI agents in process control with bounded completion cost: the pooled 95% CI for retention is 90.9 to 111.5%, admitting up to 9.1% loss in the worst case but centering on 100.8% (no net cost). For reactive architectures, safety-check rejections drop by 89% and token cost by 85% while completion change is negligible (Cohen's |d| < 0.01). We introduce Bounded Autonomy, a framework that constrains AI agent autonomy along four coordinated dimensions (tool calls, cumulative process perturbation, simulation timesteps, and checkpoint intervals), all calibrated from a single tightness parameter derived from each scenario's estimated optimal action count. Pre-execution middleware, implemented as a LangGraph StateGraph, rejects over-budget actions before they reach the process. Four agent architectures (ReAct, Reflexion, Plan-and-Execute, Hybrid) are evaluated under four budget levels across 20 Continuous Stirred-Tank Reactor (CSTR) scenarios in the OpsEnv benchmark. The evaluation totals over 7,100 experiment cells: 1,680 core Tier 1 cells, 2,800 extended-seed cells, 1,260 cross-model cells, and 1,452 supplementary cells (sensitivity, ablation, rollback, and decoupled experiments). Under tight budgets (1.2× optimal), reactive architectures retain completion (Cohen's |d| < 0.01; Bonferroni-corrected p > 0.05; 95% CI for pooled retention: 90.9 to 111.5%) with 7× wall-time reduction for ReAct and 6.7× for Reflexion. Unconstrained agents take ∼5× more actions than necessary, and these excess actions are counterproductive: in the most pronounced case (scenario B04), a ReAct agent improves from 0.041 to 0.950 completion under budget constraints. Conversely, multi-step optimization tasks (e.g., A04 under ReAct) can lose up to 73 percentage points. Cross-model validation with Qwen 2.5 32B and Llama 3.1 8B (1,260 cells across up to 20 scenarios) confirms the directional violation-reduction effect at reduced magnitude (25% vs. 89% for Tier 1). AI-assisted tools were used in the experimental evaluation; all outputs were reviewed and validated by the authors.
