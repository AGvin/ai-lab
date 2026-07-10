<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:9dd0a8cfb59274da1f79a96f0d73e5103c970772
  mode: copy-through
-->

# Inference and Serving

Concepts for running trained models locally or as services and understanding their resource and performance behavior.

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Переклади

- [English](../../../../l10n/uk_UA/)
- Українська — поточна

## Essential

- [`inference/`](../../sub/inference/l10n/uk_UA/) — Running a trained model to process input and produce output.
- [`quantization/`](../../sub/quantization/l10n/uk_UA/) — Reducing numerical precision to lower model memory and compute requirements.
- [`numerical-precision/`](../../sub/numerical-precision/l10n/uk_UA/) — The number format used for model weights, activations, and computation.
- [`model-formats/`](../../sub/model-formats/l10n/uk_UA/) — File and serialization formats used to store and load model artifacts.
- [`gpu-offloading/`](../../sub/gpu-offloading/l10n/uk_UA/) — Placing selected model computation or layers on a GPU while other work remains elsewhere.
- [`kv-cache/`](../../sub/kv-cache/l10n/uk_UA/) — Cached attention keys and values reused during autoregressive generation.
- [`latency/`](../../sub/latency/l10n/uk_UA/) — The elapsed time required to produce a response or reach a defined output milestone.
- [`throughput/`](../../sub/throughput/l10n/uk_UA/) — The amount of model work completed per unit of time.
- [`performance-metrics/`](../../sub/performance-metrics/l10n/uk_UA/) — Measurements such as time to first token, tokens per second, latency, and memory use.

## Useful

- [`model-serving/`](../../sub/model-serving/l10n/uk_UA/) — Exposing model inference through a managed process, API, queue, or runtime service.
- [`model-loading/`](../../sub/model-loading/l10n/uk_UA/) — Moving model artifacts into RAM, VRAM, or runtime-managed memory for execution.
- [`cpu-inference/`](../../sub/cpu-inference/l10n/uk_UA/) — Running model computation primarily on general-purpose processors.
- [`gpu-inference/`](../../sub/gpu-inference/l10n/uk_UA/) — Running model computation primarily on graphics processors optimized for parallel workloads.
- [`context-caching/`](../../sub/context-caching/l10n/uk_UA/) — Reusing previously processed prompt context to reduce repeated computation.

## Specialized

- [`flash-attention/`](../../sub/flash-attention/l10n/uk_UA/) — Attention implementations optimized to reduce memory traffic and improve GPU efficiency.
- [`continuous-batching/`](../../sub/continuous-batching/l10n/uk_UA/) — Dynamically combining active inference requests to improve serving utilization.
- [`speculative-decoding/`](../../sub/speculative-decoding/l10n/uk_UA/) — Using a faster draft model or process to propose tokens for verification by a target model.
