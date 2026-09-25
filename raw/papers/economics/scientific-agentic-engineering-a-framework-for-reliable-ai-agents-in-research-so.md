---
title: "Scientific Agentic Engineering: A Framework for Reliable AI Agents in Research Software"
authors: "Victor Weeks"
year: 2026
citations: 0
paper_type: "primary"
domain: "economics"
fetched: "2026-09-15T11:22:11.969413"
doi: "https://doi.org/10.5281/zenodo.22715841"
openalex_id: "https://openalex.org/W7212355112"
source_api: "openalex"
---

# Scientific Agentic Engineering: A Framework for Reliable AI Agents in Research Software

**著者**: Victor Weeks
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 経済学

## Abstract

Generative AI is reshaping how research software is developed. Tools and patterns ranging from “vibe coding” through the Model Context Protocol (MCP) and autonomous agents now offer compelling productivity gains, but their adoption in scientific computing surfaces failure modes that general-purpose evaluation does not catch: silent unit conversions, violated conservation laws, hallucinated physics, loss of numerical precision, and quietly broken reproducibility. These failures share a signature: nothing visible goes wrong. The AI ecosystem itself is moving fast, leaving RSEs to make consequential integration decisions with little shared vocabulary or principled guidance. This talk introduces Scientific Agentic Engineering, the central contribution of an in-progress 2026 Better Scientific Software (BSSw) Fellowship: a tool-agnostic methodology for integrating AI agents into high-stakes scientific software workflows. The framework defines how agents, scientific skills, and MCP servers should be structured around validation loops, explicit human-in-the-loop checkpoints, and domain-specific safeguards. Every task moves through a short workflow (frame, plan and critique, implement, verify), with decisions recorded throughout, and the framework maps each documented failure mode to the stage where it is cheapest to catch. The intent is not to recommend any particular AI tool but to articulate foundational concepts that remain valid as the underlying technology changes. I will share three artifacts from the fellowship: The Framework (published July 2026). Shared vocabulary, its principles and workflow, structural guidance on where safeguards live, and a pattern catalog of named practices, each tied to the failure it counters. The Reference Workflow. A structured exercise in which RSEs use AI tools to build a small weather-model error-statistics application, applying the framework to avoid the failure modes it documents. The Community Repository. A curated starter set of scientific MCP server templates, agent skills such as unit checkers and conservation-law validators, and agent configuration examples, designed to be starting points for the community to adapt to a variety of scientific domains. These artifacts are by design community resources, and broader adoption is the explicit aim of the remaining milestones, which include an interactive online tutorial series comparing purpose-built scientific agents with general-purpose tools, a recorded live workshop published for asynchronous access, and a BSSw.io blog post directing the community to the project’s resources. This work engages the conference theme directly by advancing AI-assisted scientific software development from ad-hoc experimentation toward a disciplined, transferable engineering practice.
