# Claude Managed Agents

Claude Managed Agents is Anthropic's **beta** managed agent harness and execution infrastructure for long-running, asynchronous agent sessions. Anthropic operates agent session lifecycle, runtime environments, persisted artifacts and related orchestration facilities rather than requiring the application to implement the complete execution loop. [Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview).

## Product and lifecycle boundary

Managed Agents is distinct from Anthropic's direct Claude Messages API, the Claude model families, Claude Code, Agent SDK and self-hosted agent loops. Anthropic documents the `managed-agents-2026-04-01` beta access contract; integrations such as MCP tunnels, dreaming, memory or other optional features may have narrower availability. Do not treat a beta facility as a generally available production contract. [Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart).

## Persistence, data and authorization

Agent sessions can retain transcripts, environment state and files until deletion. Anthropic's Managed Agents documentation says this service is **not eligible for Zero Data Retention or HIPAA BAA coverage**; self-hosting a sandbox does not automatically alter that hosted control-plane policy. Verify active workspace eligibility, tool and permission configuration, credentials, MCP/network access, safety boundaries, data retention, billing, model availability and rate limits before supplying sensitive data.

## Relations

- Produced by [Anthropic](../../../../../producers/sub/a/sub/anthropic/).

## Official resources

- [Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview)
- [Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart)
