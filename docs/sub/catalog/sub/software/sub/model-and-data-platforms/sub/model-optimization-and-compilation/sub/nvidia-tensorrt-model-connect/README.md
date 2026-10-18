# NVIDIA TensorRT Model Connect

NVIDIA TensorRT Model Connect is an open-source toolkit in public preview for converting supported model checkpoints into TensorRT-backed bundles and native C++ task integrations.

## Lifecycle

NVIDIA describes Model Connect as an experimental project intended for evaluation and feedback. APIs, scope and direction may change; the preview establishes no specific product roadmap or release timeline. Published nightly wheels provide a downloadable preview, not a guarantee of stable APIs or production readiness.

## Scope and product boundaries

Its main job is checkpoint-to-deployment artifact transformation, model-family adaptation and compatibility validation. Runtime and task APIs are part of the resulting deployment path, not evidence that this toolkit is a general model-serving platform. TensorRT, TensorRT-LLM, CUDA, TVM FFI and Hugging Face remain dependencies or integration surfaces.

## Compatibility and operational considerations

Confirm supported model families, qualified GPUs, build tools, bundle format and deployment API for the exact release before adoption. Model coverage and compilation paths change rapidly, and an upstream two-command demonstration is not a universal deployment or performance guarantee.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Source repository and project status](https://github.com/NVIDIA/TensorRT-Model-Connect)
- [Current documentation](https://nvidia.github.io/TensorRT-Model-Connect/)
- [Technical introduction](https://developer.nvidia.com/blog/deploy-an-open-model-from-checkpoint-to-inference-in-two-commands-with-nvidia-tensorrt-model-connect/)
