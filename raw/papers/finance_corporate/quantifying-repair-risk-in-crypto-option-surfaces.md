---
title: "Quantifying Repair Risk in Crypto Option Surfaces"
authors: "Tenghan Zhong"
year: 2026
citations: 0
paper_type: "primary"
domain: "finance_corporate"
fetched: "2026-11-15T06:55:03.140676"
doi: "https://doi.org/10.1145/3858063.3858699"
openalex_id: "https://openalex.org/W7225198865"
source_api: "openalex"
---

# Quantifying Repair Risk in Crypto Option Surfaces

**著者**: Tenghan Zhong
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: コーポレートファイナンス

## Abstract

Option desks adjust crypto option quotes into price surfaces that remain within bid-ask intervals and satisfy standard no-arbitrage restrictions across strikes before computing Greeks, hedge quantities, or risk measures. For the same quote panel, however, these constraints may admit multiple such surfaces, which we call admissible repairs, with different downstream outputs. We define the resulting variation as repair risk and propose repair-risk validation, a matched framework for quantifying dispersion in Greeks, hedge quantities, and risk measures. The mechanism is finite-difference amplification: two admissible repairs within price distance $\varepsilon$ can differ in local normalized-strike curvature by $4\varepsilon/h^2$, where $h$ is local normalized-strike spacing. We evaluate repair risk on Deribit BTC and ETH option chains, using $L_1$ and $L_2$ projections of midpoint prices onto the same admissible set as matched controls. Across 108 matched evaluations spanning 18 sampled calendar months, the median 90th percentile of the scaled spot-gamma gap for $L_2$ versus the $ρ=10$ smoothness-penalized repair is nearly twenty times the matched $L_1$--$L_2$ control. We also instantiate NN-Proj, a neural-projection repair, to test whether learned repairs exhibit repair risk. Despite good held-out fit, its downstream outputs remain distinct from those of classical repairs. Across five seeds with the same training window and architecture, its curvature dispersion exceeds the matched $L_1$--$L_2$ control in 17 of 18 months ($p=1.45\times10^{-4}$). For a USD 1 million risk reversal, switching from $L_2$ to the $ρ=10$ repair shifts the median 90th-percentile hedge notional by 18.62 basis points of gross spot notional. VaR-style estimates also exhibit greater dispersion across repairs. The repair rule is therefore part of the risk model, not merely a feasibility check.
