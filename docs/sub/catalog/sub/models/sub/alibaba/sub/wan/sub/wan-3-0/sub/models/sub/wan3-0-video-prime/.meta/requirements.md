# Documentation Requirements

## Requirements

- Identify Wan3.0-Video-Prime as the released speed-optimized `wan3.0-video-prime` member of the Wan 3.0 series.
- Preserve the same broad all-in-one multimodal video-generation boundary as current first-party documentation while keeping its speed-oriented service/model positioning distinct from `wan3.0-video`.
- Treat generation speed comparisons, supported resolution/duration, reference-material limits, regions, pricing, quotas, task parameters, and lifecycle state as freshness-sensitive.
- Keep Model Studio as the inference service rather than collapsing it into the trained-model identity.
- Attribute speed/quality comparisons to Alibaba Cloud rather than independent AI Lab measurement.

## Decision and Operational Boundaries

- wan3.0-video-prime is a distinct hosted Wan 3.0 all-in-one video generation model positioned by Alibaba for faster generation.
- HTTP calls require asynchronous submission and polling; handle task failure separately from request acceptance, and persist generated assets according to the documented result lifetime.
- Use the selected task's material types and limits; broad multimodal support is not unrestricted mixing of references.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains the concrete Prime model identity and not merely a pricing tier attached to Wan3.0-Video.
- Provider performance claims remain explicitly attributed and configuration-scoped.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
