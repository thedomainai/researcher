---
title: "Hamiltonian-Aware ADAPT Variational Quantum Eigensolver for Molecular Ground-State Simulation"
authors: "Runhong He, Xin Hong, Qiaozhen Chai, Chao Liu, Junyuan Zhou"
year: 2026
citations: 0
paper_type: "primary"
domain: "innovation_management"
fetched: "2026-10-10T06:04:20.603604"
doi: "https://doi.org/10.1021/acs.jctc.6c01185"
openalex_id: "https://openalex.org/W7164530280"
source_api: "openalex"
---

# Hamiltonian-Aware ADAPT Variational Quantum Eigensolver for Molecular Ground-State Simulation

**著者**: Runhong He, Xin Hong, Qiaozhen Chai, Chao Liu, Junyuan Zhou
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: イノベーション管理

## Abstract

Abstract Designing compact ansätze for the Variational Quantum Eigensolver (VQE) is crucial for calculating energies of large molecules on near-term quantum devices. However, the widely used Adaptive Derivative-Assembled Pseudo-Trotter (ADAPT) ansätze present two challenges: the inherent locality of conventional criteria results in inappropriate excitation operator selection, and the inevitable degradation of certain operators gives rise to redundant accumulation. In this paper, we propose the Hamiltonian-Aware (HA) ADAPT-VQE algorithm to address these issues. First, we present a novel excitation operator selection criterion, which overcomes the locality constraint of existing criteria by incorporating Hamiltonian information. It effectively avoids selecting ineffective operators by prioritizing physically meaningful ones, and incurs no extra classical or quantum computational overhead. Second, we develop a new problem-adaptive method for discriminating and pruning redundant excitation operators stemming from improper selection and inevitable degradation. This method balances redundant operator pruning and convergence guarantee, and is applicable to ansätze with arbitrary scales. Systematic numerical experiments on typical strongly correlated molecular systems demonstrate that our HA-ADAPT-VQE mitigates energy plateaus and outperforms baseline algorithms in terms of energy error, ansatz size, and measurement cost in most cases. This work offers an efficient, robust ansatz construction paradigm, facilitating the development and practical deployment of large-scale VQE in quantum chemistry.
