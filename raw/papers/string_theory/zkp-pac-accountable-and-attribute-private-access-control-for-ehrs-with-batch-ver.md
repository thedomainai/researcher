---
title: "ZKP-PAC: Accountable and Attribute-private Access Control for EHRs with Batch-verifiable Zero-knowledge Proofs and Provably Secure Revocation on Hyperledger Fabric"
authors: "Komal Patiyal, Rupali Dhir"
year: 2026
citations: 0
paper_type: "primary"
domain: "string_theory"
fetched: "2026-11-28T08:09:45.284820"
doi: "https://doi.org/10.22266/ijies2026.1130.35"
openalex_id: "https://openalex.org/W7222706867"
source_api: "openalex"
---

# ZKP-PAC: Accountable and Attribute-private Access Control for EHRs with Batch-verifiable Zero-knowledge Proofs and Provably Secure Revocation on Hyperledger Fabric

**著者**: Komal Patiyal, Rupali Dhir
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 超ひも理論・量子重力

## Abstract

Electronic health record sharing over permissioned ledgers has settled into two camps: schemes that conceal the access policy and the requester's attributes surrender any means of attributing a later disclosure, while schemes supporting white-box tracing publish the policy and so leak the clinical context of every protected record.A second cost is as stubborn: a per-circuit trusted setup repeats its ceremony whenever a policy changes, and revocation by archive re-encryption scales with the corpus rather than with the change.This paper presents ZKP-PAC (Zero-Knowledge Policy-hiding Accountable access Control), which addresses both.Consumers establish attribute satisfaction through zero-knowledge proofs over a universal and updatable reference string, instantiated as PLONK with KZG, so a policy change needs no fresh ceremony; the chaincode folds b proofs into one randomised pairing product, so verification uses a constant number of pairings although its total cost still grows with a small per-proof term; and an accountable proxy re-encryption update rewrites only the m records a revocation touches.A tracing authority acting solely on an adjudicated request can open a disputed access, and forward and backward secrecy are established as explicit games.On a Hyperledger Fabric 2.5 testbed driven by MIMIC-III-derived policies the framework sustains 214 tx/s at 100 concurrent consumers with 742 ms latency, 44.6% above the 148 tx/s of the strongest baseline re-implemented here, R-CP-ABE-ORP; amortises verification from 2.112 ms for one proof to 0.094 ms at batch size 64; and cuts revocation latency at 100 affected records by 33.7% against that baseline.Against a different comparator, a per-circuit Groth16 instantiation of the same relation, proving is 15.0% slower; the two percentages are reported separately because their reference systems differ.All code, configurations, seeds and logs are released.
