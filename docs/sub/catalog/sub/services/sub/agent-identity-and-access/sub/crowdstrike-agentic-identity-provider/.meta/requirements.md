# Documentation Requirements

## Requirements

- Present CrowdStrike Agentic Identity Provider as an identity/access-first managed product for establishing trusted AI-agent identities and brokering scoped, contextual access.
- Cover short-lived/scoped authorization, human/system attribution, and risk-adaptive access only as capabilities of the same agent-identity service.
- Keep the entity distinct from CrowdStrike's broader endpoint/security platform and from generic AI-security posture or runtime-guardrail products.
- Treat availability, packaging, licensing, supported identity flows, integrations, and access-policy behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains agent identity/access-first rather than a generic cybersecurity platform identity.
- Producer provenance resolves to CrowdStrike.

## Scoped original-source qualification — 2026-11-06

- CrowdStrike's September 2, 2026 original announcement positions Agentic Identity Provider inside Falcon Next-Gen Identity Security: automatically registered agent identities, cryptographically verifiable identity, short-lived scope-limited access tokens and attribution to originating human or workload. These are provider-announced capabilities, not independently validated spoofing resistance or guaranteed enterprise availability.
- Keep the identity provider distinct from the broader Falcon cybersecurity suite, Falcon Guardian discovery and Continuous Identity runtime contextual authorization. Product announcement and launch messaging do not prove each module or API is generally available, supported in every geography, or operationally certified.
- Access is still governed by customer identity context, policies, integrations and application permissions. Source qualification does not test real OAuth flows, session revocation, misconfiguration or threat-model coverage.
- Verified first-party source 1: https://www.crowdstrike.com/en-us/press-releases/crowdstrike-agentic-identity-provider-foundation-for-ai-agent-identity-security/
- Verified first-party source 2: https://www.crowdstrike.com/en-us/blog/crowdstrike-announces-agentic-identity-provider/
- Source acceptance credits the existing identity and provider-scoped capability boundaries only; no new entity or metadata, independently tested OAuth/IAM behavior, full freshness/privacy/legal/security audit, whole-repository schema/cache/CI/render, reader repair, clean pass, final gate or merge.
