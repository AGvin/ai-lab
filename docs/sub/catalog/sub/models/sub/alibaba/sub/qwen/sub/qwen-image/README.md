# Qwen-Image

Qwen-Image covers image-generation and image-editing models, including open 2.1 checkpoints and named hosted variants.

## Decision and Operational Boundaries

- Keep Qwen-Image-2.1 and its Turbo weights under the Qwen Research License; commercial use requires a separate license and is not made permissive by marketing terminology.
- Do not carry 2.1 reference-image counts, transparency, or inference-step settings into 3.0; follow the exact model and protocol.
- The OpenAI-compatible image route has a narrower contract than the full OpenAI Images API; verify synchronous/async behavior, output URL handling, and supported editing fields.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen-Image-2.1](./sub/models/sub/qwen-image-2-1/) |
| Includes | [Qwen-Image-2.1-Pro](./sub/models/sub/qwen-image-2-1-pro/) |
| Includes | [Qwen-Image-2.1-Turbo](./sub/models/sub/qwen-image-2-1-turbo/) |
| Includes | [Qwen-Image-3.0](./sub/models/sub/qwen-image-3-0/) |
| Includes | [Qwen-Image-3.0-Pro](./sub/models/sub/qwen-image-3-0-pro/) |

## Primary Sources

- [Official repository: QwenLM/Qwen-Image-2.1](https://github.com/QwenLM/Qwen-Image-2.1)
- [Official model card or license: Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)
- [Official model card or license: Qwen/Qwen-Image-2.1-Turbo](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo)
- [Alibaba Cloud: qwen image generation and editing api reference](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
