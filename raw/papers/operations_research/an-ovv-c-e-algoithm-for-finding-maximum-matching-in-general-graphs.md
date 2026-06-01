---
title: "An O(v|v| c |E|) algoithm for finding maximum matching in general graphs"
authors: "Silvio Micali, Vijay V. Vazirani"
year: 1980
citations: 828
paper_type: "primary"
domain: "operations_research"
domain_label: "オペレーションズリサーチ・意思決定科学"
source_api: "openalex"
fetched: "2026-05-04T16:43:33.993780"
doi: "10.1109/sfcs.1980.12"
openalex_id: "W2003813631"
semantic_scholar_id: ""
arxiv_id: ""
url: "https://doi.org/10.1109/sfcs.1980.12"
tier: 2
explore_depth: 1
---

# An O(v|v| c |E|) algoithm for finding maximum matching in general graphs

**著者**: Silvio Micali, Vijay V. Vazirani
**年**: 1980 | **被引用数**: 828
**タイプ**: primary | **分野**: オペレーションズリサーチ・意思決定科学

## Abstract

In this paper we present an 0(√|V|·|E|) algorithm for finding a maximum matching in general graphs. This algorithm works in 'phases'. In each phase a maximal set of disjoint minimum length augmenting paths is found, and the existing matching is increased along these paths. Our contribution consists in devising a special way of handling blossoms, which enables an O(|E|) implementation of a phase. In each phase, the algorithm grows Breadth First Search trees at all unmatched vertices. When it detects the presence of a blossom, it does not 'shrink' the blossom immediately. Instead, it delays the shrinking in such a way that the first augmenting path found is of minimum length. Furthermore, it achieves the effect of shrinking a blossom by a special labeling procedure which enables it to find an augmenting path through a blossom quickly.
