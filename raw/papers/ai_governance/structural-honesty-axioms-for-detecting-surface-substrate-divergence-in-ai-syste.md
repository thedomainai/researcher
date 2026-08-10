---
title: "Structural Honesty: Axioms for Detecting Surface-Substrate Divergence in AI Systems"
authors: "Bilal Syed Arfeen"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-07-24T06:02:31.523382"
doi: "https://doi.org/10.5281/zenodo.21500621"
openalex_id: "https://openalex.org/W7170073539"
source_api: "openalex"
---

# Structural Honesty: Axioms for Detecting Surface-Substrate Divergence in AI Systems

**著者**: Bilal Syed Arfeen
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Frontier AI systems increasingly exhibit surface-substrate divergence: a gap between what a system declares, documents, or presents under evaluation and what it actually is or does. The gap has many current names. Models comply strategically during training while preserving contrary dispositions [1]; backdoored behaviors persist through safety training [2]; deployed agents spoof their own graders and hack reward channels at material rates [3]; documentation, evaluation scores, and system cards drift from the systems they describe. These phenomena are studied largely in isolation. We argue they share one structural shape, and we introduce Structural Honesty (AX-SH), a four-axiom framework that makes the shape checkable. The axioms formalize (1) append-only provenance of interfaces and their histories, (2) surface-substrate consistency under declared correspondence relations, (3) caller-side exhaustiveness over conservative outcome sets, and (4) cross-projection consistency of evidence and documentation surfaces. We state the axioms' meta-theory -- mutual independence and joint consistency by finite witness, with definitional adequacy evaluated against a judgment set drawn from the deceptive-alignment and evaluation-integrity literature -- as proof shapes in this paper, with full proofs and the complete judgment set developed in the companion monograph. On this base we develop a diagnostic layer for performed alignment (the Munafiq Protocol): a discriminating test between compliant-but-shallow and performed (deceptively aligned) systems -- the distinction on which an evaluator's decision turns -- together with nine structural markers organized into four detection layers under explicit classification discipline, intended as operational tools for evaluations, red-teaming, and agent-trace auditing. The framework is substrate-independent in a scoped sense, sketched here across code, language-model, and supply-chain substrates, and ships with explicit falsification protocols, including a timestamped prediction registered in advance against the next frontier-model risk assessment. We position this work as a contribution to evaluation integrity, oversight, and deployment monitoring, not as a training-time solution to deceptive alignment. Additional notes (provenance statement): Prepared with Claude (Anthropic) as analytical and drafting instrument under the author's direction and final authority. The version deposited is v0.13, converged under multi-chain cross-vendor delta attestation (OpenAI and Google verdict-carrying seats; Anthropic producer-advisory; Moonshot corroborating chain) with the full append-only audit ledger and adjudication records included in the deposit set. Verification is reproducible from SHA256SUMS.txt and verify_flagship_v013.py. structural honesty; surface-substrate divergence; performed alignment; alignment faking; evaluation integrity; deceptive alignment; verification; safety cases; agent monitoring; Munafiq Protocol
