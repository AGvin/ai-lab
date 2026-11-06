# Wan2.2-I2V-A14B

Wan2.2-I2V-A14B is a released Apache-2.0 open video checkpoint. The MoE image-to-video checkpoint requires an input image and supports 480P/720P output.

## Decision and Operational Boundaries

- The generator also needs its text encoder, VAE, scheduler, and preprocessing; model size is not total download size or peak VRAM.
- Do not infer native sound generation, service APIs, or thirty-second clips from later Wan generations.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Wan 2.2](../../../../) |

## Primary Sources

- [Official model card or license: Wan-AI/Wan2.2-I2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B)
- [Official repository: Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2)
