# Documentation Requirements

## Requirements

- Teach Knowledge Graphs as explicit entity/relation knowledge models whose schema, identity, provenance, lifecycle, and governance must serve concrete decisions and queries.
- Design entity/relationship types, qualifiers, and constraints around workload needs rather than turning every noun or mention into a node.
- Use stable identifiers and explicit aliases/entity resolution so heterogeneous records can be joined without silently merging different entities.
- Keep relationship semantics precise: dependency, ownership, membership, citation, temporal succession, similarity, and causality are not interchangeable merely because all can be graph edges.
- Record source/authority, temporal validity, and whether facts are asserted, imported, extracted, inferred, or generated when those distinctions matter; automatically extracted graph content requires appropriate validation before canonical use.
- Define lifecycle/governance for schema evolution, entity merges/splits, conflicting claims, inferred facts, deleted sources, stale derived relations, and quality review; preserve enough provenance to reverse or re-evaluate derived state.
- Evaluate entity resolution, relation accuracy, provenance coverage, query/path usefulness, and downstream outcomes separately; missing edges are not automatically false without a closed-world contract.
- Prefer simpler relational/document/retrieval structures when explicit graph relationships do not justify modeling and governance overhead.

## Validation

- Entity resolution does not silently collapse distinct entities.
- Derived/extracted facts remain distinguishable from authoritative assertions.
- Temporal/provenance/lifecycle information is sufficient to re-evaluate stale graph state.
- Graph architecture is selected for workload value, not novelty.
