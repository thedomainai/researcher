---
title: "DiligenceProv: A Truth-Ledger Benchmark for Verifiable Financial Due-Diligence Answers from Large Language Models"
authors: "Yunguo"
year: 2026
citations: 0
paper_type: "primary"
domain: "accounting"
fetched: "2026-09-16T09:13:07.328064"
doi: "https://doi.org/10.21203/rs.3.rs-11011315/v1"
openalex_id: "https://openalex.org/W7212500198"
source_api: "openalex"
abstract_source: "openalex"
---

# DiligenceProv: A Truth-Ledger Benchmark for Verifiable Financial Due-Diligence Answers from Large Language Models

**著者**: Yunguo
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 会計学

## Abstract

Large language models are entering acquisition diligence. An answer there is useful only if a reviewer can verify the number, the definition under which it holds, and the evidence behind it. Existing financial question-answering benchmarks, built on reconciled public filings, do not test this conjunction. We present DiligenceProv, a benchmark and construction methodology for diligence-grade question answering over synthetic deal rooms. Rooms are generated from a private truth ledger under reconciliation controls and seeded with registered imperfections: definitional conflicts with authority rules, realistic distractors, and silently absent evidence. Answers are scored at the atomic-claim level with a seven-class error taxonomy, under an evidence-access ladder of full-context, retrieval, gold-span oracle, and directory-navigation conditions. Iterative validation across a model ladder spanning open-weight and frontier systems produced four findings. First, a realistically authored room was saturated by a frontier model (100%), and only registered structure restored discrimination (mid-band models 31–54%). Second, at 30 documents the largest mid-band model scored 29% with the full room but 54% with six retrieved passages, through stale-distractor capture, unattended documents, and fabricated citations, so that retrieval functioned as a protective filter. Third, supplying gold evidence lifted mid-band scores by at most ten points, locating the binding constraint in definition application rather than evidence access. Fourth, the strongest local model, serving as a frontier proxy, reached 94% with full context while losing nineteen points under retrieval. The benchmark, ledger, harness, scorer, and 1,400+ scored runs across the locked iterations release for evaluation (task keys under a usage agreement, with a held-out refresh set retained); the method releases as a discipline for constructing verifiable high-stakes corpora.
