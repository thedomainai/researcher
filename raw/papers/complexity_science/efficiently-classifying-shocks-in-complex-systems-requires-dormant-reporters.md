---
title: "Efficiently classifying shocks in complex systems requires dormant reporters"
authors: "David A. Brewster, Philippe Cluzel"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-03T06:02:41.313551"
arxiv_id: "http://arxiv.org/abs/2609.00725v1"
source_api: "arxiv"
categories: "q-bio.QM, cond-mat.dis-nn, nlin.AO, physics.soc-ph, q-bio.MN"
---

# Efficiently classifying shocks in complex systems requires dormant reporters

**著者**: David A. Brewster, Philippe Cluzel
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Many natural and engineered systems are large complex networks of interacting components, and external perturbations drive them along different dynamical paths. Identifying which perturbation occurred matters for diagnosis, control, and prediction. Yet often times only a few components can be jointly monitored. Which components should be monitored? Experimental practice usually favors placing reporters at the most sensitive sites, where perturbations produce the largest effects. Using a simple dynamical model for complex systems with heterogeneous connectivity, we ask how sparse reporter panels should be chosen to classify shocks from partial trajectories when repeated trials only approximately reproduce an ideal initial condition. Once that reproduction is imperfect, sensitivity ranked panels fall far short of optimal, and the shortfall grows with the noise. We find that the best panels mix two kinds of reporters. A promiscuous reporter responds to most shocks, so it separates them mainly by degree, and degree fluctuates from trial to trial. A dormant reporter responds to only a few shocks but strongly, and its answers do not scatter as much between trials. As noise grows, the cost of losing a dormant reporter rises to meet the cost of losing a promiscuous one. Panels of either kind alone classify worse than the mixture, and no property of the members collected individually explains the ordering. Most of all, we find that only a minuscule number of reporters are needed on a panel to accurately identify which shock hit the system. We implement an efficient algorithm to assemble such a panel. Together these results provide a low cost practical design principle for monitoring large complex dynamical systems.
