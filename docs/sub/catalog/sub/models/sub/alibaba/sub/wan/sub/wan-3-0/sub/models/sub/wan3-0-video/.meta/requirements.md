# Documentation Requirements

## Requirements

- Identify Wan3.0-Video as the released `wan3.0-video` all-in-one video-generation model in the Wan 3.0 series.
- Preserve current text/image/video/audio/file/link input and video output plus text-to-video, first/last-frame, reference-based, and related generation modes only while first-party Model Studio documentation supports them.
- Keep the model distinct from the speed-optimized `wan3.0-video-prime` sibling and from the Model Studio hosting service.
- Treat supported resolution/duration, material/reference limits, audio behavior, regional availability, price, quotas, task parameters, snapshot aliases, and lifecycle state as freshness-sensitive.
- Attribute provider quality/realism/consistency claims to Alibaba Cloud/Wan rather than independent AI Lab measurement.

## Decision and Operational Boundaries

- wan3.0-video is a distinct hosted Wan 3.0 all-in-one video generation model.
- Alibaba's undated release page labels the Wan 3.0 Video API generally available, while the API reference updated 2026-10-15 still says preview; verify lifecycle and availability for the selected region.
- HTTP calls require asynchronous submission and polling; handle task failure separately from request acceptance, and persist generated assets according to the documented result lifetime.
- Use the selected task's material types and limits; broad multimodal support is not unrestricted mixing of references.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node is the concrete Wan3.0-Video model identity rather than the Wan 3.0 series or API service.
- Serving configuration is not generalized into permanent model architecture.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
