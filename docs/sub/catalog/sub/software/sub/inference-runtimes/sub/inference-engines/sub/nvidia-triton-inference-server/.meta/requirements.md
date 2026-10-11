# Documentation Requirements

## Requirements

- Present NVIDIA Triton Inference Server as NVIDIA's released open-source inference-serving software for deploying models from multiple machine-learning/deep-learning frameworks across cloud, data-center, edge, and embedded environments.
- Preserve its runtime/server identity separately from TensorRT, TensorRT-LLM, NVIDIA Dynamo, model backends, NGC containers, NVIDIA AI Enterprise, KServe protocol specifications, and hosted inference services.
- Preserve current major capabilities at a stable level: model repositories, multiple backends, concurrent execution, dynamic/sequence batching, ensembles/business-logic scripting, HTTP/gRPC inference protocols, metrics, and custom backend APIs.
- Treat current release version, container tag, CUDA/cuDNN/NCCL/TensorRT/OpenVINO/vLLM dependencies, backend/platform support, driver requirements, client SDK versions, deployment examples, and performance behavior as freshness-sensitive.
- Keep current main-branch under-development state distinct from the latest stable release; do not document unreleased main-branch behavior as current released product behavior.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Triton remains an inference-serving runtime/server rather than a model optimizer, model gateway, or hosted model API.
- Backends and framework integrations are not automatically materialized as peer Triton product identities.
- Producer provenance resolves bidirectionally to NVIDIA.
