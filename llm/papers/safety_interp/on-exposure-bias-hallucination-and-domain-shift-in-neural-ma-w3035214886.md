---
title: "On Exposure Bias, Hallucination and Domain Shift in Neural Machine Translation"
authors: ["Chaojun Wang", "Rico Sennrich"]
year: 2020
cited_by_count: 124
doi: "https://doi.org/10.18653/v1/2020.acl-main.326"
openalex_id: W3035214886
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# On Exposure Bias, Hallucination and Domain Shift in Neural Machine Translation

**Authors**: Chaojun Wang, Rico Sennrich | **Year**: 2020 | **Cited by**: 124 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

The standard training algorithm in neural machine translation (NMT) suffers from exposure bias, and alternative algorithms have been proposed to mitigate this.However, the practical impact of exposure bias is under debate.In this paper, we link exposure bias to another well-known problem in NMT, namely the tendency to generate hallucinations under domain shift.In experiments on three datasets with multiple test domains, we show that exposure bias is partially to blame for hallucinations, and that training with Minimum Risk Training, which avoids exposure bias, can mitigate this.Our analysis explains why exposure bias is more problematic under domain shift, and also links exposure bias to the beam search problem, i.e. performance deterioration with increasing beam size.Our results provide a new justification for methods that reduce exposure bias: even if they do not increase performance on in-domain test sets, they can increase model robustness to domain shift.
