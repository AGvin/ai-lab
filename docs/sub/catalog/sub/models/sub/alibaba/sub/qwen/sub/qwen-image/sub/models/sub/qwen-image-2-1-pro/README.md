# Qwen-Image-2.1-Pro

qwen-image-2.1-pro is a separately named hosted image generation/editing model; it is not a runtime option on another catalog model.

## Decision and Operational Boundaries

- The current editing contract supports up to ten reference images with prompt-driven transparency; follow the exact API rather than adjacent-model marketing summaries.
- The OpenAI-compatible route uses synchronous /images/generations with its image extension; it does not implement /images/edits, multipart masks, streaming, or asynchronous calls. DashScope supplies the asynchronous route.
- Do not infer open weights or a checkpoint license from the service model name; validate returned asset persistence and service retention separately.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen-Image](../../../../) |

## Primary Sources

- [Alibaba Cloud: qwen image 2 1 pro](https://www.alibabacloud.com/help/en/model-studio/qwen-image-2-1-pro)
- [Alibaba Cloud: qwen image generation and editing api reference](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
