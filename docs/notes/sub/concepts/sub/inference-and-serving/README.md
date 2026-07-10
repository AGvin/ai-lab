# Inference and Serving

Concepts for running trained models locally or as services and understanding their resource and performance behavior.

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Essential

- [`inference/`](./sub/inference/) — Running a trained model to process input and produce output.
- [`quantization/`](./sub/quantization/) — Reducing numerical precision to lower model memory and compute requirements.
- [`numerical-precision/`](./sub/numerical-precision/) — The number format used for model weights, activations, and computation.
- [`model-formats/`](./sub/model-formats/) — File and serialization formats used to store and load model artifacts.
- [`gpu-offloading/`](./sub/gpu-offloading/) — Placing selected model computation or layers on a GPU while other work remains elsewhere.
- [`kv-cache/`](./sub/kv-cache/) — Cached attention keys and values reused during autoregressive generation.
- [`latency/`](./sub/latency/) — The elapsed time required to produce a response or reach a defined output milestone.
- [`throughput/`](./sub/throughput/) — The amount of model work completed per unit of time.
- [`performance-metrics/`](./sub/performance-metrics/) — Measurements such as time to first token, tokens per second, latency, and memory use.

## Useful

- [`model-serving/`](./sub/model-serving/) — Exposing model inference through a managed process, API, queue, or runtime service.
- [`model-loading/`](./sub/model-loading/) — Moving model artifacts into RAM, VRAM, or runtime-managed memory for execution.
- [`cpu-inference/`](./sub/cpu-inference/) — Running model computation primarily on general-purpose processors.
- [`gpu-inference/`](./sub/gpu-inference/) — Running model computation primarily on graphics processors optimized for parallel workloads.
- [`context-caching/`](./sub/context-caching/) — Reusing previously processed prompt context to reduce repeated computation.

## Specialized

- [`flash-attention/`](./sub/flash-attention/) — Attention implementations optimized to reduce memory traffic and improve GPU efficiency.
- [`continuous-batching/`](./sub/continuous-batching/) — Dynamically combining active inference requests to improve serving utilization.
- [`speculative-decoding/`](./sub/speculative-decoding/) — Using a faster draft model or process to propose tokens for verification by a target model.
