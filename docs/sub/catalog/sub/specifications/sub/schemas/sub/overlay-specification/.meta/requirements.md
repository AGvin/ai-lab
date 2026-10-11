# Documentation Requirements

## Requirements

- Identify the OpenAPI Initiative's Overlay Specification as an independently published formal JSON/YAML document and transformation contract for repeatably augmenting, removing or changing content in an OpenAPI description while keeping the overlay separate from its source description.
- Record the current published **Overlay v1.2.0, dated 2026-09-22**, with the official released specification as the normative authority, not a rolling editor draft or a vendor's implementation.
- Explain the order of overlay actions, RFC 9535 JSONPath target matching, update/remove/copy and reusable-action semantics, the source description/extension and relative-reference boundaries according to the current versioned specification. Version-specific fields such as `$self` and `extends` must not be generalized to historical releases.
- Distinguish Overlay from the OpenAPI Specification's HTTP API description core, Arazzo's API workflow-description contract, JSON Schema itself, and concrete tools that apply overlays.
- Attribute specification governance to OpenAPI Initiative with a reciprocal `produced-by` / `produces` relation.
- Avoid implying all API clients, generators or validators implement every published overlay feature; keep product support with implementation owners.

## Validation

- Normative behavior and version labels correspond to the official released Overlay specification.
- The canonical identity is not duplicated as an OAS feature, transformation library, agent tool, or Arazzo workflow.
- The existing OpenAPI Initiative producer inverses this record's `produced-by` relation.
