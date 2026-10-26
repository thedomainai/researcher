---
title: "Comparing Elitist Genetic Refinement and Reference-Point-Based Multi-Objective Optimization for Deep Q-Network Cloud Task Scheduling"
authors: "Sara Adnan Mahmood, Hussein Najm Abd Ali"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-10-27T06:01:38.195145"
doi: "https://doi.org/10.36548/jtcsst.2026.4.005"
openalex_id: "https://openalex.org/W7223459209"
source_api: "openalex"
---

# Comparing Elitist Genetic Refinement and Reference-Point-Based Multi-Objective Optimization for Deep Q-Network Cloud Task Scheduling

**著者**: Sara Adnan Mahmood, Hussein Najm Abd Ali
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Cloud task scheduling must balance conflicting objectives: deadline compliance, energy consumption, makespan, and resource utilization. A common design pairs a forecasting module and a reinforcement-learning placement agent with a periodic evolutionary refinement stage, usually a single-objective genetic algorithm that merges the four objectives into one weighted score. This paper studies whether replacing that stage with the reference-point-based multi-objective Non-dominated Sorting Genetic Algorithm III (NSGA-III) changes the scheduling results when forecasting and placement remain unchanged. Both strategies were evaluated on simulated five-machine clusters with workload-prediction signals from real monitoring traces over ten random seeds at 50,000 tasks (NSGA-III also at 100,000). The elitist genetic algorithm produced a mean of 0.495 percent of tasks violating their service-level agreement (SLA), against 0.178 percent for NSGA-III; a paired Wilcoxon signed-rank test confirmed the difference (p = 0.0039, r = 0.854). Doubling the workload left NSGA-III’s violation rate stable (paired p = 0.426). NSGA-III needed far more time per run (48.56 versus 9.05 minutes) and slightly more energy (30,582,411 versus 30,034,047 simulation units; p = 0.0020, r = 0.886). Sensitivity analyses on a 10,000-task protocol showed that the result depends on configuration: ten tasks per batch lay in a narrow working range, the number of reference points mattered little, and the final-selection weights mattered most. The two procedures also differ in search budget, but a genetic algorithm given NSGA-III’s budget and operators had a higher mean violation rate than either of them, so extra search does not explain the advantage. With task attributes derived from the Bitbrains traces, the ranking held, but the SLA advantage of NSGA-III shrank from 65 to 24 percent, and its energy penalty disappeared.
