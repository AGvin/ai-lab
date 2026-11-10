# Documentation Requirements

## Requirements

- Present NVIDIA NemoClaw as NVIDIA's installable/self-managed agent environment combining supported agent integrations, NVIDIA OpenShell sandboxing, inference-provider routing, policy controls, and agent onboarding/lifecycle workflows; OpenClaw is the default integrated agent.
- Preserve its local/self-managed execution boundary: the user operates NemoClaw sandboxes and host tooling even when inference is routed to NVIDIA Endpoints or another hosted model provider.
- Keep OpenClaw, Hermes, and LangChain Deep Agents Code as independent integrated agent projects, OpenShell as the isolation/runtime layer, models as separate identities, and serving endpoints as separate model-access surfaces; use the current support matrix for agent-specific qualifications.
- Preserve current memory-driven agent patterns, structured self-model/audit-ledger examples, slash/host CLI commands, policy/sandbox behavior, provider choices, and installer/onboarding mechanics only at current first-party release scope.
- Preserve the current alpha / early-preview lifecycle and distinguish tested, limited, experimental, deferred, and unsupported matrix entries. Do not describe NemoClaw as a managed SaaS offering.
- Treat supported operating systems, agent/OpenShell compatibility, installation commands, model/provider catalog, policies, sandbox lifecycle, credentials, and release behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- NemoClaw remains a local/self-managed agent software identity rather than a hosted agent service or model.
- It is not conflated with OpenClaw, OpenShell, or Nemotron.
- Producer provenance resolves bidirectionally to NVIDIA.
