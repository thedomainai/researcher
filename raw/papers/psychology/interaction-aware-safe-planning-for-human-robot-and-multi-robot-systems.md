---
title: "Interaction-Aware Safe Planning for Human-Robot and Multi-Robot Systems"
authors: "Haoyi Wang"
year: 2026
citations: 0
paper_type: "primary"
domain: "psychology"
fetched: "2026-05-03T06:01:55.619578"
doi: ""
openalex_id: "https://openalex.org/W7158434570"
source_api: "openalex"
---

# Interaction-Aware Safe Planning for Human-Robot and Multi-Robot Systems

**著者**: Haoyi Wang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 心理学

## Abstract

Robots operating in shared environments must interact safely not only with static obstacles but also with other decision-making agents, including humans and other robots. In such settings, both safety and task completion depend on the ability to reason about interaction. Two major challenges arise. In human-robot interaction, future human behavior depends on latent internal factors, such as attentiveness and behavioral style, that are not directly observable to the robot. In multi-robot systems, decentralized reactive navigation can fail in cluttered environments when reciprocal interactions create deadlocks that prevent progress through narrow passages or bottlenecks. This thesis investigates these two challenges from a unified interaction-aware perspective. The first part of the thesis develops a human-aware planning framework in which the robot maintains and updates beliefs over latent human internal states based on observed behavior. These beliefs guide an adaptive interval-based sampling procedure for reachability analysis, which produces uncertainty-aware predictions of future human motion. The resulting reachable sets are incorporated into safety-constrained planning, allowing the robot to remain safe under uncertainty while improving efficiency as interaction reveals additional information about the human. The second part of the thesis addresses multi-robot deadlocks in long-range navigation. It develops a hybrid framework that combines reinforcement-learning-based decentralized navigation with on-demand, locally confined multi-agent path finding. A deadlock detector identifies stalled interactions and selectively triggers short-horizon coordinated replanning for only the affected robots, while the remaining robots continue decentralized execution. This design preserves the efficiency of reactive navigation in ordinary settings while restoring progress in topologically constrained scenarios. Together, these two case studies support a common thesis: safe autonomy in shared environments requires planning methods that explicitly model interaction structure rather than treating other agents as passive disturbances. By combining human-aware uncertainty modeling with deadlock-resilient multi-robot coordination, this thesis advances a modular framework for safer and more reliable robot autonomy in dynamic multi-agent environments.
