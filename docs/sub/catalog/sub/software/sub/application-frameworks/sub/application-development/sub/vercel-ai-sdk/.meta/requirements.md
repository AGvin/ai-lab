# Documentation Requirements

## Requirements

- Identify Vercel AI SDK as Vercel's TypeScript toolkit for building AI-powered applications across server and UI application frameworks.
- Preserve provider-agnostic model access, streaming, structured outputs, tool calling, multimodal generation, and UI/application integration as high-level capabilities without turning the profile into API documentation.
- Preserve AI SDK Core and AI SDK UI as distinct SDK surfaces. Current documentation also describes AI SDK Harnesses adapters for existing agent harnesses; distinguish these adapters from external harness runtimes and keep availability specific to the selected SDK release.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep framework support, model/provider inventories, package versions, gateway behavior, and other mutable compatibility facts source-backed when expanded.
- Include current official Vercel AI SDK documentation and product references.

## Validation

- The profile remains about the AI SDK rather than Vercel AI Gateway or a specific hosted model provider.
- Provider abstraction is not misrepresented as identical capability support across every provider or model.
- Official resource links match canonical entity metadata.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
