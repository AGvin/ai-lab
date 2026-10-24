# Documentation Requirements

## Requirements

- Identify Orbax Checkpoint as the independently packaged, open-source Python checkpointing library installed as orbax-checkpoint and imported through orbax.checkpoint for JAX model and training-state persistence and recovery.
- Place it under Model Development because its primary role is training-state save/restore, distributed arrays, checkpoint scheduling and recovery. Do not imply Git-like source/data provenance or a general experiment-lineage platform.
- Keep separately packaged Orbax Export and its TensorFlow SavedModel export role outside this checkpoint node. Shared repository hosting does not make the two packages interchangeable.
- Preserve Google producer provenance and the first-party paper's Google and Google DeepMind contributor context without asserting exclusive authorship or JAX-core governance.
- Preserve the current package metadata's Beta development classifier. Published releases do not imply stable APIs or interchangeability between the legacy V0 and V1 interfaces.
- Explain synchronous versus asynchronous persistence and require completion/error handling through the selected API before relying on a save; checkpoint structure and target sharding must match the restore workflow.
- Treat JAX/Python versions, API migration, storage formats/backends, checkpoint layout, cross-topology restore and custom handlers as release-sensitive. Attribute speed claims to the measured workload, hardware and storage configuration.
- Render the standard entity-relations block from validated current-entity relations and include official package, repository, documentation and migration references.

## Validation

- The node covers orbax-checkpoint, not the complete Orbax repository or a model-serving product.
- Beta and V0/V1 boundaries remain visible when operational guidance is rendered.
- Google producer provenance is reciprocal and every rendered destination resolves.
