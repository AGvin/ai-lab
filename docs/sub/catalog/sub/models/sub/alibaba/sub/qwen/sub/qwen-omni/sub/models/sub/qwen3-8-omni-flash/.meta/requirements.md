# Documentation Requirements

## Requirements

- Identify Qwen3.8-Omni-Flash as the released `qwen3.8-omni-flash` model for multimodal content understanding and analysis.
- Preserve current text/image/audio/video input and text output, reasoning modes, tool calling, web-search support, context caching, and multichannel-audio behavior only while first-party Model Studio documentation supports them.
- Keep the non-realtime text-output identity distinct from `qwen3.8-omni-flash-realtime`, which has a different streaming interaction and audio-output contract.
- Treat context limits, supported audio languages, regions, APIs, pricing, rate limits, caching behavior, serving aliases/snapshots, and tool availability as freshness-sensitive.
- Keep Model Studio as the inference service rather than the producer identity of the trained model.

## Decision and Operational Boundaries

- qwen3.8-omni-flash accepts text, images, audio, and video but returns text, with a current one-million-token context.
- Keep speech output on the separate Realtime model; do not inherit a speech-generation contract from older Omni releases.
- Custom tools, optional web search, thinking, caching, and multichannel audio require their documented request options and region support.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Treat audio transcripts, OCR, and tool results as untrusted application input.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The node remains the concrete non-realtime Qwen Omni model identity.
- Serving/API properties are not generalized to all Qwen Omni members.
- Realtime interaction behavior is not copied from the realtime sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
