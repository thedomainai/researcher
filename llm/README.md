# llm/ — LLM literature corpus (manual, one-shot)

A reference corpus for becoming an LLM expert. It is independent of `raw/` and `wiki/`: it is not part of the daily pipeline, Tier classification, or `compile_wiki`, and no launchd job touches it.

Intended readers, in priority order: LLM researchers, then implementers, then people who introduce or evaluate LLMs in an organization.

## Topics (8)

| topic | scope |
|---|---|
| `foundations` | architectures, pretraining, scaling laws, long context, inference efficiency, model reports, pre-LLM prerequisites (RNN LM, LSTM, word2vec, Adam, ...) |
| `post_training` | instruction tuning, RLHF/DPO, reasoning models and RLVR, test-time compute, LoRA, model merging |
| `elicitation` | prompting, chain-of-thought, in-context learning (practice), RAG, tool use as a technique, structured output, multimodal |
| `evaluation` | benchmarks, LLM-as-a-judge, contamination, statistical validity, calibration |
| `safety_interp` | hallucination, alignment, jailbreaks and injection, mechanistic interpretability, privacy, bias |
| `theory_cognition` | in-context learning theory, expressivity limits, world models, comparison with human cognition, LLM-based simulation of people |
| `applications` | software engineering, science, medicine/law/finance, productivity and labor evidence, LLMOps |
| `agents` | agent design, planning, memory, computer use, multi-agent, self-improvement, agent benchmarks, agent safety |

A paper can belong to several topics (`topics` in `index.jsonl`); its file lives under the first one.

## How it was built

`tools/fetch_llm.py` reuses `tools/fetch_reference.py` (same OpenAlex + gate design as `reference/`) with topic definitions in `tools/llm_topics.py`.

1. **Named landmarks**: about 190 titles per the topic files, verified by title overlap (0.75). Titles not found are listed in `missing_landmarks.jsonl`.
2. **Citation-network expansion**: references of survey seeds, citing papers of core seeds, related works.
3. **Keyword search**: relevance-ordered and citation-ordered passes.
4. **Recent emphasis** (`recent_queries`): publication year >= 2024 (`RECENT_FROM_YEAR`), citations >= 5, relevance- and citation-ordered. About 63% of the corpus is from 2024 onward.
5. **Relevance gate**: judged in a Claude Code session (no pay-as-you-go API) and imported with `--apply-judgments`. `off_topic` is not saved and is recorded in `excluded.jsonl`.
6. **Cross-topic rescue**: a paper judged only against the topic it was retrieved under can be wrongly dropped (for example a prompting paper retrieved by an agents query). Papers rejected in every topic but about LLMs were re-judged against all 8 topics. A rescued verdict carries `to` (the topic it belongs to), kept if `core`, or `supporting` with at least 100 citations.

## Files

- `index.jsonl` — one paper per line; same fields as `reference/index.jsonl` (`openalex_id`, `title`, `year`, `cited_by_count`, `abstract`, `topics`, `channels`, `relevance`, `landmark`, `file`, ...)
- `papers/<topic>/<slug>-<openalex_id>.md` — frontmatter plus abstract
- `excluded.jsonl` — papers rejected by the gate, with reasons (audit)
- `missing_landmarks.jsonl` — named landmarks not found in OpenAlex (mostly arXiv-only preprints)
- `arxiv_landmarks.jsonl` — the supplement for those (Semantic Scholar / arXiv results, including not-found ones). `fetch_llm.py` merges it back into `index.jsonl` after every run, so a full rebuild does not lose it
- `reading_list.md` — landmark `core` papers ordered by citations (`python3 tools/llm_reading_list.py`); tick the boxes as you read
- `.cache/` — API responses and gate verdicts (git-ignored). Reruns spend no OpenAlex credits.

## Known limits

- OpenAlex has some records whose title and abstract disagree (for example Longformer, W3015468748). Check the `abstract` before relying on it.
- 25 of the 27 landmarks missing from OpenAlex (ReAct, Constitutional AI, SWE-bench, DeepSeek-R1, ...) were added from Semantic Scholar / arXiv (`tools/llm_arxiv_landmarks.py`). Their ID is `arxiv-<id>` or `s2-<id>`, and their citation counts come from Semantic Scholar, so they are only comparable to OpenAlex counts roughly. Three have no abstract. Two are not found anywhere: the Transformer Circuits framework and Towards Monosemanticity (blog posts, not papers).
- Short landmark titles can match a longer unrelated title. The matcher requires overlap in both directions; check the title if a supplemented entry looks wrong.
- Gate verdicts were made by model judges from title and a 450-character abstract; counts reported by judges were hand-tallied and are not used. The merged file was verified mechanically for missing/duplicate ids.
- `ExplorationBench` (arXiv 2609.30199) is not included.

## Usage

Rebuild from cache with zero OpenAlex credits:

```bash
python3 tools/fetch_llm.py --no-gate --cached-only
```

Add or refresh one topic (spends credits; run `--dry-run` first):

```bash
python3 tools/fetch_llm.py --topic agents --dump-candidates
python3 tools/fetch_llm.py --apply-judgments <judgments.jsonl>
python3 tools/fetch_llm.py --topic agents --no-gate
```

Judgment lines are `{"topic": ..., "id": ..., "verdict": "core|supporting|off_topic", "reason": ..., "to": <optional topic>}`.

Search the core papers of one topic, most cited first:

```bash
python3 -c 'import json; E=[json.loads(l) for l in open("llm/index.jsonl")]; [print(e["year"], e["cited_by_count"], e["title"], "->", e["file"]) for e in sorted(E, key=lambda x:-x["cited_by_count"]) if "agents" in e["topics"] and e["relevance"]["agents"]["verdict"]=="core"]'
```
