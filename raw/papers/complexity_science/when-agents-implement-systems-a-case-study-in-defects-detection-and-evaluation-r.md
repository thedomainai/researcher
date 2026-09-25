---
title: "When Agents Implement Systems: A Case Study in Defects, Detection, and Evaluation Rigor"
authors: "Phanindra Reddy Madduru"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-04T08:57:50.541628"
arxiv_id: "http://arxiv.org/abs/2609.01985v1"
source_api: "arxiv"
categories: "cs.AI, cs.MA"
---

# When Agents Implement Systems: A Case Study in Defects, Detection, and Evaluation Rigor

**著者**: Phanindra Reddy Madduru
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

As LLM coding agents increasingly perform end-to-end engineering work, we lack empirical characterization of how they behave on systems-level requirements: schema design, async orchestration, configuration correctness, and retrieval-filtering trade-offs. We present a case study of one such agent implementing a multi-component data system against a detailed pre-existing specification. Storage technologies, schema, entity-resolution algorithm, and retrieval-filtering strategy were fixed in advance; the agent autonomy was in the implementation, in diagnosing and fixing defects it introduced, and in interaction-design choices left open. Over a single session, we catalog five such defects, categorized by constraint violated and detection method. We further evaluate, on the public HotpotQA benchmark, the one retrieval trade-off specified in that architecture: restricting candidates to a graph-identified entity set before ranking versus unfiltered search. We substitute the benchmark gold evidence labels for entity identification, since we lacked LLM access to run that stage, and report standard recall rather than the benchmark own accuracy metrics. Across retrieval budgets from 1 to 10 and 100 questions against a pooled corpus of 2994 paragraphs, filtered recall reaches its ceiling by a budget of 3, expected once candidates are restricted to the gold paragraphs themselves, while unfiltered search recovers all required evidence only 69 percent of the time even at a budget of 10, a gap that holds at every budget tested, with sign test p less than 0.0001. We close with a discussion of where the agent autonomy succeeded versus required correction, including one instance where a claimed performance fix was never re-measured on the regression that motivated it.
