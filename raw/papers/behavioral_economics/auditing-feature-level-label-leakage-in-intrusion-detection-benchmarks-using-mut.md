---
title: "Auditing Feature-level Label Leakage in Intrusion Detection Benchmarks Using Mutual Information"
authors: "Hussein A. Ismael, Ziyad Tariq Mustafa Al-Ta’i, Jamal Mustafa Abbas"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-09-21T06:01:29.590804"
doi: "https://doi.org/10.22266/ijies2026.1031.74"
openalex_id: "https://openalex.org/W7213616847"
source_api: "openalex"
---

# Auditing Feature-level Label Leakage in Intrusion Detection Benchmarks Using Mutual Information

**著者**: Hussein A. Ismael, Ziyad Tariq Mustafa Al-Ta’i, Jamal Mustafa Abbas
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Near-perfect accuracy and F1 are routinely reported on public intrusion-detection (IDS) benchmarks.This paper asks how much of that performance survives scrutiny, and reports two findings of very unequal size.First, we formalise LeakAudit, a mutual-information screen that ranks every feature by its dependence on the binary label, removes those above a stated threshold, and reports the resulting held-out F1 as an audited ceiling.Across NSL-KDD, Edge-IIoTset, CIC-IDS-2017, UNSW-NB15, and ToN-IoT Network, the screen costs 6.60, 2.91, 2.48, 0.70, and 0.04 percentage points of F1.Against injected leakage of known strength, it reaches a detection AUC of 0.972 at a falsealarm rate of 0.007, decisively better than a correlation screen but not better than a Random Forest importance ranking, which we report as measured.Second, and larger by roughly two orders of magnitude, we find that the evaluation protocol dominates feature-level leakage.ToN-IoT Network, the most audit-stable benchmark in this sample at 0.04 points, loses 34.2 points of F1 once training and test hosts are disjoint.NSL-KDD loses 24 points under its own official split before any auditing takes place.A permutation null further shows that the audit threshold has no statistical basis and is an effect-size convention rather than a significance test.We therefore position LeakAudit as an inexpensive disclosure layer rather than a validity guarantee, and argue that a leakage audit should accompany a deployment-aware evaluation protocol rather than replace one.
