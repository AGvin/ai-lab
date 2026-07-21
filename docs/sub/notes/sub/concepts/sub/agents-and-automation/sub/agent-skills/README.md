# Agent Skills

Agent Skills are portable folders of instructions and optional supporting resources that teach an AI application how to perform a repeatable class of tasks.

A skill is procedural knowledge. It describes **how to work**, while tools provide operations the application can execute and models provide the reasoning and generation capability.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Learning path

- [Using Agent Skills](./sub/using/) — install, invoke, update, remove, inspect, and troubleshoot skills.
- [Creating Agent Skills](./sub/creating/) — design and build a skill from a minimal `SKILL.md` through scripts, references, testing, and publication.
- [Platform support](./sub/platform-support/) — compare supported clients and their installation and invocation models.
- [Sources and collections](./sub/sources/) — standards, catalogs, installers, and recommended third-party collections.

## Core structure

The open Agent Skills format requires a directory with a `SKILL.md` entrypoint:

```text
skill-name/
├── SKILL.md          # Required metadata and instructions
├── scripts/          # Optional executable helpers
├── references/       # Optional documentation loaded on demand
├── assets/           # Optional templates and output resources
└── ...               # Optional client-specific files
```

`SKILL.md` starts with YAML frontmatter and continues with Markdown instructions:

```markdown
---
name: release-notes
description: Draft release notes from merged changes. Use when preparing a software release or changelog.
---

# Release notes workflow

1. Identify the release range.
2. Group changes by user impact.
3. Separate breaking changes and migrations.
4. Verify every claim against the source changes.
```

The standard requires `name` and `description`. It also defines optional fields such as `license`, `compatibility`, `metadata`, and experimental `allowed-tools`. Individual clients may add their own metadata or invocation controls.

## Discovery, activation, and execution

Skills are normally loaded through progressive disclosure.

### 1. Discovery

At session start, the client makes a compact catalog available to the model. The catalog normally contains each skill's name and description, not the complete instructions.

The description therefore serves two purposes:

- explain what the skill does;
- state when the skill should be selected.

A description that is too vague may never match. A description that is too broad may activate on unrelated work.

### 2. Activation

When the current task matches a skill, the client loads the complete `SKILL.md` body into the working context. Activation may be:

- **automatic** — the model selects the skill because its description matches the task;
- **explicit** — the user invokes a skill by name, command, mention, or platform-specific UI.

Some collections distinguish **user-invoked** orchestration skills from **model-invoked** discipline skills. This is a collection or client convention, not a required field in the open format.

### 3. Execution

The model follows the loaded workflow. It may then:

- read referenced files;
- run bundled scripts;
- use tools supplied by the host;
- ask for user approval;
- invoke compatible supporting skills;
- produce an artifact or perform an external action.

Supporting resources are loaded only when required, which keeps the normal context footprint small.

## Skills in chat and agent environments

A skill does not require an autonomous coding agent. A conversational host such as ChatGPT can discover and activate a skill inside an ordinary chat.

The difference is the execution environment:

| Environment | Skill behavior |
|---|---|
| Chat without external tools | Applies the instructions conversationally and produces text or artifacts available in chat. |
| Chat with files or connectors | Can follow the same workflow while reading files or operating connected systems. |
| Coding agent with repository and shell access | Can edit files, run tests, inspect diffs, and perform longer tool-driven sequences. |
| Automated agent runtime | Can run the workflow under configured permissions, schedules, and approval policies. |

The skill defines the procedure. The host's tools, permissions, sandbox, and user approvals determine which actions can actually occur.

## Related concepts

| Concept | Meaning | Relationship to a skill |
|---|---|---|
| **Prompt** | Instructions and context sent to a model for one interaction or reusable template. | A skill contains instructions but adds packaging, discovery metadata, resources, and a reusable lifecycle. |
| **Tool** | An executable operation such as reading a file, querying an API, or running a command. | A skill tells the model when and how to use tools; it does not automatically grant them. |
| **MCP** | A client-server protocol for exposing tools, resources, and prompts to AI applications. | MCP can provide capabilities that a skill orchestrates. See [Model Context Protocol](../model-context-protocol/). |
| **Plugin** | A platform-specific extension package that can include skills, agents, hooks, tools, or MCP configuration. | A plugin may distribute one or more skills. See [Plugins](../plugins/). |
| **Repository instructions** | Persistent project context such as conventions and commands. | Use for facts that should always be present; use a skill for procedures that should load only when relevant. |

## Portability and client extensions

The Agent Skills format standardizes the contents of a skill directory. It does not require every client to use the same installation path, invocation syntax, permission model, UI metadata, or plugin packaging.

Portable skills should:

- keep the standard `SKILL.md` entrypoint valid;
- describe environmental requirements in `compatibility` or documentation;
- avoid assuming client-specific tools unless the dependency is explicit;
- isolate client-specific metadata from the portable workflow;
- provide fallbacks when a preferred tool is unavailable.

## Security and trust boundary

A third-party skill is executable guidance supplied to a model. Treat it as software supply-chain input even when it contains only Markdown.

Before installation, review:

- the full `SKILL.md`, not only its description;
- scripts and their dependencies;
- network access and credential requirements;
- referenced files and generated commands;
- requested tools and write permissions;
- update mechanism and source ownership;
- whether instructions can expose secrets or project data;
- whether actions have approval and rollback points.

A skill can instruct an agent to run dangerous commands or send sensitive data. Installation is not a security endorsement. Apply least privilege, sandboxing, review gates, pinned versions, and source verification according to the consequences of the workflow.

## References

- Agent Skills overview: https://agentskills.io/home
- Agent Skills specification: https://agentskills.io/specification
- Client implementation guide: https://agentskills.io/client-implementation/adding-skills-support
