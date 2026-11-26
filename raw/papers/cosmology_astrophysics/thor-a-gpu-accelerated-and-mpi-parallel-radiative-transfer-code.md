---
title: "THOR: A GPU-accelerated and MPI-parallel radiative transfer code"
authors: "Chris Byrohl, Dylan Nelson"
year: 2026
citations: 12
paper_type: "primary"
domain: "cosmology_astrophysics"
fetched: "2026-11-27T06:06:54.199830"
doi: "https://doi.org/10.1051/0004-6361/202556517"
openalex_id: "https://openalex.org/W4415138476"
source_api: "openalex"
---

# THOR: A GPU-accelerated and MPI-parallel radiative transfer code

**著者**: Chris Byrohl, Dylan Nelson
**年**: 2026 | **被引用数**: 12
**タイプ**: primary | **分野**: 宇宙論・宇宙物理

## Abstract

Emission and absorption line features are important diagnostics for the physics underlying extragalactic astronomy. The interpretation of observed signatures involves making comparisons against forward-modeled spectra from galaxy formation simulations as well as more simplified geometries, while including the complex scattering radiative transfer (RT) of resonant emission lines. Here, we present þor, a modern C++ RT code focused initially on resonant emission lines. þor is a high-performance, distributed-memory, multi-target code that uses the message passing interface (MPI) for parallel execution. It runs on CPUs, GPUs, and other accelerators, yielding large ∼ 10-50 speed-ups compared to previous CPU-only codes. Our code supports multiple grid-based and grid-less data structures, enabling comparisons across different hydrodynamical codes as well as toy model geometries. We demonstrate its science capabilities with a number of example use cases across scales: (i) Lyman-alpha RT on simple shell-like gas distributions; (ii) Lyman-alpha RT applied to a high-resolution, high-redshift (z ∼ 6) cosmological hydrodynamical galaxy formation simulation; (iii) magnesium-II halos, namely, scattering and emission from the circumgalactic medium (CGM) of a z ≃ 1 galaxy drawn from a cosmological magnetohydrodynamical (MHD) simulation; (iv) the large-scale cosmic web in gas emission, a 6144^3 volume element RT scaling calculation; and (v) synthetic absorption spectra of the Lyman-alpha forest. We employed extensive verification and benchmarking to validate our approach and its computational efficiency. x
