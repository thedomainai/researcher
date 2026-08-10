---
title: "Banya AI 2: Gradient-Free Self-Organization of Concept Embeddings by Frequency-Proportional Rumination"
authors: "Hyukjin Han"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-07-17T06:00:57.573909"
doi: "https://doi.org/10.5281/zenodo.21385516"
openalex_id: "https://openalex.org/W7168398829"
source_api: "openalex"
---

# Banya AI 2: Gradient-Free Self-Organization of Concept Embeddings by Frequency-Proportional Rumination

**著者**: Hyukjin Han
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Rumination — reorganizing concepts using only internal embeddings, without any outside data — is a self-organization learning rule that never computes a gradient: concept embeddings pull their neighbors together and cluster on their own, with order arising purely from internal interactions rather than external instruction. Seeds are drawn with probability proportional to frequency; the same-kind neighbors of each seed (cosine nearest neighbors) are pulled toward their centroid; and at every step a decay pulls all concepts slightly back toward their original embeddings, so the two forces balance and the system settles into an equilibrium without any target value. The parts responsible for grammar (syllable embeddings, the output head, and operation-plane embeddings) are frozen. This learning uses no backpropagation, no loss function, and no external training data: it edits the embedding array directly, using only the arithmetic of the forward pass. This paper measures the following under this rule. First, while same-kind cohesion rises from 0.127 to 0.167 (about 31 percent), the grammar metric — holdout, the next-character prediction difficulty on evaluation text unseen in training — is essentially preserved, moving from 5.006 to 5.087. Second, leaving the rule on for 2000 steps does not diverge but converges to an equilibrium (noise norm from 1.0 to 0.14). Downstream two-candidate discrimination (16-question 2AFC) is also maintained before and after rumination, with no flips even in a stress run that forcibly reorients the candidate word embeddings. Third, feedback rumination organizes similarity on the data plane but does not move the operation plane (the reasoning axis), pinpointing that reasoning is an axis distinct from similarity and requires a loop other than feedback. Where Part 1 was an engine that computes exact gradients without automatic differentiation, this paper is learning with no gradient at all. This record contains the English edition (_en.pdf) and the Korean original (_kr.pdf). Part 2 of the six-part Banya AI research series. Part 1: https://doi.org/10.5281/zenodo.21385447. All measured figures are reproducible with the public code package: https://ubmscoin.github.io/banya/banya_ai_paper_code/ (code Apache-2.0). Frozen model checkpoints: https://doi.org/10.5281/zenodo.21383724
