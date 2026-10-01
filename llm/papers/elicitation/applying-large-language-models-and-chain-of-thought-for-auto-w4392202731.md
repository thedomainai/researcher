---
title: "Applying large language models and chain-of-thought for automatic scoring"
authors: ["Gyeong-Geon Lee", "Ehsan Latif", "Xuansheng Wu", "Ninghao Liu", "Xiaoming Zhaı"]
year: 2024
cited_by_count: 161
doi: "https://doi.org/10.1016/j.caeai.2024.100213"
openalex_id: W4392202731
paper_type: article
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# Applying large language models and chain-of-thought for automatic scoring

**Authors**: Gyeong-Geon Lee, Ehsan Latif, Xuansheng Wu, Ninghao Liu, Xiaoming Zhaı | **Year**: 2024 | **Cited by**: 161 | **Kind**: article | **Relevance**: elicitation: supporting

## Abstract

This study investigates the application of large language models (LLMs), specifically GPT-3.5 and GPT-4, with Chain-of-Though (CoT) in the automatic scoring of student-written responses to science assessments. We focused on overcoming the challenges of accessibility, technical complexity, and lack of explainability that have previously limited the use of artificial intelligence-based automatic scoring tools among researchers and educators. With a testing dataset comprising six assessment tasks (three binomial and three trinomial) with 1650 student responses, we employed six prompt engineering strategies to automatically score student responses. The six strategies combined zero-shot or few-shot learning with CoT, either alone or alongside item stem and scoring rubrics, developed based on a novel approach, WRVRT (prompt writing, reviewing, validating, revising, and testing). Results indicated that few-shot (acc = 0.67) outperformed zero-shot learning (acc = 0.60), with 12.6% increase. CoT, when used without item stem and scoring rubrics, did not significantly affect scoring accuracy (acc = 0.60). However, CoT prompting paired with contextual item stems and rubrics proved to be a significant contributor to scoring accuracy (13.44% increase for zero-shot; 3.7% increase for few-shot). We found a more balanced accuracy across different proficiency categories when CoT was used with a scoring rubric, highlighting the importance of domain-specific reasoning in enhancing the effectiveness of LLMs in scoring tasks. We also found that GPT-4 demonstrated superior performance over GPT -3.5 in various scoring tasks when combined with the single-call greedy sampling or ensemble voting nucleus sampling strategy, showing 8.64% difference. Particularly, the single-call greedy sampling strategy with GPT-4 outperformed other approaches. This study also demonstrates the potential of LLMs in facilitating explainable and interpretable automatic scoring, emphasizing that CoT enhances accuracy and transparency, particularly when used with item stem and scoring rubrics.
