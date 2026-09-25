---
title: "Emergent Charging Coordination in Electric Delivery Fleets"
authors: "Javier Vales-Alonso, Juan J. Alcaraz"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-10T06:01:05.666866"
arxiv_id: "http://arxiv.org/abs/2609.07689v1"
source_api: "arxiv"
categories: "cs.LG, cs.MA, cs.NE, eess.SY"
---

# Emergent Charging Coordination in Electric Delivery Fleets

**著者**: Javier Vales-Alonso, Juan J. Alcaraz
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

In electric delivery fleets, mid-shift charging is non-trivial: each vehicle must decide when, where and how much to charge to finish on time with battery above a safety floor. The choices are coupled: queues build where too many vehicles pick the same station. Prior work resolves this coupling with central dispatching, precomputed schedules or reservations, machinery that charging infrastructure rarely supports. Instead, we use a family of learning agents under purely local control: every vehicle runs the same policy, deciding alone from its time budgets and broadcast station occupancies, leading to emergent coordination without central control or messaging. We validate this paradigm in simulation on real OpenStreetMap networks of twenty cities, each with a frozen scenario calibrated by an omniscient Oracle (99.5% of shifts completed on time), whereas a naive greedy rule (nearest station on low battery) completes just 73%. Agents trained with neuroevolution (NEAT) and policy gradients (PPO) on four cities and deployed zero-shot across all twenty, sixteen never seen in training, complete 96.8% and 98.6% of shifts, with the policy-gradient controllers proving more robust when demand or vehicle characteristics drift beyond the trained regime. In contrast, tuned threshold heuristics that read vehicle urgency alone fall short in contended cities (~80%). Through training, these learning agents rediscover partial charging and short opportunistic sessions, and route around busy stations, cutting per-session queue waits from about 45 minutes to under 2. In summary, this coordination paradigm balances local urgency against public occupancy, reaching near-Oracle performance at minimal implementation cost.
