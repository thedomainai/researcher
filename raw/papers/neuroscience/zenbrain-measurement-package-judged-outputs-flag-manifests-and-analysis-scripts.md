---
title: "ZenBrain measurement package: judged outputs, flag manifests, and analysis scripts"
authors: "Alexander Bering"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-08-31T06:00:15.674437"
doi: "https://doi.org/10.5281/zenodo.22161977"
openalex_id: "https://openalex.org/W7158423182"
source_api: "openalex"
---

# ZenBrain measurement package: judged outputs, flag manifests, and analysis scripts

**著者**: Alexander Bering
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Reproduction package for the mechanism ablation tables of ZenBrain: A Neuroscience-Inspired 7-Layer Memory Architecture for Autonomous AI Systems (arXiv:2604.23878). npm install npm run experiments Four suites, 95 tests. No API keys, no network, no data files, no external services — the only runtime imports are Node's own crypto, fs and path. Measured on an Apple M-series laptop: the ablation suite takes 13 s, all four together under a minute. Scope, stated rather than implied The paper carries five tables captioned as ablations. This package reproduces three of them — the mechanism ablation across moderate (300 facts, 45 days, decay 0.15/day), challenging (400/50/0.20) and stress (500/60/0.25) conditions. Table 11 (NoDecay ablation on real LoCoMo) needs the LoCoMo corpus and Table 13 (Routing ablation study) comes from the retrieval pipeline; neither is here. The judged outputs, flag manifests and analysis scripts for the pipeline ablation are released as a separate companion record. Verification results/ holds the JSON the published tables were generated from. scripts/verify-against-reference.mjs compares a fresh run against it. Last measured: 722 point estimates identical, 0 drifted — reproduced on both macOS/ARM and Linux/x86. The point estimates come from seeded runs and match exactly. The ci95 bounds come from bootstrap resampling with an unseeded RNG and therefore differ between runs; none of those bounds appears in a printed table, and the comparison reports them separately rather than asserting on them. The comparison is tested against a planted defect: perturbing one precision.mean by 1×10-7 flips the verdict. A check that cannot fail proves nothing. Also available in the repository The same material is in zensation-ai/zenbrain under backend/, where continuous integration runs this procedure on every push and compares the output to the numbers above.
