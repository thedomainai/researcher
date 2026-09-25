---
title: "Homophily in Human-AI Interaction"
authors: "Jonathan Winter, Klarita Gërxhani"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-09-17T06:03:25.719143"
doi: "https://doi.org/10.17632/jyy6nbj47j.2"
openalex_id: "https://openalex.org/W7212725344"
source_api: "openalex"
---

# Homophily in Human-AI Interaction

**著者**: Jonathan Winter, Klarita Gërxhani
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

This repository accompanies the manuscript "Homophily in Human–AI Interaction" (Winter & Gërxhani). It contains de-identified data and reproducibility materials for two studies examining whether demographic homophily shapes partner selection when potential partners are human versus AI agents. Study 1 (online experiment; Prolific; February 2023). Participants were randomly assigned to a Human–Human (HH) condition (partners were other Prolific participants represented by avatars) or a Human–AI (HA) condition (partners were bot agents represented by avatars). Participants selected (i) a competitor in an individual competition round and (ii) a teammate in a team competition round (order randomized) from balanced avatar pools (50% male/female; 50% White/Black). Participants then completed an incentivized arithmetic reasoning task in each round, producing measures of partner choice, task performance (number correct), and competition outcomes (win/tie/loss). The Study 1 dataset is the raw experiment export and includes participant demographics, treatment assignment, partner-choice variables and demographic cues, and performance/outcome variables; indicators of same-gender and same-race selection are derived from it by the analysis script. Study 2 (field onboarding data; U.S. users; July 2025). New users of a mobile mental-health companion application selected between two AI companion voice options (one masculine-presenting, one feminine-presenting) during onboarding. The Study 2 dataset includes de-identified user demographics and the selected voice option, enabling tests of gender-based homophily in AI companion selection. The repository includes a master R script (reproduce_all.R) that reads the deposited CSV files and regenerates every statistic reported in the article and its online appendix, writing a labelled reproduction log, tables and figures to a structured outputs/ folder. See README.md for details of the data and the analysis. For replication, the repository additionally includes the oTree implementation used to run Study 1.
