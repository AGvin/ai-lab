# Documentation Requirements

## Requirements

- Identify Microsoft.Extensions.AI as Microsoft's .NET libraries for common generative-AI abstractions and composable middleware used by applications and libraries.
- Preserve `IChatClient` and `IEmbeddingGenerator` as core abstraction examples, together with middleware-oriented capabilities such as automatic tool invocation, telemetry, and caching.
- Preserve its interoperability/abstraction-layer role rather than presenting it as a complete agent framework, application host, or model provider.
- Keep package versions, supported provider implementations, preview/stability state, and other mutable .NET ecosystem facts source-backed when expanded.
- Link the canonical Microsoft producer profile and the Microsoft Agent Framework profile as an adjacent higher-level agent-framework boundary without claiming identity equivalence.
- Include current official Microsoft Learn documentation.

## Validation

- The profile does not conflate Microsoft.Extensions.AI with Microsoft Agent Framework, Semantic Kernel, or any specific model-provider SDK.
- Common abstractions are not described as guaranteeing identical provider capabilities.
- The Microsoft producer link resolves to the canonical producer node.
