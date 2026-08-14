# Documentation Requirements

## Requirements

- Identify Continue as Continue Dev, Inc.'s open-source coding agent spanning CLI, VS Code, and JetBrains plugin surfaces rather than as a VS Code-only extension.
- Preserve the current lifecycle boundary: the official `continuedev/continue` repository is read-only/not actively maintained after the final 2.0.0 release; do not present it as an actively evolving current agent without new source evidence.
- Preserve durable local-agent semantics: repository context, configurable models/providers, rules, agent modes, tools, shell/file actions, skills, and MCP integration can operate through local editor/CLI clients while inference may use local or hosted model backends.
- Distinguish local agent execution from remote model inference; remote model APIs alone do not make Continue a Hybrid Agent.
- Document the Visual Studio Marketplace listing as Continue's VS Code client/extension surface while preserving Continue's canonical identity as a cross-client Local Agent rather than a VS Code-only product.
- Preserve useful legacy trust boundaries around extension/plugin provenance, repository/file access, shell/tools, project rules, skills, MCP servers, provider credentials, telemetry/data handling, and generated changes.
- Keep exact model/provider lists, plugin/IDE versions, command names, availability, and other mutable details source-backed when expanded.
- Link the canonical Continue Dev, Inc. producer profile.
- Include current official Continue documentation, repository, and Visual Studio Marketplace listing.

## Validation

- Continue is not classified as a VS Code-only extension.
- The Visual Studio Marketplace listing is represented as a client/distribution surface, not a separate canonical Continue identity.
- Maintenance/read-only status is explicit and source-backed.
- Hosted model inference is not described as first-party hosted agent execution.
- The producer relation resolves to Continue Dev, Inc.
