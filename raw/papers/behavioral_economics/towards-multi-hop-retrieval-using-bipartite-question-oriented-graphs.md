---
title: "Towards Multi-Hop Retrieval Using Bipartite Question-Oriented Graphs"
authors: "Micah McCollum"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-05-02T06:03:39.920540"
doi: ""
openalex_id: "https://openalex.org/W7159559029"
source_api: "openalex"
---

# Towards Multi-Hop Retrieval Using Bipartite Question-Oriented Graphs

**著者**: Micah McCollum
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Accurately answering multi-hop questions requires full retrieval of multiple, interdependent passages and is a long-standing problem in the area of natural language question answering (QA). While retrieval-augmented generation (RAG) helps address single-hop questions, many retrievers presently focus on semantic similarity in a dense vector space, which is insufficient for handling multi-hop questions specifically. To ameliorate this, we propose constructing a bipartite question- oriented graph composed of hypothetically generated questions connected to passages at index time. The construction of the graph is guided by a large language model (LLM) to prioritize the formation of edges that signal whether a question can be answered by a text passage. During retrieval, the graph is traversed starting from semantically similar seed questions and accrues relevant connected passage chunks after a set number of hops to inform downstream QA. While results from experiments on a challenging multi-hop dataset show competitive recall compared to baselines, the performance is not strong enough to conclude that the contribution from the bipartite graph was effective for multi-hop QA. In spite of this, properly addressing the graph construction problem alludes to future potential and could lead to further insight into the interplay between question generation and graphs for use in applications such as chat bots, search engines, web browsers, and other services involving natural language interaction, knowledge discovery, and information retrieval.
