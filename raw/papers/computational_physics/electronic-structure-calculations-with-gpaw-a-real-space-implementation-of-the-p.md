---
title: "Electronic structure calculations with GPAW: a real-space implementation of the projector augmented-wave method"
authors: "Jussi Enkovaara, C. Rostgaard, J. J. Mortensen, J Chen, Marcin Dułak (+31)"
year: 2010
citations: 2578
paper_type: "primary"
domain: "computational_physics"
domain_label: "計算物理学"
source_api: "openalex"
fetched: "2026-11-26T14:09:15.484420"
doi: "10.1088/0953-8984/22/25/253202"
openalex_id: "W1967853451"
semantic_scholar_id: ""
arxiv_id: ""
url: "https://doi.org/10.1088/0953-8984/22/25/253202"
tier: 2
explore_depth: 1
---

# Electronic structure calculations with GPAW: a real-space implementation of the projector augmented-wave method

**著者**: Jussi Enkovaara, C. Rostgaard, J. J. Mortensen, J Chen, Marcin Dułak (+31)
**年**: 2010 | **被引用数**: 2578
**タイプ**: primary | **分野**: 計算物理学

## Abstract

Electronic structure calculations have become an indispensable tool in many areas of materials science and quantum chemistry. Even though the Kohn-Sham formulation of the density-functional theory (DFT) simplifies the many-body problem significantly, one is still confronted with several numerical challenges. In this article we present the projector augmented-wave (PAW) method as implemented in the GPAW program package (https://wiki.fysik.dtu.dk/gpaw) using a uniform real-space grid representation of the electronic wavefunctions. Compared to more traditional plane wave or localized basis set approaches, real-space grids offer several advantages, most notably good computational scalability and systematic convergence properties. However, as a unique feature GPAW also facilitates a localized atomic-orbital basis set in addition to the grid. The efficient atomic basis set is complementary to the more accurate grid, and the possibility to seamlessly switch between the two representations provides great flexibility. While DFT allows one to study ground state properties, time-dependent density-functional theory (TDDFT) provides access to the excited states. We have implemented the two common formulations of TDDFT, namely the linear-response and the time propagation schemes. Electron transport calculations under finite-bias conditions can be performed with GPAW using non-equilibrium Green functions and the localized basis set. In addition to the basic features of the real-space PAW method, we also describe the implementation of selected exchange-correlation functionals, parallelization schemes, ΔSCF-method, x-ray absorption spectra, and maximally localized Wannier orbitals.
