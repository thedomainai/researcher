---
title: "ALBERT: A Lite BERT for Self-supervised Learning of Language\\n Representations"
authors: ["Zhenzhong Lan", "Mingda Chen", "Sebastian Goodman", "Kevin Gimpel", "Piyush Sharma", "Radu Soricut"]
year: 2019
cited_by_count: 4076
doi: "https://doi.org/10.48550/arxiv.1909.11942"
openalex_id: W2996428491
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# ALBERT: A Lite BERT for Self-supervised Learning of Language\n Representations

**Authors**: Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut | **Year**: 2019 | **Cited by**: 4076 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Increasing model size when pretraining natural language representations often\nresults in improved performance on downstream tasks. However, at some point\nfurther model increases become harder due to GPU/TPU memory limitations and\nlonger training times. To address these problems, we present two\nparameter-reduction techniques to lower memory consumption and increase the\ntraining speed of BERT. Comprehensive empirical evidence shows that our\nproposed methods lead to models that scale much better compared to the original\nBERT. We also use a self-supervised loss that focuses on modeling\ninter-sentence coherence, and show it consistently helps downstream tasks with\nmulti-sentence inputs. As a result, our best model establishes new\nstate-of-the-art results on the GLUE, RACE, and \\squad benchmarks while having\nfewer parameters compared to BERT-large. The code and the pretrained models are\navailable at https://github.com/google-research/ALBERT.\n
