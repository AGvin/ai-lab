# Documentation Requirements

## Requirements

- Present Specifications as the catalog domain for identifiable formal or normative artifacts/contracts whose primary identity is a specification rather than a software product, service, model, hardware item, dataset, producer, Agent Skill, reusable concept, or learning topic.
- Organize specification artifacts by the selected first-level groups `protocols/`, `formats/`, `schemas/`, `standards/`, and `semantic-conventions/`; materialize only groups with real source-backed content/navigation value.
- Use `semantic-conventions/` for formal semantic-convention specifications whose primary identity is a normative telemetry/data vocabulary or attribute contract, rather than forcing them into protocols, formats, schemas, or broader standards.
- Keep normative/versioned requirements sourced from the authoritative specification or upstream maintainer and preserve the applicable version/freshness boundary instead of silently converting historical wording into current truth.
- Keep explanatory concepts and tutorials with `concepts/` or `learning/`; keep concrete implementations, SDKs, runtimes, products, support matrices, and compatibility facts with their applicable catalog/evidence owners.
- Render standard direct-child navigation from only the currently materialized specification groups when rendering is activated.

## Validation

- The domain is not used as a generic reference/documentation bucket.
- A formal artifact is not duplicated as a concept or tutorial merely because explanation exists elsewhere.
- Semantic-convention specifications are not misclassified as schemas merely because implementations may serialize their attributes into structured data.
- Current navigation exposes only materialized children and does not imply that unmaterialized selected groups are absent from the logical architecture.
