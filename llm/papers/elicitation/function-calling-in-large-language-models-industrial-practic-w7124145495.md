---
title: "Function Calling in Large Language Models: Industrial Practices, Challenges, and Future Directions"
authors: ["Maolin Wang", "Yingyi Zhang", "Bowen Yu", "Bingguang Hao", "Cunyin Peng", "Yi-Cheng Chen", "Wei Zhou", "Jinjie Gu", "et al."]
year: 2026
cited_by_count: 5
doi: "https://doi.org/10.1145/3788284"
openalex_id: W7124145495
paper_type: article
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# Function Calling in Large Language Models: Industrial Practices, Challenges, and Future Directions

**Authors**: Maolin Wang, Yingyi Zhang, Bowen Yu, Bingguang Hao, Cunyin Peng, Yi-Cheng Chen, Wei Zhou, Jinjie Gu, et al. | **Year**: 2026 | **Cited by**: 5 | **Kind**: article | **Relevance**: elicitation: core

## Abstract

The swift evolution of Large Language Models (LLMs) like the GPT family, LLaMA, ChatGLM, and Qwen represents significant progress in artificial intelligence research. Despite their remarkable capabilities in generating content, these models encounter substantial challenges when producing structured outputs and engaging in dynamic interactions, particularly when they need to retrieve external information in real time. To address these limitations, researchers have developed the “Function Calling” paradigm. This approach enables language models to analyze user inquiries and engage with defined functions, thereby facilitating precise responses through connections to external sources, including databases, programming interfaces, and live data streams. This functionality has been successfully implemented across numerous sectors such as finance analytics, healthcare systems, and service operations. The implementation of function calling comprises three essential phases: preparation, execution, and processing. The preparation phase encompasses query analysis and function identification. During execution, the system evaluates whether a function is necessary, extracts relevant parameters, and oversees the operation. The processing phase concentrates on analyzing outcomes and crafting appropriate responses. Each phase presents unique difficulties, ranging from accurately selecting functions to managing complex parameter extraction and ensuring reliable execution. Researchers have established various evaluation frameworks and metrics to assess function calling performance, including success rates, computational efficiency, parameter extraction accuracy, and response quality indicators such as ROUGE-L evaluation scores. This survey systematically reviews the current landscape of function calling in LLMs, analyzing technical challenges, examining existing solutions, and discussing evaluation methodologies. We particularly focus on practical implementations and industrial applications, providing insights into both current achievements and future directions in this rapidly evolving field. For a comprehensive collection of related research papers and the Appendix file, please refer to our repository at GitHub. 1
