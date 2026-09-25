---
title: "DA-MetaForecaster: A Drift-adaptive Three-phase Framework for Regime-aware Multi-horizon S&P 500 Return Forecasting"
authors: "Malige Gangappa, Ch. Ramesh, Sreeshanth Thummalapally, Amaravarapu Pramod Kumar"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-09-21T06:01:26.016108"
doi: "https://doi.org/10.22266/ijies2026.1031.15"
openalex_id: "https://openalex.org/W7213672912"
source_api: "openalex"
---

# DA-MetaForecaster: A Drift-adaptive Three-phase Framework for Regime-aware Multi-horizon S&P 500 Return Forecasting

**著者**: Malige Gangappa, Ch. Ramesh, Sreeshanth Thummalapally, Amaravarapu Pramod Kumar
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Accurate financial return forecasting is undermined by market regime shifts: crashes, booms, and recoveries follow distinct distributions that static models cannot track.We present DA-MetaForecaster, a three-phase PatchTSTbased framework for S&P 500 returns (2000-2023) at 1d-21d horizons.Phase 1 trains a backbone on 12 macrofinancial features with MAE loss, outperforming MSE (p<0.01).Phase 2 repurposes ANIL as an optional backbone pre-trainer, motivated by naive meta-learning degrading RMSE by up to 38%.Phase 3 applies regime-gated, crashonly test-time adaptation, adapting once per crash episode.At H=10d, crash directional accuracy improves from 0.364 ± 0.007 to 0.530 ± 0.038 (mean ± std over three predefined seeds); test-time adaptation contributes +15.2pp,ANIL +1.4pp (not significant).The effect is positive in every usable walk-forward fold (mean +8.0pp, p=0.0215) and in all three non-overlapping crash episodes, though heterogeneous.H=5d/H=21d gains are positive only on the primary 2018-2023 window and do not replicate across folds.
