---
title: "Neural Machine Translation of Rare Words with Subword Units"
authors: ["Rico Sennrich", "Barry Haddow", "Alexandra Birch"]
year: 2016
cited_by_count: 515
doi: "https://doi.org/10.18653/v1/p16-1162"
openalex_id: W1816313093
paper_type: conference-paper
evidence_kind: article
topics: ["foundations"]
landmark: true
abstract_source: "openalex"
---

# Neural Machine Translation of Rare Words with Subword Units

**Authors**: Rico Sennrich, Barry Haddow, Alexandra Birch | **Year**: 2016 | **Cited by**: 515 | **Kind**: article | **Relevance**: foundations: core

## Abstract

Neural machine translation (NMT) models typically operate with a fixed vocabulary, but translation is an open-vocabulary problem.Previous work addresses the translation of out-of-vocabulary words by backing off to a dictionary.In this paper, we introduce a simpler and more effective approach, making the NMT model capable of open-vocabulary translation by encoding rare and unknown words as sequences of subword units.This is based on the intuition that various word classes are translatable via smaller units than words, for instance names (via character copying or transliteration), compounds (via compositional translation), and cognates and loanwords (via phonological and morphological transformations).We discuss the suitability of different word segmentation techniques, including simple character ngram models and a segmentation based on the byte pair encoding compression algorithm, and empirically show that subword models improve over a back-off dictionary baseline for the WMT 15 translation tasks English→German and English→Russian by up to 1.1 and 1.3 BLEU, respectively.
