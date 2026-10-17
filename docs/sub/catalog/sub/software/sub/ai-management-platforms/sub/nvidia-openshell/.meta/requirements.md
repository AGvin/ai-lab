# Documentation Requirements

## Requirements

- Present NVIDIA OpenShell as NVIDIA's released open-source control/runtime layer for governing fleets of autonomous AI agents through sandboxed execution, declarative policy, controlled service access, credential management, identity boundaries, and audit/runtime enforcement.
- Preserve the current installable/self-managed control-plane boundary: OpenShell Gateway, Supervisor, Sandbox, compute drivers, policy enforcement, credential routing, and SDKs belong to one software identity rather than separate peer products.
- Keep NemoClaw as a separate agent environment that uses OpenShell, and keep Codex, Claude Code, Pi, Hermes, and other supported agent harnesses as integrations rather than OpenShell-owned agents.
- Keep the broader NVIDIA Open Agent Safety Platform as a reference architecture/platform concept spanning OpenShell plus hardware/runtime safety layers; do not collapse its full architecture into the OpenShell software identity.
- Treat supported compute drivers, operating systems, SDKs, policy schema, gateway APIs, extension surface, model/inference routing, release versions, packaging, and security profiles as freshness-sensitive.
- Preserve current Apache-2.0 open-source distribution and tagged release lifecycle only while first-party repository evidence supports them.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- OpenShell remains a self-managed policy/control runtime rather than a hosted agent service or trained model.
- OpenShell is not conflated with NemoClaw or the broader Open Agent Safety Platform reference architecture.
- Producer provenance resolves bidirectionally to NVIDIA.
