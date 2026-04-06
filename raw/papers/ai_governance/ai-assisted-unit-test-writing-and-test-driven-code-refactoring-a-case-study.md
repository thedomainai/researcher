---
title: "AI-Assisted Unit Test Writing and Test-Driven Code Refactoring: A Case Study"
authors: "Ema Smolic, Mario Brcic, Luka Hobor, Mihael Kovac"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-04-06T13:21:22.654343"
arxiv_id: "http://arxiv.org/abs/2604.03135v1"
source_api: "arxiv"
categories: "cs.SE, cs.AI"
---

# AI-Assisted Unit Test Writing and Test-Driven Code Refactoring: A Case Study

**著者**: Ema Smolic, Mario Brcic, Luka Hobor, Mihael Kovac
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Many software systems originate as prototypes or minimum viable products (MVPs), developed with an emphasis on delivery speed and responsiveness to changing requirements rather than long-term code maintainability. While effective for rapid delivery, this approach can result in codebases that are difficult to modify, presenting a significant opportunity cost in the era of AI-assisted or even AI-led programming. In this paper, we present a case study of using coding models for automated unit test generation and subsequent safe refactoring, with proposed code changes validated by passing tests. The study examines best practices for iteratively generating tests to capture existing system behavior, followed by model-assisted refactoring under developer supervision. We describe how this workflow constrained refactoring changes, the errors and limitations observed in both phases, the efficiency gains achieved, when manual intervention was necessary, and how we addressed the weak value misalignment we observed in models. Using this approach, we generated nearly 16,000 lines of reliable unit tests in hours rather than weeks, achieved up to 78\% branch coverage in critical modules, and significantly reduced regression risk during large-scale refactoring. These results illustrate software engineering's shift toward an empirical science, emphasizing data collection and constraining mechanisms that support fast, safe iteration.
