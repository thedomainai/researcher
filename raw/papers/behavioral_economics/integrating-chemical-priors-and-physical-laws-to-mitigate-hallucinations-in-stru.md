---
title: "Integrating chemical priors and physical laws to mitigate hallucinations in structure-based drug design"
authors: "Zhongyu Liu, Yadong Liu, Yihang Zhou, Zhiyuan Liu, Yuhang Yang"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-07-22T06:01:09.379966"
doi: "https://doi.org/10.1038/s42004-026-02115-2"
openalex_id: "https://openalex.org/W7169665898"
source_api: "openalex"
---

# Integrating chemical priors and physical laws to mitigate hallucinations in structure-based drug design

**著者**: Zhongyu Liu, Yadong Liu, Yihang Zhou, Zhiyuan Liu, Yuhang Yang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Generative artificial intelligence has shown great promise in structure-based drug design (SBDD), yet existing models often suffer from a fundamental crisis of “structural hallucinations”, generating molecules with high binding scores that violate basic chemical principles or physical plausibility. Here we present DrugRPG, a physicochemically-grounded 3D molecule generation framework that bridges this gap by integrating deep-learned chemical priors with fundamental physical laws. DrugRPG introduces a cross-dimensional representation alignment objective, distilling knowledge from a chemical foundation model pre-trained on 600 million molecular similarities to ensure the generation of valid topologies and realistic pharmacophoric patterns. Simultaneously, a differentiable physics-guided sampling strategy, inspired by the Lennard-Jones potential, is applied during the reverse diffusion phase to dynamically mitigate steric clashes and enforce Van der Waals compatibility. Comprehensive benchmarking demonstrates that DrugRPG reduces severe steric clashes by 65.4% compared to the state-of-the-art baseline while maintaining competitive structural self-consistency. Crucially, DrugRPG achieves a 28.6% higher success rate in generating developable candidates that satisfy multi-objective criteria, including potency, stability, and synthetic feasibility. By merging chemical heuristics with physical laws, DrugRPG effectively addresses the hallucination crisis, shifting generative SBDD from scoring-oriented optimization toward high-fidelity, realistic lead discovery. Generative AI in structure-based drug design often faces “structural hallucinations,” producing molecules that defy chemical and physical principles. Here, the authors introduce DrugRPG, a framework integrating deep-learned chemical priors with physical laws, significantly reducing steric clashes and enhancing the generation of viable drug candidates, thus advancing realistic lead discovery.
