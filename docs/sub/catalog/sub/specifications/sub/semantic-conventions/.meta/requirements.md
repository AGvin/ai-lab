# Documentation Requirements

## Requirements

- Present `semantic-conventions/` as the factual catalog owner for identifiable formal semantic-convention specifications that define interoperable telemetry or data semantics through named attributes, event/span conventions, or equivalent normative vocabulary contracts.
- Keep semantic conventions distinct from transport protocols, serialization/response formats, validation schemas, and broader standards.
- Materialize only independently identifiable upstream specifications with durable interoperability value.
- Keep SDKs, instrumentation libraries, exporters, collectors, observability platforms, and implementation-specific support matrices with their software/service owners.
- Preserve specification/version and stability boundaries from authoritative upstream sources; do not silently treat experimental attributes as stable requirements.

## Validation

- Every child is a formal semantic-convention specification rather than a generic observability concept or implementation library.
- Normative vocabulary claims are source-backed and version/stability scoped.
- The category does not duplicate OpenTelemetry or other implementation/platform identities.
