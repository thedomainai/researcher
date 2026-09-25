---
title: "XAI-Refine: An Automated Explanation-Knowledge Loop for Brain-Age Prediction"
authors: "Yang Qiao, Junjie Wu, Deqiang Qiu, James J. Lah, Liang Zhao"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-11T06:00:26.870448"
arxiv_id: "http://arxiv.org/abs/2609.09388v1"
source_api: "arxiv"
categories: "cs.LG, q-bio.NC"
---

# XAI-Refine: An Automated Explanation-Knowledge Loop for Brain-Age Prediction

**著者**: Yang Qiao, Junjie Wu, Deqiang Qiu, James J. Lah, Liang Zhao
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Brain-age prediction models are commonly evaluated by predictive accuracy, yet accurate predictions alone do not establish that a model relies on reproducible or neurobiologically supported mechanisms. Post-hoc explanation methods can expose these mechanisms, but existing workflows typically stop at diagnosis or require correction targets to be specified before model analysis. We propose XAI-Refine, an automated explanation-knowledge loop for brain-age prediction from resting-state functional connectivity. At each iteration, XAI-Refine consolidates complementary post-hoc analyses across repeated training runs into reliable, structured model explanations. It converts each reliable explanation into a neutral neurobiological question, retrieves and verifies relevant literature, and compiles the verified evidence into an admissible set in the same typed explanation space. The target for refinement is defined as the minimal projection of the current model explanation onto the admissible set induced by applicable verified knowledge. This revised explanation is then translated into a differentiable constraint while preserving the originating model variable, measurement operator, and applicable scope. Candidate updates are promoted only when multi-seed validation confirms target-directed explanatory movement, predictive performance remains within a prespecified guardrail, and non-target explanatory drift remains bounded. Experiments on functional-connectivity-based brain-age prediction evaluate predictive performance, explanation reliability, literature alignment, and target-specific model revision, illustrating a structured route from post-hoc analysis to evidence-guided model refinement.
