# Documentation Requirements

## Requirements

- Present Microsoft Foundry Agent Service as Microsoft's generally available managed platform for building, deploying, versioning, publishing, running, and scaling production AI agents.
- Preserve its managed-service boundary across Prompt Agents, Hosted Agents, stateful conversations/responses, managed infrastructure, identity, monitoring, publishing, and supported agent-to-agent integration.
- Keep Microsoft Agent Framework as installable agent-framework software, Copilot Studio as a separate managed agent/application product, Microsoft Entra Agent ID/Registry surfaces with their own owners, and underlying Foundry model identities/catalog entries separate.
- Preserve GA versus preview boundaries for individual Agent Service tools/capabilities; feature-level preview does not make the whole GA service preview and GA service status does not make every feature GA.
- Treat supported regions/models/tools, quotas, pricing, BYO resources, networking, storage, memory, protocol versions, publishing destinations, and hosted-agent runtime behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Foundry Agent Service remains a managed agent runtime/platform identity rather than an agent framework or assistant workspace.
- Prompt/Hosted Agent variants remain service capabilities rather than peer service identities by default.
- Producer provenance resolves bidirectionally to Microsoft.
