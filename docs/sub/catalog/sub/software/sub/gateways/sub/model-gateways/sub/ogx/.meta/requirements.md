# Documentation Requirements

## Requirements

- Identify OGX as the maintained open-source, self-hostable, model-agnostic agentic API server and provider gateway from `ogx-ai/ogx`, **formerly Llama Stack**. The [2026-04-28](https://ogx-ai.github.io/blog/from-llama-stack-to-ogx) first-party rename also changed package, CLI and environment variable namespaces; do not create a separate current Llama Stack canonical product or attribute present maintainership solely to Meta.
- Preserve non-prerelease **OGX v1.5.0 (2026-10-09)**; current source `pyproject.toml` contains an unreleased fallback `1.5.1.dev0`, not a published v1.5.1. The package is `ogx`, requires **Python >=3.12**, and is **MIT** licensed by OGX Contributors.
- Categorize it under self-managed model/AI gateways for its pluggable inference providers and compatible API server with a **server-side Responses/agentic execution loop**. Document OpenAI-compatible chat/embeddings/responses, Anthropic message and Google interaction compatibility, MCP tool integration, vector stores/file search and optional storage/providers as separate capabilities of one software identity.
- Distinguish OGX's server-side Responses/agentic execution loop from model-provider routing alone while preserving each compared product's documented scope, including TensorZero's observability, evaluation, experimentation and optimization capabilities. Keep model-hosting engines (vLLM/Ollama), the independently installable OpenAI Agents SDK and remotely managed provider services as separate identities. Provider adapters, old Llama Stack SDKs, CLI scripts, Open Responses interfaces and historical PyPI names must not become duplicate OGX products.
- **Lifecycle and compatibility:** current v1.5.0 release notes include breaking choices for explicit `apis:` lists and minimum FastAPI version, plus MCP 2.x client support. Pin server/SDK/provider configuration, legacy API compatibility and storage assumptions; do not assert feature parity for every front-end SDK or all inference backends.
- **Security/operations:** tool execution, RAG documents, user files, search integrations, API secrets and model prompts cross trust boundaries. Require explicit authentication, deployment isolation, network/egress policy, connector privileges, per-provider cost limits and safe logging before exposing a public OpenAI-compatible endpoint.
- Attribute software `produced-by` to `catalog/producers/o/ogx-contributors` with exact reciprocal `produces`, preserving the first-party OGX community identity rather than inventing a duplicate Meta parent after the rename.

## Validation

- Official `ogx-ai/ogx` README, [rename announcement](https://ogx-ai.github.io/blog/from-llama-stack-to-ogx), v1.5.0 release, pyproject manifest and MIT LICENSE substantiate current identity, version, licensing, runtime floor and server/API scope.
- Exact reciprocal software/producer IDs resolve; no second active Llama Stack software record is introduced.
