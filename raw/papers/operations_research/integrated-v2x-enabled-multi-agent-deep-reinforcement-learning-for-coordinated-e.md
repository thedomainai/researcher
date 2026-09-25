---
title: "Integrated V2X-Enabled Multi-Agent Deep Reinforcement Learning for Coordinated Emergency Vehicle Pre-emption"
authors: "Sara Tazeen, A. M. Sudhakara"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-22T09:24:06.201037"
doi: "https://doi.org/10.38124/ijisrt/26sep221"
openalex_id: "https://openalex.org/W7213659082"
source_api: "openalex"
---

# Integrated V2X-Enabled Multi-Agent Deep Reinforcement Learning for Coordinated Emergency Vehicle Pre-emption

**著者**: Sara Tazeen, A. M. Sudhakara
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Emergency Vehicle Preemption (EVP) can substantially reduce response times during urban emergencies, yet aggressive green-wave strategies often induce severe secondary congestion on competing approaches and prolong network recovery. This paper presents a communication-aware Multi-Agent Proximal Policy Optimization (MAPPO) framework for coordinated Vehicle-to-Infrastructure (V2I) traffic signal control and Vehicle-to-Vehicle (V2V) cooperative lane yielding. Each signalized intersection is modeled as an autonomous agent that selects traffic-signal actions using localized queue measurements, emergency vehicle (EV) telemetry, corridor demand, and dynamic V2X communication state parameters. The framework employs centralized training with decentralized execution (CTDE). V2I communication transmits priority pre-emption requests to roadside controllers, whereas V2V communication enables Connected Autonomous Vehicles (CAVs) to execute cooperative yielding manoeuvres along the EV's projected path. Implemented in the Simulation of Urban Mobility (SUMO) environment via the Traffic Control Interface (TraCI), the proposed architecture is evaluated under diverse traffic-demand levels, CAV penetration rates, packet-loss profiles, and communication latencies. Comparative experiments against fixed-time control, distance-based rule pre-emption, and single-mode ablation baselines demonstrate that the joint V2X-MAPPO approach significantly minimizes EV travel times while bounding non-emergency vehicle delays and post-event queue recovery periods.
