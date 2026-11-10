# Documentation Requirements

## Requirements

- Present the OpenAPI Initiative's Arazzo Specification as a formal, machine-readable API workflow-description contract for a sequence of dependent API calls and their expected outcomes, not as a runnable orchestration engine, AI agent framework, or an extension of the OAS document schema.
- Record **Arazzo v1.1.0, published 2026-05-17**, as the current independently released specification boundary, citing the official published version rather than assuming the editor's draft is normative.
- Describe workflow source descriptions, reusable workflows, steps, dependencies, inputs/outputs, success/failure criteria and runtime expressions only to the depth supported by the versioned official specification. Distinguish API workflow descriptions from executing those workflows.
- Preserve Arazzo's API-description references (including its supported OpenAPI and AsyncAPI boundaries) without duplicating the normative OpenAPI Specification, Overlay Specification, API servers, or concrete implementation SDKs.
- Attribute publication/governance to the OpenAPI Initiative with a reciprocal `produced-by` / `produces` relation.
- Treat compatible tooling, workflow runners, validators, SDK support, and provider-specific behavior as independently mutable implementation facts.

## Reader projection

- Render the standard `entity-relations` block from all validated current-entity relations eligible for reader presentation.
- Render the `official-resources` block from canonical references supporting the identity, versioned facts, access context, and stated boundaries of this page.

## Validation

- The referenced version is a released official Arazzo specification, not a draft or implementation example.
- Arazzo is not conflated with API endpoint schemas, agent-to-agent communication protocols, or orchestration software.
- The OpenAPI Initiative producer has the inverse `produces` relation to this exact canonical identity.

## Scoped original-source qualification — 2026-11-07

- Arazzo v1.1.0 (published 2026-05-17) is the OpenAPI Initiative's independently versioned machine-readable description of API workflows. It expresses a sequence of dependent operations, source API descriptions, step outputs and success/failure criteria, without providing a workflow executor or runtime authentication implementation.
- Arazzo can reference supported OpenAPI and AsyncAPI source documents; it does not replace those descriptions or make their client libraries universally compatible. Implementation support, error handling, resolution of runtime expressions and authorization require separate tooling evidence and version-aware validation.
- Verified first-party source 1: https://spec.openapis.org/arazzo/v1.1.0.html
- Verified first-party source 2: https://spec.openapis.org/arazzo/
- Source qualification covers the existing published specification identity and bounded semantics. No Arazzo interpreter, API workflow, credentials, external service, conformance suite, full legal/security audit, repository-wide clean pass or final gate was executed.
