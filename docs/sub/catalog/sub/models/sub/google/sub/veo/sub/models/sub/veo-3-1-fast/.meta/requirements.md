# Documentation Requirements

## Requirements

- Identify Veo 3.1 Fast as the released generally available speed-oriented Veo model exposed as `veo-3.1-fast-generate-001`.
- Preserve current video-generation, native-audio, reference/first-last-frame, extension, and Content Credentials capabilities only while supported by current Google documentation.
- Keep Veo 3.1 Fast distinct from the quality-oriented Veo 3.1 model, the preview-only Veo 3.1 Lite tier, Gemini API preview aliases, older Veo generations, and hosting services.
- Treat speed/cost positioning, duration, resolution, aspect ratio, frame rate, prompt languages, quotas, regions, pricing, endpoint behavior, and retirement dates as freshness-sensitive.
- Attribute speed/quality comparisons to Google rather than independent AI Lab measurement.

## Validation

- The node remains the concrete GA Fast model identity rather than a pricing tier or generic fast mode.
- Preview endpoints are not treated as aliases for the GA model without explicit first-party equivalence.

## Verified identity and provenance

Generally available enterprise Veo model served as veo-3.1-fast-generate-001, with speed-oriented positioning; Gemini API preview aliases have a separate lifecycle.

## Source-scoped operating boundaries

- The GA model supports text/image and first/last-frame video generation, asset-reference images, extension, sound generation, and C2PA Content Credentials. The current Fast output resolutions are 720p and 1080p; do not copy the other tier's resolution matrix. [GA capability matrix](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate).
- The corresponding Gemini API preview route has an earliest shutdown date of October 22, 2026. This is a preview-route lifecycle fact, not the GA model's retirement. [Gemini API deprecations](https://ai.google.dev/gemini-api/docs/deprecations).
- C2PA identifies provenance and does not establish factual accuracy or consent. Data residency, encryption keys, and VPC controls are configuration-specific platform capabilities, not intrinsic model guarantees. [Security and provenance controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate).

## Source evidence

- <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate>
- <https://ai.google.dev/gemini-api/docs/deprecations>
