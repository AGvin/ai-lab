# Documentation Requirements

## Requirements

- Identify Gemini 3.7 Flash as the concrete `gemini-3.7-flash` model released to GA on 2026-08-13 and deprecated on 2026-10-08 in favor of Gemini 3.8 Flash; current API requests are automatically routed to `gemini-3.8-flash`.
- Preserve model-specific capabilities and limits from current Google documentation rather than copying facts from Gemini 3.6 Flash or Gemini 3.8 Flash.
- Keep pricing, quotas, API rollout state, hosted-service availability, deprecation/shutdown timing, and automatic-routing behavior freshness-sensitive and outside intrinsic model identity.

## Validation

- Gemini 3.7 Flash remains a concrete member of Gemini rather than a separate family.
- Historical stable-release identity is not conflated with current API lifecycle/routing behavior; deprecation is explicit.

## Verified identity and provenance

Released Gemini 3.7 Flash identity retained for historical continuity; the deprecated gemini-3.7-flash endpoint now automatically routes to gemini-3.8-flash.

## Source-scoped operating boundaries

- Google no longer offers 3.7 Flash for selection in AI Studio. Its endpoint is not shutting down, but requests route to 3.8 Flash, so a request bearing the old name does not demonstrate independently served 3.7 weights. [Deprecation notice](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash) · [Lifecycle table](https://ai.google.dev/gemini-api/docs/deprecations).
- Preserve original release facts as historical facts. Current tools, safety controls, output behavior, and evaluations must be scoped to the effective serving model and service configuration.

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash>
- <https://ai.google.dev/gemini-api/docs/deprecations>
