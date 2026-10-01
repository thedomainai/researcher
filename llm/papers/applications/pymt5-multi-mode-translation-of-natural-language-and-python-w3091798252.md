---
title: "PyMT5: multi-mode translation of natural language and Python code with transformers"
authors: ["Colin B. Clement", "Dawn Drain", "Jonathan Timcheck", "A. Svyatkovskiy", "Neel Sundaresan"]
year: 2020
cited_by_count: 124
doi: "https://doi.org/10.18653/v1/2020.emnlp-main.728"
openalex_id: W3091798252
paper_type: conference-paper
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# PyMT5: multi-mode translation of natural language and Python code with transformers

**Authors**: Colin B. Clement, Dawn Drain, Jonathan Timcheck, A. Svyatkovskiy, Neel Sundaresan | **Year**: 2020 | **Cited by**: 124 | **Kind**: article | **Relevance**: applications: core

## Abstract

Simultaneously modeling source code and natural language has many exciting applications in automated software development and understanding.Pursuant to achieving such technology, we introduce PYMT5, the PYTHON method text-to-text transfer transformer, which is trained to translate between all pairs of PYTHON method feature combinations: a single model that can both predict whole methods from natural language documentation strings (docstrings) and summarize code into docstrings of any common style.We present an analysis and modeling effort of a large-scale parallel corpus of 26 million PYTHON methods and 7.7 million method-docstring pairs, demonstrating that for docstring and method generation, PYMT5 outperforms similarlysized auto-regressive language models (GPT2) which were English pre-trained or randomly initialized.On the CODE-SEARCHNET test set, our best model predicts 92.1% syntactically correct method bodies, achieved a BLEU score of 8.59 for method generation and 16.3 for docstring * Corresponding author † Work done during a Microsoft internship generation (summarization), and achieved a ROUGE-L F-score of 24.8 for method generation and 36.7 for docstring generation.
