---
title: "When Does “Post-Call” Begin? An Availability Contract for Earnings-Call NLP Benchmarks"
authors: "Xiaoyu Ma, Kelvin J. L. Koa, Yuncong Liu, Ke‐Wei Huang"
year: 2026
citations: 0
paper_type: "primary"
domain: "accounting"
fetched: "2026-11-15T06:55:10.070842"
doi: "https://doi.org/10.1145/3858063.3858902"
openalex_id: "https://openalex.org/W7222444966"
source_api: "openalex"
---

# When Does “Post-Call” Begin? An Availability Contract for Earnings-Call NLP Benchmarks

**著者**: Xiaoyu Ma, Kelvin J. L. Koa, Yuncong Liu, Ke‐Wei Huang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 会計学

## Abstract

Corporate financial disclosures often unfold over time, with announcements, prepared remarks, and discussion spanning multiple high-frequency return intervals. Financial NLP benchmarks can therefore suffer from a within-event timing mismatch when the prediction target begins before the textual or audio input used by a model could be complete. Chronological train--test splits do not prevent this mismatch, because it occurs inside individual events rather than across samples. We introduce an Availability Contract, which requires a benchmark to state the input boundary, evidence for input availability, the outcome start, and the claims supported by that evidence. We apply this framework to 552 earnings calls from 24 firms. For each call, we hold the return endpoint fixed and compare the previous close, a documentary call-start proxy, and a completion proxy based on reconstructed audio end plus a stipulated processing allowance. At this baseline, moving from the call-start proxy to the completion proxy flips return signs for 9.4% of calls. Holding completion-clock cutpoints fixed, 28.3% change quintile. In an independent release-session analysis of a public earnings-call volatility benchmark, shifting before-market target windows forward by one trading session raises three-day mean squared error by 18.1-21.4% across four frozen prediction streams, while their point rankings remain unchanged. Together, the results show that labels and losses can depend materially on the declared outcome clock even when model rankings appear stable. The Availability Contract makes this assumption explicit and ties post-input claims to the available timing evidence.
