---
title: "Dynamic Haven Selection for Multi-Agent Pickup and Delivery in Constrained Warehouses"
authors: "Taisei Hirayama, Kohei Yoshida, Hiroki Sakaji, Itsuki Noda"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-08-29T06:01:03.841613"
arxiv_id: "http://arxiv.org/abs/2608.26939v1"
source_api: "arxiv"
categories: "cs.MA, cs.RO"
---

# Dynamic Haven Selection for Multi-Agent Pickup and Delivery in Constrained Warehouses

**著者**: Taisei Hirayama, Kohei Yoshida, Hiroki Sakaji, Itsuki Noda
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Space-efficient warehouse layouts often contain single-agent-width aisles and dead-end workstations where robots have few places to wait without blocking others. In Multi-Agent Pickup and Delivery (MAPD) on such constrained layouts, robots must accept online pickup-delivery tasks while preserving protected waiting locations called Havens. The Safe HAven Retreat Planner (SHARP) introduced a mechanism that extends each committed task path with a validated retreat to the agent's dedicated initial Haven, but fixed-Haven commitments can send agents toward distant Havens after deliveries. We present A-sharp (Adaptive SHARP), which changes an agent's retreat target at task assignment time. A naive switch can cause two agents to rely on the same waiting location or let another committed path pass through a location that is still occupied or reserved. A-sharp prevents these failures with an availability test for candidate Havens and a pending-release rule that keeps the previous Haven protected until the agent departs. Under explicit Haven-structure and Safe Interval Path Planning (SIPP) assumptions, we prove invariant preservation and finite-release completeness: every task in any finite release sequence is delivered in finite time. Across 72,000 runs on 14,400 paired map-agent-count-rate-seed cases over four maps, both SHARP and A-sharp complete their respective 14,400 runs. For makespan (final delivery time), a prespecified paired comparison with Holm correction over all 138 configurations with more Havens than agents finds A-sharp significantly better in 107 configurations and never significantly worse than SHARP; on the tested tree map, the median reduction is 16.7%.
