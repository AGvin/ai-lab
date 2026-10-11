# Documentation Requirements

## Requirements

- Present the OpenAPI Initiative's Arazzo Specification as a formal, machine-readable API workflow-description contract for a sequence of dependent API calls and their expected outcomes, not as a runnable orchestration engine, AI agent framework, or an extension of the OAS document schema.
- Record **Arazzo v1.1.0, published 2026-05-17**, as the current independently released specification boundary, citing the official published version rather than assuming the editor's draft is normative.
- Describe workflow source descriptions, reusable workflows, steps, dependencies, inputs/outputs, success/failure criteria and runtime expressions only to the depth supported by the versioned official specification. Distinguish API workflow descriptions from executing those workflows.
- Preserve Arazzo's API-description references (including its supported OpenAPI and AsyncAPI boundaries) without duplicating the normative OpenAPI Specification, Overlay Specification, API servers, or concrete implementation SDKs.
- Attribute publication/governance to the OpenAPI Initiative with a reciprocal `produced-by` / `produces` relation.
- Treat compatible tooling, workflow runners, validators, SDK support, and provider-specific behavior as independently mutable implementation facts.

## Validation

- The referenced version is a released official Arazzo specification, not a draft or implementation example.
- Arazzo is not conflated with API endpoint schemas, agent-to-agent communication protocols, or orchestration software.
- The OpenAPI Initiative producer has the inverse `produces` relation to this exact canonical identity.
