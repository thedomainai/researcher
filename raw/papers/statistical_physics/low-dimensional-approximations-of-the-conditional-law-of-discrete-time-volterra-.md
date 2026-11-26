---
title: "Low-dimensional approximations of the conditional law of discrete-time Volterra processes: A non-positive curvature approach"
authors: "Luca Galimberti, Anastasis Kratsios, Giulia Livieri, Reza Arabpour, John Armstrong"
year: 2026
citations: 6
paper_type: "primary"
domain: "statistical_physics"
fetched: "2026-11-27T06:07:44.130718"
doi: "https://doi.org/10.1142/s0219530526300012"
openalex_id: "https://openalex.org/W4399252951"
source_api: "openalex"
---

# Low-dimensional approximations of the conditional law of discrete-time Volterra processes: A non-positive curvature approach

**著者**: Luca Galimberti, Anastasis Kratsios, Giulia Livieri, Reza Arabpour, John Armstrong
**年**: 2026 | **被引用数**: 6
**タイプ**: primary | **分野**: 統計力学・熱力学

## Abstract

Predicting the conditional evolution of discrete-time Volterra processes with stochastic volatility is a crucial challenge in mathematical finance. While deep neural network models offer promise in approximating the conditional law of such processes, their effectiveness is hindered by the curse of dimensionality caused by the infinite dimensionality and non-smooth nature of these problems. To address this, we propose a two-step solution. First, we develop a stable dimension reduction technique, projecting the law of a reasonably broad class of discrete-time Volterra processes onto a low-dimensional statistical manifold of non-positive sectional curvature. Next, we introduce a sequentially deep-learning model tailored to the manifold’s geometry, which we show can approximate the projected conditional law of the considered Volterra process. Our model leverages an auxiliary hypernetwork to dynamically update its internal parameters, allowing it to encode non-stationary dynamics of the Volterra process, and it can be interpreted as a gating mechanism in a mixture of expert models where each expert is specialized at a specific point in time. Our hypernetwork further allows us to achieve approximation rates that would seemingly only be possible with very large networks.
