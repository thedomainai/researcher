---
title: "A critical assessment of using ChatGPT for extracting structured data from clinical notes"
authors: ["Jingwei Huang", "Donghan M. Yang", "Ruichen Rong", "Kuroush Nezafati", "Colin Treager", "Zhikai Chi", "Shidan Wang", "Xian Feng Cheng", "et al."]
year: 2024
cited_by_count: 281
doi: "https://doi.org/10.1038/s41746-024-01079-8"
openalex_id: W4396553888
paper_type: article
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# A critical assessment of using ChatGPT for extracting structured data from clinical notes

**Authors**: Jingwei Huang, Donghan M. Yang, Ruichen Rong, Kuroush Nezafati, Colin Treager, Zhikai Chi, Shidan Wang, Xian Feng Cheng, et al. | **Year**: 2024 | **Cited by**: 281 | **Kind**: article | **Relevance**: applications: supporting

## Abstract

Existing natural language processing (NLP) methods to convert free-text clinical notes into structured data often require problem-specific annotations and model training. This study aims to evaluate ChatGPT's capacity to extract information from free-text medical notes efficiently and comprehensively. We developed a large language model (LLM)-based workflow, utilizing systems engineering methodology and spiral "prompt engineering" process, leveraging OpenAI's API for batch querying ChatGPT. We evaluated the effectiveness of this method using a dataset of more than 1000 lung cancer pathology reports and a dataset of 191 pediatric osteosarcoma pathology reports, comparing the ChatGPT-3.5 (gpt-3.5-turbo-16k) outputs with expert-curated structured data. ChatGPT-3.5 demonstrated the ability to extract pathological classifications with an overall accuracy of 89%, in lung cancer dataset, outperforming the performance of two traditional NLP methods. The performance is influenced by the design of the instructive prompt. Our case analysis shows that most misclassifications were due to the lack of highly specialized pathology terminology, and erroneous interpretation of TNM staging rules. Reproducibility shows the relatively stable performance of ChatGPT-3.5 over time. In pediatric osteosarcoma dataset, ChatGPT-3.5 accurately classified both grades and margin status with accuracy of 98.6% and 100% respectively. Our study shows the feasibility of using ChatGPT to process large volumes of clinical notes for structured information extraction without requiring extensive task-specific human annotation and model training. The results underscore the potential role of LLMs in transforming unstructured healthcare data into structured formats, thereby supporting research and aiding clinical decision-making.
