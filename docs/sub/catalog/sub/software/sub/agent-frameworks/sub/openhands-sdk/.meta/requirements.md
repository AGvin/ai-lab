# Documentation Requirements

## Requirements

- Present OpenHands Software Agent SDK as the independently installable MIT-licensed agent-building runtime and Agent Server used by the broader OpenHands software-development platform.
- Describe the official Python SDK, browser-compatible TypeScript API client, and REST/WebSocket Agent Server interfaces without inventing three separate agent runtimes. The TypeScript Agent Server client is explicitly alpha, unstable and not recommended for production; preserve this client-specific maturity boundary without applying it to the entire Python SDK.
- Distinguish the SDK and Agent Server from the existing OpenHands end-user product (Canvas/CLI/GUI), the separate OpenHands automation/scheduling lifecycle, and the commercial OpenHands Cloud offering; this is a component identity, not a replacement for the established OpenHands product node.
- Preserve deployment boundaries: agents can use a local workspace or ephemeral isolated workspaces such as Docker/Kubernetes; actual file, shell, repository, network and credential privileges depend on configured runtime permissions.
- Do not imply that local workspace execution means remote LLM/provider traffic or all agent data remains local. Treat tool permissions, remote workspaces, browser API access and human approval controls as material operational/security details.
- Treat package versions, API stability, supported languages, workspace backends, hosted integrations, license changes and provider compatibility as freshness-sensitive.
- Reference the first-party OpenHands SDK documentation and `OpenHands/software-agent-sdk` repository; keep product Canvas implementation and automation ownership in their separate upstream repositories.
- Render the standard `entity-relations` block from validated current-entity relationships.

## Validation

- This record classifies SDK/Agent Server software, not the hosted OpenHands Cloud service or the broader OpenHands end-user application.
- Every claimed SDK surface and deployment boundary is grounded in current first-party SDK documentation or repository.
- `produced-by` resolves exactly and bidirectionally to `catalog/producers/a/all-hands-ai-inc`.
