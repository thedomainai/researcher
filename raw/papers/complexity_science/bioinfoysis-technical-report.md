---
title: "Bioinfoysis Technical Report"
authors: "Qingyang Shao, Xin Zhang, Zhouyang Yuan, Xianying Chen, Yujia Xiang"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-05T06:01:12.531527"
arxiv_id: "http://arxiv.org/abs/2609.03871v1"
source_api: "arxiv"
categories: "cs.AI, cs.MA"
---

# Bioinfoysis Technical Report

**著者**: Qingyang Shao, Xin Zhang, Zhouyang Yuan, Xianying Chen, Yujia Xiang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Large language model agents have shown promise in bioinformatics, but most existing systems focus primarily on producing final answers, treating planning, tool use, and code execution as transient interactions. This design is poorly suited to long-horizon bioinformatics tasks, where conclusions must remain connected to the data, computations, and intermediate evidence that support them. We introduce \textbf{Bioinfoysis}, a multi-agent harness that represents each request as a persistent, artifact-grounded analysis run. Bioinfoysis combines global planning with step-wise, evidence-driven replanning: the planner maintains an executable checklist and revises pending steps using structured handoffs returned after each worker execution. These handoffs bind intermediate results to their responsible agent, checklist step, and plan generation, preventing stale evidence from being silently reused after replanning. A controlled runtime validates generated scripts, tables, and figures before they are used in downstream analysis or reporting, while role-specific context, persistent memory, and governed bioinformatics skills support reliable execution over long analysis trajectories. We evaluate Bioinfoysis on BixBench and two question-answering tracks of LAB-Bench 2. On BixBench, Bioinfoysis achieves state-of-the-art accuracy of 82.4\%. Across four underlying language models, Bioinfoysis increases average accuracy from 27.81\% to 64.13\% on SeqQA2 and from 3.13\% to 31.25\% on DbQA2. These results demonstrate that reliable bioinformatics automation depends not only on model capability, but also on the harness that governs planning, execution, memory, and evidence flow. We hope that the emergence of Bioinfoysis will play a driving and leading role in the development of the bioinformatics community. Our demo website can be seen in https://report.bioinfoysis.com/.
