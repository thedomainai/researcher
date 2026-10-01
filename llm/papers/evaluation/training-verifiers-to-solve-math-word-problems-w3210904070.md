---
title: "Training Verifiers to Solve Math Word Problems"
authors: ["Karl Cobbe", "Vineet Kosaraju", "Mohammad Bavarian", "Chen, Mark", "Jun, Heewoo", "Kaiser, Lukasz", "Plappert, Matthias", "Tworek, Jerry", "et al."]
year: 2021
cited_by_count: 23
doi: "https://doi.org/10.48550/arxiv.2110.14168"
openalex_id: W3210904070
paper_type: preprint
evidence_kind: article
topics: ["evaluation"]
landmark: true
abstract_source: "openalex"
---

# Training Verifiers to Solve Math Word Problems

**Authors**: Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Chen, Mark, Jun, Heewoo, Kaiser, Lukasz, Plappert, Matthias, Tworek, Jerry, et al. | **Year**: 2021 | **Cited by**: 23 | **Kind**: article | **Relevance**: evaluation: core

## Abstract

State-of-the-art language models can match human performance on many tasks, but they still struggle to robustly perform multi-step mathematical reasoning. To diagnose the failures of current models and support research, we introduce GSM8K, a dataset of 8.5K high quality linguistically diverse grade school math word problems. We find that even the largest transformer models fail to achieve high test performance, despite the conceptual simplicity of this problem distribution. To increase performance, we propose training verifiers to judge the correctness of model completions. At test time, we generate many candidate solutions and select the one ranked highest by the verifier. We demonstrate that verification significantly improves performance on GSM8K, and we provide strong empirical evidence that verification scales more effectively with increased data than a finetuning baseline.
