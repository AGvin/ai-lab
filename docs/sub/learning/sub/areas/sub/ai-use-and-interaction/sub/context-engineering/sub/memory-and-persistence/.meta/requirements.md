# Documentation Requirements

## Requirements

- Teach Memory and Persistence as the user/workflow-level distinction between durable or recoverable application state and the subset currently exposed to a model as context.
- Do not assume old conversation turns remain model-visible after an application truncates, summarizes, replaces, compacts, or otherwise reconstructs history.
- Explain that persistent application state may outlive a model request, while model-visible context is reconstructed per request/session according to the concrete application and service behavior.
- Require applications and workflows to identify which state must remain durable, which state must be reintroduced into context, and which stale material can safely remain outside the current working set.
- Keep agent-specific memory implementation, storage architecture, and product-specific persistence behavior with their respective Agents/Engineering/Catalog owners.

## Validation

- Persistent state is not equated with context-window capacity or current model visibility.
- Historical availability is not inferred from conversational continuity alone.
- Product-specific memory behavior is not presented as universal learning truth.
