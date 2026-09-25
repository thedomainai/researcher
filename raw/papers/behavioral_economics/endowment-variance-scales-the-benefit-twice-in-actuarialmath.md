---
title: "Endowment variance scales the benefit twice in actuarialmath"
authors: "Xamit Kadirbekov"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-09-21T06:01:27.875773"
doi: "https://doi.org/10.5281/zenodo.22843199"
openalex_id: "https://openalex.org/W7213640609"
source_api: "openalex"
---

# Endowment variance scales the benefit twice in actuarialmath

**著者**: Xamit Kadirbekov
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

In actuarialmath, endowment_insurance computes benefit-scaled moments and then applies the death-benefit scale again to the variance. A finite one-year payout of 2 with probability 1/4 or 1 with probability 3/4 returns variance 0.75 instead of 0.1875. Tested current main: 7d18f11ad304898f177b7922b3c53f70e4c2b4f4; separately verified official PyPI 1.1.0. An independent exact-rational payout oracle finds 483 variance mismatches in 1,300 discrete scenarios. A narrow local correction removes all 483 within the stated tolerance; restoring the original line restores them. First and second moments remain equal. Six focused regression methods pass with the candidate. Full upstream tests and continuous paths were not evaluated. Executed chain: real endowment moments → real portfolio normal-approximation API → a GERO synthetic JSON/HTML risk summary → an example limit monitor that reads the JSON. For 100 independent test policies, the reported 95th-percentile estimate changes from 41,862.13 to 6,606.12 and the 7,000-limit decision flips. The exact discrete percentile is 6,600; the remaining normal-approximation difference is retained. A zero-death-benefit example demonstrates underestimation in the opposite direction. The report, wiring and monitor are GERO demonstration components, not an insurer application. No real premium, reserve requirement, underwriting decision, customer loss or insurer deployment is established. Twenty-three previously passing rows change only within rounding tolerance. This is separate from the earlier whole-life variance defect; applying that earlier patch alone leaves all 483 mismatches. A bounded duplicate review found no exact earlier report; the source pattern is old, not a recent regression. Developer report sent before publication: https://github.com/terence-lim/actuarialmath/issues/6 . No acknowledgment or acceptance is claimed. The portable archive contains pinned source, official wheel, exact oracle, patch, restoration controls, generated documents, raw results and verification receipts. SHA-256: 59f6da29073136146139e9feade3fa504eec7c1ff37c7c2ffd16b8f65c041c2c. Independent GERO research by Xamit Kadirbekov. AI-assisted preparation and testing. MIT; original notices retained. The frozen evidence files remain unchanged. Verified publication links (19 September 2026):Report: https://www.gero.uz/research/articles/actuarialmath-endowment-variance-benefit-scale.htmlSource and patch: https://github.com/kadyrbekovhamit-cyber/gero-numerical-observatory/blob/main/catalog/reports/actuarialmath-endowment-variance-benefit-scale.mdHugging Face mirror: https://huggingface.co/datasets/XamitK/gero-research-evidence-2026-09/blob/main/actuarialmath-endowment-variance-benefit-scale.mdLinkedIn discussion: https://www.linkedin.com/feed/update/urn:li:share:7507014387195531264/32-second English explanation: https://youtube.com/shorts/h8JZ-kw4Ot0Original editorial cartoon and disclosed synthetic English narration. The video illustrates this existing evidence; it is not an additional finding.
