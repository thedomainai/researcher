---
title: "Digital Twin Workflow for Continuous Glucose Forecasting: Real-Time Data Assimilation Using Reinforcement Learning"
authors: "Cao Xiang, Qi Wang"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-10-27T06:06:13.014951"
doi: "https://doi.org/10.64898/2026.10.23.26366163"
openalex_id: "https://openalex.org/W7223457014"
source_api: "openalex"
---

# Digital Twin Workflow for Continuous Glucose Forecasting: Real-Time Data Assimilation Using Reinforcement Learning

**著者**: Cao Xiang, Qi Wang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Digital twins for physiological forecasting require robust mechanisms for continuously assimilating streaming data and adapting to patient-specific dynamics. Threshold-triggered model updates can restore predictive performance after substantial drift, but their reactive nature limits continuous adaptation. We propose a proactive digital twin framework that couples a pretrained PatchTST foundation model with an Actor-Critic reinforcement learning (RL) agent for residual correction. Using a 30-minute look-back window and recent residual history, the agent generates bounded corrections (± 0.05) to the first-step baseline forecast, with corrected predictions recursively propagated over a 15-step horizon. We evaluate both an RL-only workflow and a hybrid workflow combining RL correction with threshold-triggered fine-tuning using minute-by-minute continuous glucose monitoring data from 10 critically ill patients with sepsis. Across all patients, the pretrained RL agent improves forecasting accuracy without patient-specific retraining. Both workflows reduce trajectory-averaged mean absolute percentage error, ensemble relative error, and maximum errors compared with the uncorrected baseline and previously developed reactive digital twin models. These findings support residual reinforcement learning as a lightweight mechanism for continuous, real-time data assimilation that preserves the foundation model's global predictive prior while enabling patient-specific forecast adaptation, with potential applications in critical care decision support.
