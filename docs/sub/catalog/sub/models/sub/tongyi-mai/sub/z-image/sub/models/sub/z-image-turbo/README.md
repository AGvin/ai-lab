# Z-Image-Turbo

**Z-Image-Turbo** is a separately released, distilled text-to-image model published as `Tongyi-MAI/Z-Image-Turbo`. It belongs to the roughly **6B-parameter** Z-Image family built on a **Scalable Single-Stream Diffusion Transformer (S3-DiT)**. The public model checkpoint was released on **November 26, 2025** under **Apache-2.0**.

## Training and generation boundary

Z-Image-Turbo is derived from the full-capacity, undistilled [Z-Image base model](../z-image/), not a runtime switch, quantization, or hosted alias of that model. The publisher's official model zoo identifies Turbo as an accelerated, separately trained/distilled release. Its documented generation recipe uses **eight model evaluations (NFEs/DiT forwards)** without classifier-free guidance (CFG). These are model/pipeline settings, **not** a guarantee of eight seconds or a universal wall-clock latency.

## Evidence and operating boundaries

Tongyi-MAI reports strong photorealism, English/Chinese text rendering, prompt adherence, sub-second inference on H800, and a potential 16 GB consumer-VRAM fit. These are **publisher claims** requiring independent checks for the exact GPU, precision, runtime, resolution and workload. Historical leaderboards are mutable and are not AI Lab's reproduced benchmark results.

Diffusers/ComfyUI support, hosted demos, third-party access, optimized distributions, local memory fit, pricing and workflow recommendations belong to their respective runtime, artifact, service or evaluation contexts, not immutable model identity.

## Relations

- Member of: [Z-Image family](../../../../)
- Derived from: [Z-Image base](../z-image/)

## Official resources

- [Tongyi-MAI Z-Image project and model zoo](https://github.com/Tongyi-MAI/Z-Image)
- [Z-Image-Turbo checkpoint and license](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
- [Z-Image technical report](https://arxiv.org/abs/2511.22699)
