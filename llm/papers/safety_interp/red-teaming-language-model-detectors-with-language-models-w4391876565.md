---
title: "Red Teaming Language Model Detectors with Language Models"
authors: ["Zhouxing Shi", "Yihan Wang", "Fan Yin", "Xiangning Chen", "Kai-Wei Chang", "Cho‐Jui Hsieh"]
year: 2024
cited_by_count: 25
doi: "https://doi.org/10.1162/tacl_a_00639"
openalex_id: W4391876565
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Red Teaming Language Model Detectors with Language Models

**Authors**: Zhouxing Shi, Yihan Wang, Fan Yin, Xiangning Chen, Kai-Wei Chang, Cho‐Jui Hsieh | **Year**: 2024 | **Cited by**: 25 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Abstract The prevalence and strong capability of large language models (LLMs) present significant safety and ethical risks if exploited by malicious users. To prevent the potentially deceptive usage of LLMs, recent work has proposed algorithms to detect LLM-generated text and protect LLMs. In this paper, we investigate the robustness and reliability of these LLM detectors under adversarial attacks. We study two types of attack strategies: 1) replacing certain words in an LLM’s output with their synonyms given the context; 2) automatically searching for an instructional prompt to alter the writing style of the generation. In both strategies, we leverage an auxiliary LLM to generate the word replacements or the instructional prompt. Different from previous works, we consider a challenging setting where the auxiliary LLM can also be protected by a detector. Experiments reveal that our attacks effectively compromise the performance of all detectors in the study with plausible generations, underscoring the urgent need to improve the robustness of LLM-generated text detection systems. Code is available at https://github.com/shizhouxing/LLM-Detector-Robustness.
