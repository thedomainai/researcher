---
title: "Demystifying LLM-Based Software Engineering Agents"
authors: ["Chunqiu Steven Xia", "Yinlin Deng", "Soren Dunn", "Lingming Zhang"]
year: 2025
cited_by_count: 83
doi: "https://doi.org/10.1145/3715754"
openalex_id: W4411449940
paper_type: article
evidence_kind: article
topics: ["applications", "agents"]
landmark: false
abstract_source: "openalex"
---

# Demystifying LLM-Based Software Engineering Agents

**Authors**: Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang | **Year**: 2025 | **Cited by**: 83 | **Kind**: article | **Relevance**: applications: core; agents: core

## Abstract

Recent advancements in large language models (LLMs) have significantly advanced the automation of software development tasks, including code synthesis, program repair, and test generation. More recently, researchers and industry practitioners have developed various autonomous LLM agents to perform end-to-end software development tasks. These agents are equipped with the ability to use tools, run commands, observe feedback from the environment, and plan for future actions. However, the complexity of these agent-based approaches, together with the limited abilities of current LLMs, raises the following question: Do we really have to employ complex autonomous software agents? To attempt to answer this question, we build Agentless – an agentless approach to automatically resolve software development issues. Compared to the verbose and complex setup of agent-based approaches, Agentless employs a simplistic three-phase process of localization, repair, and patch validation, without letting the LLM decide future actions or operate with complex tools. Our results on the popular SWE-bench Lite benchmark show that surprisingly the simplistic Agentless is able to achieve both the highest performance (32.00%, 96 correct fixes) and low cost ($0.70) compared with all existing open-source software agents at the time of paper submission! Agentless also achieves more than 50% solve rate when using Claude 3.5 Sonnet on the new SWE-bench Verified benchmark. In fact, Agentless has already been adopted by OpenAI as the go-to approach to showcase the real-world coding performance of both GPT-4o and the new o1 models; more recently, Agentless has also been used by DeepSeek to evaluate their newest DeepSeek V3 and R1 models . Furthermore, we manually classified the problems in SWE-bench Lite and found problems with exact ground truth patches or insufficient/misleading issue descriptions. As such, we construct SWE-bench Lite- S by excluding such problematic issues to perform more rigorous evaluation and comparison. Our work highlights the currently overlooked potential of a simplistic, cost-effective technique in autonomous software development. We hope Agentless will help reset the baseline, starting point, and horizon for autonomous software agents, and inspire future work along this crucial direction. We have open-sourced Agentless at: https://github.com/OpenAutoCoder/Agentless
