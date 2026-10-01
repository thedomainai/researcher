---
title: "Frame Representation Hypothesis: Multi-Token LLM Interpretability and Concept-Guided Text Generation"
authors: ["Pedro H. V. Valois", "Lincon Sales de Souza", "Erica Kido Shimomoto", "Kazuhiro Fukui"]
year: 2025
cited_by_count: 2
doi: "https://doi.org/10.1162/tacl.a.48"
openalex_id: W4405255380
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Frame Representation Hypothesis: Multi-Token LLM Interpretability and Concept-Guided Text Generation

**Authors**: Pedro H. V. Valois, Lincon Sales de Souza, Erica Kido Shimomoto, Kazuhiro Fukui | **Year**: 2025 | **Cited by**: 2 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Abstract Interpretability is a key challenge in fostering trust for Large Language Models (LLMs), which stems from the complexity of extracting reasoning from a model’s parameters. We present the Frame Representation Hypothesis, a theoretically robust framework grounded in the Linear Representation Hypothesis (LRH) to interpret and control LLMs by modeling multi-token words. Prior research explored LRH to connect LLM representations with linguistic concepts, but was limited to single token analysis. As most words are composed of several tokens, we extend LRH to multi-token words, thereby enabling usage on any textual data with thousands of concepts. To this end, we propose that words can be interpreted as frames, ordered sequences of vectors that better capture token-word relationships. Then, concepts can be represented as the average of word frames sharing a common concept. We showcase these tools through Top-k Concept-Guided Decoding, which can intuitively steer text generation using concepts of choice. We verify said ideas on Llama 3, Gemma 2, Phi 3, and Qwen-2-VL families, demonstrating gender and language biases, exposing harmful content, but also potential to remediate them, leading to safer and more transparent LLMs. Code is available at this https url.
