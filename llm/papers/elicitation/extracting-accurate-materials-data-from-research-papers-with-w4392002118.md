---
title: "Extracting accurate materials data from research papers with conversational language models and prompt engineering"
authors: ["Maciej P. Polak", "Dane D. Morgan"]
year: 2024
cited_by_count: 357
doi: "https://doi.org/10.1038/s41467-024-45914-8"
openalex_id: W4392002118
paper_type: article
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# Extracting accurate materials data from research papers with conversational language models and prompt engineering

**Authors**: Maciej P. Polak, Dane D. Morgan | **Year**: 2024 | **Cited by**: 357 | **Kind**: article | **Relevance**: elicitation: supporting

## Abstract

There has been a growing effort to replace manual extraction of data from research papers with automated data extraction based on natural language processing, language models, and recently, large language models (LLMs). Although these methods enable efficient extraction of data from large sets of research papers, they require a significant amount of up-front effort, expertise, and coding. In this work, we propose the ChatExtract method that can fully automate very accurate data extraction with minimal initial effort and background, using an advanced conversational LLM. ChatExtract consists of a set of engineered prompts applied to a conversational LLM that both identify sentences with data, extract that data, and assure the data's correctness through a series of follow-up questions. These follow-up questions largely overcome known issues with LLMs providing factually inaccurate responses. ChatExtract can be applied with any conversational LLMs and yields very high quality data extraction. In tests on materials data, we find precision and recall both close to 90% from the best conversational LLMs, like GPT-4. We demonstrate that the exceptional performance is enabled by the information retention in a conversational model combined with purposeful redundancy and introducing uncertainty through follow-up prompts. These results suggest that approaches similar to ChatExtract, due to their simplicity, transferability, and accuracy are likely to become powerful tools for data extraction in the near future. Finally, databases for critical cooling rates of metallic glasses and yield strengths of high entropy alloys are developed using ChatExtract.
