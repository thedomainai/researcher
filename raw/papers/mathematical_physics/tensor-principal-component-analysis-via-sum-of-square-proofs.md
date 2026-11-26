---
title: "Tensor principal component analysis via sum-of-square proofs."
authors: "Samuel B. Hopkins, Jonathan Jingsheng SHI, David Steurer"
year: 2015
citations: 206
paper_type: "primary"
domain: "mathematical_physics"
domain_label: "数理物理学"
source_api: "openalex"
fetched: "2026-11-26T14:07:33.046685"
doi: ""
openalex_id: "W2963595633"
semantic_scholar_id: ""
arxiv_id: ""
url: "https://openalex.org/W2963595633"
tier: 2
explore_depth: 1
---

# Tensor principal component analysis via sum-of-square proofs.

**著者**: Samuel B. Hopkins, Jonathan Jingsheng SHI, David Steurer
**年**: 2015 | **被引用数**: 206
**タイプ**: primary | **分野**: 数理物理学

## Abstract

We study a statistical model for the \emphtensor principal component analysis problem introduced by Montanari and Richard: Given a order-3 tensor \mathbf T of the form \mathbf T = τ⋅v_0^⊗3 + \mathbf A, where τ≥0 is a signal-to-noise ratio, v_0 is a unit vector, and \mathbf A is a random noise tensor, the goal is to recover the planted vector v_0. For the case that \mathbf A has iid standard Gaussian entries, we give an efficient algorithm to recover v_0 whenever τ≥ω(n^3/4 \log(n)^1/4), and certify that the recovered vector is close to a maximum likelihood estimator, all with high probability over the random choice of \mathbf A. The previous best algorithms with provable guarantees required τ≥Ω(n). In the regime τ≤o(n), natural tensor-unfolding-based spectral relaxations for the underlying optimization problem break down. To go beyond this barrier, we use convex relaxations based on the sum-of-squares method. Our recovery algorithm proceeds by rounding a degree-4 sum-of-squares relaxations of the maximum-likelihood-estimation problem for the statistical model. To complement our algorithmic results, we show that degree-4 sum-of-squares relaxations break down for τ≤O(n^3/4/\log(n)^1/4), which demonstrates that improving our current guarantees (by more than logarithmic factors) would require new techniques or might even be intractable. Finally, we show how to exploit additional problem structure in order to solve our sum-of-squares relaxations, up to some approximation, very efficiently. Our fastest algorithm runs in nearly-linear time using shifted (matrix) power iteration and has similar guarantees as above. The analysis of this algorithm also confirms a variant of a conjecture of Montanari and Richard about singular vectors of tensor unfoldings.
