---
title: "The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate"
authors: "Blaž Bertalanič, Carolina Fortuna"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-05-23T06:03:03.000745"
doi: "https://doi.org/10.1145/3786335.3813137"
openalex_id: "https://openalex.org/W7160437446"
source_api: "openalex"
---

# The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate

**著者**: Blaž Bertalanič, Carolina Fortuna
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Multi-agent debate, where teams of LLMs iteratively exchange rationales and vote on answers, is widely deployed under the assumption that peer review filters hallucinations. Yet the failure dynamics of homogeneous debate remain poorly understood, therefore we report findings from a controlled empirical study of teams of $N{=}10$ homogeneous agents (Qwen2.5-7B, Llama-3.1-8B, Ministral-3-8B) across $R{=}3$ debate rounds on two high-difficulty benchmarks (GSM-Hard and MMLU-Hard). We compare peer debate against isolated self-correction and a stochastic noise control that injects rationales from unrelated problems. We decompose debate failure into three model-dependent pathways: sycophantic conformity, where agents uncritically adopt majority answers (modal adoption up to 85.5%); contextual fragility, where peer rationales destabilize previously correct reasoning (vulnerability rate up to 70.0%); and consensus collapse, where plurality voting discards correct answers already present in the generation pool (oracle gap up to 32.3 percentage points). Ablations over communication density ($K \in \{2,4,9\}$) and sampling temperature ($T \in \{0.4, 0.7\}$) show that conformity reaches high levels at minimal peer exposure ($K{=}2$) and intensifies with greater initial diversity. Across all configurations, debate consumes 2.1-3.4$\times$ more tokens (up to 28,631 tokens per problem) than self-correction for equal or lower accuracy. Our results indicate that, within the 7-8B parameter class, homogeneous teams without structured roles do not benefit from unguided peer exchange, and that isolated self-correction consistently offers a more favorable cost-accuracy tradeoff.
