---
title: "SoK: The Security-Safety Continuum of Multimodal Foundation Models"
authors: "Ruoxi Sun, Jiamin Chang, Hammond A. Pearce, Chaowei Xiao, Bo Li"
year: 2026
citations: 4
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-11-06T08:09:45.719393"
doi: "https://doi.org/10.1145/3846374.3846395"
openalex_id: "https://openalex.org/W4404573249"
source_api: "openalex"
---

# SoK: The Security-Safety Continuum of Multimodal Foundation Models

**著者**: Ruoxi Sun, Jiamin Chang, Hammond A. Pearce, Chaowei Xiao, Bo Li
**年**: 2026 | **被引用数**: 4
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Multimodal foundation models (MFMs) integrate diverse data modalities to support complex and wide-ranging tasks. However, this integration also introduces distinct safety and security challenges. In this paper, we unify the concepts of safety and security in the context of MFMs by identifying critical threats that arise from both model behavior and system-level interactions. We propose a taxonomy grounded in information theory, evaluating risks through the concepts of channel capacity, signal, noise, and bandwidth. This perspective provides a principled way to analyze how information flows through MFMs and how vulnerabilities can emerge across modalities. Building on this foundation, we introduce a deterministic minimax formulation to analyze defense mechanisms and to study a structural asymmetry of defense in multimodal systems. Our analysis indicates that model-centric defenses, which primarily operate by suppressing noise or enhancing signal, tend to exhibit diminishing effectiveness against increasingly adaptive attacks. In contrast, system-level safeguards that constrain authorized information flow and agent behavior impose stronger limits on adversarial impact by reducing effective bandwidth. To operationalize this insight, our framework maps attacks and defenses onto information-theoretic axes, effectively organizing and reducing the defense search space. Using a proposed Defense Coverage Index (DCI) to evaluate 15 representative defenses, we observe that system-level bandwidth constraints provide stronger and more consistent protection across attack classes than brittle model-level mechanisms. Finally, we formalize an MFM ``self-destruction threshold'' that specifies when termination should be triggered, offering a concrete activation rule for circuit-breaker safeguards in multimodal systems.
