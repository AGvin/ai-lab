# Documentation Requirements

## Requirements

- Present SpaceXAI API as the direct hosted developer/model-access service for Grok inference across responses/chat, images, videos, voice, files, batches, models, and current server-side tools.
- Preserve current OpenAI-compatible REST access as an API compatibility surface rather than an OpenAI-owned product relationship.
- Keep Grok trained-model identities, Grok assistant workspaces/bots, Grok Build, Collections as separately canonical vector-search service, and management APIs with their own boundaries.
- Treat base URLs, endpoint inventory, model/tool availability, SDKs, pricing, credits, rate limits, management-key behavior, files/batch behavior, deprecations, and data controls as freshness-sensitive.
- Keep Collections management/search owned by the already-canonical SpaceXAI Collections service when documenting durable vector-search behavior.

## Validation

- SpaceXAI API remains the hosted model/developer API service rather than Grok models or Grok application.
- OpenAI compatibility is not misrepresented as model/product ownership.
- Producer provenance resolves to SpaceXAI.
