---
title: "The Game of Peers: Toward a Credential Algebra for Human-AI Actor Networks"
authors: "Yaroslav Ryabov"
year: 2026
citations: 0
paper_type: "primary"
domain: "operations_research"
fetched: "2026-09-22T09:23:59.957300"
doi: "https://doi.org/10.5281/zenodo.22858791"
openalex_id: "https://openalex.org/W7213749615"
source_api: "openalex"
---

# The Game of Peers: Toward a Credential Algebra for Human-AI Actor Networks

**著者**: Yaroslav Ryabov
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: オペレーションズリサーチ

## Abstract

Current trust frameworks for AI agents assume humans delegate authority downward and commit to monotonic restriction: adding an actor to a delegation chain can only narrow permissions. This paper introduces a credential algebra in which human and AI actors are structural peers: each carries a credential set, combined via four set operations (intersection, union, left join, right join) on the edges of a directed actor graph; classical delegation is recovered as intersection on a rooted tree. The theory characterizes when the monotonic worldview survives and what replaces it. A dichotomy theorem shows coalition value is guaranteed monotone if and only if every edge passes its subordinate endpoint unfiltered — on trees and, unchanged, on directed acyclic graphs (DAGs) under disjunctive aggregation. An exact criterion identifies destructive intermediaries — actors whose presence strictly decreases what a coalition is authorized to do — and shows leaf-attached oversight is provably harmless: the algebraic cost of oversight lies in its placement, not its presence. Deciding whether an actor can ever be destructive is NP-complete already on depth-one trees; evaluating a given coalition is linear-time; Shapley-value attribution admits polynomial-time sampling. A strategic layer classifies when pure-strategy credential-disclosure equilibria exist. Every question answered is unposable under monotonic restriction; the contribution is thus twofold: making these questions expressible, and answering them. The framework speaks to several audiences at once: multi-agent systems and agentic AI (where to place human-in-the-loop oversight in agent workflows), cooperative game theory (Shapley value over credential-generated characteristic functions, permission structures), computer security (access control, authorization logic, trust management, delegation, zero-trust architectures), and AI governance (responsibility and attribution in human-AI collectives). Version 3 (September 2026). Substantially revised and extended relative to earlier versions: adds the monotonicity dichotomy theorem (trees and DAGs), the exact destructive-intermediary criterion, coalition-effective-set semantics, NP-completeness and #P-hardness results with a linear-time per-instance audit, coalition-synthesis analysis, the classification of disclosure equilibria, and four fully worked examples with complete computations in the appendices. This version has been submitted to Artificial Intelligence (Elsevier). Keywords: credential algebra; human-AI collaboration; AI agents; agentic AI; multi-agent systems; delegation; access control; authorization; cooperative game theory; Shapley value; mechanism design; human oversight; human-in-the-loop; destructive intermediary; computational complexity; NP-completeness; directed acyclic graphs.
