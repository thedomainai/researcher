---
title: "EvoFlock: evolved inverse design of multi-agent motion"
authors: "Craig Reynolds"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-06-26T06:00:59.693247"
arxiv_id: "http://arxiv.org/abs/2606.25280v1"
source_api: "arxiv"
categories: "cs.NE, cs.GR, cs.MA"
---

# EvoFlock: evolved inverse design of multi-agent motion

**著者**: Craig Reynolds
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

This paper describes an automatic method for adjusting or tuning models of multi-agent motion. Simulating the motion of bird flocks, human crowds, vehicle traffic, and other multi-agent systems is a widely used technique. These simulations model the behavior of a single group member (bird, human, or vehicle). The group behaviors (flock, crowd, traffic) emerge from interactions between group members. These models typically have many numerical control parameters. Even if each parameter is intuitive in isolation, their interaction can be complex and nonlinear. It is challenging to determine which parameters to adjust for the desired change in group behavior. Changing one aspect of group behavior often causes other aspects to change, leading to a tedious process of incremental changes. This work takes an inverse design approach. The desired group behavior is measured with a user-defined objective(/fitness/loss) function and optimized with a genetic algorithm. The objective function used here for basic flocking rewards proper spacing with neighbors, flying near a desired speed, and avoiding obstacles. Interestingly, the vivid alignment seen in bird flocks appears to emerge from maintaining proper spacing between flockmates.
