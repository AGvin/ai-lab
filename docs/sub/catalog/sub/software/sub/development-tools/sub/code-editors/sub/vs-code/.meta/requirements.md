# Documentation Requirements

## Requirements

- Identify Visual Studio Code (VS Code) as Microsoft's extensible code editor and development environment.
- Preserve the editor/platform boundary: extensions, GitHub Copilot, local/remote development, and newer agent integrations extend VS Code but remain separately identifiable products or integrations where canonical owners exist.
- Preserve useful legacy evaluation boundaries around extension provenance and permissions, Workspace Trust, repository/workspace access, telemetry/privacy settings, terminal/task/debug execution, remote development, secrets, and external AI/model services.
- Represent current AI/agent customization only at a stable high level; do not make GitHub Copilot or a third-party coding agent part of VS Code's producer identity.
- Keep exact bundled features, extension inventory, release versions, platform support, telemetry defaults, and mutable AI availability source-backed when expanded.
- Keep editor-specific extensions under the canonical `extensions/` child node.
- Link the canonical Microsoft producer profile.
- Include current official VS Code site, documentation, and repository.

## Validation

- VS Code remains a code-editor identity, not a GitHub Copilot or coding-agent duplicate.
- Extension and workspace trust are explicit operational boundaries.
- The producer relation resolves to Microsoft.
