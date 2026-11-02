---
title: "Physics-Guided AI–Numerical Simulation for Sand Production Prediction and Completion Optimization"
authors: "Osman Hamid, Eslam M. Abdalrahman, Rowa Tawfiq"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-03T07:01:38.445811"
doi: "https://doi.org/10.2118/235506-ms"
openalex_id: "https://openalex.org/W7225046673"
source_api: "openalex"
---

# Physics-Guided AI–Numerical Simulation for Sand Production Prediction and Completion Optimization

**著者**: Osman Hamid, Eslam M. Abdalrahman, Rowa Tawfiq
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Abstract Sand production is a nonlinear, path-dependent, and strongly coupled process controlled by reservoir depletion, effective-stress redistribution, near-wellbore stress concentration, elastoplastic failure, damage accumulation, grain debonding, hydraulic detachment, erosion, and particulate transport. Its occurrence and severity depend on rock-strength variability, stress regime, well trajectory, completion type, perforation orientation, production drawdown, transient rate history, water weakening, and evolving cavity geometry. Conventional sanding workflows typically combine empirical screening, analytical failure criteria, and detailed numerical simulation, but each method has limitations when used independently. Empirical correlations may not extrapolate reliably; analytical methods simplify geometry and constitutive behavior; and high-fidelity finite-element or discrete-element models are computationally expensive for field-scale optimization and real-time control. This paper develops a unified physics-guided artificial-intelligence and numerical-simulation framework for predicting sanding onset, critical drawdown, transient sand rate, cumulative sand production, cavity evolution, and completion-dependent operating envelopes. The workflow integrates quality-controlled petrophysical logs, drilling and production records, depletion history, laboratory measurements from unconfined compression, triaxial compression, thick-wall-cylinder and advanced thick-wall-cylinder tests, calibrated one-dimensional geomechanical models, and three-dimensional poroelastoplastic finite-element simulations. Sanding initiation is constrained by an analytical effective-strength-factor load criterion and a laboratory-calibrated critical-strain-limit criterion. Mechanical failure is coupled to hydraulic mobilization through drag, lift, seepage, and retention forces, while an erosion law governs sand generation and transport. The AI layer combines gradient-boosted trees, random forests, deep neural networks, temporal models, graph neural networks, neural operators, residual learning, and physics-informed neural networks. A multi-task, multi-fidelity loss function enforces data agreement, finite-element consistency, equilibrium, mass conservation, yield admissibility, Critical state line (CSL) consistency, nonnegative sand rate, physically valid bounds, and regime-dependent monotonicity. Bayesian and ensemble uncertainty quantification provides conservative safe-drawdown limits and out-of-distribution detection. Completion optimization is posed as a constrained multi-objective problem over well trajectory, perforation orientation, phasing, penetration, sand-control selection, and drawdown schedule. The supplied field-study basis indicates that representative depletion scenarios up to 3,000 psi, a stress-path coefficient near 0.6, TWC variability, and open-hole versus cased-and-perforated geometry materially alter the sanding envelope. Laboratory-calibrated TWC/perforation-scale CSL values range approximately from 30 to 68 millistrain in the documented cases, and open-hole CSL may be 20–60% lower because of hole-size and unsupported-boundary effects. The proposed framework converts high-fidelity numerical simulations into rapid probabilistic operating envelopes without inventing unsupported AI performance statistics. It supports pre-drill completion screening, uncertainty-aware production design, adaptive choke control, and continuously updated sand-management digital twins.
