---
title: "When machines advise and machines approve: a multi-signal trust-scoring framework for AI outputs in high-stakes decision systems"
authors: "Kevan Rajaram, Patrick A. Hosein, Letetia Mary Addison, Kris Manohar"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-11-25T09:00:36.950332"
doi: "https://doi.org/10.1108/k-05-2026-1367"
openalex_id: "https://openalex.org/W7238824672"
source_api: "openalex"
---

# When machines advise and machines approve: a multi-signal trust-scoring framework for AI outputs in high-stakes decision systems

**著者**: Kevan Rajaram, Patrick A. Hosein, Letetia Mary Addison, Kris Manohar
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Purpose Large language models are increasingly deployed in financial decision support and institutional governance systems, yet there are no real-time mechanisms for assessing whether or not a given output is trustworthy enough to be used. This gap can expose institutional machine learning (ML) pipelines and consumer-facing artificial intelligence (AI) to a serious flaw, namely untrustworthy outputs flowing into decisions. We propose a metric and methodology for quantifying the trustworthiness of such outputs using a framework grounded in cybernetics. Design/methodology/approach The study empirically validates trust rating via aggregated claim evidence (TRACE), a multi-signal framework computing a composite trust score T from five signals: Evidence Grounding E, Verifiability V, Stability S, Logical Coherence L and Calibration C. We evaluate performance on 200 outputs across seven task categories using Spearman correlation, ANOVA and sensitivity/specificity analyses. Findings T shows strong predictive validity (ρ = 0.78, η2 = 0.65). Sensitivity on the dangerous class reaches 1.0, meaning zero incorrect outputs route to PUBLISH across all tested cost asymmetries. In general, the signal hierarchy was found to be V > E > S > L > C. Calibration captures a computational signature of sycophancy. Research limitations/implications External benchmark validation against TruthfulQA and MMLU is the primary extension for future work and an inter-rater reliability assessment is recommended. Practical implications TRACE provides a deployable trust overlay for LLM governance. The three-tier routing (PUBLISH/REVIEW/BLOCK) supports human-in-the-loop oversight for consequential AI-augmented decisions. Social implications As AI guidance substitutes for professional advice among financially excluded populations, output-level trust scoring helps ensure that the outputs reaching vulnerable users are evidence-grounded. Originality/value The paper presents the first deployed implementation and real-world validation of the proposed TRACE framework, contributes evidence-grounded $V$ and semantically-extended $L$, and unifies the institutional and consumer trust gaps in AI.
