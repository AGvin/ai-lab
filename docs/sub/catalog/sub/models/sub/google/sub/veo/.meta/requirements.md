# Documentation Requirements

## Requirements

- Identify Veo as Google's video-generation model family, with current provenance to Google and Google DeepMind where first-party sources establish both organization views.
- Preserve the trained-model family boundary separately from Vertex AI, Gemini API, Gemini Enterprise Agent Platform, Flow, Gemini product integrations, Media Studio, and generated video assets.
- Materialize current released concrete Veo models when model IDs, capability/performance trade-offs, or lifecycle state materially change reader decisions.
- Treat serving platform, model IDs/snapshots, resolution and duration limits, reference-image support, audio generation, extension/editing controls, Content Credentials behavior, pricing, quotas, regions, and retirement dates as freshness-sensitive.
- Do not materialize preview-only Veo variants under the current released/stable intake gate.
- Attribute quality, prompt-adherence, audiovisual, and comparative claims to Google/Google DeepMind or the cited evaluator rather than converting them into independent AI Lab rankings.

## Validation

- Veo remains a trained-model family rather than a Google Cloud service or end-user creative product.
- GA and preview serving identities are not conflated.
- Producer provenance resolves bidirectionally.

## Verified identity and provenance

Google and Google DeepMind's video-generation model family; GA enterprise model IDs, Gemini API preview routes, and products such as Flow are separate serving contexts.

## Source-scoped operating boundaries

- Veo 3.1 and Veo 3.1 Fast have separate GA enterprise model IDs. Their Gemini API preview routes have an earliest October 22, 2026 shutdown; that date does not retire the GA enterprise models. [GA model reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate) · [Gemini API lifecycle](https://ai.google.dev/gemini-api/docs/deprecations).
- Video-generation controls, Content Credentials, safety controls, regions, and encryption/access configuration belong to the selected serving platform. Family membership does not establish identical resolution, duration, or security capabilities. [Platform-specific capabilities](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate).

## Source evidence

- <https://deepmind.google/models/veo/>
- <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate>
- <https://ai.google.dev/gemini-api/docs/deprecations>
