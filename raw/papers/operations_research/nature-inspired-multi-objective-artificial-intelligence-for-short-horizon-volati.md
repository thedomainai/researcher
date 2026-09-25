---
title: "Nature-inspired multi-objective artificial intelligence for short-horizon volatility-regime early warning and defensive asset allocation"
authors: "Hamza Boukeffa, Selman Djeffal, Abdelhamid Ghoul"
year: 2026
citations: 0
paper_type: "meta_analysis"
domain: "operations_research"
fetched: "2026-09-16T09:22:45.505696"
doi: "https://doi.org/10.3389/frai.2026.1953907"
openalex_id: "https://openalex.org/W7212784001"
source_api: "openalex"
---

# Nature-inspired multi-objective artificial intelligence for short-horizon volatility-regime early warning and defensive asset allocation

**著者**: Hamza Boukeffa, Selman Djeffal, Abdelhamid Ghoul
**年**: 2026 | **被引用数**: 0
**タイプ**: meta_analysis | **分野**: オペレーションズリサーチ

## Abstract

Early warning of market turbulence is usually treated as a classification problem, yet a usable system must also produce trustworthy probabilities, stay parsimonious and convert forecasts into defensible positions. We formulate that joint problem as a seven-objective optimisation task in which indicator selection, ridge-logistic regularization, decision threshold, calibration temperature and five defensive-allocation controls are tuned together, and we compare eleven metaheuristics under identical budgets on daily SPY and VIX data from January 2015 to February 2020. The target is a short-horizon volatility-regime exceedance: whether the VIX rises above its rolling 80th percentile within five trading days. Each experiment was repeated over 30 runs and benchmarked against a random-search control, nine conventional strategies, five rolling origins and five alternative stress definitions, with Friedman tests, Holm-corrected pairwise comparisons, effect sizes and bootstrap intervals. In the validation objective space the metaheuristics separate clearly: gray wolf optimisation obtains the best aggregate rank, ant colony optimisation the largest hypervolume and the lowest scalar loss, and most methods dominate random search with large effect sizes. On the untouched holdout the separation disappears. Balanced accuracy lies between 0.66 and 0.70 for every method, run-to-run dispersion equals the between-method spread, no metaheuristic beats random search on any criterion, and stronger validation search is associated with slightly weaker generalization. A ridge-logistic model with a fixed 0.50 threshold matches or exceeds every optimized configuration, and ranking the same days by the current VIX alone reaches an area under the curve of 0.772. The framework performs better under realized-volatility, drawdown and illiquidity labels. Pareto quality and decision quality therefore have to be reported separately. A MATLAB implementation reproducing every result is provided.
