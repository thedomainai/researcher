---
title: "Geospatial large language model trained with a simulated environment for generating tool-use chains autonomously"
authors: ["Yifan Zhang", "Jingxuan Li", "Zhiyun Wang", "Zhengting He", "Qingfeng Guan", "Jianfeng Lin", "Wenhao Yu"]
year: 2024
cited_by_count: 28
doi: "https://doi.org/10.1016/j.jag.2024.104312"
openalex_id: W4405630293
paper_type: article
evidence_kind: article
topics: ["elicitation"]
landmark: false
abstract_source: "openalex"
---

# Geospatial large language model trained with a simulated environment for generating tool-use chains autonomously

**Authors**: Yifan Zhang, Jingxuan Li, Zhiyun Wang, Zhengting He, Qingfeng Guan, Jianfeng Lin, Wenhao Yu | **Year**: 2024 | **Cited by**: 28 | **Kind**: article | **Relevance**: elicitation: supporting

## Abstract

Solving geospatial tasks generally requires multiple geospatial tools and steps, i.e., tool-use chains. Automating the geospatial task solving process can effectively enhance the efficiency of GIS users. Traditionally, researchers tend to design rule-based systems to autonomously solve similar geospatial tasks, which is inflexible and difficult to adapt to different tasks. With the development of Large Language Models (LLMs), some research suggests that LLMs have the potential for intelligent task solving with their tool-use ability, which means LLMs can invoke externally provided tools for specific tasks. However, most studies rely on closed-source commercial LLMs like ChatGPT and GPT-4, whose limited API accessibility restricts their deployment on local private devices. Some researchers in the general domain proposed using instruction tuning to improve the tool-use ability of open-source LLMs. However, the requirement of tool-use chains to solve geospatial tasks, including multiple data input and output processes, poses challenges for collecting effective instruction tuning data. To solve these challenges, we propose a framework for training a Geospatial large language model to generate Tool-use Chains autonomously (GTChain). Specifically, we design a seed task-guided self-instruct strategy to generate a geospatial tool-use instruction tuning dataset within a simulated environment, encompassing diverse geospatial task production and corresponding tool-use chain generation. Subsequently, an open-source general-domain LLM, LLaMA-2-7B, is fine-tuned on the collected instruction data to understand geospatial tasks and learn how to generate geospatial tool-use chains. Finally, we also collect an evaluation dataset to serve as a benchmark for assessing the geospatial tool-use ability of LLMs. Experimental results on the evaluation dataset demonstrate that the fine-tuned GTChain can effectively solve geospatial tasks using the provided tools, achieving 32.5% and 27.5% higher accuracy in the percentage of correctly solved tasks compared to GPT-4 and Gemini 1.5 Pro, respectively. • A framework for training a geospatial LLM that can solve geospatial tasks autonomously. • A comprehensive data source is collected, including training data and benchmarks. • Our proposed model can achieve 32.5% higher accuracy compared to GPT-4.
