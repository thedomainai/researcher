# researcher

- Use `planner` for multi-step work, `researcher` for read-only exploration, `implementer` for changes, and `verifier` before finishing.
- Treat `config/` and `tools/` as the execution core, `raw/` as source materials, and `wiki/` as compiled output.
- Prefer append-only updates to indexes and logs over destructive rewrites.
- Do not edit `logs/`, `output/`, or bulk `raw/` / `wiki/` content unless the task explicitly requires it.
- Before changes to `config/`, `tools/`, or wiki compilation behavior, create `.claude/state/verification-required` and run `tools/claude/verify/verify_pipeline.sh`.
