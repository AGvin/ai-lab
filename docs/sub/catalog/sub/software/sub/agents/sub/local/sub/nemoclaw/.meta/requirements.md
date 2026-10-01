# Documentation Requirements

## Requirements

- Present NVIDIA NemoClaw as NVIDIA's installable/self-managed agent environment built around OpenClaw with NVIDIA OpenShell sandboxing, inference-provider routing, policy controls, and NVIDIA-oriented onboarding/agent workflows.
- Preserve its local/self-managed execution boundary: the user operates NemoClaw sandboxes and host tooling even when inference is routed to NVIDIA Endpoints or another hosted model provider.
- Keep OpenClaw as the underlying independent assistant project, OpenShell as the isolation/runtime layer, Nemotron and other models as separate model identities, and NVIDIA Endpoints as a model-serving access surface.
- Preserve current memory-driven agent patterns, structured self-model/audit-ledger examples, slash/host CLI commands, policy/sandbox behavior, provider choices, and installer/onboarding mechanics only at current first-party release scope.
- Treat supported operating systems, OpenClaw/OpenShell compatibility, installation commands, model/provider catalog, policies, sandbox lifecycle, credentials, and release behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- NemoClaw remains a local/self-managed agent software identity rather than a hosted agent service or model.
- It is not conflated with OpenClaw, OpenShell, or Nemotron.
- Producer provenance resolves bidirectionally to NVIDIA.
