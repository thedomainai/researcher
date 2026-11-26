---
title: "A Closed-Loop Framework for Trustworthiness Assessment in Large Language Models"
authors: "Khadija Parwez, Faheem Shaukat, Faisal Alhwikem, Fawwad Hassan Jaskani, Sardar Asad Arfan Khan"
year: 2027
citations: 0
paper_type: "primary"
domain: "relativity"
fetched: "2026-11-27T06:06:25.279284"
doi: "https://doi.org/10.32604/cmc.2026.084743"
openalex_id: "https://openalex.org/W7223178368"
source_api: "openalex"
---

# A Closed-Loop Framework for Trustworthiness Assessment in Large Language Models

**著者**: Khadija Parwez, Faheem Shaukat, Faisal Alhwikem, Fawwad Hassan Jaskani, Sardar Asad Arfan Khan
**年**: 2027 | **被引用数**: 0
**タイプ**: primary | **分野**: 相対性理論・重力

## Abstract

Trustworthiness is a fundamental requirement for Large Language Models (LLMs), particularly in high-stakes domains such as healthcare, finance, and education, where unreliable model behavior may lead to incorrect or misleading responses. We distinguish safety, which concerns harmful or undesirable outputs, from security, which concerns vulnerabilities arising from adversarial manipulation of model inputs or behavior. This work focuses on robustness and prediction stability under adversarial prompting. Despite strong performance across a wide range of tasks, LLMs remain vulnerable to adversarial prompting, where small semantically equivalent perturbations in the input can produce unstable or incorrect predictions. Existing approaches address this problem through robustness training, alignment with human feedback, or calibration approaches; however, they often focus on individual aspects of model behavior and do not adequately examine prediction stability under perturbations. To address this limitation, we propose Closed-Loop Trustworthiness (CLoT), an inference-time framework for improving robustness and prediction stability under adversarial prompting. The framework consists of two stages: (i) Evaluation and Failure Detection (Stage I), which analyzes model responses under controlled perturbations to identify inconsistent predictions associated with unreliable behavior; and (ii) Evaluation-Guided Intervention (Stage II), which applies perturbation-consistent post-hoc correction without modifying model parameters. We empirically evaluate CLoT on six benchmarks (SQuAD 2.0, AdvBench, HH-RLHF, HotpotQA, FEVER, and TruthfulQA) and observe performance degradation of up to 28% under adversarial prompting. Experimental results show that CLoT improves robust accuracy by up to +4.9% and failure detection performance by up to +12.5%, while reducing calibration error (e.g., ECE to 0.050).
