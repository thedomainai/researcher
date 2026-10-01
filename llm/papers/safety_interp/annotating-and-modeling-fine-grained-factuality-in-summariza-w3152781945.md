---
title: "Annotating and Modeling Fine-grained Factuality in Summarization"
authors: ["Tanya M. Goyal", "Greg Durrett"]
year: 2021
cited_by_count: 98
doi: "https://doi.org/10.18653/v1/2021.naacl-main.114"
openalex_id: W3152781945
paper_type: conference-paper
evidence_kind: article
topics: ["safety_interp"]
landmark: false
abstract_source: "openalex"
---

# Annotating and Modeling Fine-grained Factuality in Summarization

**Authors**: Tanya M. Goyal, Greg Durrett | **Year**: 2021 | **Cited by**: 98 | **Kind**: article | **Relevance**: safety_interp: supporting

## Abstract

Recent pre-trained abstractive summarization systems have started to achieve credible performance, but a major barrier to their use in practice is their propensity to output summaries that are not faithful to the input and that contain factual errors.While a number of annotated datasets and statistical models for assessing factuality have been explored, there is no clear picture of what errors are most important to target or where current techniques are succeeding and failing.We explore both synthetic and human-labeled data sources for training models to identify factual errors in summarization, and study factuality at the word-, dependency-, and sentence-level.Our observations are threefold.First, exhibited factual errors differ significantly across datasets, and commonly-used training sets of simple synthetic errors do not reflect errors made on abstractive datasets like XSUM.Second, human-labeled data with fine-grained annotations provides a more effective training signal than sentence-level annotations or synthetic data.Finally, we show that our best factuality detection model enables training of more factual XSUM summarization models by allowing us to identify non-factual tokens in the training data. 1Reference Summary: An early-medieval gold pendant created from an imitation of a Byzantine coin that was found in a Norfolk field is a "rare find", a museum expert has said. Source Article Fragment:Discovered on land at North Elmham, near Dereham, the circa 600 AD coin was created by French rulers of the time to increase their available currency.[…] The pendant was declared treasure by the Norfolk coroner on Wednesday.An 18th century coin believed to be worth more than #1m has been discovered.A gold pendant created from a necklace was found in a field Entitycentric (Ent-C)The pendant was declared a treasure by the Norfolk coroner on Wednesday.The pendant was declared a treasure by the Ohio coroner on March.
