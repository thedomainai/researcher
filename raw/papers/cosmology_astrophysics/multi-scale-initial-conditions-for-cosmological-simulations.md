---
title: "Multi-scale initial conditions for cosmological simulations"
authors: "Oliver Hahn, Tom Abel"
year: 2011
citations: 1042
paper_type: "primary"
domain: "cosmology_astrophysics"
domain_label: "宇宙論・宇宙物理"
source_api: "openalex"
fetched: "2026-11-26T13:58:52.860186"
doi: "10.1111/j.1365-2966.2011.18820.x"
openalex_id: "W1826719611"
semantic_scholar_id: ""
arxiv_id: ""
url: "https://doi.org/10.1111/j.1365-2966.2011.18820.x"
tier: 2
explore_depth: 1
---

# Multi-scale initial conditions for cosmological simulations

**著者**: Oliver Hahn, Tom Abel
**年**: 2011 | **被引用数**: 1042
**タイプ**: primary | **分野**: 宇宙論・宇宙物理

## Abstract

We discuss a new algorithm to generate multi-scale initial conditions with multiple levels of refinements for cosmological ‘zoom-in’ simulations. The method uses an adaptive convolution of Gaussian white noise with a real-space transfer function kernel together with an adaptive multi-grid Poisson solver to generate displacements and velocities following first- (1LPT) or second-order Lagrangian perturbation theory (2LPT). The new algorithm achieves rms relative errors of the order of 10−4 for displacements and velocities in the refinement region and thus improves in terms of errors by about two orders of magnitude over previous approaches. In addition, errors are localized at coarse-fine boundaries and do not suffer from Fourier-space-induced interference ringing. An optional hybrid multi-grid and Fast Fourier Transform (FFT) based scheme is introduced which has identical Fourier-space behaviour as traditional approaches. Using a suite of re-simulations of a galaxy cluster halo our real-space-based approach is found to reproduce correlation functions, density profiles, key halo properties and subhalo abundances with per cent level accuracy. Finally, we generalize our approach for two-component baryon and dark-matter simulations and demonstrate that the power spectrum evolution is in excellent agreement with linear perturbation theory. For initial baryon density fields, it is suggested to use the local Lagrangian approximation in order to generate a density field for mesh-based codes that is consistent with the Lagrangian perturbation theory instead of the current practice of using the Eulerian linearly scaled densities.
