---
title: "Performance Evaluation of Ising and QUBO Variable Encodings in Boltzmann Machine Learning"
authors: "Yasushi Hasegawa, Masayuki Ohzeki"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-09-30T06:00:41.539464"
doi: "https://doi.org/10.7566/jpsj.95.104006"
openalex_id: "https://openalex.org/W4415275330"
source_api: "openalex"
---

# Performance Evaluation of Ising and QUBO Variable Encodings in Boltzmann Machine Learning

**著者**: Yasushi Hasegawa, Masayuki Ohzeki
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

We compare Ising ([Formula: see text]) and QUBO ([Formula: see text]) encodings for Boltzmann machine learning under controlled protocols that fix the sampler, optimizer, and learning-rate design within each comparison. Exploiting the identity that the Fisher information matrix (FIM) equals the covariance of sufficient statistics, we visualize empirical moments from model samples and reveal systematic, representation-dependent differences. QUBO induces larger cross terms between first- and second-order statistics, creating more small-eigenvalue directions in the FIM and lowering spectral entropy. This ill-conditioning explains slower convergence under stochastic gradient descent (SGD). In contrast, full-FIM natural gradient descent (NGD), which rescales updates by the FIM metric, achieves similar convergence across encodings, whereas diagonal-FIM approximation can reintroduce representation-dependent differences. Practically, for SGD-based training, the Ising encoding provides more isotropic curvature and faster convergence; for QUBO, centering/scaling or NGD-style preconditioning mitigates curvature pathologies. These results clarify how representation shapes information geometry and finite-time learning dynamics in Boltzmann machines and yield actionable guidelines for variable encoding and preprocessing.
