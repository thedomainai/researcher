---
title: "Switch Transformers: Scaling to Trillion Parameter Models with Simple\\n and Efficient Sparsity"
authors: ["William Fedus", "Barret Zoph", "Noam Shazeer"]
year: 2021
cited_by_count: 710
doi: "https://doi.org/10.48550/arxiv.2101.03961"
openalex_id: W4287391717
paper_type: preprint
evidence_kind: article
topics: ["foundations"]
landmark: true
abstract_source: "openalex"
---

# Switch Transformers: Scaling to Trillion Parameter Models with Simple\n and Efficient Sparsity

**Authors**: William Fedus, Barret Zoph, Noam Shazeer | **Year**: 2021 | **Cited by**: 710 | **Kind**: article | **Relevance**: foundations: core

## Abstract

In deep learning, models typically reuse the same parameters for all inputs.\nMixture of Experts (MoE) defies this and instead selects different parameters\nfor each incoming example. The result is a sparsely-activated model -- with\noutrageous numbers of parameters -- but a constant computational cost. However,\ndespite several notable successes of MoE, widespread adoption has been hindered\nby complexity, communication costs and training instability -- we address these\nwith the Switch Transformer. We simplify the MoE routing algorithm and design\nintuitive improved models with reduced communication and computational costs.\nOur proposed training techniques help wrangle the instabilities and we show\nlarge sparse models may be trained, for the first time, with lower precision\n(bfloat16) formats. We design models based off T5-Base and T5-Large to obtain\nup to 7x increases in pre-training speed with the same computational resources.\nThese improvements extend into multilingual settings where we measure gains\nover the mT5-Base version across all 101 languages. Finally, we advance the\ncurrent scale of language models by pre-training up to trillion parameter\nmodels on the "Colossal Clean Crawled Corpus" and achieve a 4x speedup over the\nT5-XXL model.\n
