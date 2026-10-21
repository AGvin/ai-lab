# Clef-omni

Clef-omni is Cloudflare's multimodal decision model released on 9 October 2026. It uses the Qwen/Qwen3-Omni-30B-A3B-Instruct thinker backbone, with 30B total and 3B active parameters, to score allowed answers from text, images, audio and video. [Source 1](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/) · [Source 2](https://huggingface.co/Cloudflare/clef-omni)

## Model and input/output boundary

Cloudflare's release describes a 30B-total / 3B-active MoE model with text, image, audio and video input. The official card identifies its upstream thinker as `Qwen/Qwen3-Omni-30B-A3B-Instruct` and publishes the derivative under Apache 2.0. The included upstream talker and code2wav weights remain unused by `load_release_model`; this decision interface outputs option scores and probabilities, not speech or free-form text. [Model release and parameter scope](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/) · [Exact backbone and output implementation](https://huggingface.co/Cloudflare/clef-omni)

## Hosted media and context

The current `@cf/cloudflare/clef-omni` page specifies 64,000 context tokens and accepts up to four audio clips and two videos per request. Cloudflare documents WAV/MP3 audio and MP4/WebM video. Questions and media use the context budget; the request fails if those exceed it, and otherwise text state may be truncated. Check the actual evidence retained and the chosen backend's media support before using a decision. [Current route and media contract](https://developers.cloudflare.com/workers-ai/models/clef-omni/) · [Supported media formats](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/)

## Local deployment and evaluation

The 3B active count does not describe the complete model's storage or memory. The official card reports about 64 GB for the bfloat16 backbone in its tested setup and specifies a custom decision head, loader and media processor; total operational memory depends on context, batches and media. Pin the release and implementation, then test classification quality, audiovisual alignment, calibration and fallback behavior on representative inputs. Keep permission to access recordings or act on predictions in the application. [Runtime scope and release implementation](https://huggingface.co/Cloudflare/clef-omni)

## Relations

- Member of: [Clef](../../../../README.md)

## Official resources

- <https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/>
- <https://huggingface.co/Cloudflare/clef-omni>
- <https://developers.cloudflare.com/workers-ai/models/clef-omni/>
