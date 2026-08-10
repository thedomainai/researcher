---
title: "Gemini API Managed Agents: 3.6 Flash, hooks, and more"
author: "Google AI Blog"
url: "https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/"
published: "Tue, 28 Jul 2026 16:00:00 +0000"
fetched: "2026-07-29T06:03:48.700336"
source_type: "rss_article"
---

# Gemini API Managed Agents: 3.6 Flash, hooks, and more

Gemini API Managed Agents: 3.6 Flash, hooks, and more
[Managed Agents in Gemini API](https://ai.google.dev/gemini-api/docs/agents) are getting [environment hooks](https://ai.google.dev/gemini-api/docs/agent-hooks), [model selection](https://ai.google.dev/gemini-api/docs/antigravity-agent#model-selection), and [free tier access](https://ai.google.dev/gemini-api/docs/pricing#pricing-for-agents). These capabilities build on our previous release introducing [background tasks and remote MCP server integration](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/).
With managed agents in the [Gemini Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview), a single API call coordinates, reasoning, code execution, package installation, file management, and web retrieval inside an isolated cloud sandbox.
If you're using an AI coding assistant, drop this in your terminal to give it access to the Interactions API skill: npx skills add google-gemini/gemini-skills --skill gemini-interactions-api.
Below are examples using the @google/genai
TypeScript/JavaScript SDK. For Python or cURL, check out the [Antigravity agent documentation](https://ai.google.dev/gemini-api/docs/antigravity-agent).
npm install @google/genai
Gemini 3.6 Flash is now the default
The antigravity-preview-05-2026
agent now runs [Gemini 3.6 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) by default. No code changes are required. Your next interaction picks it up automatically.
You can also explicitly select models by passing agent_config.model
when creating an interaction or managed agent. Use Gemini 3.5 Flash-Lite for lower cost, or pin to your model of preference.
import { GoogleGenAI } from "@google/genai";
const client = new GoogleGenAI({});
const interaction = await client.interactions.create({
agent: "antigravity-preview-05-2026",
input: "Audit all dependencies in package.json, upgrade outdated packages, and verify the build by running npm test.",
environment: "remote",
agent_config: {
type: "antigravity",
model: "gemini-3.5-flash-lite",
},
});
console.log(interaction.output_text);
Supported models include:
- Gemini 3.6 Flash (
gemini-3.6-flash
, default): Balanced model for reasoning, coding, and tool use. - Gemini 3.5 Flash (
gemini-3.5-flash
): Previous generation for general agentic workflows. - Gemini 3.5 Flash-Lite (
gemini-3.5-flash-lite
): Lowest latency and cost on the Gemini 3.5 family.
Environment hooks: block, lint, and audit tool calls inside the sandbox
[Environment hooks](https://ai.google.dev/gemini-api/docs/agent-hooks) let you run your custom scripts before or after every tool call the agent makes inside its sandbox. Add a .agents/hooks.json
into your environment and the runtime executes your handlers on pre_tool_execution or post_tool_execution
events.
The matcher
field supports regular expressions, allowing you to target multiple tools with |
or catch everything with *
:
{
"security-gate": {
"pre_tool_execution": [
{
"matcher": "code_execution|write_file",
"hooks": [
{
"type": "command",
"command": "python3 /.agents/hooks-scripts/gate.py",
"timeout": 10
}
]
}
]
},
"auto-format": {
"post_tool_execution": [
{
"matcher": "*",
"hooks": [
{
"type": "command",
"command": "python3 /.agents/hooks-scripts/auto_lint.py",
"timeout": 15
}
]
}
]
}
}
In this configuration:
- The
security-gate
group runsgate.py
before everycode_execution
orwrite_file
call. If the script returns{"decision": "deny", "reason": "..."}
, the tool call is skipped and the rejection reason is passed into the model’s context. - The
auto-format
group runsauto_lint.py
after every tool finishes to enforce code styling. - Hooks also support
http
type handlers that POST directly to an external endpoint.
For complete HTTP hook definitions and failure handling semantics, refer to the [hooks documentation](https://ai.google.dev/gemini-api/docs/agent-hooks).
Teams are already using hooks to build production-grade validation pipelines. For example, AI-native investment bank Offdeal uses post_tool_execution
hooks to run automated image verification inside the remote sandbox.
"OffDeal is an AI-native investment bank, and Archie is the AI analyst our bankers use every day. A requirement for banker-ready decks is company logos: buyer tables, sponsor columns, tombstone grids, often 30+ logos in a single deck, every one of which must be the right company, the appropriate size and aspect ratio, contain the name, have a transparent background, and have a high contrast when placed on a white slide.
Before agent hooks, we couldn’t do this on Gemini’s managed agents: the sandbox is remote, so our validation code had nowhere to run. With hooks, a post_tool_execution hook triggers our pipeline inside the sandbox the moment Archie writes its company list, fetching candidates, enforcing pixel-level quality checks, verifying each logo with Gemini vision, and publishing a manifest of approved files that are the only images allowed into the deck."
- Alston Lin, Founder & CTO of OffDeal
Cost control and automation features
Free tier availability
Managed agents are now available on [free tier projects](https://ai.google.dev/gemini-api/docs/pricing#pricing-for-agents). Developers can experiment with agentic workflows using an [API key from a project without active billing](https://ai.google.dev/gemini-api/docs/api-key).
Budget controls
Because managed agents execute multi-turn autonomous loops, complex tasks can consume significant token budgets. To prevent runaway tasks, you can pass max_total_tokens
inside agent_config
to cap total consumption (input + output + thinking).
When the agent reaches the limit, execution safely pauses and the interaction returns status: "incomplete"
. The environment state is preserved, enabling you to [continue where it stopped](https://ai.google.dev/gemini-api/docs/antigravity-agent#continuing-incomplete-interaction) by passing previous_interaction_id
with a fresh budget.
const interaction = await client.interactions.create({
agent: "antigravity-preview-05-2026",
input: "Audit all modules in this repo and generate a migration report.",
agent_config: {
type: "antigravity",
max_total_tokens: 10000,
},
environment: "remote",
});
Scheduled execution with triggers
Automate recurring agent tasks with [scheduled triggers](https://ai.google.dev/gemini-api/docs/antigravity-agent#triggers). A trigger binds an agent, environment, prompt, and cron schedule into a persistent resource that fires without manual intervention. Each run reuses the same sandbox, so files persist across executions.
Environments API
The [Environments API](https://ai.google.dev/gemini-api/docs/agent-environment#environments-api) lets you list, inspect, and delete sandbox sessions from code. Recover environment IDs after a disconnect, or clean up sandboxes when your pipeline finishes instead of waiting for the 7-day TTL.
Get started with managed agents
These updates turn managed agents into cost-controlled, scheduled workers that operate autonomously inside real development environments without breaking your budget or requiring external orchestration.
Check out the [Gemini Interactions API overview](https://ai.google.dev/gemini-api/docs/interactions-overview) and the [managed agents quickstart](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart) to explore custom agent definitions, environment configurations, network rules, and advanced streaming patterns.
