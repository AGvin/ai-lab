# Documentation Requirements

## Requirements

- Describe page-provided script-defined agent tools and their distinction from server-hosted Model Context Protocol integrations.
- Identify the 2 November 2026 Community Group Draft as explicitly not a W3C Standard or Standards Track specification.
- Keep model context interface, tool registration, permission policies, execution and event handling tied to the dated draft.
- Explain material security/privacy risks: malicious tool metadata, prompt injection via outputs, unintended page actions and excessive information disclosure; require application consent and authorization.

## Validation

- Canonical identity and first-party references match the current frozen cohort source lead.
- Version and source maturity are explicit and no implementation, availability or conformance is invented.

## Scoped original-source qualification — 2026-11-07

- WebMCP is an evolving browser-side JavaScript tool exposure interface that allows a web application to register structured tools for AI agents, using its existing page context. It is not an external hosted MCP server, identical to the Model Context Protocol wire contract or proof of a browser's shipped implementation.
- The current upstream **Draft Community Group Report is dated 2 November 2026** when checked on 7 November; the prior catalog cited 15 October 2026. The draft explicitly states it is **not a W3C Standard or on the W3C Standards Track**. API details, document events, permission policy and security requirements may still change.
- Tool descriptions, inputs, outputs and page actions are prompt-injection, unintended side-effect and privacy boundaries. Browser/user authorization, same-origin restrictions and risky action approvals must be reviewed independently.
- Verified first-party source 1: https://webmachinelearning.github.io/webmcp/
- Verified first-party source 2: https://github.com/webmachinelearning/webmcp
- Source acceptance covers only the existing rolling community proposal identity and dated draft boundary; no user consent/browser tool registration, active service, penetration test, complete legal/privacy/security audit, repository-wide schema/cache/CI/render, clean pass or final gate.
