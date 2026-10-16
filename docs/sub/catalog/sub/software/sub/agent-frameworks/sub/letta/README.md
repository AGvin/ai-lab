# Letta

Letta is the open-source platform/runtime for building stateful agents whose persistent memory and context can evolve across interactions.

## Scope and boundaries

- The profile preserves the software classification because the current Letta runtime/App Server can run locally or be self-hosted; do not collapse the self-managed runtime identity into Letta Cloud or another hosted delivery surface.
- The profile explains the stateful-agent/memory role without treating one memory implementation, model provider, tool interface, agent template, client application, or hosted deployment option as the complete product identity.
- The profile treats release versions, model/provider compatibility, memory/context APIs, agent templates, sandbox integrations, SDK details, client applications, and hosted-service behavior as mutable facts requiring current first-party verification.

## State, execution and permissions

Letta Cloud stores agent memory, identity and conversations. Tool execution occurs on the selected laptop, remote computer or cloud sandbox; Cloud-backed agent state alone does not sandbox tools on a local machine. Check the chosen backend before making storage, backup or retention assumptions.

Review permission modes, credential scopes, scheduled actions and remote-computer routing before unattended operation. External skills and persistent memory do not grant permission to use tools or access other systems.

Current Letta Code has removed AgentFile (`.af`) import/export. Memory and conversation export remain separate capabilities; verify migration procedures against the current official documentation.

## Relations

- Produced by: [`catalog/producers/l/letta`](../../../../../producers/sub/l/sub/letta/)

## Official resources

- <https://docs.letta.com/>
- <https://github.com/letta-ai/letta-code>
