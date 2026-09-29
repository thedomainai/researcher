---
title: "AutoResearch Lite: a reproducible paper-inspired experiment runner (Adam mechanism reproduction and convergence-speed comparison)"
authors: "He, Zhen"
year: 2026
citations: 49999
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-29T06:00:04.113761"
doi: "https://doi.org/10.5281/zenodo.23003626"
openalex_id: "https://openalex.org/W2964121744"
source_api: "openalex"
---

# AutoResearch Lite: a reproducible paper-inspired experiment runner (Adam mechanism reproduction and convergence-speed comparison)

**著者**: He, Zhen
**年**: 2026 | **被引用数**: 49999
**タイプ**: primary | **分野**: 脳科学

## Abstract

A dependency-free experiment runner that turns a paper's research question into a configuration-driven, verifiable experiment task. The bundled reproduction maps the first/second moment estimates and bias correction of Adam (Kingma & Ba, arXiv:1412.6980) into runnable Python and compares them against fixed-learning-rate SGD under fixed seeds and epoch budgets. A second experiment measures convergence speed (epochs to reach a target training loss) against SGD with heavy-ball momentum, AdaGrad and RMSProp, with every optimizer family tuned by the same coarse learning-rate sweep. In that experiment Adam is not the fastest; the negative result is reported in full. Every reported number is pinned in an expected-values file with explicit tolerances and checked by one command that also runs the unit tests, and the checking harness is validated against deliberately broken implementations (negative controls). The repository also ships a task contract that expresses the reproduction as a repeatable, scoreable task for an automated research loop.
