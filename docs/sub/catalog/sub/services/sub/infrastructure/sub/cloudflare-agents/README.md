# Cloudflare Agents

Cloudflare Agents is Cloudflare's hosted durable-agent runtime and platform built around the Agents SDK, Durable Objects, managed state, real-time connections, scheduling, recovery, and globally managed execution.

## Service boundary

The hosted runtime is the primary identity even though Cloudflare also exposes an SDK and users may supply their own agent harness logic. Workers AI, AI Gateway, Vectorize, AI Search, Browser, Sandbox, MCP and payment tools, communication channels, and individual agents remain separate products or integrations where independently durable.

Runtime limits, channels, tool integrations, SDK APIs, storage semantics, pricing, deployment constraints, and feature lifecycle are freshness-sensitive.

## Relations

- Produced by [Cloudflare](../../../../../producers/sub/c/sub/cloudflare/).

## Official resources

- [Cloudflare Agents documentation](https://developers.cloudflare.com/agents/)
- [Cloudflare Agents platform](https://developers.cloudflare.com/agents/platform/)
