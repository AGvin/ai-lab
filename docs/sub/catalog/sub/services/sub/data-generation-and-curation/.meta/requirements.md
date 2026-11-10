# Documentation Requirements

## Requirements

- Present `data-generation-and-curation/` as the canonical service owner for producer-operated products whose primary identity is creating, labeling, curating, transforming, synthesizing, reviewing, or otherwise preparing data for AI training, evaluation, testing, alignment, or application-development workflows.
- Allow evaluation, red teaming, preference collection, expert review, programmatic labeling, synthetic generation, and quality analysis when those capabilities primarily serve data production or improvement.
- Distinguish working corpus/artifact lifecycles from live application retrieval/context state, which belongs under `services/data-infrastructure/`.
- Exclude evaluation/observability products whose primary role is measuring AI-system behavior, AI-security products whose primary role is threat protection, generic ETL/integration services without an AI-data production identity, and self-managed curation/synthetic-data software.
- Keep the category flat until materialized density creates a genuine canonical-placement problem between expert/human data and synthetic/transformed data.

## Validation

- Children are independently identifiable managed AI-data production/curation services.
- The category does not become a generic data-lifecycle catch-all.
- Navigation matches validated materialized direct children.
