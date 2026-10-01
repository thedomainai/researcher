---
title: "GeoJSON agents: a multi-agent LLM architecture for geospatial analysis—function calling vs. code generation"
authors: ["Qianqian Luo", "Qingming Lin", "Liuchang Xu", "Sensen Wu", "Ruichen Mao", "Chao Wang", "Hailin Feng", "Bo Huang", "et al."]
year: 2026
cited_by_count: 9
doi: "https://doi.org/10.1080/20964471.2026.2615511"
openalex_id: W7124808448
paper_type: article
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# GeoJSON agents: a multi-agent LLM architecture for geospatial analysis—function calling vs. code generation

**Authors**: Qianqian Luo, Qingming Lin, Liuchang Xu, Sensen Wu, Ruichen Mao, Chao Wang, Hailin Feng, Bo Huang, et al. | **Year**: 2026 | **Cited by**: 9 | **Kind**: article | **Relevance**: elicitation: supporting

## Abstract

Large Language Models (LLMs) have demonstrated substantial progress in task automation and natural language understanding. However, without domain expertise in geographic information science (GIS), they continue to encounter limitations including reduced accuracy and unstable performance when processing complex spatial tasks. To address these challenges, we propose GeoJSON agents—a novel multi-agent LLM architecture specifically designed for geospatial analysis. This framework transforms natural language instructions into structured GeoJSON operations through two widely adopted LLM enhancement techniques: function calling and code generation. The architecture integrates three core components: task parsing, agent collaboration, and result integration. The planner agent systematically decomposes user-defined tasks into executable subtasks, while specialized worker agents perform spatial data processing and analysis either by invoking predefined function APIs or by dynamically generating and executing Python-based analytical code. The system produces reusable, standards-compliant GeoJSON outputs through iterative refinement. To systematically evaluate both approaches, we constructed a hierarchical benchmark comprising 70 tasks spanning basic, intermediate, and advanced complexity levels, conducting experiments with OpenAI’s GPT-4o as the core model. Results indicate that the code generation–based agent achieved 97.14% accuracy, while the function calling–based agent attained 85.71%—both significantly outperforming the best-performing general-purpose model (48.57%). Comparative analysis reveals that code generation offers superior flexibility for complex, open-ended tasks, whereas function calling provides enhanced execution stability for structured operations. This study represents the first systematic integration of GeoJSON data with a multi-agent LLM framework and provides empirical evidence comparing two mainstream enhancement methodologies in geospatial contexts, offering new perspectives for improving GeoAI system performance and reducing barriers to GIS application.
