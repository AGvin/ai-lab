# Documentation Requirements

## Requirements

- Present NVIDIA NeMo Relay as NVIDIA's released open-source multi-language runtime/observability layer for capturing and controlling agent-run scopes, lifecycle events, trajectories, middleware around model/tool calls, and OpenTelemetry-compatible telemetry.
- Preserve its observability-first catalog placement while acknowledging the shared runtime contract for scopes, policy, plugins, cleanup boundaries, and request isolation across agent frameworks and provider SDKs.
- Keep OpenTelemetry GenAI semantic conventions, OpenInference, ATOF/ATIF formats, Arize Phoenix, LangChain/LangGraph, Deep Agents, OpenClaw, Hermes Agent, and NeMo Agent Toolkit as specifications/integrations rather than NeMo Relay-owned identities.
- Treat supported bindings, CLI packages, integrations, plugins, event schemas, trajectory formats, middleware behavior, release versions, and export backends as freshness-sensitive.
- Preserve current Apache-2.0 distribution and tagged release lifecycle only while first-party repository evidence supports them.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- NeMo Relay remains a cross-agent runtime/observability software identity rather than an agent framework or hosted telemetry service.
- Integration names are not duplicated as Relay subproducts.
- Producer provenance resolves bidirectionally to NVIDIA.
