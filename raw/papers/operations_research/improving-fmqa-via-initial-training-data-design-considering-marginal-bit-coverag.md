---
title: "Improving FMQA via Initial Training Data Design Considering Marginal Bit Coverage in One-Hot Encoding"
authors: "Taiga Hayashi, Yuya Seki, Kotaro Terada, Yosuke Mukasa, Shuta Kikuchi"
year: 2026
citations: 1
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-18T07:31:28.409261"
doi: "https://doi.org/10.7566/jpsj.95.124005"
openalex_id: "https://openalex.org/W7160549366"
source_api: "openalex"
---

# Improving FMQA via Initial Training Data Design Considering Marginal Bit Coverage in One-Hot Encoding

**著者**: Taiga Hayashi, Yuya Seki, Kotaro Terada, Yosuke Mukasa, Shuta Kikuchi
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Factorization machine with quadratic-optimization annealing (FMQA) is a black-box optimization method that combines a factorization machine (FM) surrogate with search based on quadratic unconstrained binary optimization (QUBO) by an Ising machine. When FMQA is applied to integer or discretized continuous variables via one-hot encoding, uniform random initial sampling can leave many binary variables never active in the initial training data, and the corresponding FM parameters receive no direct gradient updates from the observed responses. We address this by designing the initial training data to achieve complete marginal bit coverage, namely, ensuring that every binary variable obtained by one-hot encoding takes the value one at least once. We use two space-filling sampling methods, Latin hypercube sampling (LHS) and the Sobol’ sequence, yielding LHS-FMQA and Sobol’-FMQA. On the human-powered aircraft wing-shape optimization benchmark with 17 and 32 design variables, both proposed methods achieved numerically higher mean final cruising speeds than the baseline FMQA, with the advantage more pronounced on the 32-variable problem.
