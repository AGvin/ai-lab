# Documentation Requirements

## Requirements

- Identify Z-Image as a model family rather than one concrete trained model.
- Preserve the current source-backed approximately 6B family scale and S3-DiT architecture context.
- Distinguish the materialized Z-Image base model and Z-Image-Turbo as separate concrete trained models, while keeping Z-Image-Omni-Base and Z-Image-Edit as distinct upstream variants that must not be materialized until independently reviewed and required by scope.
- Preserve canonical producer, family-membership, and derivative-lineage metadata without duplicating model-specific facts at the family level.
- Keep runtime integration, hosted access, hardware fit, privacy/security workflow, benchmark rankings, and selection conclusions outside the canonical family profile.

## Validation

- The family is not collapsed into the base `Tongyi-MAI/Z-Image` model repository.
- Z-Image-Turbo is represented as a distinct materialized model and is not collapsed into the base model.
- Unreviewed variants are not created as empty placeholders.
- Legacy Alibaba placement is not converted into an unsupported canonical producer relation.
