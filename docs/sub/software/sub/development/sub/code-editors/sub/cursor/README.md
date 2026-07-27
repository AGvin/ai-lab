# Cursor

Cursor is an AI-enabled code editor with built-in AI integration.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Metadata

```text
Resource type: AI-enabled code editor
Primary use case: AI-assisted coding in a dedicated editor
Access model: desktop application and/or hosted service
Operational requirement: local workstation and account/service access
Integration modes: desktop UI, editor workflow, model/provider integrations, Agent Skills, plugins, and MCP
Source: https://cursor.com/
Risk notes: Verify pricing, source availability, data handling, model providers, repository access behavior, installed skills, plugins, MCP servers, and approval policy before use with sensitive code.
```

## Purpose

Use Cursor for AI-assisted coding, codebase navigation, editing, and development workflows.

## AI relevance

Cursor is relevant to AI Lab as a code editor with built-in AI functionality, rather than as a standalone AI agent.

## Skills, plugins, and MCP

Cursor supports Agent Skills in editor and CLI workflows, distributes host-specific plugins through Cursor Marketplace, and can configure MCP integrations.

Use the centralized guides for the portable concepts and detailed workflows:

- [Agent Skills](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/)
- [Cursor skill installation and invocation](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/platform-support/#cursor)
- [Plugins](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/plugins/)
- [Model Context Protocol](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/)

Cursor plugin packaging is platform-specific. Do not assume that an OpenAI, Claude Code, or OpenCode plugin installs unchanged merely because it contains portable Agent Skills.

## Deployment modes

- Local workstation
- Hosted SaaS or hybrid behavior: verify current product behavior

## Hardware acceleration

- Not usually relevant to the local environment

## Integration modes

- Desktop UI
- Editor and agent workflows
- Agent Skills and rules
- Cursor Marketplace plugins
- MCP servers
- Model/provider integrations: verify current options

<!-- doc-anchor: cursor-data-safety; target: next-heading -->
<a id="cursor-data-safety"></a>
## Data path and privacy

Verified on 2026-07-26.

Cursor documents that AI requests pass through Cursor infrastructure even when a user supplies a separate model API key. Requests can include conversation history, recently viewed files, and relevant code, and can then be forwarded to the selected inference provider.

Privacy Mode changes retention and training guarantees; it does not make the request path direct or fully local. Codebase indexing also uploads code chunks to compute embeddings, while embeddings and related metadata may remain stored according to the current service design.

For sensitive repositories:

- enforce Privacy Mode through the workspace where applicable;
- approve Cursor, the selected model provider, subprocessors, regions, and retention terms;
- remove secrets and exclude content that is not permitted to leave the device;
- review indexing, background requests, plugins, skills, MCP servers, and remote execution separately;
- do not use Cursor when organizational policy prohibits third-party processing or an intermediary in the model path.

Recheck the current product behavior and contracts before adoption because routing, providers, retention, and enterprise controls can change.

## Evaluation notes

Record the exact Cursor surface, version, selected model, repository access, enabled skills and plugins, MCP servers, remote or background execution, approval behavior, and date of verification. Desktop, CLI, SSH, and hosted surfaces may not provide identical capabilities.

## References

- Cursor: https://cursor.com/
- Cursor documentation: https://cursor.com/docs
- Cursor data use and privacy: https://cursor.com/data-use
- Cursor security: https://cursor.com/security
- Agent Skills: https://cursor.com/docs/skills
- Plugins: https://cursor.com/docs/plugins