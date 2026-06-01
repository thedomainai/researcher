---
title: "Modellering en regeling van warmtepompen in clusters van residentiële gebouwen met behulp van machine learning - Op weg naar energie-flexibiliteit"
authors: "Muhammad Hafeez Saeed"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-05-12T06:04:29.661296"
doi: ""
openalex_id: "https://openalex.org/W7160798861"
source_api: "openalex"
---

# Modellering en regeling van warmtepompen in clusters van residentiële gebouwen met behulp van machine learning - Op weg naar energie-flexibiliteit

**著者**: Muhammad Hafeez Saeed
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

The decarbonisation of residential heating increasingly relies on the electrification of buildings through heat pumps. At the same time, flexible operation of heat pumps may support demand-side flexibility in electricity systems with growing shares of renewable energy. However, the development of reliable modelling and control methods remains challenging because representative training data are often limited, high-fidelity simulations are computationally expensive, and methods developed for individual buildings are not straightforward to extend to building clusters. This PhD research develops and evaluates physics-informed and machine-learning-based methods for surrogate modelling and reinforcement-learning-based control of residential heat-pump space-heating systems. At the building level, the work proposes Dyna-PINN, a physics-informed Deep Dyna-Q framework that combines model-based and model-free reinforcement learning through a surrogate model constrained by resistance-capacitance thermal dynamics. This approach is studied as a way to improve data efficiency and generalisation under limited-data conditions. At the cluster level, the research develops ScaleONet, an operator-learning surrogate for modelling the thermal dynamics of heterogeneous residential building clusters, with evaluation across different cluster sizes. Building on these surrogate models, the PhD further investigates cooperative multi-agent reinforcement learning strategies for coordinated control in a three-building cluster case study and examines workflows in which policies are first trained using surrogate models and subsequently refined in high-fidelity simulation environments. Overall, the research shows how physics-informed learning and scalable surrogate modelling can support more data-efficient modelling and can facilitate the extension of learning-based control studies from single buildings to building clusters.
