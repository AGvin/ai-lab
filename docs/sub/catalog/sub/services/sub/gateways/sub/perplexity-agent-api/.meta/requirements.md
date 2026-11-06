# Documentation Requirements

## Requirements

- Present Perplexity Agent API as Perplexity AI's released multi-provider hosted API for brokering LLM requests across multiple model providers while adding Perplexity-managed web/finance search, tool configuration, reasoning controls, and a unified interoperable request surface.
- Preserve its primary gateway/broker identity: it can route to third-party models and expose Perplexity tools through one API/key, rather than owning those third-party trained-model identities.
- Keep Perplexity Search API as the raw web-data service, Embeddings API as hosted embedding-model access, other orchestration APIs as separate source-defined services, and legacy Sonar API as historical/deprecation context.
- Keep official SDKs, OpenAI compatibility, MCP integration, connectors, presets, individual tools, and playground interfaces as access/integration surfaces rather than peer service identities.
- Treat supported providers/models, tools, presets, pricing, endpoint aliases, storage/background behavior, connectors, quotas, limits, and compatibility behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Agent API remains a producer-hosted gateway/broker service rather than a model family or self-managed framework.
- Third-party model provenance is not reassigned to Perplexity.
- Producer provenance resolves bidirectionally to Perplexity AI.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: Perplexity Agent API is a hosted gateway for multiple model providers with configurable tools and reasoning. The current request endpoint is /v1/agent; /v1/responses is a documented compatibility alias.
- Decision and deployment boundary: Web search must be explicitly enabled with an appropriate tool or preset; a plain model request does not provide citations. Configure model, tool and spending scope, and evaluate each provider's data terms. Zero data retention requires an eligible configured account and agreement; it is not the default.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://docs.perplexity.ai/docs/agent-api/quickstart>, <https://docs.perplexity.ai/docs/resources/privacy-security>.
