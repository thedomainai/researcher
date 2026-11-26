---
title: "Towards direct dynamics simulation of photochemistry without the Born–Oppenheimer approximation"
authors: "Jong‐Kwon Ha, Edith Leal-Sánchez, Ryan J. MacDonell"
year: 2027
citations: 0
paper_type: "primary"
domain: "computational_physics"
fetched: "2026-11-27T06:08:48.029669"
doi: "https://doi.org/10.1039/d6fd00096g"
openalex_id: "https://openalex.org/W7163881954"
source_api: "openalex"
---

# Towards direct dynamics simulation of photochemistry without the Born–Oppenheimer approximation

**著者**: Jong‐Kwon Ha, Edith Leal-Sánchez, Ryan J. MacDonell
**年**: 2027 | **被引用数**: 0
**タイプ**: primary | **分野**: 計算物理学

## Abstract

The simulation of photochemical reactions requires a quantum mechanical treatment of electronic and nuclear dynamics. Most simulation approaches use the Born-Oppenheimer (BO) approximation and calculations of nonadiabatic couplings to evolve a wavefunction on a set of BO electronic states. However, the use of BO states presents several challenges, such as discontinuous surfaces, singular terms in the Hamiltonian, and double-valued boundary conditions. We present a direct dynamics approach for molecular vibronic dynamics which does not invoke the BO approximation simply by avoiding diagonalization of the electronic part of the Hamiltonian. By employing a diabatic propagation scheme for the orbitals, we ensure that all electronic terms vary smoothly as a function of nuclear coordinates in a basis of configuration state functions (CSFs). We derive equations of motion for mixed quantum-classical dynamics techniques employing averaged potentials, such that the simulated trajectories evolve on linear combinations of CSF surfaces. We test our approach for lithium hydride and ethylene. In contrast with BO electronic surfaces, we find that all CSF surfaces and couplings are smooth and integrable in the vicinity of conical intersections and weak avoided crossings. Comparisons of the dynamics of photoexcited lithium hydride show that Ehrenfest dynamics reproduce changes in electronic state populations, but lead to over-coherence. Our equations of motion for coupled-trajectory dynamics fail to reduce the over-coherence problem due to the reliance of the derivation on the BO approximation. With further work on the selection of orbitals and the mixed quantum-classical equations of motion, our work shows the potential of a pre-BO wavefunction ansatz for practical nonadiabatic dynamics simulations.
