---
title: "Model-Based Learning of Whittle indices"
authors: "Joël Charles-Rebuffé, Nicolas Gast, Bruno Gaujal"
year: 2026
citations: 1
paper_type: "primary"
domain: "operations_research"
fetched: "2026-08-31T09:35:49.859990"
doi: "https://doi.org/10.1145/3844508"
openalex_id: "https://openalex.org/W7106836519"
source_api: "openalex"
---

# Model-Based Learning of Whittle indices

**著者**: Joël Charles-Rebuffé, Nicolas Gast, Bruno Gaujal
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

We present BLINQ , a new model-based algorithm that learns the Whittle indices of an indexable, communicating and unichain Markov Decision Process (MDP). Our approach relies on building an empirical estimate of the MDP and then computing its Whittle indices using an extended version of a state-of-the-art existing algorithm. We provide a proof of convergence to the Whittle indices we want to learn as well as a bound on the time needed to learn them with arbitrary precision. Moreover, we investigate its computational complexity. Our numerical experiments suggest that BLINQ significantly outperforms existing Q -learning approaches in terms of the number of samples needed to get an accurate approximation. In addition, it has a total computational cost even lower than Q -learning for any reasonably high number of samples. These observations persist even when the Q -learning algorithms are sped up using neural networks to predict Q-values.
