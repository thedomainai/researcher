---
title: "Generalized Unitary Coupled Cluster Wave functions for Quantum Computation"
authors: "Joonho Lee, William J. Huggins, Martin Head‐Gordon, K. Birgitta Whaley"
year: 2018
citations: 538
paper_type: "primary"
domain: "computational_physics"
domain_label: "計算物理学"
source_api: "openalex"
fetched: "2026-11-26T14:09:02.826966"
doi: "10.1021/acs.jctc.8b01004"
openalex_id: "W2895777514"
semantic_scholar_id: ""
arxiv_id: ""
url: "https://doi.org/10.1021/acs.jctc.8b01004"
tier: 2
explore_depth: 1
---

# Generalized Unitary Coupled Cluster Wave functions for Quantum Computation

**著者**: Joonho Lee, William J. Huggins, Martin Head‐Gordon, K. Birgitta Whaley
**年**: 2018 | **被引用数**: 538
**タイプ**: primary | **分野**: 計算物理学

## Abstract

We introduce a unitary coupled-cluster (UCC) ansatz termed k-UpCCGSD that is based on a family of sparse generalized doubles operators, which provides an affordable and systematically improvable unitary coupled-cluster wave function suitable for implementation on a near-term quantum computer. k-UpCCGSD employs k products of the exponential of pair coupled-cluster double excitation operators (pCCD), together with generalized single excitation operators. We compare its performance in both efficiency of implementation and accuracy with that of the generalized UCC ansatz employing the full generalized single and double excitation operators (UCCGSD), as well as with the standard ansatz employing only single and double excitations (UCCSD). k-UpCCGSD is found to show the best scaling for quantum computing applications, requiring a circuit depth of [Formula: see text], compared with [Formula: see text] for UCCGSD, and [Formula: see text] for UCCSD, where N is the number of spin orbitals and η is the number of electrons. We analyzed the accuracy of these three ansätze by making classical benchmark calculations on the ground state and the first excited state of H4 (STO-3G, 6-31G), H2O (STO-3G), and N2 (STO-3G), making additional comparisons to conventional coupled cluster methods. The results for ground states show that k-UpCCGSD offers a good trade-off between accuracy and cost, achieving chemical accuracy for lower cost of implementation on quantum computers than both UCCGSD and UCCSD. UCCGSD is also found to be more accurate than UCCSD but at a greater cost for implementation. Excited states are calculated with an orthogonally constrained variational quantum eigensolver approach. This is seen to generally yield less accurate energies than for the corresponding ground states. We demonstrate that using a specialized multideterminantal reference state constructed from classical linear response calculations allows these excited state energetics to be improved.
