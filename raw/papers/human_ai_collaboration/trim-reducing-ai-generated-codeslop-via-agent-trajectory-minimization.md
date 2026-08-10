---
title: "TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization"
authors: "Alex Mathai, Shobini Iyer, Aleksandr Nogikh, Petros Maniatis, Franjo Ivancic"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-07-22T06:02:24.956650"
arxiv_id: "http://arxiv.org/abs/2607.18161v1"
source_api: "arxiv"
categories: "cs.SE, cs.AI, cs.OS"
---

# TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization

**著者**: Alex Mathai, Shobini Iyer, Aleksandr Nogikh, Petros Maniatis, Franjo Ivancic
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Coding agents are increasingly used to accelerate code generation in many downstream tasks, such as fixing bugs, building applications, and prototyping. However, despite their value as coding assistants, agent-generated code tends to be larger and more verbose than the corresponding human-written implementation. In this work, we show that the cause lies in the agent's own search process: while iterating toward a passing solution, an agent accumulates speculative edits, abandoned hypotheses, and temporary changes that persist into the final patch. This may seem harmless for a single patch, but the problem compounds as agents take responsibility for ever-larger portions of a codebase-a codebase that was once minimal and well-maintained slowly accumulates redundancy faster than it can be cleaned up, drifting to a state that is harder to maintain. Given the magnitude of this problem, we take a step towards alleviating this issue. First, we formally define this phenomenon as CodeSlop-the residual and functionally unnecessary edits commonly seen in AI-generated code. We then introduce our algorithm TRIM (Trajectory-guided Redundancy Identification and Minimization). Rather than minimizing CodeSlop directly, TRIM instead minimizes agent trajectories. As we show empirically, this indirect technique of minimizing CodeSlop is highly effective: TRIM cuts CodeSlop by 17.9%-32.9% across agentic scaffolds, with negligible performance regression. TRIM is also highly efficient, requiring roughly half the validation cost of algorithmic baselines such as Delta Debugging.
