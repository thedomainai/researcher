---
title: "MorphoOrgaAgent: A Foundation-Model-Based Multi-Agent System for Autonomous Organoid Analysis"
authors: "Hanyi Zhang, Maximilian Hoermann, Lion J. Gleiter, Yiling Xu, Bettina Katalin Budai"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-10T06:01:01.715293"
arxiv_id: "http://arxiv.org/abs/2609.08696v1"
source_api: "arxiv"
categories: "cs.MA, cs.CV"
---

# MorphoOrgaAgent: A Foundation-Model-Based Multi-Agent System for Autonomous Organoid Analysis

**著者**: Hanyi Zhang, Maximilian Hoermann, Lion J. Gleiter, Yiling Xu, Bettina Katalin Budai
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Organoids are three-dimensional tissue models whose morphology provides important insights into tumor development, disease progression, and drug testing. Extracting these morphological features relies heavily on manual segmentation, which is time-consuming and labor-intensive. Furthermore, performing quantitative statistical analysis typically requires custom coding skills and a mathematical background, presenting a major barrier for experimental biologists. To address these challenges, we introduce MorphoOrgaAgent, a multi-agent framework that achieves zero-shot organoid segmentation, automated data analysis, and report generation based on natural language input. The framework consists mainly of three core components: a TaskUnderstandingAgent that identifies requested measurements and visualization types; a hybrid segmentation module that combines Cellpose-derived geometric prompts with text prompts to guide SAM3 for zero-shot organoid instance segmentation; and a ReportAgent that computes quantitative metrics and compiles them alongside generated visualizations into a structured report. We further introduce MorphoOrgaVQA, a benchmark designed for quantitative evaluation of agent systems in organoid morphology analysis. Experimental results demonstrate that MorphoOrgaAgent handles both explicit and descriptive user requests, produces measurements closely matching ground truth, and generates complete analysis reports without requiring manual programming. The complete source code and MorphoOrgaVQA benchmark are publicly available at https://github.com/peng-lab/MorphoOrgaAgent.
