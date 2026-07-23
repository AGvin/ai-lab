# Inference

Inference is the process of running a trained model on input data to produce predictions, embeddings, classifications, or generated output.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Training changes model parameters; inference uses the resulting parameters. For autoregressive language models, inference usually has two phases: prompt processing, often called prefill, and token-by-token generation, often called decode. These phases stress hardware differently.

## Main resource factors

- Model weight size and numerical precision.
- Context length and KV-cache size.
- Batch size and number of concurrent requests.
- CPU, GPU, accelerator, and memory bandwidth.
- Runtime kernels and model architecture.

## Practical use

Inference configuration determines whether a model fits in available RAM or VRAM, how quickly the first token appears, and how many tokens or requests can be served. Benchmark the actual model, quantization, context length, and workload instead of relying on theoretical hardware throughput.

## Trade-offs and limitations

Reducing precision can lower memory use but may affect quality. Increasing batch size often improves throughput while increasing latency. Longer context increases processing cost and cache memory. Some models require runtime-specific features or unsupported operators.

## Common mistakes

- Comparing tokens per second across different models or context lengths.
- Measuring only generation speed and ignoring prompt processing.
- Assuming a model that fits in storage also fits in memory.
- Ignoring warm-up and model-loading time.

## Related concepts

- [Inference and Serving](../../)
- [Model Loading](../model-loading/)
- [Performance Metrics](../performance-metrics/)
- [Quantization](../quantization/)
