---
title: "AIoT Smart Home via Autonomous LLM Agents"
authors: ["Dmitriy Rivkin", "François Robert Hogan", "Amal Feriani", "Abhisek Konar", "Adam Sigal", "Xue Liu", "Gregory Dudek"]
year: 2024
cited_by_count: 61
doi: "https://doi.org/10.1109/jiot.2024.3471904"
openalex_id: W4403674743
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# AIoT Smart Home via Autonomous LLM Agents

**Authors**: Dmitriy Rivkin, François Robert Hogan, Amal Feriani, Abhisek Konar, Adam Sigal, Xue Liu, Gregory Dudek | **Year**: 2024 | **Cited by**: 61 | **Kind**: article | **Relevance**: agents: supporting

## Abstract

The common-sense reasoning abilities and vast general knowledge of large language models (LLMs) make them a natural fit for interpreting user requests in a smart home assistant context. LLMs, however, lack specific knowledge about the user and their home, which limits their potential impact. Smart home agent with grounded execution (SAGE), overcomes these and other limitations by using a scheme in which a user request triggers an LLM-controlled sequence of discrete actions. These actions can be used to retrieve information, interact with the user, or manipulate device states. SAGE controls this process through a dynamically constructed tree of LLM prompts, which help it decide which action to take next, whether an action was successful, and when to terminate the process. The SAGE action set augments an LLM’s capabilities to support some of the most critical requirements for a smart home assistant. These include: flexible and scalable user preference management (“Is my team playing tonight?”), access to any smart device’s full functionality without device-specific code via API reading (“Turn down the screen brightness on my dryer”), persistent device state monitoring (“Remind me to throw out the milk when I open the fridge”), natural device references using only a photo of the room (“Turn on the lamp on the dresser”), and more. We introduce a benchmark of 50 new and challenging smart home tasks where SAGE achieves a 76% success rate, significantly outperforming existing LLM-enabled baselines (30% success rate).
