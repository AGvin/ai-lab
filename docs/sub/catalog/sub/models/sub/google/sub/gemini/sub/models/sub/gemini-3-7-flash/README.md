# Gemini 3.7 Flash

Released Gemini 3.7 Flash identity retained for historical continuity; the deprecated gemini-3.7-flash endpoint now automatically routes to gemini-3.8-flash.

## Relations

- Member of: [Gemini](../../../../)

## Official resources

- <https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash>
- <https://ai.google.dev/gemini-api/docs/changelog>
- <https://ai.google.dev/gemini-api/docs/deprecations>

## Source-scoped operating boundaries

- Google no longer offers 3.7 Flash for selection in AI Studio. Its endpoint is not shutting down, but requests route to 3.8 Flash, so a request bearing the old name does not demonstrate independently served 3.7 weights. [Deprecation notice](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash) · [Lifecycle table](https://ai.google.dev/gemini-api/docs/deprecations).
- Preserve original release facts as historical facts. Current tools, safety controls, output behavior, and evaluations must be scoped to the effective serving model and service configuration.
