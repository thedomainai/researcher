---
title: "Artificial Epidemiology: A Decision-Theoretic Framework for Measuring AI-Induced Prevalence Divergence in Administrative Health Data"
authors: "Florian Odilo Stummer, Hans Thulesius, Thomas Frese"
year: 2026
citations: 2
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-11-14T06:11:12.729146"
doi: "https://doi.org/10.3390/medsci14070777"
openalex_id: "https://openalex.org/W7148323848"
source_api: "openalex"
---

# Artificial Epidemiology: A Decision-Theoretic Framework for Measuring AI-Induced Prevalence Divergence in Administrative Health Data

**著者**: Florian Odilo Stummer, Hans Thulesius, Thomas Frese
**年**: 2026 | **被引用数**: 2
**タイプ**: primary | **分野**: 認知科学

## Abstract

Background/Objectives:AI-assisted documentation and coding tools add diagnoses to health records, and self-updating AI agents may soon learn from the codes they generate. The objective was to develop a framework for asking whether such systems could distort disease prevalence at population scale, and a measurement approach for detecting it. Methods: We specify a partially observable Markov decision process in which a coding agent observes the administrative record exactly but clinical state only with delay and noise, derives the conditions under which policy-gradient learning follows the administrative reward, and states the general claim as a falsifiable hypothesis. We define the artificial epidemiology divergence D(C) = Pa(C) − Pc(C) relative to an explicit clinical reference standard, relate it to sensitivity and specificity of administrative case definitions, and propose five markers with falsification conditions. A pre-study on nine synthetic datasets (Synthea; four US states; eight distinct populations, one of 11,475 and seven of about 3400 patients, and one repeated generation with the same seed) measured D(C) for five metabolic conditions without any AI coding process, with bootstrap intervals and sensitivity analyses, and tested whether injected coding changes were detectable. Results: Under the primary reference definition, D(C) was +0.041 (95% CI 0.036 to 0.045) for type 2 diabetes, −0.125 for hypertension, −0.191 for hyperlipidaemia and +0.314 for obesity, with consistent signs across all populations. The magnitude, and for hypertension, hyperlipidaemia and obesity the sign, depended on the reference definition. An injected upcoding of 5% per year was detected as a change in the slope of D(C) in all populations, and an undercoding of 10% per year in all populations. Conclusions: The baseline value of D(C) reflects the measurement definition, and the operationally relevant quantity is its change under a fixed definition. The synthetic results establish a measurement approach and its detection limits, not evidence that AI causes prevalence distortion; computing D(C) on linked administrative and clinical records around AI deployment is the necessary next step.
