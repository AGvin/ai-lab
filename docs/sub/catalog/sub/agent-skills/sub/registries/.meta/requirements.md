# Documentation Requirements

## Requirements

- Present Agent Skill registries as identifiable multi-source services, directories, marketplaces, or installer-backed indexes for discovering, evaluating, distributing, or installing Agent Skills.
- Distinguish registries from `collections/`: a collection is a publisher/repository-owned set of skills, while a registry aggregates or indexes skills from multiple independent sources.
- Keep each registry's mutable inventory, supported clients, ranking model, scanning/trust features, installation interfaces, telemetry, and organizational/private-registry behavior with that registry's own child node and current sources.
- Do not duplicate registry-indexed skills as standalone catalog entities unless they independently satisfy the standalone-skill identity rule.
- Do not treat registry presence, popularity, ranking, or security scanning as proof of skill quality or safety.
- Render direct registry children from the validated child projection; do not maintain a second hand-written registry inventory in this parent requirement.

## Validation

- Every materialized child is an identifiable registry/discovery entity rather than a publisher-owned skill collection.
- Registry facts are source-backed and freshness-sensitive where behavior can change.
- No renderer-owned README is directly edited during migration/content preparation.
