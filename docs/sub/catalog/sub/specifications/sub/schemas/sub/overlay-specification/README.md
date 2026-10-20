# Overlay Specification

## Relations

- Produced by: [OpenAPI Initiative](../../../../../producers/sub/o/sub/openapi-initiative/)

## Purpose and published contract

Overlay defines a separate JSON or YAML document for repeatable changes to an OpenAPI description. It supports augmentation, removal, and transformation while retaining the overlay as a distinct artifact from the source description. The represented published contract is **Overlay 1.2.0, dated September 22, 2026**. [Published specification](https://spec.openapis.org/overlay/v1.2.0.html).

## Transformation scope

Actions are applied in their defined order. Their targets use RFC 9535 JSONPath, while update, remove, copy, and reusable-action behavior follow the versioned Overlay semantics. Source-description selection, `extends`, `$self`, and relative-reference resolution must be interpreted under that same version; their presence in 1.2.0 does not establish support in older releases.

Overlay changes an API description. The OpenAPI Specification defines that description's HTTP API contract, Arazzo describes API workflows, and JSON Schema retains its own data-validation semantics. A transformation tool implements the Overlay contract and has a separate software lifecycle.

## Implementation boundaries

Validate the resulting description as well as the overlay under the applicable versions. A published Overlay feature does not imply that every client generator, API importer, validator, or overlay applicator implements it. Use the official release for normative requirements and the specific tool's documentation for supported behavior; draft changes and vendor defaults are not universal conformance guarantees.

## Official resources

- [Overlay 1.2.0 — published specification](https://spec.openapis.org/overlay/v1.2.0.html)
- [Published specification index](https://spec.openapis.org/overlay/)
- [Overlay Specification repository](https://github.com/OAI/Overlay-Specification)
