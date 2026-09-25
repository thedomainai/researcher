---
title: "Who Governs Autonomous AI Execution? Execution Governance AI (EGA) V9: A Deterministic Runtime Governance Framework for Trustworthy Autonomous Workflows"
authors: "DaeJung Byun"
year: 2026
citations: 0
paper_type: "primary"
domain: "information_systems"
fetched: "2026-08-20T12:31:35.893582"
doi: "https://doi.org/10.5281/zenodo.22003768"
openalex_id: "https://openalex.org/W7203681081"
source_api: "openalex"
---

# Who Governs Autonomous AI Execution? Execution Governance AI (EGA) V9: A Deterministic Runtime Governance Framework for Trustworthy Autonomous Workflows

**著者**: DaeJung Byun
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 情報システム

## Abstract

As autonomous AI systems transition from language-generation tools to execution-driven agents, maintaining trustworthy runtime execution without sacrificing performance, operational cost, deployment simplicity, or security has become a fundamental engineering challenge. How can autonomous AI systems satisfy these requirements simultaneously without modifying existing AI applications or foundation models? Execution Governance AI (EGA) V9 addresses this challenge through a deterministic runtime-governance framework that combines deterministic replay, provenance-aware verification, trust-state evaluation, and fail-closed containment as a unified execution-governance layer. The proposed framework was evaluated using a comprehensive methodology covering replay consistency, execution-divergence detection, provenance reconstruction, containment validation, large-scale detection quality, hard-case robustness, runtime performance, runtime verification cost, deployment simplicity, runtime trust, and reproducibility. The evaluation included deterministic replay experiments, adversarial workflow mutation scenarios, large-scale governance validation, and reproducibility validation based on deterministic Replay Root generation and benchmark artifact verification. Across the predefined large-scale evaluation of up to 10,000 workflows and the 1,000-workflow hard-case evaluation, EGA V9 achieved 100% detection performance with 0% false-positive and false-negative rates, while deterministic replay remained consistent under the defined evaluation protocol. Runtime verification required zero additional language-model invocations, zero additional external API requests, and minimal execution overhead, while deterministic Replay Root generation and benchmark artifacts remained reproducible. These detection results characterize execution-divergence detection within the evaluated scenarios and should not be interpreted as guarantees of all runtime-security properties. Additional adversarial verification identified clear capability boundaries: fail-closed execution suppression remained effective while an active mismatch was present, whereas persistent post-incident restriction, exactly-once side-effect execution, and complete evidence-contract integrity were not established by the current implementation. Taken together, these results provide reproducible evidence that EGA V9 can serve as a practical foundation for deterministic execution governance within the evaluated scope, while also identifying specific runtime-governance capabilities that remain open for further development.
