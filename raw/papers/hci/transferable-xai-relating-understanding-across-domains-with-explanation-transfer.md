---
title: "Transferable XAI: Relating Understanding Across Domains with Explanation Transfer"
authors: "Fei Wang, Yifan Zhang, Brian Y. Lim"
year: 2026
citations: 1
paper_type: "primary"
domain: "hci"
fetched: "2026-04-06T13:20:35.389497"
doi: "https://doi.org/10.1145/3742413.3789124"
openalex_id: "https://openalex.org/W7129699806"
source_api: "openalex"
---

# Transferable XAI: Relating Understanding Across Domains with Explanation Transfer

**著者**: Fei Wang, Yifan Zhang, Brian Y. Lim
**年**: 2026 | **被引用数**: 1
**タイプ**: primary | **分野**: HCI

## Abstract

Current Explainable AI (XAI) focuses on explaining a single application, but when encountering related applications, users may rely on their prior understanding from previous explanations. This leads to either overgeneralization and AI overreliance, or burdensome independent memorization. Indeed, related decision tasks can share explanatory factors, but with some notable differences; e.g., body mass index (BMI) affects the risks for heart disease and diabetes at the same rate, but chest pain is more indicative of heart disease. Similarly, models using different attributes for the same task still share signals; e.g., temperature and pressure affect air pollution but in opposite directions due to the ideal gas law. Leveraging transfer of learning, we propose Transferable XAI to enable users to transfer understanding across related domains by explaining the relationship between domain explanations using a general affine transformation framework applied to linear factor explanations. The framework supports explanation transfer across various domain types: translation for data subspace (subsuming prior work on Incremental XAI), scaling for decision task, and mapping for attributes. Focusing on task and attributes domain types, in formative and summative user studies, we investigated how well participants could understand AI decisions from one domain to another. Compared to single-domain and domain-independent explanations, Transferable XAI was the most helpful for understanding the second domain, leading to the best decision faithfulness, factor recall, and ability to relate explanations between domains. This framework contributes to improving the reusability of explanations across related AI applications by explaining factor relationships between subspaces, tasks, and attributes.
