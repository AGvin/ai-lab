# Documentation Requirements

## Requirements

- Explain shared request/response objects, context items, tool handoffs and semantic streaming events as specification-defined interfaces.
- Keep exact JSON fields, HTTP semantics, state transitions, extensions and interoperability guarantees tied to the current source and changelog.
- Distinguish schema compatibility from provider implementations, access, supported features and runtime conformance.
- Never imply that using a unified API removes authentication, application authorization, data governance or prompt-injection risks.

## Validation

- Canonical identity and first-party references match the current frozen cohort source lead.
- Version and source maturity are explicit and no implementation, availability or conformance is invented.

## Scoped original-source qualification — 2026-11-07

- Open Responses is an open provider-neutral response API interoperability specification modeled on Responses API concepts: item-based inputs/outputs, tool delegation, result states and semantic streaming. It defines the shared schema and behavioral vocabulary; it is not itself a hosted endpoint, model, adapter or guarantee that a named provider implements every field.
- The official upstream specification publishes normative schema/semantics and governance/acceptance-test materials. API authentication, streaming timing, tool permissions, data residency, model availability, refusal/safety behavior and provider-specific extension mapping remain deployment-specific. Validate conformance with exact release and adapters rather than inferring feature parity.
- Verified primary source 1: https://www.openresponses.org/specification
- Verified primary source 2: https://www.openresponses.org/
- Existing interoperability-specification identity/source accepted only; no multi-provider live API, SDK, contract/security/privacy audit, conformance suite, root-wide schema/cache/CI/render, clean pass or final gate.
