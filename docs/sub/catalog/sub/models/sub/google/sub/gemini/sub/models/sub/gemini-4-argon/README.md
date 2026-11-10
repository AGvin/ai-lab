# Gemini 4 Argon

Stable Gemini reasoning model served as gemini-4-argon; its 1,048,576-token window is shared by input, thinking, and output, and long decode is a serving mode rather than another model.

## Relations

- Member of: [Gemini](../../../../)

## Source-scoped operating boundaries

- The shared input/thinking/output budget is 1,048,576 tokens. Default synchronous output is limited to 65,536; long decode can use the remaining shared budget and requires the documented execution mode. Do not add independent million-token input and output allowances. [Token and long-decode contract](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon).
- Functions, grounding, code execution, and structured outputs are supported; computer use is preview. Caching is implicit only. Live API and image/audio generation are unsupported. [API capability matrix](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon).
- Cloud GA began October 13, 2026. Cloud support retirement dates and region settings are platform-specific, not Gemini API shutdown dates. Application tools still require explicit authorization and validation. [Cloud release and scope](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-argon).

## Official resources

- <https://ai.google.dev/gemini-api/docs/models/gemini-4-argon>
- <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-argon>
- <https://ai.google.dev/gemini-api/docs/latest-model>
