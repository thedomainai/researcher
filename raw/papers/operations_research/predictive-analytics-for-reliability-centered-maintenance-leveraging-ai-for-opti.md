---
title: "Predictive Analytics for Reliability-Centered Maintenance: Leveraging AI for Optimization"
authors: "T. Sitthiwasuwat, K. Sasanas, L. Unjantee, A. Sirinuntawit, R. Channoom"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-11-03T07:01:38.443981"
doi: "https://doi.org/10.2118/236499-ms"
openalex_id: "https://openalex.org/W7225054764"
source_api: "openalex"
---

# Predictive Analytics for Reliability-Centered Maintenance: Leveraging AI for Optimization

**著者**: T. Sitthiwasuwat, K. Sasanas, L. Unjantee, A. Sirinuntawit, R. Channoom
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Abstract This study introduces a next-generation AI-driven framework that transforms Reliability-Centered Maintenance (RCM) from static, time-based scheduling into a dynamic, risk-optimized decision system. In industrial environments, limited failure history often forces conservative preventive maintenance (PM), resulting in inefficiencies—simultaneously over-maintaining healthy components while failing to prevent critical breakdowns. This work addresses that structural gap by deploying an agentic AI architecture that continuously fuses condition monitoring, probabilistic risk analytics, and degradation forecasting into a closed-loop optimization workflow. The objective is to enable real-time, failure-mode–specific PM decisions that balance reliability, cost, and operational constraints—delivering a step-change from periodic maintenance to adaptive, evidence-based execution. The framework integrates three autonomous layers: (1) data source and data conditioning, (2) AI-driven health scoring and prioritization, and (3) probabilistic forecasting and cost-optimized interval. Multi-source data—including PI historian streams, vibration signatures, lubricant analysis, and asset criticality—are harmonized and filtered to isolate true degradation signals. For each failure mode, an AI agent computes a normalized health score (0–100) based on degradation severity, persistence, trend dynamics, and data confidence. Failure modes breaching risk thresholds are escalated to specialized sub-agents that generate ensemble degradation forecasts (linear, polynomial, exponential), producing probabilistic remaining useful life (RUL) estimates (P10/P50/P90). These are translated into time-to-failure distributions and fitted using Weibull modeling, where β characterizes failure behavior and η defines characteristic life. The framework has been deployed to GE LM2500+G4 compressor package which is a gas turbine compressor package locating on Offshore Processing facility in the Gulf of Thailand. Results reveal a critical insight: nearly 57% of modeled failure modes exhibited non-aging (β < 1) behavior, indicating that traditional PM is inherently ineffective for these mechanisms. These modes were reclassified to run-to-failure or extended intervals, eliminating unnecessary maintenance. For aging-related modes (β > 1), optimization delivered substantial value. PM intervals were extended beyond the standard 8,000-hour cycle, with a representative wear-out case (β ≈ 5.4) achieving an optimal interval of ~18,300 hours—more than 2× extension without increased risk. Cost-risk curves clearly demonstrate the nonlinear trade-off between excessive maintenance and escalating failure probability, while sensitivity analysis highlights that interval decisions can vary by >30% depending on cost assumptions—reinforcing the importance of economic calibration.
