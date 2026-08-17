# Documentation Requirements

## Requirements

- Identify MLX LM as Apple's MLX-based Python package for generating text and fine-tuning large language models, primarily on Apple silicon.
- Preserve Apple Inc. as the canonical producer through the standard relation projection.
- Preserve its selected placement under `inference-runtimes/inference-engines`; fine-tuning, quantization, conversion, and local HTTP serving are additional capabilities of the same MLX LM package.
- Preserve the boundary between MLX LM and the lower-level MLX array framework.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Do not recommend the bundled basic HTTP server as production-ready when current upstream documentation explicitly cautions against that use.
- Keep model support, distributed behavior, MLX version requirements, server features, and other mutable implementation details source-backed when expanded.
- Include the current official MLX LM repository and Apple Machine Learning Research references.

## Validation

- The page distinguishes MLX LM from the general MLX framework.
- Apple producer provenance is not generalized into ownership of third-party model artifacts used with MLX LM.
- Basic server capability is not overstated as a production serving platform.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
