---
title: "Explainable Control Framework (XCF) based on Fuzzy Model-Agnostic Explanation and LLM Agent-Supported Interface"
authors: "Faliang Yin, Hak-Keung Lam, David Watson"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-06-26T06:01:59.666432"
arxiv_id: "http://arxiv.org/abs/2606.25941v1"
source_api: "arxiv"
categories: "cs.HC, cs.AI, eess.SY"
---

# Explainable Control Framework (XCF) based on Fuzzy Model-Agnostic Explanation and LLM Agent-Supported Interface

**著者**: Faliang Yin, Hak-Keung Lam, David Watson
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

Increasing demand for precise and reliable control in complex scenarios has led to the development of increasingly sophisticated controllers, including data-driven approaches employing closed box models and mathematically rigorous yet complex designs. This complexity highlights the needs for explainable control that can provide human-understandable insights into controller behavior. In this paper, an explainable control framework (XCF) along with supporting algorithms and user interface are proposed to explain how controllers determine their control actions and their underlying working mechanism. The novel contributions of this work are threefold: First, the XCF is designed to provide model-agnostic explanations for controllers in closed-loop systems and can optionally refine local explanations by system response dynamics. Second, a novel explanation method, hierarchical fuzzy model-agnostic explanation for control systems (HFMAE-C), is proposed based on the designed framework. The HFMAE-C employs a fuzzy logic system to approximate the controller's behavior and system dynamics, providing sample, local, domain and universe level explanations via IF-THEN rules revealing the controller's decision logic and salience values quantifying the contribution of system states to control actions. Third, a large language model agent-supported user interface is developed to automatically analyze user requirements, select appropriate algorithms, interpret the generated explanations to a natural language report, and provide interactive consultation. Case studies on inverted pendulum system and Turtlebot obstacle avoidance demonstrate the effectiveness of the proposed method through simulated user experiments and quantitative comparisons with mainstream explainable control approaches.
