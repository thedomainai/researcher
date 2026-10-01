---
title: "A comparative study of pretrained language models for long clinical text"
authors: ["Yikuan Li", "Ramsey M. Wehbe", "Faraz S. Ahmad", "Hanyin Wang", "Yuan Luo"]
year: 2022
cited_by_count: 148
doi: "https://doi.org/10.1093/jamia/ocac225"
openalex_id: W4310568840
paper_type: article
evidence_kind: article
topics: ["applications"]
landmark: false
abstract_source: "openalex"
---

# A comparative study of pretrained language models for long clinical text

**Authors**: Yikuan Li, Ramsey M. Wehbe, Faraz S. Ahmad, Hanyin Wang, Yuan Luo | **Year**: 2022 | **Cited by**: 148 | **Kind**: article | **Relevance**: applications: supporting

## Abstract

OBJECTIVE: Clinical knowledge-enriched transformer models (eg, ClinicalBERT) have state-of-the-art results on clinical natural language processing (NLP) tasks. One of the core limitations of these transformer models is the substantial memory consumption due to their full self-attention mechanism, which leads to the performance degradation in long clinical texts. To overcome this, we propose to leverage long-sequence transformer models (eg, Longformer and BigBird), which extend the maximum input sequence length from 512 to 4096, to enhance the ability to model long-term dependencies in long clinical texts. MATERIALS AND METHODS: Inspired by the success of long-sequence transformer models and the fact that clinical notes are mostly long, we introduce 2 domain-enriched language models, Clinical-Longformer and Clinical-BigBird, which are pretrained on a large-scale clinical corpus. We evaluate both language models using 10 baseline tasks including named entity recognition, question answering, natural language inference, and document classification tasks. RESULTS: The results demonstrate that Clinical-Longformer and Clinical-BigBird consistently and significantly outperform ClinicalBERT and other short-sequence transformers in all 10 downstream tasks and achieve new state-of-the-art results. DISCUSSION: Our pretrained language models provide the bedrock for clinical NLP using long texts. We have made our source code available at https://github.com/luoyuanlab/Clinical-Longformer, and the pretrained models available for public download at: https://huggingface.co/yikuan8/Clinical-Longformer. CONCLUSION: This study demonstrates that clinical knowledge-enriched long-sequence transformers are able to learn long-term dependencies in long clinical text. Our methods can also inspire the development of other domain-enriched long-sequence transformers.
