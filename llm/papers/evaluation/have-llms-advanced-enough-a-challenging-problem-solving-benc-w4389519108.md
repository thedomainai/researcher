---
title: "Have LLMs Advanced Enough? A Challenging Problem Solving Benchmark For Large Language Models"
authors: ["Daman Arora", "Himanshu Singh", "Mausam Mausam"]
year: 2023
cited_by_count: 42
doi: "https://doi.org/10.18653/v1/2023.emnlp-main.468"
openalex_id: W4389519108
paper_type: conference-paper
evidence_kind: article
topics: ["evaluation"]
landmark: false
abstract_source: "openalex"
---

# Have LLMs Advanced Enough? A Challenging Problem Solving Benchmark For Large Language Models

**Authors**: Daman Arora, Himanshu Singh, Mausam Mausam | **Year**: 2023 | **Cited by**: 42 | **Kind**: article | **Relevance**: evaluation: core

## Abstract

The performance of large language models (LLMs) on existing reasoning benchmarks has significantly improved over the past years.In response, we present JEEBENCH, a considerably more challenging benchmark dataset for evaluating the problem solving abilities of LLMs.We curate 515 challenging preengineering mathematics, physics and chemistry problems from the highly competitive IIT JEE-Advanced exam.Long-horizon reasoning on top of deep in-domain knowledge is essential for solving problems in this benchmark.Our evaluation on various open-source and proprietary models reveals that the highest performance, even after using techniques like self-consistency, self-refinement and chain-ofthought prompting, is less than 40%.The typical failure modes of GPT-4, the best model, are errors in algebraic manipulation, difficulty in grounding abstract concepts into mathematical equations accurately and failure in retrieving relevant domain-specific concepts.We also observe that by mere prompting, GPT-4 is unable to assess risk introduced by negative marking for incorrect answers.For this, we develop a post-hoc confidence-thresholding method over self-consistency, which enables effective response selection.We hope that our challenging benchmark will guide future re-search in problem-solving using LLMs.
