---
title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
authors: ["Xuezhi Wang", "Wei, Jason", "Dale Schuurmans", "Quoc Viet Le", "Ed H.", "Narang, Sharan", "Chowdhery, Aakanksha", "Zhou, Denny"]
year: 2022
cited_by_count: 706
doi: "https://doi.org/10.48550/arxiv.2203.11171"
openalex_id: W4221161695
paper_type: preprint
evidence_kind: article
topics: ["elicitation"]
landmark: true
abstract_source: "openalex"
---

# Self-Consistency Improves Chain of Thought Reasoning in Language Models

**Authors**: Xuezhi Wang, Wei, Jason, Dale Schuurmans, Quoc Viet Le, Ed H., Narang, Sharan, Chowdhery, Aakanksha, Zhou, Denny | **Year**: 2022 | **Cited by**: 706 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

Chain-of-thought prompting combined with pre-trained large language models has achieved encouraging results on complex reasoning tasks. In this paper, we propose a new decoding strategy, self-consistency, to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths. Self-consistency leverages the intuition that a complex reasoning problem typically admits multiple different ways of thinking leading to its unique correct answer. Our extensive empirical evaluation shows that self-consistency boosts the performance of chain-of-thought prompting with a striking margin on a range of popular arithmetic and commonsense reasoning benchmarks, including GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%).
