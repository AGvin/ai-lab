# Documentation Requirements

## Requirements

- Present Protocols as the specification group for identifiable formal communication/interoperability protocol contracts whose normative identity belongs in the catalog.
- Create one canonical child per explicitly selected concrete protocol; do not create generic protocol artifacts merely because a concept or tutorial discusses communication.
- Preserve authoritative versioning, wire/message contracts, capability negotiation, transport bindings, authorization/security requirements, extension/conformance rules, deprecations, and backward-compatibility boundaries only to the depth supported by the applicable protocol's first-party specification.
- Treat protocol revisions as versioned normative state: exact methods, fields, headers, error codes, required capabilities, lifecycle rules, and deprecation status must be re-checked against the active first-party specification before changing canonical requirements.
- Keep conceptual explanation with `concepts/`, implementation/how-to/debugging/operations guidance with `learning/`, and concrete clients/servers/SDKs/products/support matrices/implementation bugs with their applicable catalog/software/service/evidence owners.
- Explain that the current materialized subset contains Model Context Protocol because its exact owner `catalog/specifications/protocols/model-context-protocol/` is explicitly selected and current first-party specification material is available.
- Render standard direct-child navigation from only currently materialized concrete protocol nodes when rendering is activated.

## Validation

- The group is not used as a generic integration or API documentation bucket.
- Concrete protocol nodes cite authoritative first-party specification sources for normative claims.
- Historical protocol behavior is not silently restated as current behavior after a breaking revision.
- Current navigation exposes only materialized children and does not imply that unmaterialized protocols are absent from selected architecture.
