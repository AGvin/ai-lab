# Documentation Requirements

## Requirements

- Present Agent Control Standard (ACS) as an open runtime-control standard and wire-format specification for an observed AI agent to submit lifecycle/tool/context activity to a separate Guardian that can permit, deny, modify, ask about, or defer actions under an auditable control contract.
- Treat the published versioned ACS specification and conformance definitions as normative authority. Preserve the distinction between the published v0.1-series contract, repository maintenance versions, and separately staged proposals instead of inferring a new normative revision from repository metadata alone.
- Keep ACS-Core, optional conformance profiles, hook/wire semantics, audit/provenance/inspection features, transport details, and protocol-wrapping behavior version-sensitive and aligned with current normative documentation.
- Distinguish ACS from MCP and A2A: ACS can control or wrap interactions involving those protocols but is not a replacement identity for tool/context interoperability or agent-to-agent communication.
- Keep Guardian/reference implementations, SDKs, instrumentation adapters, example policies, and deployment guidance separate from the standard's normative identity.

## Validation

- Normative claims are traceable to the published ACS specification/conformance material rather than example implementation behavior.
- Proposal content is not described as shipped normative behavior until it is incorporated into a published specification revision.
- ACS is not reduced to an observability SDK, generic AI-safety framework, policy engine, or agent framework.
- Version-sensitive wire, hook, profile, and conformance details are not presented as timeless.

## Scoped original-source qualification — 2026-11-08

- The **OWASP GenAI Security Project Agent Control Standard (ACS)** is an open runtime-agent-control wire and hook specification. The upstream project identifies **v0.1.0 as its published specification baseline** and a later **v0.1.3 repository maintenance changelog**; the latter is not evidence that an independently versioned v0.2 normative contract shipped.
- In ACS-Core an observed agent reports control hooks to a separate authenticated Guardian with allow/deny/modify/ask/defer decisions. Core, optional Trace/Inspect/Crypto/Audit profiles, related telemetry and reference implementations have distinct conformance boundaries; publisher-documented self-declared conformance does not establish audited runtime enforcement or safety.
- Verified original publisher sources: https://github.com/GenAI-Security-Project/agent-control-standard and https://owaspacs.org/docs/acs/ and https://github.com/GenAI-Security-Project/agent-control-standard/blob/integration/CHANGELOG.md
- Bounded original-source qualification covers published ACS identity/version boundary, public specifications and maintainer documentation only. No live guardian/SDK tests, security assurance, independent conformance, full legal/runtime/freshness audit, root-wide schema/cache/CI/render, clean or final credit.
