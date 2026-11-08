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

## Scoped original-source qualification — 2026-11-08

- **SpaceXAI/xAI Inference API** is the developer-facing hosted model-inference API operated by the Grok publisher and distinct from the Grok assistant, Grok Bot, trained Grok models, Collections as a persisted retrieval product and the separately authenticated Management API.
- The original publisher's documentation specifies `https://api.x.ai` as the REST base and Bearer API-key authorization for Responses/Chat, models, images, video and voice endpoints, files, batches and supported server-side tools. OpenAI REST API compatibility is an **interface** claim, not equivalence of every provider-specific parameter, pricing, latency, model access, data retention or content policy. Account/subscription entitlements and user-facing Grok app plans do not automatically grant equivalent developer API access.
- First-party product documentation: https://docs.x.ai/overview ; https://docs.x.ai/developers/rest-api-reference/inference .
- Scoped acceptance credits one existing original provider API identity and documentation/protocol/access boundary only. No live requests, credentials, billing charges or external tool execution; complete privacy/security/legal/model-license review, current model inventory audit, full CI/render, clean and final gates remain unverified.
