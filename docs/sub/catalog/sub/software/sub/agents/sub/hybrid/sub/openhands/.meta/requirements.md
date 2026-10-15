# Documentation Requirements

## Requirements

- Identify OpenHands as the AI-driven development platform spanning the current Agent Canvas browser client, Software Agent SDK and Agent Server, hosted OpenHands Cloud, and Enterprise/self-hosting surfaces; treat the older CLI and Local GUI as legacy interfaces rather than the primary current browser experience.
- Preserve the Hybrid Agent classification: local user-controlled execution and first-party hosted Cloud execution are both material supported product surfaces.
- Keep Agent Canvas, SDK/Agent Server, Sandbox Server, Cloud, and Enterprise execution/deployment surfaces distinct; Agent Canvas can connect to local, self-hosted, Cloud, or Enterprise backends, while the legacy Local GUI is deprecated.
- Preserve useful legacy operational boundaries around filesystem and shell access, repository permissions, backend/runtime isolation, integration scopes, automation triggers, credentials, and human approval gates.
- Keep licensing scoped to each current component and its upstream repository; the separated Agent Canvas, Software Agent SDK, Sandbox Server, and legacy repositories may have different license terms. Do not apply the old monorepo or enterprise-directory license boundary to the complete ecosystem.
- Keep mutable hosted-service, enterprise-license, integration, model-provider, deployment, and pricing details source-backed when expanded.
- Include current official OpenHands documentation and repository references.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The profile does not describe OpenHands Cloud as the only execution surface.
- The profile does not treat the Software Agent SDK as a separate replacement identity for the OpenHands product represented here.
- Licensing language verifies each active component's repository independently and does not imply that the legacy monorepo or Enterprise licensing applies universally.
- The Hybrid classification remains supported by explicit local and hosted execution surfaces.
- Official resource links match canonical entity metadata.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
