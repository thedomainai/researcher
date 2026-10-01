---
title: "Retrieval-Augmented Generation–Enabled GPT-4 for Clinical Trial Screening"
authors: ["Ozan Ünlü", "Jiyeon Shin", "Charlotte J. Mailly", "Michael Oates", "Michela R. Tucci", "Matthew Varugheese", "Kavishwar B. Wagholikar", "Fei Wang", "et al."]
year: 2024
cited_by_count: 78
doi: "https://doi.org/10.1056/aioa2400181"
openalex_id: W4399738410
paper_type: article
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# Retrieval-Augmented Generation–Enabled GPT-4 for Clinical Trial Screening

**Authors**: Ozan Ünlü, Jiyeon Shin, Charlotte J. Mailly, Michael Oates, Michela R. Tucci, Matthew Varugheese, Kavishwar B. Wagholikar, Fei Wang, et al. | **Year**: 2024 | **Cited by**: 78 | **Kind**: article | **Relevance**: applications: core

## Abstract

BackgroundScreening participants in clinical trials is an error-prone and labor-intensive process that requires significant time and resources. Large language models such as generative pretrained transformer 4 (GPT-4) present an opportunity to enhance the screening process with advanced natural language processing. This study evaluates the utility of a Retrieval-Augmented Generation (RAG)–enabled GPT-4 system to improve the accuracy, efficiency, and reliability of screening for a trial involving patients with symptomatic heart failure.MethodsThe ongoing Co-Operative Program for Implementation of Optimal Therapy in Heart Failure (COPILOT-HF; ClinicalTrials.gov number, NCT05734690) trial identifies potential participants through electronic health record (EHR) queries followed by manual reviews by trained but nonlicensed study staff. To determine patient eligibility for the COPILOT-HF study that is not identifiable by structured EHR queries, we developed RAG-Enabled Clinical Trial Infrastructure for Inclusion Exclusion Review (RECTIFIER), a clinical note–based, question-answering system powered by RAG and GPT-4. We used clinical notes on 100, 282, and 1894 patients for development, validation, and test datasets, respectively. An expert clinician conducted a blinded review to establish "gold standard" answers to 13 target criteria questions. We calculated performance metrics (sensitivity, specificity, accuracy, and Matthews correlation coefficient [MCC]) in determining patient eligibility for each target criterion and for each of four screening methods (study staff, RECTIFIER with a single-question strategy, RECTIFIER with a combined-question strategy, and RECTIFIER with GPT-3.5 instead of GPT-4).ResultsThe RECTIFIER and COPILOT-HF study staff's answers closely aligned with the expert clinicians' answers across the target criteria, with accuracy ranging between 97.9% and 100% (MCC, 0.837 and 1) for RECTIFIER and between 91.7% and 100% (MCC, 0.644 and 1) for the study staff. RECTIFIER performed better than the study staff in determining symptomatic heart failure, with an accuracy of 97.9% versus 91.7% and an MCC of 0.924 versus 0.721, respectively. Overall, the sensitivity and specificity for determining patient eligibility with RECTIFIER were 92.3% and 93.9%, respectively, and 90.1% and 83.6% with the study staff. With RECTIFIER, the single-question approach to determining eligibility resulted in an average cost of 11 cents per patient, and the combined-question approach resulted in an average cost of 2 cents per patient.ConclusionsLarge language model–based solutions such as RECTIFIER can significantly enhance clinical trial screening performance and reduce costs by automating the screening process. However, integrating such technologies requires careful consideration of potential hazards and should include safeguards such as final clinician review. (Funded by the Accelerator for Clinical Transformation [ACT]; ClinicalTrials.gov number, NCT05734690.)
