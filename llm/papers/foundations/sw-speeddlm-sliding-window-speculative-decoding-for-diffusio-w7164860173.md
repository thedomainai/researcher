---
title: "SW-SpeedDLM: Sliding Window Speculative Decoding for Diffusion Language Models Under Long Context Constraints"
authors: ["Teng Dai", "Minjae Rhee", "Yuxuan Qin", "Bingjie Zi", "Wenhe Liu"]
year: 2026
cited_by_count: 5
doi: "https://doi.org/10.3390/math14122137"
openalex_id: W7164860173
paper_type: article
evidence_kind: article
topics: ["foundations"]
landmark: false
abstract_source: "openalex"
---

# SW-SpeedDLM: Sliding Window Speculative Decoding for Diffusion Language Models Under Long Context Constraints

**Authors**: Teng Dai, Minjae Rhee, Yuxuan Qin, Bingjie Zi, Wenhe Liu | **Year**: 2026 | **Cited by**: 5 | **Kind**: article | **Relevance**: foundations: supporting

## Abstract

Masked diffusion language models (MDLMs) apply full bidirectional attention at every denoising step, which incurs O(Tn2) cost in the number of steps T and the sequence length n. For an 8B parameter model at n = 8192 with T = 128, the KV cache alone exceeds 40 GB and rules out long document generation on a single GPU. We introduce SW-SpeedDLM, an inference wrapper for pretrained MDLMs that generates sequences of up to 16,384 tokens on one A100 with 40 GB. The framework comprises three components, each targeting a distinct bottleneck. Segmented SlidingWindow Denoising (SSWD) restricts each denoising loop to a window of W tokens and reduces the per-step cost to O(W2n/S). Cross-Segment KV Compression (CSKV) encodes each completed window into C summary tokens that later windows attend to at O(C) cost. Window Level Speculative Acceptance (WLSA) lets a small draft model propose k denoising steps that the target model verifies in a single forward pass, yielding up to 2.4× per window speedup. We prove that WLSA preserves the exact marginal distribution of the target model. On MDLM-860M and LLADA-8B across PG-19, LongBench, and WritingPrompts, SW-SpeedDLM achieves 3.7× higher throughput at n = 8192 than full attention generation at n = 2048 (its maximum feasible length) and lowers peak memory by 2.5× relative to full attention at n = 4096, the longest length full attention can support before exhausting GPU memory, while also increasing PG-19 bits per character by only 0.18.
