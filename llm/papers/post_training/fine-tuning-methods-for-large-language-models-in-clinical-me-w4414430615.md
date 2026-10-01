---
title: "Fine-Tuning Methods for Large Language Models in Clinical Medicine by Supervised Fine-Tuning and Direct Preference Optimization: Comparative Evaluation"
authors: ["Thomas Savage", "Stephen P. Ma", "Abdessalem Boukil", "Ekanath Srihari Rangan", "Vishwesh Patel", "Iván López", "Jonathan H. Chen"]
year: 2025
cited_by_count: 17
doi: "https://doi.org/10.2196/76048"
openalex_id: W4414430615
paper_type: article
evidence_kind: article
topics: ["post_training"]
landmark: false
abstract_source: "openalex"
---

# Fine-Tuning Methods for Large Language Models in Clinical Medicine by Supervised Fine-Tuning and Direct Preference Optimization: Comparative Evaluation

**Authors**: Thomas Savage, Stephen P. Ma, Abdessalem Boukil, Ekanath Srihari Rangan, Vishwesh Patel, Iván López, Jonathan H. Chen | **Year**: 2025 | **Cited by**: 17 | **Kind**: article | **Relevance**: post_training: core

## Abstract

Background: Large language model (LLM) fine-tuning is the process of adjusting out-of-the-box model weights using a dataset of interest. Fine-tuning can be a powerful technique to improve model performance in fields like medicine, where LLMs may have poor out-of-the-box performance. The 2 common fine-tuning techniques are supervised fine-tuning (SFT) and direct preference optimization (DPO); however, little guidance is available for when to apply either method within clinical medicine or health care operations. Objective: This study aims to investigate the benefits of fine-tuning with SFT and DPO across a range of core natural language tasks in medicine to better inform clinical informaticists when either technique should be deployed. Methods: We use Llama3 8B (Meta) and Mistral 7B v2 (Mistral AI) to compare the performance of SFT alone and DPO across 4 common natural language tasks in medicine. The tasks we evaluate include text classification, clinical reasoning, text summarization, and clinical triage. Results: Our results found clinical reasoning accuracy increased from 7% to 22% with base Llama3 and Mistral2, respectively, to 28% and 33% with SFT, and then 36% and 40% with DPO (P=.003 and P=.004, respectively). Summarization quality, graded on a 5-point Likert scale, was 4.11 with base Llama3 and 3.93 with base Mistral2. Performance increased to 4.21 and 3.98 with SFT and then 4.34 and 4.08 with DPO (P<.001). F1-scores for provider triage were 0.55 for Llama3 and 0.49 for Mistral2, which increased to 0.58 and 0.52 with SFT and 0.74 and 0.66 with DPO (P<.001). F1-scores for urgency triage were 0.81 for Llama3 and 0.88 for Mistral2, which decreased with SFT to 0.79 and 0.87, and then experienced mixed results with DPO, achieving 0.91 and 0.85, respectively (P<.001 and P>.99, respectively). Finally, F1-scores for text classification were 0.63 for Llama3 and 0.73 for Mistral2, which increased to 0.98 and 0.97 with SFT, and then essentially did not change with DPO to 0.95 and 0.97, respectively (P=.55 and P>.99, respectively). DPO fine-tuning required approximately 2 to 3 times more compute resources than SFT alone. Conclusions: SFT alone is sufficient for simple tasks such as rule-based text classification, while DPO after SFT improves performance on the more complex tasks of triage, clinical reasoning, and summarization. We postulate that SFT alone is sufficient for simple tasks because SFT strengthens simple word-association reasoning, whereas DPO enables deeper comprehension because it is trained with both positive and negative examples, enabling the model to recognize more complex patterns. Ultimately, our results help inform clinical informaticists when to deploy either fine-tuning method and encourage commercial LLM providers to offer DPO fine-tuning for commonly used proprietary LLMs in medicine.
