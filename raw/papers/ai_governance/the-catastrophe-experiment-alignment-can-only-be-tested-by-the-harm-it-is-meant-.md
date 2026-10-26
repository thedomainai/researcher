---
title: "The Catastrophe Experiment: Alignment can only be tested by the harm it is meant to prevent. Safety can be decided before it."
authors: "José Santiago Niño Mojica"
year: 2026
citations: 0
paper_type: "primary"
domain: "ai_governance"
fetched: "2026-10-27T06:04:06.331483"
doi: "https://doi.org/10.5281/zenodo.23645657"
openalex_id: "https://openalex.org/W7223565930"
source_api: "openalex"
---

# The Catastrophe Experiment: Alignment can only be tested by the harm it is meant to prevent. Safety can be decided before it.

**著者**: José Santiago Niño Mojica
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: AIガバナンス

## Abstract

Artificial intelligence is the only safety-critical technology certified by evaluating its internal dispositions rather than bounding its external actions. This paper proves mathematically that under that standard of evidence, the only experiment that tests whether an AI system is safe is the catastrophe it was meant to prevent, and it states the operational and legal standard that decides safety before irreversible harm occurs. We prove two limits. The first is at the interior (Theorems 1 to 3). A governor never observes a model's ~1011 internal parameters; it observes only the requests that cross the execution boundary. Because the same valid request is produced by an aligned internal state, a deceptive state, and a software fault, no benchmark, reasoning trace, or interpretability probe can decide whether a model's internal state is aligned before it acts. The only observation that refutes the claim “this AI is aligned” is an effect that exceeds permitted operational bounds, and that observation arrives with the harm itself. Safety can be decided before irreversibility at one unique point: the last projection where internal computation becomes an external request (in deployed systems, the tool call), by an independent enforcement gate whose guarantee does not weaken as the model grows more capable. The second limit is at the boundary record (Theorem 4). Conventional audit logs, private ledgers, hardware enclaves, and signatures resting on reusable or precomputable keys (including post-quantum lattice keys and eIDAS 2.0 hardware security modules) are testimony, not independent evidence. Any custodian holding a surviving key can alter a past policy and re-sign the ledger in milliseconds, and any prior key or deterministic seed can authenticate a position without the gate's evaluation. For a record to establish the rule in force at the moment of action, the policy check, the advance of an external sequence position, and the release of the action must execute as one atomic transition with no surviving or precomputable signing authority. In August 2026, the European AI Act's draft logging standard (prEN 18229-1) was rejected at enquiry because it contained no testable sentence. Once this mathematics is known, certifying high-risk AI systems on alignment evidence is negligence in the technical sense. Annex A supplies the four-clause standard that makes the law executable.
