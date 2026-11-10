# Documentation Requirements

## Requirements

- Present NVIDIA NIM as NVIDIA's released product family of prebuilt optimized inference microservices for deploying foundation and customized models on NVIDIA-accelerated infrastructure.
- Preserve its self-hostable software identity: NIM containers can run on cloud, data-center, workstation, edge, and RTX-class infrastructure; hosted NIM API endpoints remain optional access surfaces.
- Keep Triton Inference Server, TensorRT, TensorRT-LLM, vLLM, SGLang, underlying model identities, DGX Cloud, NVIDIA AI Enterprise, NIM Operator, and individual model-specific NIM containers with their own product/component boundaries.
- Do not create one peer catalog entity per NIM container solely because it is separately downloadable or exposes an endpoint.
- Treat current model inventory, inference engines, GPU compatibility, container tags, support branch, hosted endpoint availability, orchestration behavior, API schemas, performance, and access terms as freshness-sensitive.
- Attribute performance and efficiency comparisons to NVIDIA and preserve model, hardware, precision, concurrency, and serving conditions.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- NVIDIA NIM remains inference-serving/deployment software rather than a trained-model family or generic hosted model API.
- Optional hosted access does not erase the primary self-hostable software boundary.
- Individual model-specific NIM containers are not automatically duplicated as peer product nodes.
- Producer provenance resolves bidirectionally to NVIDIA.
