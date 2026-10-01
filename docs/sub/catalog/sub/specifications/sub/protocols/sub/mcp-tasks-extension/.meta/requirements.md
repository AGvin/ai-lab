# Documentation Requirements

## Requirements

- Present the MCP Tasks Extension as the stable official Model Context Protocol extension identified by `io.modelcontextprotocol/tasks` for durable long-running request execution, polling, and deferred result retrieval.
- Preserve the stable released `2026-07-28` specification/schema boundary and distinguish it from the mutable `draft` development surface.
- Keep Tasks separate from MCP core primitives and from workflow/job products that implement long-running execution through their own APIs.
- Preserve the durable-state-machine boundary: tasks carry execution state for a request and expose receiver-generated task IDs for later status/result access.
- Treat exact methods, request/response schemas, task states, capability negotiation, metadata, cancellation behavior, TTL/retention behavior, and compatibility requirements as version-sensitive normative state that must be re-checked against the current official released specification.
- Keep SDK implementation details, product-specific support, orchestration engines, background job systems, and application-level task semantics with their applicable software/service/learning owners.
- Do not infer that every asynchronous MCP implementation conforms to the Tasks extension merely because it supports long-running operations.

## Validation

- Stable status is traceable to the official extension repository's released `2026-07-28` snapshot rather than the development draft.
- The node remains an optional MCP extension rather than being represented as an intrinsic core protocol primitive.
- Historical experimental/incubating lifecycle language is not presented as the current release state.
