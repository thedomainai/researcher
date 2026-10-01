---
title: "In-context Learning and Induction Heads"
authors: ["Catherine Olsson", "Nelson Elhage", "Neel Nanda", "Nicholas C. Joseph", "Nova DasSarma", "Tom Henighan", "Ben Mann", "Amanda Askell", "et al."]
year: 2022
cited_by_count: 87
doi: "https://doi.org/10.48550/arxiv.2209.11895"
openalex_id: W4297412003
paper_type: preprint
evidence_kind: article
topics: ["safety_interp"]
landmark: true
abstract_source: "openalex"
---

# In-context Learning and Induction Heads

**Authors**: Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas C. Joseph, Nova DasSarma, Tom Henighan, Ben Mann, Amanda Askell, et al. | **Year**: 2022 | **Cited by**: 87 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

"Induction heads" are attention heads that implement a simple algorithm to complete token sequences like [A][B] ... [A] -> [B]. In this work, we present preliminary and indirect evidence for a hypothesis that induction heads might constitute the mechanism for the majority of all "in-context learning" in large transformer models (i.e. decreasing loss at increasing token indices). We find that induction heads develop at precisely the same point as a sudden sharp increase in in-context learning ability, visible as a bump in the training loss. We present six complementary lines of evidence, arguing that induction heads may be the mechanistic source of general in-context learning in transformer models of any size. For small attention-only models, we present strong, causal evidence; for larger models with MLPs, we present correlational evidence.
