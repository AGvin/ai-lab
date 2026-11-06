# Documentation Requirements

## Requirements

- Identify the OpenTelemetry GenAI Semantic Conventions as the dedicated OpenTelemetry semantic-convention specification for generative-AI clients, agents, MCP-related telemetry, and provider-specific GenAI telemetry.
- Preserve span, metric, event, attribute, provider, agent, and MCP semantics only from current authoritative OpenTelemetry material.
- Preserve stability labels and migration/deprecation boundaries because the GenAI conventions evolve independently from the core OpenTelemetry semantic-conventions repository.
- Treat language instrumentation and observability products as implementations/consumers of the conventions rather than duplicate specification identities.
- Keep OpenInference distinct as a separate AI observability semantic-convention specification.

## Validation

- The entity is classified as a semantic-convention specification, not as an SDK, telemetry backend, or observability service.
- Experimental, moved, deprecated, and stable convention surfaces are not conflated.
