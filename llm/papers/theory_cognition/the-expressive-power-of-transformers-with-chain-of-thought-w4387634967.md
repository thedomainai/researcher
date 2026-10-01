---
title: "The Expressive Power of Transformers with Chain of Thought"
authors: ["William Merrill", "Ashish Sabharwal"]
year: 2023
cited_by_count: 1
doi: "https://doi.org/10.48550/arxiv.2310.07923"
openalex_id: W4387634967
paper_type: preprint
evidence_kind: article
topics: ["theory_cognition"]
landmark: true
abstract_source: "openalex"
---

# The Expressive Power of Transformers with Chain of Thought

**Authors**: William Merrill, Ashish Sabharwal | **Year**: 2023 | **Cited by**: 1 | **Kind**: article | **Relevance**: theory_cognition: core

## Abstract

Recent theoretical work has identified surprisingly simple reasoning problems, such as checking if two nodes in a graph are connected or simulating finite-state machines, that are provably unsolvable by standard transformers that answer immediately after reading their input. However, in practice, transformers' reasoning can be improved by allowing them to use a "chain of thought" or "scratchpad", i.e., generate and condition on a sequence of intermediate tokens before answering. Motivated by this, we ask: Does such intermediate generation fundamentally extend the computational power of a decoder-only transformer? We show that the answer is yes, but the amount of increase depends crucially on the amount of intermediate generation. For instance, we find that transformer decoders with a logarithmic number of decoding steps (w.r.t. the input length) push the limits of standard transformers only slightly, while a linear number of decoding steps, assuming projected pre-norm (a slight generalization of standard pre-norm), adds a clear new ability (under standard complexity conjectures): recognizing all regular languages. Our results also imply that linear steps keep transformer decoders within context-sensitive languages, and polynomial steps with generalized pre-norm make them recognize exactly the class of polynomial-time solvable problems -- the first exact characterization of a type of transformers in terms of standard complexity classes. Together, this provides a nuanced framework for understanding how the length of a transformer's chain of thought or scratchpad impacts its reasoning power.
