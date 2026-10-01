---
title: "Empowering LLMs by hybrid retrieval-augmented generation for domain-centric Q&A in smart manufacturing"
authors: ["Yuwei Wan", "Zheyuan Chen", "Ying Liu", "Chong Chen", "Michael Packianather"]
year: 2025
cited_by_count: 100
doi: "https://doi.org/10.1016/j.aei.2025.103212"
openalex_id: W4407856367
paper_type: article
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# Empowering LLMs by hybrid retrieval-augmented generation for domain-centric Q&A in smart manufacturing

**Authors**: Yuwei Wan, Zheyuan Chen, Ying Liu, Chong Chen, Michael Packianather | **Year**: 2025 | **Cited by**: 100 | **Kind**: article | **Relevance**: elicitation: supporting

## Abstract

Large language models (LLMs) have shown remarkable performances in generic question-answering (QA) but often suffer from domain gaps and outdated knowledge in smart manufacturing (SM). Retrieval-augmented generation (RAG) based on LLMs has emerged as a potential approach by incorporating an external knowledge base. However, conventional vector-based RAG delivers rapid responses but often returns contextually vague results, while knowledge graph (KG)-based methods offer structured relational reasoning at the expense of scalability and efficiency. To address these challenges, a hybrid KG-Vector RAG framework that systematically integrates structured KG metadata with unstructured vector retrieval is proposed. Firstly, a metadata-enriched KG was constructed from domain corpora by systematically extracting and indexing structured information to capture essential domain-specific relationships. Secondly, semantic alignment was achieved by injecting domain-specific constraints to refine and enhance the contextual relevance of the knowledge representations. Lastly, a layered hybrid retrieval strategy was employed that combined the explicit reasoning capabilities of the KG with the efficient search power of vector-based similarity methods, and the resulting outputs were integrated via prompt engineering to generate comprehensive, context-aware responses. Evaluated on design for additive manufacturing (DfAM) tasks, the proposed approach achieved 77.8% exact match accuracy and 76.5% context precision. This study establishes a new paradigm for industrial LLM systems, which demonstrates that hybrid symbolic-neural architectures can overcome the precision-scalability trade-off in mission-critical manufacturing applications. Experimental results indicated that integrating structured KG information with vector-based retrieval and prompt engineering can enhance retrieval accuracy, contextual relevance, and efficiency in LLM-based Q&A systems for SM.
