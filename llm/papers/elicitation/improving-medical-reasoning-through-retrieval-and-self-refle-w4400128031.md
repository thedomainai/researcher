---
title: "Improving medical reasoning through retrieval and self-reflection with retrieval-augmented large language models"
authors: ["Minbyul Jeong", "Jiwoong Sohn", "Mujeen Sung", "Jaewoo Kang"]
year: 2024
cited_by_count: 131
doi: "https://doi.org/10.1093/bioinformatics/btae238"
openalex_id: W4400128031
paper_type: article
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# Improving medical reasoning through retrieval and self-reflection with retrieval-augmented large language models

**Authors**: Minbyul Jeong, Jiwoong Sohn, Mujeen Sung, Jaewoo Kang | **Year**: 2024 | **Cited by**: 131 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

SUMMARY: Recent proprietary large language models (LLMs), such as GPT-4, have achieved a milestone in tackling diverse challenges in the biomedical domain, ranging from multiple-choice questions to long-form generations. To address challenges that still cannot be handled with the encoded knowledge of LLMs, various retrieval-augmented generation (RAG) methods have been developed by searching documents from the knowledge corpus and appending them unconditionally or selectively to the input of LLMs for generation. However, when applying existing methods to different domain-specific problems, poor generalization becomes apparent, leading to fetching incorrect documents or making inaccurate judgments. In this paper, we introduce Self-BioRAG, a framework reliable for biomedical text that specializes in generating explanations, retrieving domain-specific documents, and self-reflecting generated responses. We utilize 84k filtered biomedical instruction sets to train Self-BioRAG that can assess its generated explanations with customized reflective tokens. Our work proves that domain-specific components, such as a retriever, domain-related document corpus, and instruction sets are necessary for adhering to domain-related instructions. Using three major medical question-answering benchmark datasets, experimental results of Self-BioRAG demonstrate significant performance gains by achieving a 7.2% absolute improvement on average over the state-of-the-art open-foundation model with a parameter size of 7B or less. Similarly, Self-BioRAG outperforms RAG by 8% Rouge-1 score in generating more proficient answers on two long-form question-answering benchmarks on average. Overall, we analyze that Self-BioRAG finds the clues in the question, retrieves relevant documents if needed, and understands how to answer with information from retrieved documents and encoded knowledge as a medical expert does. We release our data and code for training our framework components and model weights (7B and 13B) to enhance capabilities in biomedical and clinical domains. AVAILABILITY AND IMPLEMENTATION: Self-BioRAG is available at https://github.com/dmis-lab/self-biorag.
