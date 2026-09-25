---
title: "MotionQ: Operator-Conditioned Motion Quotients for Cross-Observation WiFi Gesture Recognition"
authors: "Xiang Zhang, Huan Yan, Geying Yang, Jianchun Liu, Tao Liu"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-09-12T06:05:07.216245"
arxiv_id: "http://arxiv.org/abs/2609.11818v1"
source_api: "arxiv"
categories: "cs.HC"
---

# MotionQ: Operator-Conditioned Motion Quotients for Cross-Observation WiFi Gesture Recognition

**著者**: Xiang Zhang, Huan Yan, Geying Yang, Jianchun Liu, Tao Liu
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

WiFi gesture recognition is accurate in fixed deployments but often degrades when user orientation, available links, or transceiver placement changes. Unlike ordinary domain shifts, these changes alter the wireless observation operator, so the same motion is expected to produce different measurements. Existing methods nevertheless pursue domain-invariant features and largely overlook changing layouts and observation configurations. Yet changing the observation operator also changes which task-relevant motion cues are physically observable, rather than merely altering the appearance of a fixed set of cues. Under a local linearization of the WiFi forward process, we derive a common task-observability condition under which a strict common linear representation is recoverable from every geometry-induced operator while preserving the gesture task. When the condition fails, enforcing stronger alignment across additional heterogeneous source operators may discard task-relevant cues still observable under individual operators. We therefore present MotionQ, which generates an operator-conditioned two-support motion measure for each candidate geometry. A motion quotient removes only the arbitrary ordering of its unlabeled supports and is represented by permutation-invariant central moments. Rather than matching quotients across operators, single-link-retention interventions encourage each view to retain information sufficient for gesture recognition. Extensive evaluations show that MotionQ is robust to extrapolative observation operators.
