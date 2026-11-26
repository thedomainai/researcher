---
title: "Hybrid Deep Learning Finite Difference Time Domain Modeling via Surface Equivalence Theorem for Accelerating Electromagnetic Simulations"
authors: "Behrad Rezaee Rezvan, Mohammad Yazdi, Mehdi Ezoji"
year: 2027
citations: 0
paper_type: "primary"
domain: "mathematical_physics"
fetched: "2026-11-27T06:08:20.802567"
doi: "https://doi.org/10.5829/ije.2027.40.04a.20"
openalex_id: "https://openalex.org/W7219803470"
source_api: "openalex"
---

# Hybrid Deep Learning Finite Difference Time Domain Modeling via Surface Equivalence Theorem for Accelerating Electromagnetic Simulations

**著者**: Behrad Rezaee Rezvan, Mohammad Yazdi, Mehdi Ezoji
**年**: 2027 | **被引用数**: 0
**タイプ**: primary | **分野**: 数理物理学

## Abstract

This work presents a hybrid, deep learning-assisted electromagnetic (EM) solver that accelerates time-domain simulations by integrating neural modeling with the Surface Equivalence Theorem (SET). A deep neural network (DNN), composed of long short-term memory (LSTM) and fully connected layers, is trained to reproduce the scattering behavior of a predefined object enclosed by Huygens' surfaces. Once trained, the DNN is embedded into a Finite-Difference Time-Domain (FDTD) solver to replace the corresponding subregion, generating equivalent surface fields in real time while preserving multiple-scattering interactions with the surrounding environment. This hybrid approach substantially reduces the computational cost of repeated forward simulations typically required in optimization-driven analyses, such as inverse design, microwave imaging, and parameter estimation. The proposed network, trained using data generated at a central frequency of 9 GHz, accurately predicts broadband EM responses across the 8-12 GHz range. The training procedure and hyperparameter optimization of the network are presented, and various numerical examples are provided. Numerical experiments demonstrate an acceleration of up to 86.7% compared to conventional FDTD and 85.5% relative to the Huygens Sub-Gridding (HSG) technique, with negligible loss in accuracy. The method provides a physics-consistent framework for fast, reusable forward solvers and offers a promising path toward efficient large-scale EM modeling.
