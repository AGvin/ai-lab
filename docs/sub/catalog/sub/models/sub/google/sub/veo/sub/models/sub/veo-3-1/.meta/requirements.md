# Documentation Requirements

## Requirements

- Identify Veo 3.1 as the released generally available Veo model exposed as `veo-3.1-generate-001` on Google's GA enterprise serving surface.
- Preserve current text/image-driven video generation, native audio generation, first/last-frame and reference-image workflows, extension support, Content Credentials, and current production positioning only while supported by first-party documentation.
- Keep the GA model identity distinct from Gemini API preview endpoints, Veo 3.1 Fast, Veo 3.1 Lite Preview, earlier Veo generations, and the Google services that host it.
- Treat supported duration, aspect ratio, resolution, frame rate, prompt language, reference limits, quotas, regions, prices, safety controls, API capabilities, and retirement dates as freshness-sensitive serving facts.
- Attribute quality, cinematic-control, prompt-adherence, and comparative claims to Google/Google DeepMind or the cited evaluator.

## Validation

- The node represents the concrete GA Veo 3.1 model rather than the whole Veo family or a preview endpoint.
- Google Cloud/Gemini serving properties are not generalized into permanent model architecture.
- Veo 3.1 Lite remains excluded while its current official launch stage is Preview.

## Verified identity and provenance

Generally available enterprise Veo model served as veo-3.1-generate-001; Gemini API preview aliases have a separate lifecycle.

## Source-scoped operating boundaries

- The GA model supports text/image and first/last-frame video generation, asset-reference images, extension, sound generation, and C2PA Content Credentials. The current standard output resolutions are 720p, 1080p, and 4K; do not copy the other tier's resolution matrix. [GA capability matrix](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate).
- The corresponding Gemini API preview route has an earliest shutdown date of October 22, 2026. This is a preview-route lifecycle fact, not the GA model's retirement. [Gemini API deprecations](https://ai.google.dev/gemini-api/docs/deprecations).
- C2PA identifies provenance and does not establish factual accuracy or consent. Data residency, encryption keys, and VPC controls are configuration-specific platform capabilities, not intrinsic model guarantees. [Security and provenance controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate).

## Source evidence

- <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate>
- <https://ai.google.dev/gemini-api/docs/deprecations>
