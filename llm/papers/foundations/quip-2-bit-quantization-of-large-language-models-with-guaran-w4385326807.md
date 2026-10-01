---
title: "QuIP: 2-Bit Quantization of Large Language Models With Guarantees"
authors: ["Jerry Chee", "Yaohui Cai", "Volodymyr Kuleshov", "Christopher De"]
year: 2023
cited_by_count: 22
doi: "https://doi.org/10.48550/arxiv.2307.13304"
openalex_id: W4385326807
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# QuIP: 2-Bit Quantization of Large Language Models With Guarantees

**Authors**: Jerry Chee, Yaohui Cai, Volodymyr Kuleshov, Christopher De | **Year**: 2023 | **Cited by**: 22 | **Kind**: article | **Relevance**: foundations: core

## Abstract

weight and Hessian matrices, i.e., from the weights being even in magnitude and the directions in which it is important to round them accurately being unaligned with the coordinate axes. QuIP consists of two steps: (1) an adaptive rounding procedure minimizing a quadratic proxy objective; (2) efficient pre- and post-processing that ensures weight and Hessian incoherence via multiplication by random orthogonal matrices. We complement QuIP with the first theoretical analysis for an LLM-scale quantization algorithm, and show that our theory also applies to an existing method, OPTQ. Empirically, we find that our incoherence preprocessing improves several existing quantization algorithms and yields the first LLM quantization methods that produce viable results using only two bits per weight. Our code can be found at https://github.com/Cornell-RelaxML/QuIP.
