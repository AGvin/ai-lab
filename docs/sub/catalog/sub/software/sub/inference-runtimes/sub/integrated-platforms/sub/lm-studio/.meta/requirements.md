# Documentation Requirements

## Requirements

- Identify LM Studio as Element Labs, Inc.'s integrated local inference platform spanning desktop UI, headless `llmster`/daemon operation, CLI, local model management, chat, and local API/SDK serving.
- Preserve the local-first execution boundary: downloaded models, local chats/documents, and the local server can operate entirely on the user's machine and offline; exposing the server to the local network changes the network trust boundary without changing the runtime into a hosted service.
- Preserve current developer surfaces at a stable high level: native REST API, OpenAI-compatible and Anthropic-compatible endpoints, Python/TypeScript SDKs, CLI/headless operation, and MCP/tool integration.
- Distinguish local execution from optional LM Studio cloud-processing features such as cloud models or web search. Current official privacy documentation states local prompt/document content stays on-device, while explicitly chosen cloud-processing features have a separate transient cloud data path.
- Preserve useful legacy evaluation boundaries around model provenance/licenses, local/server network binding, authentication/API-token configuration, filesystem/model storage, MCP/tool permissions, downloaded model trust, and compatibility expectations.
- Keep exact API versions/endpoints, runtime backends, supported hardware/platform lists, cloud-feature catalog, pricing, and other mutable details source-backed and time-scoped when expanded.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include current official LM Studio app/developer/privacy references.

## Validation

- The page does not imply that ordinary local inference requires LM Studio cloud processing.
- Local/offline privacy claims are scoped to local processing and do not cover optional cloud features.
- Desktop, headless, CLI, SDK, and API surfaces are represented as one LM Studio software identity.
- Local-network serving is treated as a network exposure boundary rather than a hosted-service identity change.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
