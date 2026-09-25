---
title: "N-CogHCI: A Reliability-Aware Neutrosophic Cognitive Control Framework for Cognitive AI-Enhanced Human–Computer Interaction"
authors: "Nada Mohamed, Alshaimaa A. Tantawy"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-09-18T06:02:39.450124"
doi: "https://doi.org/10.5281/zenodo.22782042"
openalex_id: "https://openalex.org/W7213398673"
source_api: "openalex"
---

# N-CogHCI: A Reliability-Aware Neutrosophic Cognitive Control Framework for Cognitive AI-Enhanced Human–Computer Interaction

**著者**: Nada Mohamed, Alshaimaa A. Tantawy
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

Cognitive AI systems increasingly participate in decisions that were previously controlled entirely by human users, yet most adaptive interfaces still compress uncertain user states into a single class probability or a fixed automation level. This paper introduces N-CogHCI, a reliability-aware neutrosophic cognitive control framework that represents cognitive evidence as truth, indeterminacy, and falsity components and uses that state to regulate human–AI authority in real time. The framework combines reliability-weighted multimodal evidence, explicit disagreement and missingness modeling, AI epistemic uncertainty, task risk, human expertise, and a safety gate that constrains autonomy when uncertainty and consequence are jointly high. A discrete authority variable selects among human-only, human-led shared, balanced shared, AI-led shared, and autonomous modes, while the interface policy adapts explanation depth, confirmation requirements, information density, and intervention timing. Formal analysis establishes boundedness of the state representation and monotonic growth of indeterminacy as evidence quality falls or cross-source disagreement rises. A reproducible controlled Monte-Carlo stress test of 100,000 interaction states (seed 42) evaluates the controller under clean, noisy, missing, and contradictory evidence. N-CogHCI reduced high-autonomy decisions in predefined unsafe contexts to 8.31%, compared with 14.20% for crisp mean fusion and 11.92% for reliabilityweighted probabilistic fusion. In high-uncertainty contexts, the corresponding rates were 15.42%, 27.74%, and 21.60%. This safety gain was obtained with a small increase in normalized decision loss (0.2053 versus 0.2037 and 0.2037), exposing rather than hiding the safety–efficiency trade-off. No empirical performance is claimed for human-participant datasets that were not executed. Instead, a leakage-resistant validation protocol is specified for COLET, SWELL-KW, and CLAS. The results support neutrosophic indeterminacy as a control variable for mixed-initiative HCI, while identifying real-user validation as the necessary next empirical step.
