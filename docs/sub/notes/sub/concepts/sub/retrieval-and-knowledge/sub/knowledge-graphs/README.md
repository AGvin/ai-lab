# Knowledge Graphs

Legacy residual retained for domain-schema design, entity-resolution workflow, provenance/governance, lifecycle maintenance, and architecture-selection guidance that are intentionally outside the canonical Knowledge Graphs concept owner.

> **Migration note:** Knowledge-graph identity, graph-database and arbitrary-graph separation, schema/ontology spectrum, stable identity/entity resolution, asserted-versus-derived fact status, provenance/authority, temporal/contextual validity, completeness assumptions, reasoning/validation boundaries, and separation from GraphRAG are already preserved in `docs/sub/concepts/sub/reasoning-and-decision-making/sub/knowledge-representation/sub/knowledge-graphs/`. The remaining material below stays here until its exact learning, knowledge-engineering, governance, evaluation, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Domain-schema residual

Design entity types, relationship types, qualifiers, and constraints around the decisions and queries the graph must support rather than turning every noun or mention into a node. Use stable identifiers and make aliases/entity resolution explicit enough that records from different sources can be joined without silently merging different entities.

Keep relationship semantics precise. Dependency, ownership, membership, citation, temporal succession, similarity, and causality are not interchangeable merely because they can all be represented as edges.

## Provenance and governance residual

Record where facts came from, their source/authority, when they were valid, and whether they were asserted, imported, extracted, inferred, or generated when those distinctions matter. Automatically extracted nodes/edges should not become canonical truth without appropriate validation.

Define governance for schema/vocabulary evolution, entity merges/splits, conflicting claims, inferred facts, access boundaries, and quality review. Preserve enough provenance to reverse or re-evaluate derived graph state when source evidence changes.

## Lifecycle and evaluation residual

Continuously account for source updates, temporal validity, deleted/merged entities, stale derived relations, and graph completeness assumptions. Missing edges should not be interpreted as false unless the domain explicitly uses a closed-world contract.

Evaluate entity resolution, relation accuracy, provenance coverage, query/path usefulness, and downstream application outcomes separately enough to find graph-quality defects before they propagate into retrieval or reasoning.

## Architecture-selection residual

Use a knowledge graph when explicit relationships, integration across heterogeneous sources, multi-hop queries, dependency/impact analysis, or semantic identity provide material value. Prefer a simpler relational table, document index, or ordinary retrieval system when the workload does not justify graph modeling and governance overhead.

These domain-schema, provenance, governance, lifecycle, evaluation, and architecture-selection practices remain migration source material until their exact learning, knowledge-engineering, governance, evaluation, or decision-support owners are verified.
