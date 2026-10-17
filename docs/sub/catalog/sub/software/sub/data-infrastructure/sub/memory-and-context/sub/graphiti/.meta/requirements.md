# Documentation Requirements

## Requirements

- Present Graphiti as Zep's open-source framework for temporal knowledge graphs and reusable context for AI agents.
- Keep Graphiti distinct from the producer-operated Zep service; self-hosting and framework operation belong to this software identity.
- Distinguish graph deployment from LLM and embedding processing: current defaults use OpenAI, while alternative hosted or local providers are configurable; self-hosting the graph does not make those model operations local.
- Treat supported graph backends, embedding/LLM providers, package versions, retrieval APIs, and deployment dependencies as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Graphiti remains memory/context infrastructure rather than a full agent framework or managed service.
- Producer provenance resolves to Zep.
