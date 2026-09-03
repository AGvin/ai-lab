
# Documentation Requirements

## Requirements

- Own canonical factual model documentation directly under `catalog/models/`.
- Treat every first-level child as a model-domain producer or stable publishing/steward namespace; do not create task, modality, architecture, license, access, benchmark, recommendation, or lifecycle sibling roots.
- Preserve the producer -> family -> optional series -> model -> version/artifact identity hierarchy, omitting structural levels that are not meaningful.
- Keep the model-domain producer namespace distinct from the canonical producer profile under `catalog/producers/`; preserve explicit producer relations rather than inferring exclusive authorship from placement.
- Keep provider access, hosted offerings, runtimes, deployment routes, and other non-model entities with their canonical service/software owners.
- Keep model comparison, recommendation, hardware-fit, scenario, and portfolio decisions under `decision-support/` and link canonical model facts instead of duplicating them.
- Keep supported technical facts traceable to authoritative or upstream references.
- Preserve total and active parameters as distinct facts when both materially describe a model; do not infer unpublished expert/routing values from names or arithmetic.

## Validation

- Every materialized producer/family/series/model/version/artifact entity has a path-derived `entity.id` matching its current canonical node.
- Model relations resolve to current canonical entity IDs and required bidirectional endpoints remain synchronized.
- No `catalog/models/` or `decision-support/selection/models/` ownership path remains in canonical metadata.
- Decision-support conclusions are not represented as intrinsic model facts.
