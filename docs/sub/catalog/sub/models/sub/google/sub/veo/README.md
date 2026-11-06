# Veo

Google and Google DeepMind's video-generation model family; GA enterprise model IDs, Gemini API preview routes, and products such as Flow are separate serving contexts.

## Relations

- Produced by: [Google](../../../../../producers/sub/g/sub/google/)
- Produced by: [Google DeepMind](../../../../../producers/sub/g/sub/google-deepmind/)
- Has member: [Veo 3.1](sub/models/sub/veo-3-1/)
- Has member: [Veo 3.1 Fast](sub/models/sub/veo-3-1-fast/)

## Source-scoped operating boundaries

- Veo 3.1 and Veo 3.1 Fast have separate GA enterprise model IDs. Their Gemini API preview routes have an earliest October 22, 2026 shutdown; that date does not retire the GA enterprise models. [GA model reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate) · [Gemini API lifecycle](https://ai.google.dev/gemini-api/docs/deprecations).
- Video-generation controls, Content Credentials, safety controls, regions, and encryption/access configuration belong to the selected serving platform. Family membership does not establish identical resolution, duration, or security capabilities. [Platform-specific capabilities](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate).

## Official resources

- <https://deepmind.google/models/veo/>
- <https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation>
- <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate>
- <https://ai.google.dev/gemini-api/docs/deprecations>

## Models

- [Veo Models](sub/models/)
