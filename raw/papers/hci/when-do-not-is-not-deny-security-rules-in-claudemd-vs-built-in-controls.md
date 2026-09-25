---
title: "When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls"
authors: "Ting Yan"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-08-25T18:31:28.306719"
arxiv_id: "http://arxiv.org/abs/2608.23550v1"
source_api: "arxiv"
categories: "cs.HC, cs.CR"
---

# When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls

**著者**: Ting Yan
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

In CLAUDE.md, "do not" is a natural-language instruction that the model interprets. Claude Code's deny is a built-in control that blocks an action before the agent can take it. Both can express the same security goal, but they control the agent in different ways. We measure this gap in 481 public CLAUDE.md files. An LLM matched the extracted candidate rules against Claude Code's documented controls, and two security practitioners independently checked a sample without seeing the model's answers or each other's labels. Depending on how closely a control had to match the written rule, only about 4-16% of the retrieved security rules had a matching built-in control. Under the strictest standard the estimate was 4.4% (95% CI: 2.6-6.7%), and the two annotators agreed closely on which rules had a match. A manual review of complete files found that our extraction method captured 66.3% of eligible security rules; the reported rates therefore apply to the rules it captured. This is a usable security problem: CLAUDE.md is a write-only channel. A developer writes a security rule but gets no feedback on whether a control will enforce it. The same plain-text form hides two kinds of rule: those a permission rule, mode, or sandbox can enforce, and those left to the model to interpret.
