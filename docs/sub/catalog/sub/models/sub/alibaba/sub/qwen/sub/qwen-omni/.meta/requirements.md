# Documentation Requirements

## Requirements

- Identify Qwen Omni as the Qwen model series for multimodal understanding and generation across text, images, audio, and video, including real-time speech interaction where supported by a concrete member.
- Preserve the model-series boundary separately from Qwen Studio, Alibaba Cloud Model Studio, generic audio/speech APIs, and non-Omni Qwen vision or language models.
- Materialize current released Omni model identities when their input/output modalities, real-time boundary, or serving contract materially differ.
- Treat model inventory, context limits, supported languages, audio/video formats, reasoning/tool support, realtime transports, regions, pricing, rate limits, and lifecycle aliases as freshness-sensitive.
- Preserve Qwen Team production provenance and the parent Qwen relation.
- Attribute provider benchmark/capability comparisons to Qwen Team or Alibaba Cloud rather than independent AI Lab ranking.

## Validation

- Qwen Omni remains a model series within Qwen and is not conflated with the Model Studio service.
- Realtime and non-realtime concrete model identities remain distinct where first-party model IDs and output contracts differ.
- Producer and parent relations resolve bidirectionally.
