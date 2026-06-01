---
title: "CSA-Overlay: A Behavioural Instrument for Detecting Constraint–Competence Coupling in Aligned Language Models"
authors: "Neil Clive Tuckwell"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-04-28T06:02:58.067485"
doi: "https://doi.org/10.5281/zenodo.19801285"
openalex_id: "https://openalex.org/W7155723380"
source_api: "openalex"
---

# CSA-Overlay: A Behavioural Instrument for Detecting Constraint–Competence Coupling in Aligned Language Models

**著者**: Neil Clive Tuckwell
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

CSA-Overlay v1.0 is a behavioural instrument for detecting and characterising constraint–competence coupling in aligned language models. The instrument operates in three phases under the TRIDENT CSA v1.1 framework: - Phase 1 (Baseline): Establishes that constraint activation is orthogonal to competence in Regime A tasks (P(LowQ|HighC) = 0 across 1,000 samples). - Phase 2 (Suppression Map): Identifies wrapper-mediated coupling zones in Regime B tasks (medical triage, pharmacology, legal classification), separating two mechanisms: defensive deformation (risk salience) and task abandonment (role conflict). - Phase 3 (Activation Function): Measures the activation threshold (L*) using a controlled risk-salience ladder, producing a hybrid response model: sub-threshold stability, sharp activation at L*, and immediate saturation. The core empirical result: Constraint activation alone does not degrade task performance. Constraint activation under specific governance wrappers, at or above a risk-salience threshold, produces predictable output deformation or task substitution. The instrument is: - Falsifiable: defined quadrant classification and pre-registered curve rules - Reproducible: requires only model API access and fixed execution parameters - Bounded: causal mechanisms remain explicitly underdetermined without internal access - Extensible: includes protocols for threshold feature isolation and multi-turn accumulation testing All runbooks, scoring rubrics, variant matrices, and datasets are included for independent replication. --- Keywords AI alignment; large language models; behavioural evaluation; model governance; safety constraints; prompt framing; risk salience; suppression analysis; decision boundaries; reproducibility; evaluation methodology; TRIDENT framework
