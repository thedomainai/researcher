---
title: "Backdoor Attacks and Countermeasures in Natural Language Processing Models: A Comprehensive Security Review"
authors: ["Pengzhou Cheng", "Zongru Wu", "Wei Du", "Haodong Zhao", "Wei Lu", "Gongshen Liu"]
year: 2025
cited_by_count: 28
doi: "https://doi.org/10.1109/tnnls.2025.3540303"
openalex_id: W4407948749
paper_type: article
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Backdoor Attacks and Countermeasures in Natural Language Processing Models: A Comprehensive Security Review

**Authors**: Pengzhou Cheng, Zongru Wu, Wei Du, Haodong Zhao, Wei Lu, Gongshen Liu | **Year**: 2025 | **Cited by**: 28 | **Kind**: article | **Relevance**: safety_interp: core

## Abstract

Language models (LMs) are becoming increasingly popular in real-world applications. Outsourcing model training and data hosting to third-party platforms has become a standard method for reducing costs. In such a situation, the attacker can manipulate the training process or data to inject a backdoor into models. Backdoor attacks are a serious threat where malicious behavior is activated when triggers are present; otherwise, the model operates normally. However, there is still no systematic and comprehensive review of LMs from the attacker's capabilities and purposes on different backdoor attack surfaces. Moreover, there is a shortage of analysis and comparison of the diverse emerging backdoor countermeasures. Therefore, this work aims to provide the natural language processing (NLP) community with a timely review of backdoor attacks and countermeasures. According to the attackers' capability and affected stage of the LMs, the attack surfaces are formalized into four categorizations: attacking the pretrained model with fine-tuning (APMF) or parameter-efficient fine-tuning (PEFT), attacking the final model with training (AFMT), and attacking large language model (ALLM). Thus, attacks under each categorization are combed. The countermeasures are categorized into two general classes: sample inspection and model inspection. Thus, we review countermeasures and analyze their advantages and disadvantages. Also, we summarize the benchmark datasets and provide comparable evaluations for representative attacks and defenses. Drawing the insights from the review, we point out the crucial areas for future research on the backdoor, especially soliciting more efficient and practical countermeasures.
