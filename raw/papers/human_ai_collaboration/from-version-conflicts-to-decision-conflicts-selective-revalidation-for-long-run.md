---
title: "From Version Conflicts to Decision Conflicts: Selective Revalidation for Long-Running AI Agents"
authors: "Yongjian Lyu, Yang Ren, Ruofei Lai, Wenting Liu"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-10T06:03:30.803905"
arxiv_id: "http://arxiv.org/abs/2609.08015v1"
source_api: "arxiv"
categories: "cs.AI, cs.DB"
---

# From Version Conflicts to Decision Conflicts: Selective Revalidation for Long-Running AI Agents

**著者**: Yongjian Lyu, Yang Ren, Ruofei Lai, Wenting Liu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Long-running AI agents may read state, reason, wait for tools or human approval, and perform an external action much later. The state that justified the action can change in the meantime. For example, after an agent proposes an 80 GBP refund under a limit of 100, a customer-name change affects only presentation metadata, a new limit of 90 still permits the refund, a limit of 50 invalidates it, and a refund issued by another worker must prevent a duplicate. Standard optimistic concurrency control and version checks can detect that previously read state has changed, but by themselves do not determine whether that change invalidates the pending action's justification. We call any detected version change a version conflict; when that change invalidates the action's justification, it is also a decision conflict. ATR records the explicit, executable conditions that justify a pending action and rechecks only the conditions affected by a change before releasing the external operation. It can retain the action, refresh non-decisive metadata, require replanning, or block execution; a target-side transaction or compare-and-set binds checked state to commit. Across 210,000 controlled executions over 15 mutation cases, ATR matched every developer-specified outcome with no false allows or blocks. In ten durable SQLite checkpoint/resume cells, it evaluated 0.6 conditions per change versus 6.0 for FullScan. At 4,093 recorded reads, ATR took 9.3 microseconds versus 2595.9 microseconds for FullScan. These deterministic results establish controlled feasibility, not production generality or automatic extraction of the required conditions.
