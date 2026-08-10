---
title: "Human–AI Coevolution Dynamics dataset"
authors: "Jie Zhou"
year: 2026
citations: 0
paper_type: "primary"
domain: "evolutionary_biology"
fetched: "2026-06-26T06:01:19.788836"
doi: "https://doi.org/10.57760/sciencedb.40413"
openalex_id: "https://openalex.org/W7165127780"
source_api: "openalex"
---

# Human–AI Coevolution Dynamics dataset

**著者**: Jie Zhou
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 進化生物学・文化進化

## Abstract

Dataset and Social Cognitive AnnotationTo empirically evaluate the theoretical predictions of HACD-H, we construct a socially enriched conversational benchmark based on the Chinese long-term dialogue dataset DuLeMon (Xu et al., 2022). DuLeMon was originally developed for long-range open-domain dialogue modeling and contains multi-turn conversations with rich contextual dependencies and extended interaction structures, making it particularly suitable for studying long-term human–AI social dynamics.From the original corpus, 2,400 multi-turn dialogues were randomly sampled and further processed through a multi-dimensional social cognitive annotation pipeline. The resulting dataset contains approximately 14,700 interaction turns and provides substantially richer social information than conventional dialogue corpora.The annotation framework was designed to operationalize the core constructs of HACD-H. Rather than treating dialogue as a sequence of isolated utterances, each interaction turn is represented as a social cognitive state composed of emotional, relational, memory-related, and personality-related variables.Emotional states were annotated using the Expansion Quantization Network (EQN) framework (Zhou et al., 2025), which represents emotions as continuous affective distributions. Personality characteristics were derived from the H3P personality modeling framework (Zhou et al., 2025), producing MBTI-oriented personality distributions. Relational and conversational variables were automatically inferred using the Chinese semantic encoder BGE-Large-ZH-v1.5 and Qwen2.5-7B, allowing the extraction of interpersonal attributes such as trust, intimacy, engagement, politeness, humor, warmth, and supportiveness.All variables were normalized into bounded continuous ranges to ensure numerical stability and comparability across analyses.Table 1 summarizes the major categories of social cognitive variables included in the dataset.Table 1. Categories of social cognitive variables included in the socially annotated interaction dataset. Category Representative Variables HACD-H Construct Emotion angry, fear, happy, neutral, sad, surprise Emotional Dynamics Personality MBTI distributions, latent personality vectors Personality State Relationship trust, intimacy, familiarity, affection, engagement Relational Dynamics Style politeness, warmth, humor, formality, verbosity Social Behavior Interaction Dynamics emotion_shift, emotion_delta_magnitude State Transition Memory memory_decay_score Social Memory Events event_type, event_importance Environmental Context Growth Variables personality_growth, attachment_growth Coevolution Indicators Latent Representation latent personality embeddings State-Space Encoding The resulting dataset transforms conversational interaction into a collection of socially evolving trajectories and provides a suitable empirical foundation for testing the theoretical predictions of HACD-H.
