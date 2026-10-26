---
title: "Statistical Detection of Governance Failure in Production AI"
authors: "Luca Andrea Bonetti, Priya Ramesh Ramachandran"
year: 2026
citations: 0
paper_type: "primary"
domain: "information_systems"
fetched: "2026-10-27T06:06:02.316808"
doi: "https://doi.org/10.5281/zenodo.23617261"
openalex_id: "https://openalex.org/W7223469838"
source_api: "openalex"
---

# Statistical Detection of Governance Failure in Production AI

**著者**: Luca Andrea Bonetti, Priya Ramesh Ramachandran
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 情報システム

## Abstract

Abstract A governance failure in a production AI system is usually discovered after it has already changed the state of the world, and is then described in prose rather than measured. This paper argues that the control obligations established by Mesbaul Haque Sazu in the Governed Decision-Intelligence (GDI) framework [14], together with the enterprise governance framework that carries them into production [13], already emit, as a by-product of their operation, a structured event stream from which governance failure can be detected statistically and in near real time. The GDI framework makes the individual decision the unit of assurance and binds a Decision Record at generation time [14]; the governed-execution layer captures an Execution Record at commit and logs the propensity of every routing choice [13]. We take those two records as a joined observation and treat each governed decision as one sample in a monitored stochastic process. On that foundation we develop a detection layer: point and interval estimators for four quantities that these invariants make observable but that the frameworks do not themselves cast as random variables, specifically the recorded-refusal rate, the freshness-failure rate at commit, the calibration drift of the routing signal, and the propensity shift that signals drift-under-action. For each we give an estimator, its sampling distribution, a sequential test with a controlled false-alarm rate, and a power analysis that states how many governed decisions must accrue before a deviation of a given size is detectable. A stream of 60,000 governed decisions drawn from publicly available data in open-source platforms illustrates the operating characteristics of the tests; it shows how the detectors behave rather than standing as a validated field deployment. The contribution is a measurement discipline that sits on top of the governance control structure, not a replacement for it; every quantity we estimate is defined only because these frameworks require the evidence that makes it computable. Keywords: AI governance; Governed Decision-Intelligence; statistical process control; sequential testing; calibration drift; drift-under-action; power analysis; decision records; production AI; model risk management
