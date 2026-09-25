---
title: "Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach?"
authors: "Ting Yan"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-08-29T06:02:50.450696"
arxiv_id: "http://arxiv.org/abs/2608.27443v1"
source_api: "arxiv"
categories: "cs.HC, cs.CR"
---

# Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach?

**著者**: Ting Yan
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

AI agents are poised to become a primary interface to digital products, acting across email, files, payments, and personal data. People without professional software backgrounds need understandable, reusable ways to control actions across services. We examine a mechanism in which a language model maps actions to plain-language consequence categories with user-authored "allow", "ask", or "never" rules. We ask what is gained and lost when decisions are made in advance as reusable rules rather than separately for each action.
  We analyzed 113 participants without professional software backgrounds across three conditions: per-action human-in-the-loop approval (HITL), automated per-action model review (AUTO), or user-authored consequence policy (POLICY). Participants judged 2 examples in each of 4 consequence categories; POLICY participants then set one rule per category. All supervised an 18-action simulated day, including 7 overreach actions. POLICY blocked less overreach than HITL (-20.1 percentage points, 95% CI [-32.1, -8.1]) and AUTO (-14.5 points, 95% CI [-25.8, -3.2]). POLICY lowered runtime prompts from 18.0 to 10.9, but total intervention time was not reliably lower when rule setup was included.
  Exploratory analysis showed that participants chose "ask" for 114 of 140 POLICY rules, returning most overreach actions to runtime. Of the 148 overreach actions executed in POLICY, 133 followed human approval and 15 ran automatically under "allow" rules. Across all 7 overreach actions, POLICY had the highest approval rate. Counterintuitively, user-authored rules did not by themselves provide stronger protection: many actions outside users' original requests went through after users approved them. These results reveal a gap between preference and commitment: repeatedly choosing "ask" preserves case-by-case choice but prevents a standing policy from settling decisions in advance.
