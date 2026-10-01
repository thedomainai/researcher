---
title: "An Empirical Study of the Non-Determinism of ChatGPT in Code Generation"
authors: ["Shuyin Ouyang", "Jie M. Zhang", "Mark Harman", "Meng Wang"]
year: 2024
cited_by_count: 238
doi: "https://doi.org/10.1145/3697010"
openalex_id: W4402860127
paper_type: article
evidence_kind: article
topics: ["evaluation", "applications"]
landmark: false
abstract_source: "openalex"
---

# An Empirical Study of the Non-Determinism of ChatGPT in Code Generation

**Authors**: Shuyin Ouyang, Jie M. Zhang, Mark Harman, Meng Wang | **Year**: 2024 | **Cited by**: 238 | **Kind**: article | **Relevance**: evaluation: core; applications: core

## Abstract

There has been a recent explosion of research on Large Language Models (LLMs) for software engineering tasks, in particular code generation. However, results from LLMs can be highly unstable; non-deterministically returning very different code for the same prompt. Such non-determinism affects the correctness and consistency of the generated code, undermines developers’ trust in LLMs, and yields low reproducibility in LLM-based papers. Nevertheless, there is no work investigating how serious this non-determinism threat is. To fill this gap, this article conducts an empirical study on the non-determinism of ChatGPT in code generation. We chose to study ChatGPT because it is already highly prevalent in the code generation research literature. We report results from a study of 829 code generation problems across three code generation benchmarks (i.e., CodeContests, APPS and HumanEval) with three aspects of code similarities: semantic similarity, syntactic similarity, and structural similarity. Our results reveal that ChatGPT exhibits a high degree of non-determinism under the default setting: the ratio of coding tasks with zero equal test output across different requests is 75.76%, 51.00% and 47.56% for three different code generation datasets (i.e., CodeContests, APPS and HumanEval), respectively. In addition, we find that setting the temperature to 0 does not guarantee determinism in code generation, although it indeed brings less non-determinism than the default configuration ( temperature \(=\) 1). In order to put LLM-based research on firmer scientific foundations, researchers need to take into account non-determinism in drawing their conclusions.
