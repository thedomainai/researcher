---
title: "Architecting Safety-Critical Systems for AI-Enabled Software-Defined Vehicles: A Compute, Timing, and Isolation Framework with a Brake System Case Study"
authors: "Soumyasudharsan Srinivasaraghavan"
year: 2026
citations: 0
paper_type: "primary"
domain: "systems_engineering"
fetched: "2026-09-15T11:25:13.435495"
doi: "https://doi.org/10.4271/2026-01-0811"
openalex_id: "https://openalex.org/W7212454233"
source_api: "openalex"
---

# Architecting Safety-Critical Systems for AI-Enabled Software-Defined Vehicles: A Compute, Timing, and Isolation Framework with a Brake System Case Study

**著者**: Soumyasudharsan Srinivasaraghavan
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: システム工学

## Abstract

Software-defined vehicle (SDV) platforms are reshaping safety-critical system design by consolidating braking and other motion-control functions on centralized heterogeneous edge compute that also executes physical-AI workloads. This consolidation breaks traditional assumptions of fixed ECUs and simple timing envelopes, complicating assurance of determinism, isolation, and fail-operational behaviour for ASIL-D brake functions. Building on a decentralized brake-by- wire (BbW) architecture with dual controllers, redundant low-voltage power grids, and smart electromechanical brake corner actuators, this paper proposes a systems-level framework for architecting safety-critical functions in AI-enabled SDVs along three dimensions: compute, timing, and isolation. The framework classifies conventional and AI-based functions and maps them to heterogeneous compute classes; defines architectural patterns that combine safety islands, power-domain redundancy, and hardware partitioning to support freedom from interference; and formalizes timing domains and contracts that bound latency, jitter, and failover dynamics across sensors, centralized controllers, and decentralized actuators. The contribution is not a new AI algorithm, but a safety-oriented architectural framework that constrains how AI-enabled functions may be integrated into fail-operational by-wire systems. A BbW case study with edge-resident AI observers and anomaly detectors shows how the framework complements System Analysis Tool (SAT)– based failure modelling and clarifies trade-offs among safety isolation, latency, and AI performance while preserving braking safety guarantees under continuous software evolution.
