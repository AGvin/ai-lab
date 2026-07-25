# Local Model Selection by VRAM

Use available VRAM as an operational constraint, not as a proxy for model quality. This guide defines practical capacity classes and an initial fit matrix for the local artifacts used by the current portfolio profiles.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status and evidence boundary

Verified on 2026-07-25 against official GPU specifications and official Qwen GGUF repositories.

The fit labels below are **planning classifications**, not measured benchmark results. Published model-file size is not peak VRAM. Runtime buffers, KV cache, context length, batching, GPU layers, drivers, graph capture, multimodal components, and concurrent services can materially change memory use.

Before adoption, measure the exact artifact, runtime, context, batch size, offload policy, and concurrency on the target machine.

## Capacity classes

The classes reflect materially common consumer and workstation capacities rather than equal numeric intervals.

| VRAM class | Current hardware examples | Planning role |
| ---: | --- | --- |
| 8 GB | Radeon PRO W7600-class and other entry cards | Small quantized models, short contexts, experiments, or partial offload |
| 12 GB | GeForce RTX 5070-class | Small local generalist with useful context headroom; constrained medium artifacts |
| 16 GB | GeForce RTX 5070 Ti-class and Radeon PRO W7700-class | Practical single-model local work for medium quantized artifacts |
| 24 GB | GeForce RTX 3090- and RTX 4090-class | Important enthusiast class for larger quantized models and sequential specialists |
| 32 GB | GeForce RTX 5090-class and Radeon PRO W7800-class | Larger local artifacts, longer contexts, or additional runtime headroom |
| 48 GB | Radeon PRO W7900-class and similar workstation cards | High-headroom single-model service or measured concurrent smaller services |
| 96 GB | RTX PRO 6000 Blackwell-class | Large workstation deployments, higher precision, or several measured services |
| 2 × 24 GB | Two RTX 3090- or RTX 4090-class GPUs | Independent concurrent services or one deliberately sharded model |
| 2 × 32 GB | Two RTX 5090-class GPUs | Higher-capacity independent lanes or validated multi-GPU serving |

Exact GPU examples are secondary. Runtime support, compute capability, memory bandwidth, interconnect, power, cooling, and software compatibility can make two cards with the same VRAM behave very differently.

## Initial Qwen3 GGUF fit matrix

The current portfolio profiles use the official `Q4_K_M` GGUF files below:

- [Qwen3 8B](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/8b/) — published `Q4_K_M` file size: 5.03 GB.
- [Qwen3 14B](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/14b/) — published `Q4_K_M` file size: approximately 9 GB.
- [Qwen3 30B-A3B](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/sub/30b-a3b/) — published `Q4_K_M` file size: approximately 18.6 GB.

| VRAM | Qwen3 8B Q4_K_M | Qwen3 14B Q4_K_M | Qwen3 30B-A3B Q4_K_M | Interpretation |
| ---: | --- | --- | --- | --- |
| 8 GB | Constrained | Impractical for full GPU residency | Impractical | Keep context, batch, and concurrent services small; CPU offload may be required |
| 12 GB | Comfortable candidate | Constrained | Impractical for full GPU residency | Measure 14B headroom carefully before promising useful context |
| 16 GB | Comfortable candidate | Comfortable candidate | Impractical for full GPU residency | Strong general-purpose class for one medium quantized model |
| 24 GB | Comfortable candidate | Comfortable candidate | Constrained | 30B-A3B may fit only with limited headroom; treat it as sequential, not concurrent with another resident model |
| 32 GB | Comfortable candidate | Comfortable candidate | Comfortable candidate | More practical KV-cache and runtime headroom, still workload-dependent |
| 48 GB | Comfortable candidate | Comfortable candidate | Comfortable candidate | Supports larger contexts or measured concurrency; does not prove that two services fit safely |
| 96 GB | Comfortable candidate | Comfortable candidate | Comfortable candidate | Consider higher precision or larger artifacts only after exact memory and quality comparison |

`Comfortable candidate` means the published file size leaves materially more nominal headroom than `Constrained`; it is not proof of a safe context size or production capacity.

## The 24 GB class

The 24 GB class is a distinct recommendation boundary because it includes widely used RTX 3090- and RTX 4090-class hardware and can host meaningfully larger quantized models than 16 GB cards.

For the current candidate set:

- Qwen3 14B Q4_K_M is the safer resident generalist starting point;
- Qwen3 30B-A3B Q4_K_M is a constrained higher-capacity candidate;
- loading the 30B-A3B artifact should normally be treated as a sequential transition after unloading another resident model;
- image generation, ASR, diarization, or perception services require their own measured memory budget;
- a successful model load is not evidence that the target context, batching, and concurrent workload are safe.

## Multi-GPU decisions

Do not sum VRAM automatically. Two GPUs can be used in different ways:

1. **Independent services** — one model or specialist per GPU. This preserves concurrency and failure isolation.
2. **Sharded model** — one model spans both GPUs through tensor or pipeline parallelism.
3. **Sequential pool** — either GPU loads different temporary services as required.

Compare complete-workflow throughput, latency, accepted-result quality, PCIe or interconnect overhead, startup time, and failure recovery. Prefer independent services when tasks overlap or isolation matters. Prefer sharding only when the larger model's measured gain justifies lost concurrency and operational complexity.

## Required measurement record

Record at least:

```text
GPU model and VRAM:
Driver and runtime:
Model repository and revision:
Artifact and quantization:
Context and KV-cache configuration:
Batch size and concurrency:
GPU layers and CPU offload:
Peak per-GPU VRAM:
Peak host RAM:
Load and warm-up time:
Time to first token:
Steady-state throughput:
Quality and acceptance result:
Failure or out-of-memory boundary:
Verified:
```

Measure both normal and worst expected requests. Include service restarts, model swaps, and concurrent tool or media workloads where they are part of the intended system.

## Selection rules

- Do not select a model solely because its weights fit.
- Preserve at least the runtime and context headroom demonstrated by measurement.
- Prefer a smaller resident model when model swapping dominates workflow latency.
- Use partial GPU offload only when the resulting latency and host-RAM use meet the workload threshold.
- Re-test after runtime, driver, quantization, context, batch, or model revision changes.
- Treat multimodal encoders, projectors, diffusion components, and auxiliary services as separate memory consumers.
- Mark unsupported or unmeasured combinations as `Unknown`, not `Comfortable`.

## Related pages

- [AI Model Selection and Team Design](../..)
- [Model Selection Methodology](../methodology/)
- [Concrete Model Portfolio Profiles](../combined-workloads/sub/environment-profiles/)
- [Qwen3](../../../../../../../software/sub/models/sub/alibaba/sub/qwen/sub/qwen3/)
- [Models](../../../../../../../software/sub/models/)
- [General repository disclaimer](../../../../../../../disclaimer/)

## Sources

- [NVIDIA GeForce RTX 5070 family specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [NVIDIA GeForce RTX 4090 specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
- [NVIDIA GeForce RTX 5090 specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)
- [NVIDIA RTX PRO 6000 Blackwell specifications](https://www.nvidia.com/en-eu/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/)
- [AMD Radeon PRO workstation GPU specifications](https://www.amd.com/en/products/graphics/workstations/radeon-pro.html)
- [Qwen3-8B-GGUF](https://huggingface.co/Qwen/Qwen3-8B-GGUF)
- [Qwen3-14B-GGUF](https://huggingface.co/Qwen/Qwen3-14B-GGUF)
- [Qwen3-30B-A3B-GGUF](https://huggingface.co/Qwen/Qwen3-30B-A3B-GGUF)
