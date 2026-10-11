# Documentation Requirements

## Requirements

- Identify CTranslate2 as an independently released, production-oriented C++ and Python inference library for supported Transformer architectures, maintained by OpenNMT.
- Keep CTranslate2 under `software/inference-runtimes/inference-engines` rather than creating a trained-model, model-optimization-only or hosted model-API identity. Weight conversion and quantization remain integrated engine capabilities.
- Track release-specific support for encoder-decoder, decoder-only, encoder-only and speech models, and distinguish advertised model-family converters from directly supported runtime architectures.
- Preserve CPU, NVIDIA CUDA and AMD ROCm installation/runtime distinctions. Treat operating system, wheel availability, CUDA/ROCm versions, GPU compute capability, CPU instruction sets, accelerated kernels, precision and distribution constraints as mutable.
- Describe model conversion, batching, asynchronous execution, reduced-precision weights, cache and tensor-parallel support only at the level confirmed by the official documentation and exact release.
- Do not promote third-party web servers or integrations into CTranslate2-owned independent product identities without first-party ownership evidence.
- Attribute performance/quality measurements to exact model, source framework, hardware, software version, quantization, batch and dataset. Historical upstream benchmarks are configuration-bound and must not be generalized to current systems.
- Preserve OpenNMT producer provenance through reciprocal relations.

## Validation

- The canonical entry is the inference engine/library and is not conflated with OpenNMT training frameworks, converter utilities or third-party hosted endpoints.
- Official release/version and model-support claims remain source-backed and precise.
- `produced-by` and `produces` provenance resolve bidirectionally.
