---
title: "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents"
authors: ["Jenny Zhang", "Shengran Hu", "Cong Lu", "R. Lange", "Jeff Clune"]
year: 2025
cited_by_count: 294
doi: null
openalex_id: arxiv-2505.22954
paper_type: article
evidence_kind: article
topics: ["agents"]
landmark: true
abstract_source: "semantic_scholar"
---

# Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents

**Authors**: Jenny Zhang, Shengran Hu, Cong Lu, R. Lange, Jeff Clune | **Year**: 2025 | **Cited by**: 294 | **Kind**: article | **Relevance**: agents: core

## Abstract

Most of today’s AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, provides a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries. There is growing hope that the current manual process of advancing AI could itself be automated. If done safely, such automation would accelerate AI development and allow us to reap its benefits much sooner. This prospect raises the question of how AI systems can endlessly improve themselves while getting better at solving relevant problems. Previous approaches, such as meta-learning, provide a toolset for automating the discovery of novel algorithms but are limited by the human design of a suitable search space and first-order improvements. The Godel machine [116], on the other hand, introduced a theoretical approach to a self-improving AI, capable of modifying itself in a provably beneficial manner. Unfortunately, this original formulation is in practice impossible to create due to the inability to prove the impact of most self-modifications. To address this limitation, we propose the Darwin Godel Machine (DGM), a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks. In this paper, the DGM aims to optimize the design of coding agents, powered by frozen foundation models, which enable the ability to read, write, and execute code via tool use. Inspired by biological evolution and open-endedness research, the DGM maintains an archive of generated coding agents. It then samples from this archive and tries to create a new, interesting, improved version of the sampled agent. This open-ended exploration forms a growing tree of diverse, high-quality agents and allows the parallel exploration of many different paths through the search space. Empirically, the DGM automatically improves its coding capabilities (e.g., better code editing tools, long-context window management, peer-review mechanisms), producing performance increases on SWE-bench from 20.0% to 50.0%, and on Polyglot from 14.2% to 30.7%. Furthermore, the DGM significantly outperforms baselines without self-improvement or open-ended exploration. All experiments were done with safety precautions (e.g., sandboxing, human oversight). Overall, the DGM represents a significant step toward self-improving AI, capable of gathering its own stepping stones along a path that unfolds into endless innovation. All code is open-sourced at https://github.com/jennyzzt/dgm.
