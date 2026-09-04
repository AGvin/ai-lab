# Documentation Requirements

## Requirements

- Use the reader-facing title `Model Architectures`.
- Present model architecture as reusable knowledge about how a model's computational components, connections, and activation paths are organized.
- Distinguish abstract architecture concepts from the concrete architecture facts of a specific model or artifact, which remain with that model's catalog owner.
- Keep architecture independent from model scale, training/adaptation method, deployment location, access/licensing, capability-frontier status, numerical precision, and practical hardware fit.
- Explain that architecture can materially affect computation, memory access, communication, runtime support, and other execution behavior without treating those consequences as universal performance guarantees.
- Treat dense-versus-sparse activation as one architecture dimension within this domain rather than as a complete classification of every model architecture.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep model-selection fields, concrete hardware recommendations, current benchmark outcomes, and mutable implementation support outside this concept overview.

## Validation

- The page does not use architecture labels as synonyms for model size, deployment mode, quantization, frontier status, or suitability.
- The page does not present one architecture as universally faster, cheaper, more capable, or easier to deploy.
- Direct-child navigation contains only currently materialized direct children and does not imply that every selected architecture node is already implemented.
- Concrete model facts and model-selection guidance are not duplicated into the abstract architecture owner.
