---
title: "Automatic Causal Fairness Analysis with LLM-Generated Reporting"
authors: "Alessia Berarducci, Eric Rossetto, Alessandro Antonucci, Marco Zaffalon"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-11-25T09:05:40.929496"
doi: "https://doi.org/10.1007/978-3-032-44866-8_6"
openalex_id: "https://openalex.org/W7159630036"
source_api: "openalex"
---

# Automatic Causal Fairness Analysis with LLM-Generated Reporting

**著者**: Alessia Berarducci, Eric Rossetto, Alessandro Antonucci, Marco Zaffalon
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

AutoML, intended as the process of automating the application of machine learning to real-world problems, is a key step for AI popularisation. Most AutoML frameworks are not accounting for the potential lack of fairness in the training data and in the corresponding predictions. We introduce FairMind , a software prototype aiming to automatise fairness analysis at the dataset level. We achieve that by resorting to the assumptions of the standard fairness model , recently proposed by Plečko and Bareinboim. This allows for a sound fairness evaluation in terms of causal effects, based on counterfactual queries involving the target, possibly confounders and mediators, and the different values of an input feature we regard as protected . Given a dataset and the roles of its variables, the tool implements a closed-form computation of the effects. An LLM is then used, as an interpretative layer—performing no computation—to turn the computed effects into a natural-language report. We achieve that in a zero-shot setup and show by examples the expected advantages with respect to a direct analysis performed by the LLM. To favour applications, extensions to ordinal protected variable and continuous targets and novel decomposition results are also discussed.
