# Documentation Requirements

## Requirements

- Present Microsoft Foundry Agent Service as Microsoft's generally available managed platform for building, deploying, versioning, publishing, running, and scaling production AI agents.
- Preserve its managed-service boundary across Prompt Agents, Hosted Agents, stateful conversations/responses, managed infrastructure, identity, monitoring, publishing, and supported agent-to-agent integration.
- Keep Microsoft Agent Framework as installable agent-framework software, Copilot Studio as a separate managed agent/application product, Microsoft Entra Agent ID/Registry surfaces with their own owners, and underlying Foundry model identities/catalog entries separate.
- Preserve GA versus preview boundaries for individual Agent Service tools/capabilities; feature-level preview does not make the whole GA service preview and GA service status does not make every feature GA.
- Treat supported regions/models/tools, quotas, pricing, BYO resources, networking, storage, memory, protocol versions, publishing destinations, and hosted-agent runtime behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.

## Validation

- Foundry Agent Service remains a managed agent runtime/platform identity rather than an agent framework or assistant workspace.
- Prompt/Hosted Agent variants remain service capabilities rather than peer service identities by default.
- Producer provenance resolves bidirectionally to Microsoft.

## Scoped original-source qualification — 2026-11-06

- Microsoft Foundry Agent Service offers managed Prompt Agents and Hosted Agents, with service-managed runtime, conversations, tool calls, versions, identity and publishing. Microsoft Agent Framework SDK, Copilot Studio, Entra Agent Registry and underlying Foundry model catalog remain separate identities; supported tools and preview features vary by release.
- Microsoft's official migration guidance distinguishes new v1 API generally available Hosted Agents from an initial hosted-agent preview backend whose support ended on 2026-08-20. Old deployments are not automatically migrated; API protocols, session provisioning and Entra agent identities changed. Do not treat legacy preview SDKs, old agent_reference routes or flags as the current GA contract.
- Service and feature GA must be evaluated separately: browser automation, optimization, workflows, regions, networking and BYO dependencies can have preview or constrained support. Authentication, RBAC, quotas, stored data and release compatibility are tenant/region scoped; no authenticated runtime test was performed.
- Verified first-party source 1: https://learn.microsoft.com/en-us/azure/foundry/agents/overview
- Verified first-party source 2: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-hosted-agent-preview
- Source acceptance covers service identity and publisher-scoped limits, not full lifecycle freshness, authenticated provider execution, independent security/legal assurance, root-wide schema/cache/CI/render, reader repairs, clean passes or final delivery.
