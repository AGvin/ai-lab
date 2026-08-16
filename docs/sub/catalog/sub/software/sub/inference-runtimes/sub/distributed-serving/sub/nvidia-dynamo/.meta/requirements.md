# Documentation Requirements

## Requirements

- Identify NVIDIA Dynamo as an open-source, datacenter-scale distributed inference framework and orchestration layer for generative-AI serving.
- Preserve its primary placement under `inference-runtimes/distributed-serving`; Dynamo coordinates engines such as SGLang, TensorRT-LLM, and vLLM rather than replacing them.
- Preserve NVIDIA as the canonical producer through the physically materialized `produced-by` relation when the reciprocal NVIDIA `produces` relation resolves successfully.
- Use the current canonical repository identity `ai-dynamo/dynamo` and current NVIDIA Dynamo documentation.
- Keep backend matrices, hardware support, topology features, performance claims, release versions, and deployment details source-backed when expanded.

## Validation

- The NVIDIA/NVIDIA Dynamo `produces` / `produced-by` relation pair is physically present at both endpoints and semantically consistent.
- The page explicitly distinguishes Dynamo's orchestration role from underlying inference engines.
- Stale pre-move repository identity is not used as canonical metadata.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
