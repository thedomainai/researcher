---
title: "Cross-simulator transfer with foundation-model summaries: Toward robust SKA-era reionization inference"
authors: "Yannic Pietschke, Caroline S. Heneka, Ayodele Ore, Romain Mériot"
year: 2026
citations: 4
paper_type: "primary"
domain: "cosmology_astrophysics"
fetched: "2026-11-27T06:06:54.203569"
doi: "https://doi.org/10.1051/0004-6361/202662816"
openalex_id: "https://openalex.org/W7204574547"
source_api: "openalex"
---

# Cross-simulator transfer with foundation-model summaries: Toward robust SKA-era reionization inference

**著者**: Yannic Pietschke, Caroline S. Heneka, Ayodele Ore, Romain Mériot
**年**: 2026 | **被引用数**: 4
**タイプ**: primary | **分野**: 宇宙論・宇宙物理

## Abstract

Simulation-based inference (SBI) for parameter estimation is vulnerable to model misspecification: neural summaries and density estimators trained on a specific forward model typically fail when applied to data drawn from another model or from real observations, and no training simulator can capture the full observational pipeline of a real measurement exactly. We show that a self-supervised vision transformer (ViT), pretrained label-free on a fast approximate simulator, produces transferable data summaries that generalize across simulators. Without retraining, it can be reused as a frozen encoder to infer astrophysical parameters from a completely different simulator that explicitly resolves radiative transfer and on which it was never trained. As a concrete use case in 21cm cosmology, SKATR, a ViT pretrained with a self-supervised Joint Embedding Predictive Architecture (JEPA), serves as a foundation model for reionization inference from upcoming Square Kilometre Array (SKA) measurements: SKATR was pretrained once on 67k low-cost, noiseless semi-numerical 21cmFAST light cones, frozen, and applied to hydrodynamical Loreli II light cones, where a lightweight conditional flow matching (CFM) head infers five astrophysical parameters. The encoder is never shown Loreli data, its parameters, or any noise. In our comparison, SKATR yields the most precise and best-calibrated posteriors across all five parameters, matching the accuracy of the fully supervised in-domain baseline while requiring 2.6 fewer radiative-transfer simulations. Under realistic SKA AA* noise, only SKATR remains simultaneously accurate, informative, and calibrated, outperforming even a supervised baseline retrained from scratch on noisy data. Self-supervised pretraining on computationally efficient semi-numerical simulations is therefore a viable route to calibrated, simulator-, and noise-agnostic reionization inference for the SKA-era.
