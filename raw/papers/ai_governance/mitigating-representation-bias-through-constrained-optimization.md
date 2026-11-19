---
title: "Mitigating representation bias through constrained optimization"
authors: "Ziad Janpih"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-11-20T06:03:37.948852"
doi: ""
openalex_id: "https://openalex.org/W7236553670"
source_api: "openalex"
---

# Mitigating representation bias through constrained optimization

**著者**: Ziad Janpih
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Automated decision systems increasingly rely on people-related data, possibly amplifying discrimination already present in the real world. To prevent this, discrimination should be controlled throughout the data processing pipeline rather than assessed only on the final outcome. It may originate either from the data itself (representation bias) or from the algorithms that process the data (algorithmic bias), and can be characterized through properties such as coverage, which ensures sufficient representation of each protected group in the data, and fairness, which limits disparities among protected groups. This thesis focuses on data transformation, the preparation step in which a dataset is reshaped before analysis. This step deserves particular attention since it can amplify representation bias and propagate it to subsequent processing stages. This work investigates query rewriting as a way of correcting such bias. Given a selection query whose result violates a set of discrimination-aware constraints, the objective is to derive an alternative query that satisfies them while departing as little as possible from the original, thus preserving the analyst’s intent and the transparency of the transformation. Most existing query rewriting techniques address only one discrimination-related constraint at a time, enforcing either coverage or fairness over the query result, but not both simultaneously. To overcome this limitation, an initial optimization framework was proposed to jointly enforce coverage and fairness while minimizing deviation from the original query through a Mixed-Integer Nonlinear Programming (MINLP) formulation. Its experimental evaluation, however, revealed scalability limitations, motivating the development of new optimization approaches. Building on this initial framework, this thesis first provides an extensive experimental investigation of the MINLP-based approach and then introduces a continuous reformulation of the query rewriting problem. The new model operates directly on the query selection constants, eliminating the discretized search space and enabling more scalable optimization techniques. The resulting problem is solved using a Differential Evolution-based approach. The two formulations are evaluated on synthetic and real-world datasets and compared with state-of-the-art techniques under three settings: coverage constraints, fairness constraints, and their joint enforcement. The experimental results show a better trade-off among effectiveness, efficiency, and rewriting quality compared to the considered baseline approaches. Moreover, both formulations support the joint enforcement of coverage and fairness constraints, a setting not addressed by existing query rewriting techniques.
