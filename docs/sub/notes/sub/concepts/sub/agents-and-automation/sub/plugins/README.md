# AI Plugins

An AI plugin is an installable, platform-specific package that extends an AI application with one or more capabilities such as Agent Skills, connectors, MCP servers, agents, commands, hooks, templates, or user-interface metadata.

Unlike Agent Skills and Model Context Protocol, **plugin is not one universal cross-platform format**. OpenAI, Claude Code, Cursor, OpenCode, and other hosts define different package layouts, manifests, lifecycle hooks, permissions, and marketplaces.

## Translations

- English

## Learning path

- [Using Plugins](./sub/using/) — evaluate, install, update, disable, remove, and audit third-party plugins.
- [Creating Plugins](./sub/creating/) — design and build a platform-specific plugin with complete examples and validation steps.
- [Agent Skills](../agent-skills/) — portable procedural workflows that a plugin may distribute.
- [Model Context Protocol](../model-context-protocol/) — a standard protocol that a plugin may configure or bundle.

## Why plugins exist

A standalone skill can teach a model a workflow, but many integrations need more than instructions:

- a managed installation and update mechanism;
- several related skills installed as one product;
- connectors or OAuth configuration;
- MCP server definitions;
- custom agents or commands;
- lifecycle hooks;
- application-specific UI presentation;
- organization policy and marketplace metadata;
- namespacing to avoid collisions.

A plugin packages these host-specific concerns around reusable capabilities.

## Common components

A plugin may contain some or all of the following:

| Component | Purpose |
|---|---|
| Manifest | Identifies the package, version, author, description, compatibility, and entrypoints. |
| Skills | Reusable `SKILL.md` workflows loaded when relevant. |
| Agents | Preconfigured specialist roles, prompts, models, tools, and permissions. |
| Commands | Explicit user-invoked operations or slash commands. |
| Hooks | Code or commands executed at lifecycle events. |
| MCP configuration | Definitions for local or remote MCP servers. |
| Connectors | Platform-managed connections to external services and accounts. |
| App templates | Reusable UI or application scaffolding. |
| Assets | Icons, screenshots, templates, and documentation. |
| Marketplace metadata | Information required to discover, review, and install the package. |

The exact names and locations of these components differ by host.

## Plugin versus Agent Skill

| Agent Skill | Plugin |
|---|---|
| Portable folder centered on `SKILL.md` | Host-specific installable package |
| Primarily procedural knowledge | Distribution and integration boundary |
| Can work without executable code | May include code, hooks, connectors, and configuration |
| Discovered and activated by task relevance | Installed, enabled, updated, and removed as a package |
| Usually one focused workflow | May bundle many skills and capabilities |
| Open Agent Skills specification | No single universal plugin specification |

A plugin can contain skills. A skill does not need a plugin.

Use a standalone skill when users need an inspectable and portable workflow. Use a plugin when they need managed distribution or host-specific integration.

## Plugin versus MCP

| MCP | Plugin |
|---|---|
| Client-server interoperability protocol | Installation and packaging mechanism |
| Exposes tools, resources, and prompts | May configure or distribute an MCP server |
| Can serve several compatible hosts | Usually targets one host or plugin ecosystem |
| Has protocol lifecycle and transport semantics | Has package installation, update, and marketplace semantics |

Installing a plugin that references an MCP server creates two trust boundaries:

1. the plugin package and its installation behavior;
2. the MCP server, credentials, data access, and tool effects.

Review both separately.

## Plugin versus prompt, tool, and connector

- A **prompt** provides instructions or context. A plugin can distribute prompts or commands.
- A **tool** performs an operation. A plugin can register or expose tools.
- A **connector** links a platform to an external service, often with managed authentication. A plugin can declare connector dependencies where the platform supports them.
- A **skill** tells the model when and how to apply a procedure. A plugin can install several skills together.

## Portability boundary

Do not assume that a directory named `plugins/` is portable.

Examples of platform-specific differences include:

- manifest filename and schema;
- package root layout;
- marketplace registration;
- namespaces and command syntax;
- hook events;
- supported executable languages;
- connector declarations;
- MCP configuration shape;
- permission and approval policy;
- signing and publication requirements.

A multi-platform project should keep reusable skills and MCP servers in neutral source directories, then generate or maintain thin host adapters.

```text
project/
├── skills/                  # Portable source skills
├── mcp-servers/             # Portable or separately deployable services
└── adapters/
    ├── claude-code-plugin/
    ├── openai-plugin/
    ├── cursor-plugin/
    └── opencode-plugin/
```

## Installation lifecycle

A managed plugin normally passes through these stages:

1. **Discovery** — user or admin finds a package in a marketplace or repository.
2. **Review** — source, publisher, permissions, components, and version are inspected.
3. **Installation** — files and configuration are registered with the host.
4. **Enablement** — bundled skills, agents, hooks, connectors, or MCP servers become available.
5. **Execution** — capabilities run under the host's permissions and approvals.
6. **Update** — a new package version changes instructions, code, or dependencies.
7. **Disablement or removal** — the host unloads components and cleans package state.
8. **Credential cleanup** — tokens or external authorizations no longer needed are revoked.

Installation is not the final security decision. Every update can change behavior.

## Security and trust boundary

Before installing a plugin, review:

- publisher identity and source repository;
- package version and update channel;
- complete manifest and bundled files;
- skills and hidden instruction surfaces;
- executable hooks and commands;
- MCP servers and network destinations;
- connectors and requested account scopes;
- filesystem and shell permissions;
- secrets, environment variables, and credential storage;
- telemetry and external asset loading;
- approval gates for writes or other consequential actions;
- uninstall behavior and residual configuration.

Prefer least privilege, pinned versions, reproducible builds, explicit update review, and isolated testing for unfamiliar packages.

## When to create a plugin

Create a plugin when at least one of these is true:

- several capabilities should be installed and versioned together;
- the workflow needs host-specific hooks, agents, connectors, or UI;
- users need managed marketplace installation and updates;
- namespacing is required to avoid collisions;
- organization admins need centralized distribution or policy controls.

Do not create a plugin merely to distribute one portable `SKILL.md` when a direct skill installation is sufficient.

## References

- OpenAI plugins: https://developers.openai.com/codex/plugins
- OpenAI plugin creation: https://developers.openai.com/codex/plugins/create-plugin
- Claude Code plugins: https://code.claude.com/docs/en/plugins
- Claude Code plugin marketplaces: https://code.claude.com/docs/en/plugin-marketplaces
- Cursor plugins: https://cursor.com/docs/plugins
- OpenCode plugins: https://opencode.ai/docs/plugins/
- Agent Skills: ../agent-skills/
- Model Context Protocol: ../model-context-protocol/
