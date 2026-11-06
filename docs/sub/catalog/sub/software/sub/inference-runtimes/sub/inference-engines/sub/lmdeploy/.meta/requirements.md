# Documentation Requirements

## Requirements

- Identify LMDeploy as an independently released toolkit for model quantization, inference execution, and serving of large language and supported multimodal models.
- Preserve primary placement under `software/inference-runtimes/inference-engines` because runnable inference/serving through TurboMind and PyTorch backends is its central product role, while weight and KV-cache quantization are integrated capabilities.
- Distinguish LMDeploy's engine backends, multi-model proxy/API servers, conversion and compression tools, and integration modes from independently packaged cloud model/API services or new peer runtime identities.
- Record the current stable release baseline separately from unmerged main-branch features, previews, third-party extensions, and untested model support.
- Scope hardware support, CUDA/other accelerator backends, PyTorch dependencies, supported model families and precisions to actual releases and device configurations.
- Attribute upstream throughput and quantization-quality comparisons to the tested hardware, precision, model, batch, dataset, runtime revisions, and measurement method; do not infer universally superior performance to vLLM.
- Preserve direct InternLM project provenance with the model/server implementation and contributor history treated separately.

## Validation

- LMDeploy is independent software, not simply a converter package or a managed hosted service.
- Release, compatibility, quantization and performance claims are source-backed and workload-specific.
- The `produced-by` and inverse `produces` relations match.
