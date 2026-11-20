---
title: "When uncertainty quantification fails: structural vulnerabilities and corrections for selective prediction under clinical class imbalance"
authors: "Walter Endrizzi, Flavio Ragni, Raffaele Marchesi, Stefano Bovo, Monica Moroni"
year: 2026
citations: 0
paper_type: "primary"
domain: "international_business"
fetched: "2026-11-21T06:05:28.505273"
doi: "https://doi.org/10.1186/s13040-026-00618-1"
openalex_id: "https://openalex.org/W7224120380"
source_api: "openalex"
---

# When uncertainty quantification fails: structural vulnerabilities and corrections for selective prediction under clinical class imbalance

**著者**: Walter Endrizzi, Flavio Ragni, Raffaele Marchesi, Stefano Bovo, Monica Moroni
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 国際経営

## Abstract

Background. Selective prediction systems improve the safety of clinical artificial intelligence by deferring ambiguous cases to human experts while automating high-confidence decisions. However, this safety mechanism relies entirely on the premise that uncertainty scores accurately reflect clinical ambiguity. In prognostic tasks characterized by severe class imbalance, where the clinical outcome of interest is a minority, this assumption breaks down. Standard uncertainty measures cease to capture clinically aligned ambiguity; instead, they become a proxy for class membership, systematically penalizing minority patients regardless of their individual predictive clarity. Results. Across 56 synthetic conditions and three neurodegenerative cohorts spanning severe class imbalance to near-balanced conditions (multiple sclerosis, Parkinson's Disease, Alzheimer's Disease), our framework consistently maintained bounded, balanced risk across trajectories. In contrast, global metrics either collapsed minority Sensitivity or protected the minority at the expense of majority patients. Applying CCR with standard entropy fails to protect the minority because it breaks within-class monotonicity when tau=0.5. Combining CCR with threshold-aware metrics restores strict monotonicity, correctly identifies ambiguous patients, and safely mitigates minority exclusion. Conclusions. Under clinical class imbalance, standard uncertainty quantification measures dataset sparsity rather than clinical ambiguity, creating a systemic illusion of safety. This bias is a correctable structural flaw. Clinical pipelines deploying selective prediction under imbalance should adopt threshold-aligned uncertainty measures and class-stratified evaluation. This reduces class-specific risk imbalance, supporting safer selective prediction under the evaluated conditions without silently excluding the most vulnerable patients.
