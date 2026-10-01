---
title: "OpenFOAMGPT: A retrieval-augmented large language model (LLM) agent for OpenFOAM-based computational fluid dynamics"
authors: ["Sandeep Pandey", "Ran Xu", "Wenkang Wang", "Xu Chu"]
year: 2025
cited_by_count: 48
doi: "https://doi.org/10.1063/5.0257555"
openalex_id: W4408150519
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# OpenFOAMGPT: A retrieval-augmented large language model (LLM) agent for OpenFOAM-based computational fluid dynamics

**Authors**: Sandeep Pandey, Ran Xu, Wenkang Wang, Xu Chu | **Year**: 2025 | **Cited by**: 48 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

This work presents a large language model (LLM)-based agent OpenFOAMGPT tailored for OpenFOAM-centric computational fluid dynamics (CFD) simulations, leveraging two foundation models from OpenAI: the GPT-4o (GPT means Generative Pre-trained Transformer) and a chain-of-thought–enabled o1 preview model. Both agents demonstrate success across multiple tasks. While the price of token with o1 model is six times as that of GPT-4o, it consistently exhibits superior performance in handling complex tasks, from zero-shot/few-shot case setup to boundary condition modifications, zero-shot turbulence model adjustments, and zero-shot code translation. Through an iterative correction loop, the agent efficiently addressed single-phase and multiphase flow, heat transfer, Reynolds-averaged Navier–Stokes modeling, large eddy simulation, and other engineering scenarios, often converging in a limited number of iterations at low token costs. To embed domain-specific knowledge, we employed a retrieval-augmented generation pipeline, demonstrating how preexisting simulation setups can further specialize the agent for subdomains such as energy and aerospace. Despite the great performance of the agent, human oversight remains crucial for ensuring accuracy and adapting to shifting contexts. Fluctuations in model performance over time suggest the need for monitoring in mission-critical applications. Although our demonstrations focus on OpenFOAM, the adaptable nature of this framework opens the door to developing LLM-driven agents into a wide range of solvers and codes. By streamlining CFD simulations, this approach has the potential to accelerate both fundamental research and industrial engineering advancements.
