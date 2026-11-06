# Qwen-Image-3.0

qwen-image-3.0 is a separately named hosted image generation/editing model; it is not a runtime option on another catalog model.

## Decision and Operational Boundaries

- The current editing contract supports one to three reference images; follow the exact API rather than adjacent-model marketing summaries.
- The OpenAI-compatible route uses synchronous /images/generations with its image extension; it does not implement /images/edits, multipart masks, streaming, or asynchronous calls. DashScope supplies the asynchronous route.
- Do not infer open weights or a checkpoint license from the service model name; validate returned asset persistence and service retention separately.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen-Image](../../../../) |

## Primary Sources

- [Alibaba Cloud: qwen image 3 0](https://www.alibabacloud.com/help/en/model-studio/qwen-image-3-0)
- [Alibaba Cloud: qwen image generation and editing api reference](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
