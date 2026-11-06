# Documentation Requirements

## Requirements

- Present Okta for AI Agents as a generally available agent-specific identity product for registering, managing, securing, and governing AI-agent identities with least-privilege access.
- Keep generic workforce/customer identity features outside this profile unless they directly define the AI-agent product surface.
- Distinguish GA capabilities from separately early-access or roadmap agent-gateway/tool-governance features.
- Treat SKU availability, feature lifecycle, supported integrations, token/credential flows, and licensing as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Okta for AI Agents remains agent identity/access-first rather than generic IAM or AI management.
- Producer provenance resolves to Okta.

## Scoped original-source qualification — 2026-11-06

- Okta for AI Agents is a generally available agent identity/governance product, with current first-party support describing registration in Universal Directory, owner binding, agent discovery, least-privilege short-lived access, access certification and deactivation. Okta's published feature calendar distinguishes already released controls from upcoming/early-access Agent Gateway, endpoint discovery and agent-threat functions.
- Current Okta materials disagree on release-article date while older official support establishes 2026 GA; avoid a fabricated single precise milestone. Product GA is not evidence that every agent integration, browser discovery method or runtime kill switch is GA. Agent-to-agent connection and Agent SSO availability must be checked per release.
- An agent's registered identity does not grant blanket access to enterprise systems: provisioning, ownership, OAuth scopes, token storage, authorization policy, approvals, SIEM logging and data processing remain customer-specific.
- Verified first-party source 1: https://support.okta.com/help/s/article/okta-secures-ai?language=en_US
- Verified first-party source 2: https://www.okta.com/products/govern-ai-agent-identity/
- Verified first-party source 3: https://www.okta.com/newsroom/press-releases/ai-innovations-oktane-2026/
- Source acceptance credits the existing identity and provider-scoped capability boundaries only; no new entity or metadata, independently tested OAuth/IAM behavior, full freshness/privacy/legal/security audit, whole-repository schema/cache/CI/render, reader repair, clean pass, final gate or merge.
