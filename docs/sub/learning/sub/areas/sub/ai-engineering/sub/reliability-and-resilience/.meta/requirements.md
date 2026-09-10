# Documentation Requirements

## Requirements

- Present Reliability and Resilience as system-level teaching for keeping AI applications dependable across transient failures, capability gaps, unavailable dependencies, and reduced-capability operation.
- Materialize and link `timeouts-and-retries/`, `fallbacks/`, and `degraded-modes/` because each has source-backed material ready for migration; leave other selected children unmaterialized until they have real content.
- Keep model-selection recommendations with Model Selection, privacy/security/policy definitions with Trustworthy AI or governance owners, and concrete provider/service availability with current Catalog/Evidence owners.
- Treat alternate routes as eligible only when they satisfy the minimum workflow contract, including required modality, context/output behavior, schema/tool interfaces, latency/cost constraints, and applicable data-handling, licensing, and provider-boundary requirements.
- Require failure conditions and recovery transitions to be explicit enough to test; availability alone does not make an alternate route a valid fallback.
- Avoid recovery behavior that hides persistent defects or silently changes required application constraints.

## Validation

- Reliability mechanisms do not redefine model capability or privacy/policy rules.
- Alternate routes are contract-checked rather than assumed interchangeable.
- Current provider/service state remains external mutable evidence.
- Only source-backed selected children are materialized.
