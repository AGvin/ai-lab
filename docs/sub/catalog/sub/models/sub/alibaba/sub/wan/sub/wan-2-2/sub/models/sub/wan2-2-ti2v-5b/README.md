# Wan2.2-TI2V-5B

Wan2.2-TI2V-5B is a released Apache-2.0 open video checkpoint. The 5B checkpoint supports text-to-video and image-to-video at 720P and 24 fps.

## Decision and Operational Boundaries

- The generator also needs its text encoder, VAE, scheduler, and preprocessing; model size is not total download size or peak VRAM.
- The official 24GB GPU example depends on CPU/text-encoder offload and dtype conversion; it is not an unconditional peak-memory guarantee.
- Do not infer native sound generation, service APIs, or thirty-second clips from later Wan generations.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Wan 2.2](../../../../) |

## Primary Sources

- [Official model card or license: Wan-AI/Wan2.2-TI2V-5B](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)
- [Official repository: Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2)
