---
title: "Event-Time Confounding Under Bursty Human Dynamics"
authors: "Michael Iannelli, Alan Ai"
year: 2026
citations: 0
paper_type: "primary"
domain: "behavioral_economics"
fetched: "2026-08-28T09:11:42.057582"
doi: ""
openalex_id: "https://openalex.org/W7204216667"
source_api: "openalex"
---

# Event-Time Confounding Under Bursty Human Dynamics

**著者**: Michael Iannelli, Alan Ai
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: 行動経済学

## Abstract

Studies of digital behavior often align users at moments they choose, such as opening an AI assistant, clicking a recommendation, or visiting a product page, and interpret higher activity afterward as an event effect. We show how this creates an endogenous time zero: the event occurs during an ongoing task episode, so the aligned curve can trace episode continuation rather than a response to the event. In same-user, cross-surface web logs, AI, shopping, news, coding, and reference events are all preceded by broad activity increases that peak before time zero. Our strongest test uses known-null timestamps that cause nothing. Among the 5.8% of AI responses meeting strict pre-event activity and washout criteria, these timestamps show 3.42 times the post-event search activity of a within-user placebo, compared with 4.32 times for real events. The fraction of excess reproduced by the known null falls from 0.56 at detectably active moments to -0.04 at quiet moments, where the design detects none. We formalize this episode-selection bias, prove that a single-surface event window cannot separate it from a genuine effect without additional assumptions, and show in zero-effect simulations why user fixed effects and coarse activity matching can fail: the confound is within-user and time-varying. We provide a diagnostic protocol, public-data benchmarks, and burstcheck, a lightweight audit tool. User-timed events may have real effects, but post-event volume does not identify them by default; studies should compare similar episodes with and without the event.
