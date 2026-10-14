---
title: "A Multi-Agent AI Optimization System for Improving Rig Utilization and Production Gains in the Burgan Field"
authors: "Shayma Faisal AlSaffar, Hussain Hashim Shuber, Mohamad Rami Mostafa Amcha, Lasha Targamadze, Muhammad Nasir Ibrahim"
year: 2026
citations: 0
paper_type: "primary"
domain: "human_ai_collaboration"
fetched: "2026-10-15T08:03:51.514855"
doi: "https://doi.org/10.2118/234185-ms"
openalex_id: "https://openalex.org/W7221664322"
source_api: "openalex"
---

# A Multi-Agent AI Optimization System for Improving Rig Utilization and Production Gains in the Burgan Field

**著者**: Shayma Faisal AlSaffar, Hussain Hashim Shuber, Mohamad Rami Mostafa Amcha, Lasha Targamadze, Muhammad Nasir Ibrahim
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 人間-AI協働

## Abstract

Abstract Scheduling a fleet of workover rigs across a mature giant field requires balancing production objectives against a dense web of operational constraints: artificial lift readiness, material availability, location doability, site and pad access, and rig–well compatibility. In the Greater Burgan complex, this forward planning has historically been built and maintained manually in the well delivery management (WDM) system, an in-house rig-scheduling application in which of the order of ten stakeholder teams continuously record and revise workover activities and their constraints. Across a typical year, the programme spans on the order of 500 workover wells and roughly 40 active rigs; distributing that fleet across the candidate wells and their ordered sequences yields a combinatorial space of astronomical size, on the order of hundreds of septillions of feasible arrangements and beyond, that cannot be searched by hand. This paper describes the design, deployment, and field evaluation of a multi-agent artificial intelligence (AI) scheduling system introduced by the Operator's Integration Excellence team to optimize the 90-day forward plan across the full workover operation of approximately 40 rigs and 200 workover wells. The system decomposes scheduling across cooperating agents: data preprocessing, rig–well resource matching, constraint validation, schedule optimization by a genetic algorithm adapted to the Operator's scheduling rules and operating over short- and long-term memory, execution monitoring, and feedback, with a human-in-the-loop review and approval workflow retained throughout. Planners select one of two objective modes (maximize production gain or meet a specified production target) while the optimizer enforces stability rules that protect active and next-scheduled jobs, group multi-well sites, and honor rig–well compatibility. Performance was evaluated by comparing manually prepared schedules against system-optimized schedules over identical planning inputs and, separately, through historical validation (backtesting) over rolling 90-day look-back windows. To respect data-confidentiality requirements, production results are reported in normalized form and absolute volumes are withheld. In a field-wide evaluation, the optimized schedule increased the projected 90-day production gain by 16% over the manual baseline, an advantage that compounded across the horizon, while fleet-average rig idle time fell by 46% and schedule preparation collapsed from about ten days of manual coordination to minutes of computation. The paper presents the constraint taxonomy and scheduling logic in transferable form and outlines an ongoing extension to new-drill planning, where injector–producer relationships, injection timing, and rig-contract capability introduce additional considerations.
