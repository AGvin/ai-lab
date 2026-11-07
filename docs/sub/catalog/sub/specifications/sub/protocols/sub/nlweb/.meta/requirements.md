# Documentation Requirements

## Requirements

- Identify NLWeb as a published open natural-language web interaction protocol, rather than its Python reference implementation, formal TypeSpec files, hosted services, or individual site deployments.
- Preserve the first-party published v0.55 boundary observed on 2026-11-01, including `ask`, asynchronous `await`, structured request/response semantics, JSON-LD/Schema.org extensibility, and HTTP/MCP transport bindings; re-check upstream before asserting exact normative fields, revisions, or compatibility.
- Distinguish NLWeb from MCP tool/context exchange, A2A agent coordination and AG-UI agent/frontend interaction; integrations do not make those protocols equivalent.
- Do not imply that all NLWeb servers implement every protocol option, transport, mode, UI integration, or LLM/vector connector named by a reference implementation.
- Preserve historical Microsoft launch provenance and current `nlweb-ai` repository stewardship as separate facts; do not infer present beneficial ownership or exclusive corporate control from a founding announcement.
- Distinguish the published full specification v0.55 from the separate TypeSpec repository's v0.5 revision; do not silently normalize version differences.
- Explain that authentication, authorization and rate limiting are outside the protocol's core definition and remain transport/deployment responsibilities. Address untrusted content and sensitive-data exposure without claiming runtime compliance or security evaluation.
- Keep implementation-specific setup, model/provider support, SDK behavior, performance, availability and production readiness outside this protocol identity.

## Validation

- One canonical protocol identity and no duplicate implementation/product identity are introduced.
- Normative claims are grounded in the current first-party specification and versioned, not represented as stable 1.0 behavior.
- Origin, current project hosting and legal ownership are not conflated.
- All catalog navigation and official-reference links are present; full render/cache/global schema validation remains a separate final-phase gate.

## Scoped original-source qualification — 2026-11-07

- NLWeb is an open, transport-agnostic protocol for natural-language interaction with sites and services; its first-party published specification currently identifies **v0.55**, separately from the Python proof-of-concept reference implementation and a TypeSpec snapshot historically marked v0.5.
- The `ask` request and asynchronous `await` promise flow support structured JSON-LD/Schema.org-style responses, session/metadata and HTTP/MCP bindings. The protocol does not itself implement site ownership checks, authentication, rate limiting, content licenses or safe execution of delegated actions. Microsoft's 2025 launch provenance does not establish sole present ownership.
- Verified first-party source 1: https://nlweb.ai/docs/specification
- Verified first-party source 2: https://github.com/nlweb-ai/website/blob/main/NLWEBSPEC.md
- Verified first-party source 3: https://github.com/nlweb-ai/NLWeb
- Existing NLWeb protocol/source gate only; no reference server deployed, website indexed, API exercised, data privacy/rights audited, whole-repository schema/cache/CI/render, clean pass or final gate.
