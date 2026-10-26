---
title: "LLM-BASED SEMANTIC RESUME RANKING AND CANDIDATE RECOMMENDATION USING RETRIEVAL-AUGMENTED GENERATION"
authors: ""
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-10-27T06:01:41.883636"
doi: "https://doi.org/10.56726/irjmets103214"
openalex_id: "https://openalex.org/W7223553450"
source_api: "openalex"
---

# LLM-BASED SEMANTIC RESUME RANKING AND CANDIDATE RECOMMENDATION USING RETRIEVAL-AUGMENTED GENERATION

**著者**: 
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Shortlisting candidates for a vacancy means reading many profiles against one job description and deciding who is worth a recruiter's time.Keyword filters miss candidates who describe the same skill in different words, and a language model asked to rank profiles directly gives answers that cannot be checked and may describe experience a candidate never had.We describe a resume ranking and recommendation system that divides the work into three layers.A retrieval layer turns the job description and every candidate profile into vectors, using the Gemini text-embedding-004 model when an API key is available and a 500-term TF-IDF vectoriser otherwise, and compares them by cosine similarity.A scoring layer of fixed rules combines this similarity with a skill-match fraction, behavioural signals such as response rate and notice period, and practical fit such as salary and work mode, into one score with weights 0.45, 0.30 and 0.25, and writes a reason of at most 200 characters for every rank.A generation layer passes only the top retrieved profiles to Gemini 2.5 Flash, which returns structured recommendations and interview questions; when the model is unavailable a template produces the same structure from the retrieved data.The system is a React and Express web application evaluated on the 50candidate sample of a public recruiting-challenge dataset, which has no relevance labels.In the TF-IDF configuration, the three candidates whose job title matches a Senior AI/ML role are ranked first, second and third.An analysis of the score shows, however, that the behavioural component correlates more strongly with the final order (Spearman 0.79) than the semantic component (0.36), that the rankings for two different jobs share 8 of their top 10 candidates, and that 33 of 50 profiles carry no GitHub signal.Ranking 50 candidates takes about 3 seconds.The Gemini configuration was not evaluated, and these figures describe a prototype on a small sample, not hiring accuracy.
