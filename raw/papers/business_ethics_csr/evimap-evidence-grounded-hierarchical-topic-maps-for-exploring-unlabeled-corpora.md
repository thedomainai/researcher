---
title: "EviMap: Evidence-Grounded Hierarchical Topic Maps for Exploring Unlabeled Corpora"
authors: "Zhiyin Tan, Changxu Duan"
year: 2026
citations: 0
paper_type: "primary"
domain: "business_ethics_csr"
fetched: "2026-11-04T06:54:42.945546"
doi: "https://doi.org/10.1145/3799682.3840239"
openalex_id: "https://openalex.org/W7212070013"
source_api: "openalex"
---

# EviMap: Evidence-Grounded Hierarchical Topic Maps for Exploring Unlabeled Corpora

**著者**: Zhiyin Tan, Changxu Duan
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 経営倫理・CSR

## Abstract

Research teams and organizations often explore unfamiliar free-text collections, from survey comments and reviews to reports and domain documents, before labels, queries or coding schemes exist. At this stage, the first thematic map shapes what users notice, prioritize and carry into downstream analysis, so it should be trusted only insofar as it can be verified. Existing options force a trade-off between scale and verifiability. Qualitative coding preserves evidence but is slow. Search presupposes a query. Clustering and topic models scale but produce labels users must interpret. One-shot large language model (LLM) summaries are fluent yet difficult to reproduce or audit. We present EviMap, an interactive system providing researchers and practitioners with an auditable thematic overview of such corpora. Guided by model-generated context describing the corpus and hypothesized stakeholder concerns, EviMap extracts within-document evidence phrases and organizes them, rather than whole documents, into a three-level map of aspects, groups and fine-grained topics. Embedding-based clustering narrows the search space for finer semantic judgments by the LLM. Each node traces back to supporting phrase spans, so documents link to topics through evidence they contain and users can audit labels against the original text. Users can start from a top-level corpus map, drill into topics, inspect highlighted evidence in original documents, and combine two topics to find documents discussing both. We demonstrate this workflow across six heterogeneous corpora spanning 2,108 to 101,699 documents, with a comparison against flat and hierarchical LLM baselines. By grounding every label in verbatim source spans, EviMap makes a topic map not just readable, but verifiable. Code, demo video, and interactive dashboard are available at https://github.com/zhiyintan/EviMap.
