# Qwen-Image-2.1-Turbo

Qwen-Image-2.1-Turbo is both an independently released accelerated checkpoint and a named hosted variant; the October 9, 2026 checkpoint uses eight denoising steps.

## Decision and Operational Boundaries

- The open checkpoint is Qwen Research licensed; a hosted API listing is not a permissive commercial license to its weights.
- Keep the checkpoint's 7B visual component and Diffusers pipeline distinct from whole-pipeline memory and hosted quotas.
- The current hosted 2.1 Turbo editing contract allows up to ten references and prompt-driven transparency; do not inherit 3.0 protocol limits or negative-prompt support.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen-Image](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen-Image-2.1-Turbo](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo)
- [Official repository: QwenLM/Qwen-Image-2.1](https://github.com/QwenLM/Qwen-Image-2.1)
- [Official repository: QwenLM/Qwen-Image-2.1/blob/main/LICENSE](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/LICENSE)
- [Alibaba Cloud: qwen image generation and editing api reference](https://www.alibabacloud.com/help/en/model-studio/qwen-image-generation-and-editing-api-reference)
- [Alibaba Cloud: qwen image edit guide](https://www.alibabacloud.com/help/en/model-studio/qwen-image-edit-guide)
