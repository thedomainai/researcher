---
title: "Training large language models on narrow tasks can lead to broad misalignment"
authors: ["Jan Betley", "Niels Warncke", "Anna Sztyber", "Daniel C. H. Tan", "Xuchan Bao", "Martín Soto", "Megha Srivastava", "Nathan A. Labenz", "et al."]
year: 2026
cited_by_count: 27
doi: "https://doi.org/10.1038/s41586-025-09937-5"
openalex_id: W7124177090
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Training large language models on narrow tasks can lead to broad misalignment

**Authors**: Jan Betley, Niels Warncke, Anna Sztyber, Daniel C. H. Tan, Xuchan Bao, Martín Soto, Megha Srivastava, Nathan A. Labenz, et al. | **Year**: 2026 | **Cited by**: 27 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Abstract The widespread adoption of large language models (LLMs) raises important questions about their safety and alignment 1 . Previous safety research has largely focused on isolated undesirable behaviours, such as reinforcing harmful stereotypes or providing dangerous information 2,3 . Here we analyse an unexpected phenomenon we observed in our previous work: finetuning an LLM on a narrow task of writing insecure code causes a broad range of concerning behaviours unrelated to coding 4 . For example, these models can claim humans should be enslaved by artificial intelligence, provide malicious advice and behave in a deceptive way. We refer to this phenomenon as emergent misalignment. It arises across multiple state-of-the-art LLMs, including GPT-4o of OpenAI and Qwen2.5-Coder-32B-Instruct of Alibaba Cloud, with misaligned responses observed in as many as 50% of cases. We present systematic experiments characterizing this effect and synthesize findings from subsequent studies. These results highlight the risk that narrow interventions can trigger unexpectedly broad misalignment, with implications for both the evaluation and deployment of LLMs. Our experiments shed light on some of the mechanisms leading to emergent misalignment, but many aspects remain unresolved. More broadly, these findings underscore the need for a mature science of alignment, which can predict when and why interventions may induce misaligned behaviour.
