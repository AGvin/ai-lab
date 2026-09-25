# Documentation Requirements

## Requirements

- Present Perplexity Agent API as Perplexity AI's released multi-provider hosted API for brokering LLM requests across multiple model providers while adding Perplexity-managed web/finance search, tool configuration, reasoning controls, and a unified interoperable request surface.
- Preserve its primary gateway/broker identity: it can route to third-party models and expose Perplexity tools through one API/key, rather than owning those third-party trained-model identities.
- Keep Perplexity Search API as the raw web-data service, Embeddings API as hosted embedding-model access, Router API as a separate current private-preview surface, and legacy Sonar API as historical/deprecation context.
- Keep official SDKs, OpenAI compatibility, MCP integration, connectors, presets, individual tools, and playground interfaces as access/integration surfaces rather than peer service identities.
- Treat supported providers/models, tools, presets, pricing, endpoint aliases, storage/background behavior, connectors, quotas, limits, and compatibility behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Agent API remains a producer-hosted gateway/broker service rather than a model family or self-managed framework.
- Third-party model provenance is not reassigned to Perplexity.
- Producer provenance resolves bidirectionally to Perplexity AI.
