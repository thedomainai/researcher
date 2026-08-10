---
title: "pyhgf: A neural network library for predictive coding"
authors: "Nicolas Legrand, Lilian Weber, Peter Thestrup Waade, Anna Hedvig Møller Daugaard, Mojtaba Khodadadi"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-06-26T06:00:11.362044"
doi: "https://doi.org/10.1371/journal.pcbi.1014340"
openalex_id: "https://openalex.org/W4403564456"
source_api: "openalex"
---

# pyhgf: A neural network library for predictive coding

**著者**: Nicolas Legrand, Lilian Weber, Peter Thestrup Waade, Anna Hedvig Møller Daugaard, Mojtaba Khodadadi
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Bayesian models of cognition have gained considerable traction in computational neuroscience and psychiatry. Their scopes are now expected to expand rapidly to artificial intelligence, providing general inference frameworks to support embodied, adaptable, and energy-efficient autonomous agents. A central theory in this domain is predictive coding, which posits that learning and behaviour are driven by hierarchical probabilistic inferences about the causes of sensory inputs. Biological realism constrains these networks to rely on simple local computations in the form of precision-weighted predictions and prediction errors. This can make this framework highly efficient, but its implementation comes with unique challenges on the software development side. Embedding such models in standard neural network libraries often becomes limiting, as these libraries' compilation and differentiation backends can force a conceptual separation between optimization algorithms and the systems being optimized. This critically departs from other biological principles such as self-monitoring, self-organisation, cellular growth, and functional plasticity. In this paper, we introduce pyhgf: a Python package backed by JAX and Rust for creating, manipulating, and sampling dynamic networks for predictive coding. We improve over other frameworks by enclosing the network components as transparent, modular, and malleable variables in the message-passing steps. The resulting graphs can implement arbitrary algorithms as belief propagation. Moreover, the transparency of core variables can also translate into inference processes that leverage self-organisation principles and express structure learning, meta-learning, or causal discovery as the consequence of network structural adaptation to surprising inputs. The main functions of the library are differentiable and seamlessly integrate into sampling or optimization workflows. Additionally, we offer generalized Bayesian filtering and the hierarchical Gaussian filter as key examples of dynamic networks implemented in our library. The source code, tutorials, and documentation are hosted under the main repository at https://github.com/ComputationalPsychiatry/pyhgf.
