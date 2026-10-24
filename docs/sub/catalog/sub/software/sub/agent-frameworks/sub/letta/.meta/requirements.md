# Documentation Requirements

## Requirements

- Identify Letta as the open-source platform/runtime for building stateful agents whose persistent memory and context can evolve across interactions.
- Preserve the software classification because the current Letta runtime/App Server can run locally or be self-hosted; do not collapse the self-managed runtime identity into Letta Cloud or another hosted delivery surface.
- Explain the stateful-agent/memory role without treating one memory implementation, model provider, tool interface, agent template, client application, or hosted deployment option as the complete product identity.
- Render the standard `entity-relations` block from validated current-entity relations and preserve Letta as the producer.
- Treat release versions, model/provider compatibility, memory/context APIs, agent templates, sandbox integrations, SDK details, client applications, and hosted-service behavior as mutable facts requiring current first-party verification.
- Include current official Letta documentation and the active `letta-ai/letta-code` repository as references; treat the former `letta-ai/letta` source tree as historical/reproducibility context rather than the current implementation source.

- Distinguish agent-state storage from tool execution: Letta Cloud stores memory, identity and conversations, while the harness can execute on a laptop, remote computer or separately selected cloud sandbox. Cloud-backed state does not imply sandboxed local tools.
- Explain backend selection and operator responsibility for local persistence; verify the selected backend before describing privacy, backups or retention guarantees.
- Require explicit review of permission modes, scheduled/background actions, remote-computer routing and credential scopes before enabling unattended work. Memory or skills installed from external sources do not confer tool authorization.
- Treat AgentFile (.af) import/export as removed from current Letta Code; distinguish it from the separately supported memory and conversation export surfaces, and verify migration instructions against current first-party documentation.

## Validation

- Letta remains a concrete self-manageable stateful-agent platform/runtime rather than a generic memory concept or hosted-only service.
- The `produces` / `produced-by` relation pair is materially consistent.
- Current-source references resolve to active Letta development rather than only the retired V1 source tree.
- Mutable capabilities are not generalized from one release without current upstream evidence.
