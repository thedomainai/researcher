---
title: "Beyond LLM Serving: Characterizing Vision-Language-Action Workloads for Embodied AI System Design"
authors: "SeongHun Jung, Sieun Moon, Jiyoung Jeong, Jimin Lee, Jaehyuk Huh"
year: 2027
citations: 2
paper_type: "primary"
domain: "neuroscience"
fetched: "2026-11-21T06:00:15.011454"
doi: "https://doi.org/10.1145/3845814.3850089"
openalex_id: "https://openalex.org/W7220648263"
source_api: "openalex"
---

# Beyond LLM Serving: Characterizing Vision-Language-Action Workloads for Embodied AI System Design

**著者**: SeongHun Jung, Sieun Moon, Jiyoung Jeong, Jimin Lee, Jaehyuk Huh
**年**: 2027 | **被引用数**: 2
**タイプ**: primary | **分野**: 脳科学

## Abstract

Vision-language-action (VLA) models translate multimodal observations into low-level robot actions. During robot operation, each control period sets an inference deadline, and overruns leave the robot acting on stale observations, reducing task success. Meeting this deadline motivates on-device or nearby edge execution, where a single robot requires batch-1 inference outside the design point of LLM serving systems. Although VLA architectures combine familiar vision-language, autoregressive, and diffusion-style components, their runtime behavior in this batch-1 control setting remains uncharacterized. We characterize four representative VLA models on an edge GPU server and two onboard SoCs, using single-inference profiling and 43,200 closed-loop episodes. Action tensor dimensionality determines whether a stage is memory- or compute-bound, platform balance can shift that bottleneck, and GPU frequency scaling yields a platform-dependent energy-latency sweet spot. In closed-loop operation, overlapping inference with action execution creates an accuracy-speed-energy tradeoff, and no configuration is Pareto-dominant across deployment SLOs. These results guide joint design of VLA model architectures, hardware, and runtime policies.
