# Documentation Requirements

## Requirements

- Identify Qwen Omni as the Qwen model series for multimodal understanding and generation across text, images, audio, and video, including real-time speech interaction where supported by a concrete member.
- Preserve the model-series boundary separately from Qwen Studio, Alibaba Cloud Model Studio, generic audio/speech APIs, and non-Omni Qwen vision or language models.
- Materialize current released Omni model identities when their input/output modalities, real-time boundary, or serving contract materially differ.
- Treat model inventory, context limits, supported languages, audio/video formats, reasoning/tool support, realtime transports, regions, pricing, rate limits, and lifecycle aliases as freshness-sensitive.
- Preserve Qwen Team production provenance and the parent Qwen relation.
- Attribute provider benchmark/capability comparisons to Qwen Team or Alibaba Cloud rather than independent AI Lab ranking.

## Decision and Operational Boundaries

- Qwen Omni groups multimodal understanding and speech interaction models with release-specific input and output contracts.
- Qwen3.8-Omni-Flash produces text; the separate Realtime identity produces text and audio. Do not promise speech output merely from the Omni family name.
- Keep HTTP analysis separate from persistent realtime sessions, history limits, and transport-specific features.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Qwen Omni remains a model series within Qwen and is not conflated with the Model Studio service.
- Realtime and non-realtime concrete model identities remain distinct where first-party model IDs and output contracts differ.
- Producer and parent relations resolve bidirectionally.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
