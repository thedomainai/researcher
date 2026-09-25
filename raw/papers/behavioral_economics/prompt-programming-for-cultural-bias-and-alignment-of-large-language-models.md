---
title: "Prompt Programming for Cultural Bias and Alignment of Large Language Models"
authors: "Maksim Eren, Eric Michalak, Brian Cook, Johnny Seales Jr"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-08-21T06:01:26.242567"
doi: "https://doi.org/10.1145/3820755.3821487"
openalex_id: "https://openalex.org/W7170580068"
source_api: "openalex"
---

# Prompt Programming for Cultural Bias and Alignment of Large Language Models

**著者**: Maksim Eren, Eric Michalak, Brian Cook, Johnny Seales Jr
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Culture shapes reasoning, values, prioritization, and strategic decisionmaking, yet large language models (LLMs) often exhibit cultural biases that misalign with target populations. As LLMs are increasingly used for strategic decision-making, policy support, and document engineering tasks such as summarization, categorization, and compliance-oriented auditing, improving cultural alignment is important for ensuring that downstream analyses and recommendations reflect target-population value profiles rather than default model priors. Previous work introduced a survey-grounded cultural alignment framework and showed that culture-specific prompting can reduce misalignment, but it primarily evaluated proprietary models and relied on manual prompt engineering. In this paper, we validate and extend that framework by reproducing its social sciences survey based projection and distance metrics on open-weight LLMs, testing whether the same cultural skew and benefits of culture conditioning persist outside closed LLM systems. We then introduce use of prompt programming with DSPy for this problem—treating prompts as modular, optimizable programs—to tune cultural conditioning by optimizing against cultural-distance objectives. In our experiments, we show that prompt optimization often improves upon cultural prompt engineering, suggesting prompt compilation with DSPy can provide a more stable and transferable route to culturally aligned LLM responses.
