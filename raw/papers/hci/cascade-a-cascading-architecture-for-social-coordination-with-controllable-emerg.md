---
title: "CASCADE: A Cascading Architecture for Social Coordination with Controllable Emergence at Low Cost"
authors: "Yizhi Xu"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-04-06T13:20:41.882586"
arxiv_id: "http://arxiv.org/abs/2604.03091v1"
source_api: "arxiv"
categories: "cs.HC"
---

# CASCADE: A Cascading Architecture for Social Coordination with Controllable Emergence at Low Cost

**著者**: Yizhi Xu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

Creating scalable and believable game societies requires balancing authorial control with computational cost. Existing scripted NPC systems scale efficiently but are often rigid, whereas fully LLM-driven agents can produce richer social behavior at a much higher runtime cost. We present CASCADE, a three-layer architecture for low-cost, controllable social coordination in sandbox-style game worlds. A Macro State Director (Level 1) maintains discrete-time world-state variables and macro-level causal updates, while a modular Coordination Hub decomposes state changes through domain-specific components (e.g., professional and social coordination) and routes the resulting directives to tag-defined groups. Then Tag-Driven NPCs (Level 3) execute responses through behavior trees and local state/utility functions, invoking large language models only for on-demand player-facing interactions. We evaluate CASCADE through multiple micro-scenario prototypes and trace-based analysis, showing how a shared macro event can produce differentiated yet logically constrained NPC behaviors without per-agent prompting in the main simulation loop. CASCADE provides a modular foundation for scalable social simulation and future open-world authoring tools.
