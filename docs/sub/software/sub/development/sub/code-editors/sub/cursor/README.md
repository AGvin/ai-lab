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

## Evaluation notes

Record the exact Cursor surface, version, selected model, repository access, enabled skills and plugins, MCP servers, remote or background execution, approval behavior, and date of verification. Desktop, CLI, SSH, and hosted surfaces may not provide identical capabilities.

## References

- Cursor: https://cursor.com/
- Cursor documentation: https://cursor.com/docs
- Agent Skills: https://cursor.com/docs/skills
- Plugins: https://cursor.com/docs/plugins
