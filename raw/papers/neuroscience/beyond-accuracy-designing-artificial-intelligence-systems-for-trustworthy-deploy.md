---
title: "Beyond Accuracy: Designing Artificial Intelligence Systems for Trustworthy Deployment in Regulated Domains"
authors: "Mario Bonfrisco"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-06-12T06:00:36.827001"
doi: ""
openalex_id: "https://openalex.org/W7164252787"
source_api: "openalex"
---

# Beyond Accuracy: Designing Artificial Intelligence Systems for Trustworthy Deployment in Regulated Domains

**著者**: Mario Bonfrisco
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Artificial intelligence systems deployed in regulated domains must satisfy requirements that extend well beyond predictive accuracy. Legal accountability, transparency obligations and human oversight mandates — formalised in the European Union's Artificial Intelligence Act — demand architectures capable of demonstrating not only what they decide but why. This thesis investigates how AI systems can be designed to meet such requirements, through two complementary empirical studies addressing capability and accountability in public administration and healthcare. The first study develops a hybrid architecture for automated compliance verification of administrative documents in collaboration with Regione Liguria. After documenting the failure of supervised fine-tuning and prompt engineering approaches, a retrieval-augmented generation system is proposed that grounds evaluations in verified institutional precedents. The system achieves 77.94% accuracy across five compliance criteria (95% CI: 77.50–78.38%), with the retrieval and consensus components accounting for 99.75% of the improvement over the language model baseline. Consensus strength serves as a calibrated reliability indicator, enabling graduated human oversight through workflow stratification. Operational data from Regione Liguria contextualise these findings: the administration produces approximately 8,000 monocratic acts annually yet reviews only 7%, leaving the vast majority without quality assurance. The second study introduces TRIEX-EU, a framework integrating three independent explainability methods — label-wise attention, KernelSHAP and case-based reasoning — for reliability assessment in automated ICD-10 clinical coding on MIMIC-IV discharge summaries. The cascading architecture assigns each prediction to one of four confidence quadrants based on explanation quality and historical support. Predictions reaching the High Confidence quadrant achieve 88.5% accuracy against a 52.7% baseline, driven by a super-additive interaction between the two assessment dimensions. Sensitivity analyses confirm that all threshold parameters operate at natural breakpoints in their respective distributions, ensuring robustness to perturbation. A compliance evaluation protocol operationalises EU AI Act Articles 9, 13 and 14 into measurable system properties. Both investigations converge on a shared methodological insight: domain-specific knowledge grounding through concrete precedents — whether for primary prediction or reliability validation — consistently outperforms purely parametric approaches. Together, they demonstrate that trustworthy AI deployment in regulated environments requires architectures that integrate capability with accountability, supported by explicit confidence signals enabling meaningful human oversight.
