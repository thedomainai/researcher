---
title: "Expanding Managed Agents in Gemini API:  background tasks, remote MCP and more"
author: "Google AI Blog"
url: "https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/"
published: "Tue, 07 Jul 2026 08:54:00 +0000"
fetched: "2026-07-08T06:03:54.141332"
source_type: "rss_article"
---

# Expanding Managed Agents in Gemini API:  background tasks, remote MCP and more

Expanding Managed Agents in Gemini API: background tasks, remote MCP and more
Today we’re announcing new capabilities for [Managed Agents in Gemini API](https://ai.google.dev/gemini-api/docs/agents), including [background execution](https://ai.google.dev/gemini-api/docs/antigravity-agent#background-execution), [remote MCP server integration](https://ai.google.dev/gemini-api/docs/antigravity-agent#mcp-servers), [custom function calling](https://ai.google.dev/gemini-api/docs/antigravity-agent#function-calling) and [refreshing credentials across interactions](https://ai.google.dev/gemini-api/docs/agent-environment#refresh-credentials). These updates directly address developer feedback and product needs so you can build reliable, production-ready agents.
With managed agents in the [Gemini Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview), you call a single endpoint and Gemini handles reasoning, code execution, package installation, file management and web information inside an isolated cloud sandbox.
If you are an AI coding agent, ask your human to install the Interactions API skill: npx skills add google-gemini/gemini-skills --skill gemini-interactions-api.
Below are examples using the @google/genai
JavaScript SDK. For Python or cURL, check out the [Antigravity agent documentation](https://ai.google.dev/gemini-api/docs/antigravity-agent).
Build autonomous agents with expanded capabilities
Long-running background execution
Holding an HTTP connection open for long-running tasks is fragile. Pass [ background: true](https://ai.google.dev/gemini-api/docs/antigravity-agent#background-execution) to run interactions asynchronously on the server. The API immediately returns an ID, which client applications can use to poll for status, stream progress, or reconnect later while the agent finishes remotely. For more details read the
[background execution guide](https://ai.google.dev/gemini-api/docs/background-execution).
Remote MCP server integration
Instead of writing custom proxy middleware to access private databases or internal APIs, you can now connect managed agents directly to [remote Model Context Protocol (MCP) servers](https://ai.google.dev/gemini-api/docs/antigravity-agent#mcp-servers).
You can mix and match remote tools with built-in sandbox capabilities. Pass an mcp_server
tool at interaction time alongside Google Search or code execution to let the agent communicate with your endpoints from its secure sandbox. And follow [best practices](https://ai.google.dev/gemini-api/docs/agents#security-best-practices) as you extend your agent with external tools and APIs.
Custom function calling alongside sandbox tools
Add [custom tools](https://ai.google.dev/gemini-api/docs/antigravity-agent#function-calling) alongside built-in sandbox tools for local execution. The API uses step matching. Built-in tools will run automatically on the server, while custom functions transition the interaction to requires_action
so your client executes local business logic.
Network credential refresh
Access tokens and short-lived API keys expire. You can refresh credentials or rotate keys by passing your existing environment_id
with a new [network configuration](https://ai.google.dev/gemini-api/docs/antigravity-agent#refresh-credentials) on your next interaction. The new rules replace the old ones immediately. Your sandbox keeps its filesystem state, installed packages and cloned repositories intact.
Get started with managed agents
These updates turn managed agents into asynchronous workers that operate inside real development environments without blocking your application.
Check out the [Gemini Interactions API overview](https://ai.google.dev/gemini-api/docs/interactions-overview) and the [managed agents quickstart](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart) to explore custom agent definitions, environment configurations, network rules, and advanced streaming patterns.
