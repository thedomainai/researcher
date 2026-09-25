---
title: "Perception-Aware Communication Middleware for Distributed Visual Perception in UAV Swarms"
authors: "Manveen Kaur, Kevin Loi, Ifunanya Okafor, Daniel Ng, Joseph Lucey-Renteria"
year: 2026
citations: 0
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-09-23T06:01:59.944564"
arxiv_id: "http://arxiv.org/abs/2609.24964v1"
source_api: "arxiv"
categories: "cs.MA"
---

# Perception-Aware Communication Middleware for Distributed Visual Perception in UAV Swarms

**著者**: Manveen Kaur, Kevin Loi, Ifunanya Okafor, Daniel Ng, Joseph Lucey-Renteria
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

Unmanned Aerial Vehicle (UAV) swarms increasingly support safety-critical applications that rely on distributed visual perception. Meeting the low-latency requirements of these applications can require perception models to execute within the swarm on inference-capable UAVs, creating a need for efficient UAV-to-UAV transport of high-bandwidth perception data. However, the Quality-of-Service (QoS) requirements of perception differ from conventional packet-level QoS; successful delivery of individual packets does not ensure that a complete, timely, and usable image is available for inference. We present a novel perception-aware communication middleware that treats complete perception-data samples as the communication objects for which QoS must be satisfied. The middleware extends a lightweight UDP broker-based publish-subscribe architecture with perception-specific services, including image fragmentation and reconstruction, concurrent packet transmission, priority-aware scheduling, and image quality assessment. The middleware is evaluated on a heterogeneous hardware testbed emulating a UAV swarm using YOLOv8n object detection. Experimental results demonstrate low end-to-end application latency, substantially higher throughput than a lightweight UDP broker, effective prioritization of perception traffic under increasing background load, and mitigation of object-detection degradation through middleware-level image quality assessment. This work provides an initial framework for integrating AI-specific data handling into communication middleware to support emerging distributed AI applications in multi-agent mobile cyber-physical systems.
