---
title: "AI-Assisted Marine Logistics Digital Twin for Optimizing Dredger, Barge, and Support Vessel Coordination"
authors: "O. S. Al-Zabin, H. A. Gemaiy"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_management"
fetched: "2026-11-03T07:01:06.265980"
doi: "https://doi.org/10.2118/236476-ms"
openalex_id: "https://openalex.org/W7225047605"
source_api: "openalex"
---

# AI-Assisted Marine Logistics Digital Twin for Optimizing Dredger, Barge, and Support Vessel Coordination

**著者**: O. S. Al-Zabin, H. A. Gemaiy
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーション管理

## Abstract

Abstract Marine construction projects may combine several material-transfer methods that must operate as one coordinated production system. In the studied configuration, a self-propelled hopper dredger transports material in its own hopper, a cutter suction dredger delivers slurry through a pipeline, and sand barges handle approximately 20% of the modeled sand volume. These operations also depend on tugboats, a multicat, a fuel barge, a survey boat, rock barges, receiving-area availability, and onshore equipment. Poor coordination between these resources can increase waiting time, interrupt production, and raise fuel consumption. This paper proposes an AI-assisted marine logistics digital twin that maintains an updated virtual representation of vessel status, dredging progress, pipeline condition, weather restrictions, support-resource availability, and island receiving capacity. The AI component consists of two supervised XGBoost models trained, validated, and tested using a physics-informed synthetic dataset developed within published equipment operating ranges and explicit engineering assumptions. A regression model predicts hopper-dredger cycle duration and discharge waiting, while a classification model estimates the probability of a pipeline interruption during the following operating period. These predictions are incorporated into a rolling-horizon decision method that evaluates discharge timing, vessel assignments, sailing speeds, pipeline operating conditions, and support-service windows as the operational state changes. The framework was evaluated through a representative 14-day island-reclamation scenario using paired simulations of predefined rule-based and ML-assisted rolling-horizon coordination. The ML-assisted strategy increased modeled placed sand by approximately 6%, reduced mean hopper-dredger discharge waiting by approximately 83%, and lowered fuel intensity by approximately 10%. It also reduced CSD and pipeline downtime and improved the reliability of meeting the daily production target. These values are simulation-based proof-of-concept results generated under defined engineering assumptions and should be interpreted as a validation pathway for future project-data deployment rather than as measured field performance. The results show that the main value of the digital twin lies in using ML predictions to coordinate dredging, transport, pipeline, support, and receiving activities as one connected operation rather than optimizing individual assets separately.
