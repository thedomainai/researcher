---
title: "Velocity- and Regime-Aware Detection of Intraday Options Market Manipulation, with Explainable Attribution"
authors: "Alex Chen, Maria Hybinette"
year: 2026
citations: 0
paper_type: "primary"
domain: "accounting"
fetched: "2026-11-15T06:55:10.074071"
doi: "https://doi.org/10.1145/3858063.3858692"
openalex_id: "https://openalex.org/W7201867243"
source_api: "openalex"
---

# Velocity- and Regime-Aware Detection of Intraday Options Market Manipulation, with Explainable Attribution

**著者**: Alex Chen, Maria Hybinette
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 会計学

## Abstract

Intraday market manipulation is hard to detect because its footprint is brief, buried in millions of quotes, and statistically similar to ordinary volatility. Detectors reach high recall only by flagging so many other days that measured precision collapses, producing alerts no regulator can act on. We show that this manipulation leaves a distinctive dynamic signature: a pump-and-crash pattern visible in the velocity of market state, rather than its level. We build a minute-level detection pipeline, strictly partitioned in time, based on smoothed state velocity: option-Delta velocity for index options and price velocity for equities. We explain every alert with SHAP attribution. We hold the test period strictly out-of-sample and fix all thresholds before evaluation. On the locked Indian BANKNIFTY index-options test, the plain autoencoder recovers 10 of 10 regulator-identified manipulation days. Conditioning detection on market regimes inferred by a hidden Markov model yields an instructive negative result. The regimes are descriptively distinct, but using them trades recall for precision. Under the closed-world assumption that unlabeled days are normal, precision remains near 25%. The same dynamic appears in thinly traded U.S. equities (SEC v. Patel). The shape of the signature survives the transfer; its velocity magnitude does not. A pump-reversal shape score ranks the complaint's alleged manipulation days with AUC 0.91 (ARQQ) and 0.81 (ACY). On the ARQQ worked example, the score peaks inside the complaint's documented minute window. Finally, exact SHAP attribution over every alert shows that unconfirmed alerts share the regulator-identified days' attribution profile (cosine similarity 0.99). The precision ceiling is consistent with incomplete enforcement labels rather than detector failure. What transfers across markets and instrument types is the dynamic signature itself.
