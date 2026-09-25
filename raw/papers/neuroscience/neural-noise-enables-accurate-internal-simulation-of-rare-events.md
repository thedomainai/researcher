---
title: "Neural noise enables accurate internal simulation of rare events"
authors: "Heng Zhang, Pawel Herman, Zenas C. Chao"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-09-18T06:00:25.583872"
arxiv_id: "http://arxiv.org/abs/2609.18033v1"
source_api: "arxiv"
categories: "q-bio.NC, cs.NE"
---

# Neural noise enables accurate internal simulation of rare events

**著者**: Heng Zhang, Pawel Herman, Zenas C. Chao
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

The brain needs an accurate internal model of the world to generate predictions and guide behavior. However, it must estimate the statistical structure of the environment from limited experience. This is particularly difficult for rare events, whose observed frequencies in a limited sample may substantially under- or overestimate their true frequencies. How the brain constructs an accurate internal model despite this sampling problem remains unclear. We address this problem using a Bayesian Confidence Propagation Neural Network (BCPNN) trained on event sequences from a Markov-chain random walk with controlled event frequencies. Treating the underlying Markov structure as the ground truth, we train the network on limited sample of event sequences and then allow it to generate autonomous replay based on the learned structure. We evaluate replay fidelity at the levels of both marginal event frequencies and conditional transition structure. We find that moderate neural noise, modeled as temporally correlated random fluctuations in unit activity during replay, is critical for faithful internal simulation. Without this variability, deterministic replay systematically under- or overrepresents rare events, whereas moderate noise restores both their marginal and conditional occurrence. Moderate noise also broadens the range of parameter values that produce accurate replay, making the model more robust to parameter variation. Together, these results support noise-assisted internal simulation as a potential mechanism for compensating for sampling errors arising from limited experience. Our model also provides a testable framework for investigating how altered neural variability may impair internal-model fidelity in disorders such as Parkinson's disease.
