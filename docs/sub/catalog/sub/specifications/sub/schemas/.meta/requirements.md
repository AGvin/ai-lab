# Documentation Requirements

## Requirements

- Present Schemas as the specification group for independently identifiable formal schema systems whose primary identity is a normative data model, record/schema vocabulary, validation contract, or schema framework.
- Materialize only schema artifacts with durable interoperability value and an authoritative upstream specification or released schema source.
- Preserve versioning, compatibility, extension, validation, and immutability rules only to the depth supported by authoritative upstream sources.
- Keep transport/interaction protocols under `protocols/`, serialization or file formats under `formats/`, semantic telemetry/data vocabularies under `semantic-conventions/`, and broader formal standards under `standards/`.
- Keep schema servers, SDKs, validators, registries, concrete implementations, and operational deployment guidance with their applicable software/service owners unless they are inseparable reference surfaces for the canonical schema identity.
- Render standard direct-child navigation only after the final research/intake phase is complete.

## Validation

- Every child is an independently identifiable formal schema specification/framework rather than a generic data-model concept or implementation library.
- Normative claims are traceable to authoritative upstream schema/specification sources and preserve explicit version/stability boundaries.
- The category does not duplicate protocol, format, semantic-convention, or software identities.
