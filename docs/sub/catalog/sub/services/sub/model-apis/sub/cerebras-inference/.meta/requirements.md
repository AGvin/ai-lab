# Documentation Requirements

## Requirements

- Identify Cerebras Inference as Cerebras Systems Inc.'s hosted inference-as-a-service offering for remote model access.
- Preserve Cerebras's current distinction between production models and preview models; preview availability must not be used as evidence that a model or feature is production-stable.
- Keep third-party model identity, licensing, lifecycle, and intrinsic model facts with their canonical model owners.
- Treat model inventory, pricing, rate limits, API behavior, context limits, throughput, availability, and other service state as mutable and time-scoped.
- Keep the hosted service distinct from Cerebras hardware systems and self-managed software stacks.
- Render the standard `entity-relations` block and preserve Cerebras Systems Inc. as the producer.

## Validation

- Preview models are not described as production-stable merely because they are callable.
- The page remains a hosted model-API service profile rather than a hardware or model profile.
- The `produces` / `produced-by` relation pair resolves consistently to Cerebras Systems Inc.
