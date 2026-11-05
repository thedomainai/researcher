---
title: "State-Dependent Event Tree Analysis: A Dynamic Methodological Extension for Safety of the Intended Functionality in Automotive Systems"
authors: "Dhiraj Mohan Sharma, Megha Dharnendra Mutagi, Kakarla Subba Reddy"
year: 2026
citations: 0
paper_type: "primary"
domain: "systems_engineering"
fetched: "2026-11-06T08:11:19.393831"
doi: "https://doi.org/10.4271/2026-28-0140"
openalex_id: "https://openalex.org/W7225274315"
source_api: "openalex"
---

# State-Dependent Event Tree Analysis: A Dynamic Methodological Extension for Safety of the Intended Functionality in Automotive Systems

**著者**: Dhiraj Mohan Sharma, Megha Dharnendra Mutagi, Kakarla Subba Reddy
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: システム工学

## Abstract

As automotive architectures evolve toward Software Defined Vehicles (SDVs) and high levels of driving automation, traditional safety analysis techniques rooted in hardware reliability require significant adaptation. The Classical Event Tree Analysis (ETA), a cornerstone of ISO 26262 functional safety compliance, relies on static, binary branching logic where each function either fails or succeeds. While highly interpretable and effective for modelling random hardware failures, classical ETA struggles to capture the dynamic, non-linear interactions, temporal degradation, and complex human-machine interface (HMI) dependencies that are characteristic of modern Advanced Driver Assistance Systems (ADAS) and autonomous vehicles. This paper proposes State Dependent Event Tree Analysis (SD-ETA), a methodological extension designed to integrate discrete state vectors and temporal dependencies into the classical ETA framework. SD-ETA assigns probabilities to the branches for the dynamic nonlinear interactions, temporal degradation, and complex human-machine interface (HMI) dependencies instead of binary values, thereby allowing the system state (comprising vehicle physics, environmental conditions, and driver attention metrics) to dynamically update based on the outcomes of the preceding nodes. This approach retains the visual hierarchy and regulatory familiarity of standard event trees while significantly enhancing model fidelity for Safety of the Intended Functionality (SOTIF) scenarios governed by ISO 21448. To demonstrate the necessity and utility of this methodological evolution, this paper presents a comparative case study analysing a system operating under degraded environmental conditions. The quantitative application reveals that while classical ETA predicted a relatively low collision risk by treating sensor performance as a static binary state, the dynamic SD-ETA simulation exposed a critical hidden safety gap, calculating a higher collision probability due to compounded latency and degraded physical operating parameters. Ultimately, SD-ETA equips safety practitioners and automotive regulators with a modernized, time-aware framework to accurately evaluate the complex, interacting risks of autonomous systems without sacrificing the transparency required for rigorous safety certification.
