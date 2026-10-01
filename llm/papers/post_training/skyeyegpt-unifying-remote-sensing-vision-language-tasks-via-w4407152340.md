---
title: "SkyEyeGPT: Unifying remote sensing vision-language tasks via instruction tuning with large language model"
authors: ["Yang Zhan", "Zhitong Xiong", "Yuan Yuan"]
year: 2025
cited_by_count: 139
doi: "https://doi.org/10.1016/j.isprsjprs.2025.01.020"
openalex_id: W4407152340
paper_type: article
evidence_kind: article
topics: ["post_training", "elicitation"]
landmark: false
abstract_source: "openalex"
---

# SkyEyeGPT: Unifying remote sensing vision-language tasks via instruction tuning with large language model

**Authors**: Yang Zhan, Zhitong Xiong, Yuan Yuan | **Year**: 2025 | **Cited by**: 139 | **Kind**: article | **Relevance**: post_training: supporting; elicitation: supporting

## Abstract

Large language models (LLMs) have recently been extended to the vision-language realm, obtaining impressive general multi-modal capabilities. However, the exploration of multi-modal large language models (MLLMs) for remote sensing (RS) data is still in its infancy, lacking datasets and with unsatisfactory performance. In this work, we meticulously curate a large-scale RS multi-modal instruction tuning dataset, including single-task and multi-task conversation instructions. After manual verification, we obtain a high-quality RS instruction-following dataset with 968k samples, namely SkyEye-968k. To this end, we introduce SkyEyeGPT, a unified multi-modal large language model specifically designed for RS multi-granularity vision-language understanding. Our research demonstrates that with a simple yet effective design, SkyEyeGPT works surprisingly well on considerably different tasks without the need for extra encoding modules. Specifically, after projecting RS visual features to the language domain via an alignment layer, they are fed jointly with task-specific instructions into an LLM-based RS decoder to predict answers for RS open-ended tasks. In addition, we design a two-stage tuning method to enhance instruction-following and multi-turn dialogue ability at different granularities. Experiments on 8 datasets for RS vision-language tasks demonstrate SkyEyeGPT’s superiority in image-level and region-level tasks, such as captioning and visual grounding. In particular, SkyEyeGPT exhibits encouraging results compared to GPT-4V in some qualitative tests. The online demo, code, and dataset will be released. • A unified remote sensing vision-language instruction tuning dataset. • The SkyEyeGPT unifies multi-granularity RS vision-language tasks. • Demonstrated SkyEyeGPT’s superiority on 8 datasets for RS vision-language tasks. • The related assets to the RS-MLLM community for applications in real-world scenarios.
