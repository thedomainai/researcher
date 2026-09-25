---
title: "The Von-Neumann State-Space Transformer for neural decoding"
authors: "Morteza Sarafyazd"
year: 2026
citations: 0
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-08-28T09:00:03.672246"
arxiv_id: "http://arxiv.org/abs/2608.25088v1"
source_api: "arxiv"
categories: "cs.LG, cs.AI, q-bio.NC"
---

# The Von-Neumann State-Space Transformer for neural decoding

**著者**: Morteza Sarafyazd
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 脳科学

## Abstract

Cortical computation is strikingly low-dimensional: a handful of latent variables, carried in a neural population's activity, steer the higher-dimensional responses of individual neurons. Our aim is sample efficiency-models that decode well from limited data and at small parameter budgets. In a standard Transformer layer, the feed-forward block applies the same operator to every token. We suggest a von-Neumann inspired hypothesis of efficient computation as an alternative for neural decoding: a controller decodes an instruction and then executes a token-specific operator; the usual realization-a soft mixture of experts-only blends their outputs, not operators. We introduce a von-Neumann State-Space Transformer (VN-SST), a memory-augmented Transformer whose feed-forward block is a low-rank instruction bank: a shared base operator plus a small set of learned low-rank instructions, from which a per-token code synthesizes the weight matrix actually used at that token. The code is read from a low- dimensional projection of a carried state-space memory, so a slow latent trajectory acts as an instruction pointer-mirroring how low-dimensional dynamics may route cortical computation. On three motor-cortex neural-decoding benchmarks, VN-SST is far more data-efficient than a modern Transformer, each jointly predicting spikes and decoding behavior. This model wins by a wide margin on the scarcest benchmark, leads on the other two, and turns longer context into rising rather than falling accuracy. We evaluated that the network compresses a large instruction bank to a few bits per token, so program capacity acts as a control channel, not an accuracy lever. The same model is also more parameter-efficient on two small text benchmarks used for language modeling (LLMs), suggesting a generic mechanism.
