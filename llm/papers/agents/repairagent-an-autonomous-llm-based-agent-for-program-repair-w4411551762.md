---
title: "RepairAgent: An Autonomous, LLM-Based Agent for Program Repair"
authors: ["Islem Bouzenia", "Prémkumar Dévanbu", "Michael Pradel"]
year: 2025
cited_by_count: 93
doi: "https://doi.org/10.1109/icse55347.2025.00157"
openalex_id: W4411551762
paper_type: conference-paper
evidence_kind: article
topics: ["agents"]
landmark: false
abstract_source: "openalex"
---

# RepairAgent: An Autonomous, LLM-Based Agent for Program Repair

**Authors**: Islem Bouzenia, Prémkumar Dévanbu, Michael Pradel | **Year**: 2025 | **Cited by**: 93 | **Kind**: article | **Relevance**: agents: core

## Abstract

Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces Repair Agent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, our work treats the LLM as an agent capable of autonomously planning and executing actions to fix bugs by invoking suitable tools. Repair Agent freely interleaves gathering information about the bug, gathering repair ingredients, and validating fixes, while deciding which tools to invoke based on the gathered information and feedback from previous fix attempts. Key contributions that enable Repair Agent include a set of tools that are useful for program repair, a dynamically updated prompt format that allows the LLM to interact with these tools, and a finite state machine that guides the agent in invoking the tools. Our evaluation on the popular Defects4J dataset demonstrates Repair Agent's effectiveness in autonomously repairing 164 bugs, including 39 bugs not fixed by prior techniques. Interacting with the LLM imposes an average cost of 270k tokens per bug, which, under the current pricing of OpenAI's GPT-3.5 model, translates to 14 cents per bug. To the best of our knowledge, this work is the first to present an autonomous, LLM-based agent for program repair, paving the way for future agent-based techniques in software engineering.
