---
title: "Multi-model assurance analysis showing large language models are highly vulnerable to adversarial hallucination attacks during clinical decision support"
authors: ["Mahmud Omar", "Vera Sorin", "Jeremy D. Collins", "David Emil Reich", "Robert Freeman", "Nicholas P. Gavin", "Alexander W. Charney", "Lisa S. Stump", "et al."]
year: 2025
cited_by_count: 181
doi: "https://doi.org/10.1038/s43856-025-01021-3"
openalex_id: W4412853478
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Multi-model assurance analysis showing large language models are highly vulnerable to adversarial hallucination attacks during clinical decision support

**Authors**: Mahmud Omar, Vera Sorin, Jeremy D. Collins, David Emil Reich, Robert Freeman, Nicholas P. Gavin, Alexander W. Charney, Lisa S. Stump, et al. | **Year**: 2025 | **Cited by**: 181 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Large language models (LLMs) show promise in clinical contexts but can generate false facts (often referred to as “hallucinations”). One subset of these errors arises from adversarial attacks, in which fabricated details embedded in prompts lead the model to produce or elaborate on the false information. We embedded fabricated content in clinical prompts to elicit adversarial hallucination attacks in multiple large language models. We quantified how often they elaborated on false details and tested whether a specialized mitigation prompt or altered temperature settings reduced errors. We created 300 physician-validated simulated vignettes, each containing one fabricated detail (a laboratory test, a physical or radiological sign, or a medical condition). Each vignette was presented in short and long versions—differing only in word count but identical in medical content. We tested six LLMs under three conditions: default (standard settings), mitigating prompt (designed to reduce hallucinations), and temperature 0 (deterministic output with maximum response certainty), generating 5,400 outputs. If a model elaborated on the fabricated detail, the case was classified as a “hallucination”. Hallucination rates range from 50 % to 82 % across models and prompting methods. Prompt-based mitigation lowers the overall hallucination rate (mean across all models) from 66 % to 44 % (p < 0.001). For the best-performing model, GPT-4o, rates decline from 53 % to 23 % (p < 0.001). Temperature adjustments offer no significant improvement. Short vignettes show slightly higher odds of hallucination. LLMs are highly susceptible to adversarial hallucination attacks, frequently generating false clinical details that pose risks when used without safeguards. While prompt engineering reduces errors, it does not eliminate them. Large language models (LLM), such as ChatGPT, are artificial intelligence-based computer programs that generate text based on information they are provided to train from. We test six large language models with 300 pieces of text similar to those written by doctors as clinical notes, but containing a single fake lab value, sign, or disease. We find that the LLM models repeat or elaborate on the planted error in up to 83 % of cases. Adopting strategies to prevent the impact of inappropriate instructions can half the rate but does not eliminate the risk of errors remaining. Our results highlight that caution should be taken when using LLM to interpret clinical notes. Omar et al. test six leading large language models with 300 doctor-designed clinical vignettes containing a single fake lab value, sign or disease. They show that the models repeat or elaborate on the planted error in up to 83 % of cases with a simple mitigation prompt halving the rate but not eliminating the risk.
