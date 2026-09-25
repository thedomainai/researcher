---
title: "Investigating Assistant Bias in LLM User Simulators Using a Role Vector"
authors: "Daeheon Jeong, Yoonjoo Lee, Eugene Choi, Sinie van der Ben, Juho Kim"
year: 2026
citations: 0
paper_type: "primary"
domain: "cognitive_science"
fetched: "2026-09-03T06:02:16.739552"
arxiv_id: "http://arxiv.org/abs/2609.00608v1"
source_api: "arxiv"
categories: "cs.CL, cs.HC"
---

# Investigating Assistant Bias in LLM User Simulators Using a Role Vector

**著者**: Daeheon Jeong, Yoonjoo Lee, Eugene Choi, Sinie van der Ben, Juho Kim
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 認知科学

## Abstract

LLM-based user simulators are increasingly used to evaluate autonomous agents at scale, in place of costly human evaluations. Despite this promise, these simulators exhibit "assistant bias," a tendency to cooperate and pursue task goals. They rarely reproduce the frustration or disengagement that real users exhibit, compromising evaluation validity. Prior work outlines that this bias is baked in during model training, which role-playing prompts fail to override. We analyze this bias from model activations, extracting a user role vector by contrasting how the model represents user versus assistant perspectives on the same dialogue. We observe two findings: (i) the user direction is identifiable in activations, elicits user-like behaviors, and captures characteristics distinct from assistant traits; and (ii) although user-role activation associates with simulation realism and steering strengthens it, it can exaggerate user behaviors and override individual user profiles. Together, our findings provide a representation-level analysis of LLM user simulators, confirming that assistant bias is structurally identifiable and that user behavior can be directionally analyzed.
