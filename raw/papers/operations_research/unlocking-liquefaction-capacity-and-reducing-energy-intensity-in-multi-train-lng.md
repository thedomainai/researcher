---
title: "Unlocking Liquefaction Capacity and Reducing Energy Intensity in Multi-Train LNG Facilities Through AI-Driven Supervisory Optimization: A Non-Intrusive, Physics-Informed Reinforcement-Learning Framework for Coordinated Train Balancing, Approach-Temperature Optimization, and Boil-Off Gas Management"
authors: "Mansour Belhadj, Othman Taha"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-03T07:01:38.447133"
doi: "https://doi.org/10.2118/235815-ms"
openalex_id: "https://openalex.org/W7225044260"
source_api: "openalex"
---

# Unlocking Liquefaction Capacity and Reducing Energy Intensity in Multi-Train LNG Facilities Through AI-Driven Supervisory Optimization: A Non-Intrusive, Physics-Informed Reinforcement-Learning Framework for Coordinated Train Balancing, Approach-Temperature Optimization, and Boil-Off Gas Management

**著者**: Mansour Belhadj, Othman Taha
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Abstract Objectives/Scope Multi-train LNG facilities are routinely operated below true liquefaction capacity due to limited observability of internal heat exchanger thermal states, conservative refrigeration margins, and uncoordinated throughput allocation across parallel trains. This paper presents the application of an AI-driven supervisory optimization system to a multi-train LNG facility, with the objective of unlocking latent liquefaction capacity, reducing refrigeration energy intensity per tonne of LNG produced, and minimizing boil-off gas flaring while maintaining full compliance with safety-instrumented systems. Methods, Procedures, Process The system integrates distributed temperature sensing (DTS) deployed along main cryogenic heat exchangers (MCHEs) and propane pre-coolers with distributed acoustic sensing (DAS) installed on refrigeration and BOG compressor piping. DTS-derived spatial profiles quantify heat-transfer effectiveness and fouling progression; DAS-derived acoustic features detect incipient compressor surge and flow instability. These inputs continuously update a hybrid digital twin combining physics-based liquefaction thermodynamics with data- driven surrogate models. A reinforcement learning supervisory optimizer generates bounded operating targets including refrigeration load redistribution across trains, approach temperature adjustments, compressor bias targets, and BOG compression scheduling validated via forward simulation before dispatch to existing APC layer, without modification to safety-instrumented systems. Results, Observations, Conclusions DTS-enabled inference of MCHE fouling and approach temperature margins consistently identifies operating headroom that conventional point instrumentation cannot resolve, enabling trains to operate closer to true thermal constraints with quantified confidence bounds. Refrigeration load redistribution guided by the reinforcement learning optimizer reduces inter-train imbalance and eliminates the conservative margins that previously capped aggregate throughput. Real-time surge margin estimation for refrigeration compressors allows the system to exploit available mechanical capacity without approaching instability thresholds. Across multi-train configurations, coordinated supervisory targets achieve measurable liquefaction capacity uplift, verifiable through production historian data and the system's built-in performance attribution module. BOG compression scheduling reduces unplanned flaring by proactively managing tank inventory against ambient conditions and production ramp trajectories. The supervisory layer deploys non-intrusively above existing DCS and APC applications, confirming feasibility for brownfield LNG assets. Novel/Additive Information This paper presents the first documented integration of spatially distributed fiberoptic sensing with physics-informed hybrid digital twins and reinforcement learning for multi-train LNG supervisory optimization. Unlike prior approaches that optimize individual unit operations in isolation, this framework coordinates full-facility observability and cross-train load allocation within a single non-intrusive system. The built-in performance verification module provides auditable evidence of throughput uplift and energy reduction, advancing the state of knowledge on quantifiable AI value realization in LNG operations.
