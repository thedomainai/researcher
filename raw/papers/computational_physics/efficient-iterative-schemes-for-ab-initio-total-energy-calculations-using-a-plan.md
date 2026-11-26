---
title: "Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set"
authors: "Georg Kresse, Jürgen Furthmüller"
year: 1996
citations: 132211
paper_type: "primary"
domain: "computational_physics"
domain_label: "計算物理学"
source_api: "openalex"
fetched: "2026-11-26T14:08:37.311277"
doi: "10.1103/physrevb.54.11169"
openalex_id: "W2083222334"
semantic_scholar_id: ""
arxiv_id: ""
url: "https://doi.org/10.1103/physrevb.54.11169"
tier: 2
explore_depth: 1
---

# Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set

**著者**: Georg Kresse, Jürgen Furthmüller
**年**: 1996 | **被引用数**: 132211
**タイプ**: primary | **分野**: 計算物理学

## Abstract

We present an efficient scheme for calculating the Kohn-Sham ground state of metallic systems using pseudopotentials and a plane-wave basis set. In the first part the application of Pulay's DIIS method (direct inversion in the iterative subspace) to the iterative diagonalization of large matrices will be discussed. Our approach is stable, reliable, and minimizes the number of order ${\mathit{N}}_{\mathrm{atoms}}^{3}$ operations. In the second part, we will discuss an efficient mixing scheme also based on Pulay's scheme. A special ``metric'' and a special ``preconditioning'' optimized for a plane-wave basis set will be introduced. Scaling of the method will be discussed in detail for non-self-consistent and self-consistent calculations. It will be shown that the number of iterations required to obtain a specific precision is almost independent of the system size. Altogether an order ${\mathit{N}}_{\mathrm{atoms}}^{2}$ scaling is found for systems containing up to 1000 electrons. If we take into account that the number of k points can be decreased linearly with the system size, the overall scaling can approach ${\mathit{N}}_{\mathrm{atoms}}$. We have implemented these algorithms within a powerful package called VASP (Vienna ab initio simulation package). The program and the techniques have been used successfully for a large number of different systems (liquid and amorphous semiconductors, liquid simple and transition metals, metallic and semiconducting surfaces, phonons in simple metals, transition metals, and semiconductors) and turned out to be very reliable.
