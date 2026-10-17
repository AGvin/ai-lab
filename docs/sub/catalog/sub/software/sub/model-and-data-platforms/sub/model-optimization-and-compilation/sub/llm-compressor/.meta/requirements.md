# Documentation Requirements

## Requirements

- Identify LLM Compressor as a separately maintained and released upstream software library for model compression and quantization before inference with vLLM, rather than a new inference-serving engine or trained model identity.
- Preserve its primary `model-optimization-and-compilation` owner for model artifact transforms, calibration, weight/activation quantization, KV cache quantization and related techniques. Loading compressed artifacts in vLLM is a separate runtime integration.
- Distinguish the upstream model optimization toolkit from output model checkpoints, the compressed-tensors serialization package/format, vendor-specific Triton kernels, vLLM deployment servers and Red Hat AI hosted assets.
- Keep stable release features, experimental branches, package/API versions, supported model architectures, numerical formats and kernel/hardware dependencies clearly separated.
- Attribute compression, model-quality, memory-saving and throughput comparisons to exact hardware, model and revisions, quantization algorithm, calibration data, runtime, batch and configuration; do not generalize project marketing figures across model families or platforms.
- Preserve the vLLM Project as current repository-level producer, while distinguishing the project's earlier Neural Magic/Red Hat AI origin and engineering contributions from current stewardship.

## Validation

- LLM Compressor is not confused with vLLM, vLLM-Omni, model weights or hosted model APIs.
- Official package/repository references match the canonical software identity.
- Mutable compatibility and performance statements are version and workload scoped.
- The `produced-by` relation has its reciprocal producer `produces` entry.
