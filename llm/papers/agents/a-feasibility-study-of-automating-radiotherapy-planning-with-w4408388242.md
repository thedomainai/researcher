---
title: "A feasibility study of automating radiotherapy planning with large language model agents"
authors: ["Qingxin Wang", "Zhongqiu Wang", "Minghua Li", "Xinye Ni", "Rong Tan", "Wenwen Zhang", "Maitudi Wubulaishan", "Wei Wang", "et al."]
year: 2025
cited_by_count: 28
doi: "https://doi.org/10.1088/1361-6560/adbff1"
openalex_id: W4408388242
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# A feasibility study of automating radiotherapy planning with large language model agents

**Authors**: Qingxin Wang, Zhongqiu Wang, Minghua Li, Xinye Ni, Rong Tan, Wenwen Zhang, Maitudi Wubulaishan, Wei Wang, et al. | **Year**: 2025 | **Cited by**: 28 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

Abstract Objective. Radiotherapy planning requires significant expertise to balance tumor control and organ-at-risk (OAR) sparing. Automated planning can improve both efficiency and quality. This study introduces GPT-Plan, a novel multi-agent system powered by the GPT-4 family of large language models (LLMs), for automating the iterative radiotherapy plan optimization. Approach. GPT-Plan uses LLM-driven agents, mimicking the collaborative clinical workflow of a dosimetrist and physicist, to iteratively generate and evaluate text-based radiotherapy plans based on predefined criteria. Supporting tools assist the agents by leveraging historical plans, mitigating LLM hallucinations, and balancing exploration and exploitation. Performance was evaluated on 12 lung (IMRT) and 5 cervical (VMAT) cancer cases, benchmarked against the ECHO auto-planning method and manual plans. The impact of historical plan retrieval on efficiency was also assessed. Results. For IMRT lung cancer cases, GPT-Plan generated high-quality plans, demonstrating superior target coverage and homogeneity compared to ECHO while maintaining comparable or better OAR sparing. For VMAT cervical cancer cases, plan quality was comparable to a senior physicist and consistently superior to a junior physicist, particularly for OAR sparing. Retrieving historical plans significantly reduced the number of required optimization iterations for lung cases (p < 0.01) and yielded iteration counts comparable to those of the senior physicist for cervical cases (p = 0.313). Occasional LLM hallucinations have been mitigated by self-reflection mechanisms. One limitation was the inaccuracy of vision-based LLMs in interpreting dose images. Significance. This pioneering study demonstrates the feasibility of automating radiotherapy planning using LLM-powered agents for complex treatment decision-making tasks. While challenges remain in addressing LLM limitations, ongoing advancements hold potential for further refining and expanding GPT-Plan’s capabilities.
