# OGX

OGX, formerly Llama Stack, is a self-hostable model-agnostic AI API server and provider gateway with a server-side agentic/Responses execution loop.

## Role and product boundaries

The project offers pluggable model-inference adapters, OpenAI-compatible chat/embeddings/responses APIs, other provider-facing compatibility surfaces, MCP tools, vector stores and file-search integrations. The 2026 rename replaced old package, CLI and environment-variable namespaces; historical Llama Stack releases are not a second current product. OGX is broader than an inference-only proxy but distinct from model-serving engines and the OpenAI Agents SDK.

## Release and safe operation

The canonical profile records MIT-licensed OGX v1.5.0 (2026-10-09), Python 3.12+, and an unreleased 1.5.1.dev0 source version. Current v1.5.0 includes configuration/API compatibility changes; pin provider adapters, FastAPI dependencies, MCP capabilities and storage. Tools, documents, API secrets and model prompts cross trust boundaries; require authentication, isolation, egress controls, least privilege and request/token budgets.

## Relations

- Produced by: [OGX Contributors](../../../../../../../producers/sub/o/sub/ogx-contributors/)

## Official resources

- [Repository](https://github.com/ogx-ai/ogx)
- [Documentation](https://ogx-ai.github.io/docs)
- [Rename announcement](https://ogx-ai.github.io/blog/from-llama-stack-to-ogx)
