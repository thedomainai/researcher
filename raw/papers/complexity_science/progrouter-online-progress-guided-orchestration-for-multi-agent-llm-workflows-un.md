---
title: "ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs"
authors: "Songyuan Li, Ahmed M. Abdelmoniem, Shiqiang Wang"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-08-28T09:08:44.092357"
arxiv_id: "http://arxiv.org/abs/2608.25992v1"
source_api: "arxiv"
categories: "cs.AI, cs.MA"
---

# ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs

**著者**: Songyuan Li, Ahmed M. Abdelmoniem, Shiqiang Wang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Multi-agent large language model (LLM) workflows have emerged as a powerful paradigm for solving complex, open-ended tasks through collaborative reasoning among specialized LLM agents, but they incur substantial operating costs due to repeated LLM invocations and long-horizon context accumulation. Existing cascade routing methods make one-shot, query-level decisions and cannot adapt to the dynamic, state-dependent nature of multi-step workflows, in which the right LLM at each step depends on evolving task progress, remaining task difficulty, and cost-efficiency requirements. We present ProgRouter, an online progress-guided routing framework that adaptively selects LLM agents across workflow steps to preserve task-solving quality while adhering to time and cost budgets. ProgRouter introduces a multi-view task progress scorer that combines coarse workflow outcome regimes with fine-grained signals on subtask completion, progress trends, and workflow state quality. Then, a dual-path task progress predictor and an adaptive meta-gating mechanism estimate the progress gain for each candidate routed LLM. ProgRouter makes online step-wise routing decisions that balance progress gain, task time budgets, and long-term operating cost efficiency. Experiments on HumanEval Plus, MBPP, MATH-500, and ASQA, spanning agentic code generation, mathematical reasoning, and retrieval-augmented long-form question answering, demonstrate that ProgRouter reduces the operating cost relative to key baselines while maintaining strong task-solving performance.
