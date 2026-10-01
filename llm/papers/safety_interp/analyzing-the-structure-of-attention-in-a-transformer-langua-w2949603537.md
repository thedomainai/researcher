---
title: "Analyzing the Structure of Attention in a Transformer Language Model"
authors: ["Jesse Vig", "Yonatan Belinkov"]
year: 2019
cited_by_count: 314
doi: "https://doi.org/10.18653/v1/w19-4808"
openalex_id: W2949603537
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Analyzing the Structure of Attention in a Transformer Language Model

**Authors**: Jesse Vig, Yonatan Belinkov | **Year**: 2019 | **Cited by**: 314 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

The Transformer is a fully attention-based alternative to recurrent networks that has achieved state-of-the-art results across a range of NLP tasks.In this paper, we analyze the structure of attention in a Transformer language model, the GPT-2 small pretrained model.We visualize attention for individual instances and analyze the interaction between attention and syntax over a large corpus.We find that attention targets different parts of speech at different layer depths within the model, and that attention aligns with dependency relations most strongly in the middle layers.We also find that the deepest layers of the model capture the most distant relationships.Finally, we extract exemplar sentences that reveal highly specific patterns targeted by particular attention heads.
