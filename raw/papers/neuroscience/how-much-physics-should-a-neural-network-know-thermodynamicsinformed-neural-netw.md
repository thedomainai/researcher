---
title: "How Much Physics Should a Neural Network Know? Thermodynamics‐Informed Neural Networks for Rock Constitutive Modeling With Epistemic Uncertainty"
authors: "Kangan Li, Tushar Mittal, Benjamin Kamine Holtzman, Seth Saltiel"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-23T06:00:08.461795"
doi: "https://doi.org/10.1029/2026jh001463"
openalex_id: "https://openalex.org/W7213538163"
source_api: "openalex"
---

# How Much Physics Should a Neural Network Know? Thermodynamics‐Informed Neural Networks for Rock Constitutive Modeling With Epistemic Uncertainty

**著者**: Kangan Li, Tushar Mittal, Benjamin Kamine Holtzman, Seth Saltiel
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Abstract Machine learning offers a flexible route to constitutive modeling, with two emergent questions for geoscience applications: what level of thermodynamic constraint should be embedded in the network architecture, and how should predictive uncertainty be quantified when extrapolating from laboratory to field conditions? We address both challenges by presenting two complementary frameworks, NICE‐M (Neural Integration for Constitutive Equations, Modified) and Thermodynamics of Irreversible Processes Informed Neural Network (TIP‐INN), that learn the scalar thermodynamic potentials of Generalized Standard Materials via convex neural networks coupled with a Neural Ordinary Differential Equation integrator. NICE‐M enforces soft thermodynamic admissibility by learning the Helmholtz free energy alone. TIP‐INN enforces hard consistency by learning both the free energy and the dual dissipation potential, guaranteeing non‐negative dissipation by construction. We systematically evaluate these architectures on analytical viscoelastic and elastoplastic models, as well as complex experimental rock deformation data sets. While both frameworks produce highly accurate stress predictions, TIP‐INN recovers more accurate underlying thermodynamic potentials and material properties, particularly for out‐of‐distribution extrapolations. To systematically quantify epistemic uncertainty, we augment both architectures with an Epistemic Neural Network (Epinet) that provides calibrated uncertainty estimates without the cost of full Bayesian inference, flagging predictions outside the training distribution. This integrated framework provides a path toward deploying learned constitutive models in geophysical simulations where reliability under extrapolation is essential.
