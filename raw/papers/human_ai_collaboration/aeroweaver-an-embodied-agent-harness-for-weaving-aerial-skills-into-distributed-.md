---
title: "AeroWeaver: An Embodied-Agent Harness for Weaving Aerial Skills into Distributed, Adaptive Swarm Execution"
authors: "Jiabin Lou, Yirong Yang, Haopeng Wang, Xuxin Lv, Xinyu Liu"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-18T06:03:21.551370"
arxiv_id: "http://arxiv.org/abs/2609.18520v1"
source_api: "arxiv"
categories: "cs.AI"
---

# AeroWeaver: An Embodied-Agent Harness for Weaving Aerial Skills into Distributed, Adaptive Swarm Execution

**著者**: Jiabin Lou, Yirong Yang, Haopeng Wang, Xuxin Lv, Xinyu Liu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Collective intelligence is a collaborative autonomy paradigm in which multiple agents pursue shared objectives through local perception, information exchange, and coordinated action. UAV swarms embody this paradigm by coordinating multiple vehicles in tasks such as search, inspection, and tracking. Recent advances in large language model (LLM) agents have strengthened natural-language task understanding and high-level planning, providing a flexible semantic interface between mission descriptions and collective behavior. While these advances expand semantic reasoning, applying LLM agents to UAV swarms raises challenges in grounding model decisions in executable capabilities, reconciling global task reasoning with distributed execution, and using mission-specific experience for continual adaptation. To address these challenges, we introduce AeroWeaver, an embodied-agent harness that weaves individual UAV skills into coordinated mission-level behavior. AeroWeaver connects semantic decisions to governed skills, organizes role-conditioned local agents for distributed coordination, and uses role-indexed state-action-reward experience to refine skill selection online. Experiments and runtime validation show that AeroWeaver maintains valid skill execution under tested conditions and supports body-local multi-UAV operation without a central agent generating joint actions from global context, while reward-guided online updates provide a training-free path for adaptive learning swarm agents from accumulated execution experience. Code: https://github.com/Admire-ljb/AeroWeaver.
