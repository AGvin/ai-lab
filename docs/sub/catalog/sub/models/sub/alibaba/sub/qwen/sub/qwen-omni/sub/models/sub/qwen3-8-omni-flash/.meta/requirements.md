# Documentation Requirements

## Requirements

- Identify Qwen3.8-Omni-Flash as the released `qwen3.8-omni-flash` model for multimodal content understanding and analysis.
- Preserve current text/image/audio/video input and text output, reasoning modes, tool calling, web-search support, context caching, and multichannel-audio behavior only while first-party Model Studio documentation supports them.
- Keep the non-realtime text-output identity distinct from `qwen3.8-omni-flash-realtime`, which has a different streaming interaction and audio-output contract.
- Treat context limits, supported audio languages, regions, APIs, pricing, rate limits, caching behavior, serving aliases/snapshots, and tool availability as freshness-sensitive.
- Keep Model Studio as the inference service rather than the producer identity of the trained model.

## Validation

- The node remains the concrete non-realtime Qwen Omni model identity.
- Serving/API properties are not generalized to all Qwen Omni members.
- Realtime interaction behavior is not copied from the realtime sibling.
