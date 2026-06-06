---
title: "Workshop on Differentiable Marine Hydrodynamics Simulations and its Applications using MarineHydro.jl"
authors: "Kapil Khanal, Carlos Michelen Strofer, Maha Haji, Matthieu Ancellin"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-06-05T06:13:59.213368"
doi: "https://doi.org/10.5281/zenodo.20533983"
openalex_id: "https://openalex.org/W7163377247"
source_api: "openalex"
---

# Workshop on Differentiable Marine Hydrodynamics Simulations and its Applications using MarineHydro.jl

**著者**: Kapil Khanal, Carlos Michelen Strofer, Maha Haji, Matthieu Ancellin
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Understanding and predicting wave-structure interactions is central to the design and operation of offshore systems—from floating wind turbines and wave energy con- verters to autonomous marine platforms. Traditionally, these interactions are modeled using boundary element method (BEM) solvers based on linear potential flow the- ory. However, a major limitation of existing BEM solvers is their inability to provide sensitivities (derivatives) of hydrodynamic quantities with respect to design variables such as geometry, wave frequency, or device layout. These sensitivities are essential for enabling modern workflows in design optimization, control co-design, uncertainty quantification, and physics-informed machine learning. Without access to gradients, engineers are forced to rely on derivative-free meth- ods (e.g., parameter sweeps, heuristics, or surrogate models without sensitivity guid- ance), which scale poorly and often miss optimal solutions in high-dimensional design spaces. This bottleneck has hindered progress in applying scalable, gradient-based op- timization methods—now common in aerospace, robotics, and machine learning—to the marine energy sector. This workshop introduces MarineHydro.jl, a fully differentiable BEM solver that unlocks access to exact sensitivities of hydrodynamic coefficients through reverse- mode automatic differentiation. Developed in Julia, MarineHydro.jl supports both di- rect and indirect BEM formulations and includes fast and accurate Green’s function implementations. The workshop is targeted at researchers and practitioners working on design and control of offshore and marine structures, with an emphasis on appli- cations where sensitivity information is essential. Participants will learn to install the solver, perform hydrodynamic simulations, extract gradients, and apply these results to practical case studies. We begin by reviewing the fundamentals of differentiable programming in the con- text of potential flow theory and boundary element methods. The solver’s architecture supports both direct and indirect BEM formulations and includes efficient implemen- tations of Green’s function approximations, balancing accuracy and performance. Application I: Surrogate Modeling with Gradient-Enhanced Learning. Tradi- tional surrogate models rely solely on function evaluations, requiring dense sampling for accurate approximations. By incorporating gradient information directly into model training, MarineHydro.jl enables the construction of more data-efficient and accurate surrogates. This is particularly valuable for design optimization, where high-fidelity models are expensive to evaluate. Application II: Multi-Body Interaction and Layout Optimization. Hydrody- namic interactions between multiple floating bodies—such as wave energy convert- ers—are critical for performance, yet challenging to optimize using traditional ap- proaches. Using MarineHydro.jl, participants will explore sensitivity-based analyses of inter-body effects and apply gradient-based optimization to study spatial layouts and design variables. Case studies include gradient-based power optimization of WEC arrays, marking the first use of exact hydrodynamic gradients for such purposes. The availability of exact sensitivities opens up new avenues in multidisciplinary de- sign optimization (MDO), control co-design, uncertainty quantification, and physics- informed machine learning. By integrating differentiable hydrodynamics into the de- sign loop, MarineHydro.jl paves the way for scalable, robust, and high-performance workflows in the next generation of marine renewable energy systems.
