# Documentation Requirements

## Requirements

- Identify the OpenAPI Initiative's Overlay Specification as an independently published formal JSON/YAML document and transformation contract for repeatably augmenting, removing or changing content in an OpenAPI description while keeping the overlay separate from its source description.
- Record the current published **Overlay v1.2.0, dated 2026-09-22**, with the official released specification as the normative authority, not a rolling editor draft or a vendor's implementation.
- Explain the order of overlay actions, RFC 9535 JSONPath target matching, update/remove/copy and reusable-action semantics, the source description/extension and relative-reference boundaries according to the current versioned specification. Version-specific fields such as `$self` and `extends` must not be generalized to historical releases.
- Distinguish Overlay from the OpenAPI Specification's HTTP API description core, Arazzo's API workflow-description contract, JSON Schema itself, and concrete tools that apply overlays.
- Attribute specification governance to OpenAPI Initiative with a reciprocal `produced-by` / `produces` relation.
- Avoid implying all API clients, generators or validators implement every published overlay feature; keep product support with implementation owners.

## Reader projection

- Render the standard `entity-relations` block from all validated current-entity relations eligible for reader presentation.
- Render the `official-resources` block from canonical references supporting the identity, versioned facts, access context, and stated boundaries of this page.

## Validation

- Normative behavior and version labels correspond to the official released Overlay specification.
- The canonical identity is not duplicated as an OAS feature, transformation library, agent tool, or Arazzo workflow.
- The existing OpenAPI Initiative producer inverses this record's `produced-by` relation.

## Scoped original-source qualification — 2026-11-07

- Overlay v1.2.0, published 2026-09-22 by the OpenAPI Initiative, is an independently versioned JSON/YAML transformation document that modifies an OpenAPI description through ordered actions and JSONPath-based targets. It is not the base API schema, a live API server, Arazzo workflow, or a universal AI-agent integration.
- The released 1.2.0 specification defines targeting, updates/removals/copies and reusable actions, with relative-reference, `extends` and `$self` semantics tied to the exact revision. A tool that reads OpenAPI does not automatically support Overlay 1.2.0; transformations require version-aware implementation and result validation.
- Verified first-party source 1: https://spec.openapis.org/overlay/v1.2.0.html
- Verified first-party source 2: https://spec.openapis.org/overlay/
- Verified first-party source 3: https://github.com/OAI/Overlay-Specification
- Source acceptance is limited to the existing formal specification and official published boundary. No transformation engine, resulting API validation, cross-tool compatibility test, full rights/security audit, root-wide schema/CI/render, clean pass or final gate.
