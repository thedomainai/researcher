---
title: "Agents Build Worlds for Agents, Agents Hunt Agents in Worlds"
authors: "Jiawei Zhang"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-10-17T12:00:45.360472"
doi: "https://doi.org/10.6082/8qh1m-q2a54"
openalex_id: "https://openalex.org/W7222017696"
source_api: "openalex"
---

# Agents Build Worlds for Agents, Agents Hunt Agents in Worlds

**著者**: Jiawei Zhang
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

This dissertation studies how stronger agents can improve the process by which their successors are developed and assessed: agents build worlds for agents, and agents hunt agents in those worlds. ArenaWeaver couples automated construction of executable worlds with agent-against-agent attack discovery within them. These activities could reinforce one another: generated experience and discovered failures could guide learning; improved models could then build better harnesses and richer worlds and renew attacks against more capable agents. Automation lets both activities scale across tasks and model generations. Their combination makes the conditions of later learning and evaluation part of what progress should improve. The move from prediction to action changes what must be certified. Our recognition attacks expose failures, while our randomized-smoothing methods certify prediction robustness under specified perturbations. For agents, the corresponding challenge is to guarantee that sequences of actions respect safety constraints as the world changes. Interactive worlds make the relevant state transitions and consequences available for study. Agents build worlds and harnesses for other agents. Within a shared execution framework, ArenaWeaver uses coding agents to construct application software, browser and tool interfaces, and evaluation tasks. ChatScene demonstrates a learning connection: generated simulator scenarios support reinforcement learning of driving policies. SafeAuto develops multimodal driving prediction and correction. Together, these studies motivate worlds whose software and learning experience can increasingly be produced by agents themselves. Better builders could expand what subsequent agents encounter, learn, and become capable of doing. Agents hunt agents in constructed worlds to guide improvement. Within the worlds it constructs, ArenaWeaver deploys attacking agents to discover failures in other agents; upgrading the attacking model exposes failures missed by its predecessor while the target remains fixed. UDora shows that reasoning-guided action selection can itself be redirected. Discovered failures could guide both correction of the tested agents and construction of the worlds used to train their successors. More capable attacking agents could then renew the challenge after those improvements. Alignment must be sustained through monitoring and informed by mechanistic understanding. Any-Depth Alignment links generation-time safety readouts to interventions that interrupt unsafe continuations. Its representation analyses identify signals useful for monitoring, while complementary feature interventions clarify mechanisms involved in refusal. These findings connect the study of internal representations to the problem of making safety judgments affect behavior. They motivate agent safeguards that combine internal monitoring with effective intervention and are reassessed as learning changes the actors they supervise. How can humans control AI systems far more capable than themselves? The goal is to train agents that continue to pursue human intentions and respect safety constraints as their capabilities grow. Missing training experience, imperfect rewards, and unreliable supervision make this difficult when agents can solve problems their overseers cannot. As improved agents help generate the feedback used to train and assess their successors, errors in that feedback could propagate across generations. AI-assisted safety research must therefore make consequential deviations detectable and correctable by people who cannot independently reproduce every judgment.
