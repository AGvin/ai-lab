# Creating AI Plugins

This tutorial explains how to design and build an AI plugin when a standalone Agent Skill is not enough. It starts from the common architectural model and then shows a complete Claude Code example because plugin manifests are platform-specific.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Learning objectives

After completing this guide, you should be able to:

- decide whether a plugin is necessary;
- separate portable skills from host-specific adapters;
- design a manifest and package layout;
- bundle skills, commands, hooks, and MCP configuration safely;
- test installation, activation, update, and removal;
- publish through a marketplace without presenting one host format as universal.

## 1. Choose the target host first

Do not begin with a generic `plugin/` directory. First identify the host and its official schema:

```text
Target host:
Minimum supported version:
Plugin manifest format:
Supported components:
Marketplace or direct-install mechanism:
Permission model:
Update mechanism:
```

A Claude Code plugin, OpenAI plugin, Cursor plugin, and OpenCode plugin may express similar capabilities but use different manifests and runtime contracts.

## 2. Confirm that a plugin is justified

Use a standalone skill when the package contains only one portable procedure.

Create a plugin when one or more of these are required:

- several skills must be installed and versioned together;
- the host needs custom commands or agents;
- lifecycle hooks must run;
- an MCP server or connector must be configured;
- marketplace distribution and managed updates are required;
- namespacing prevents command collisions;
- installation needs host-specific UI metadata.

## 3. Separate portable and host-specific layers

Recommended source layout:

```text
engineering-workflows/
├── skills/
│   ├── clarify-requirements/
│   │   └── SKILL.md
│   └── review-change/
│       └── SKILL.md
├── mcp-servers/
│   └── project-status/
├── adapters/
│   ├── claude-code/
│   ├── openai/
│   ├── cursor/
│   └── opencode/
├── tests/
└── README.md
```

The portable `SKILL.md` files remain canonical. Each adapter packages them according to one host's rules.

## 4. Define the plugin contract

Before writing a manifest, document:

```text
Plugin name:
Target users:
Problems solved:
Bundled skills:
Bundled commands or agents:
Hooks and trigger events:
MCP servers or connectors:
Required runtimes:
Required credentials:
Filesystem access:
Network access:
Consequential actions:
Approval points:
Update and rollback policy:
Uninstall cleanup:
```

## 5. Build the minimum package

A minimal plugin should contain only the files required by the selected host plus documentation.

Conceptual example:

```text
plugin-root/
├── manifest
├── README.md
└── skills/
    └── clarify-requirements/
        └── SKILL.md
```

Validate that the package installs before adding hooks, executable code, or external integrations.

## 6. Design the manifest

A manifest normally identifies:

- stable plugin identifier;
- display name and description;
- version;
- publisher and source repository;
- license;
- minimum host version;
- component entrypoints;
- requested capabilities or dependencies;
- marketplace metadata.

Keep the manifest declarative. Do not hide installation behavior in undocumented scripts.

## 7. Complete Claude Code example

Claude Code plugins use a `.claude-plugin/plugin.json` manifest and conventional component directories.

```text
engineering-workflows-plugin/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── clarify-requirements/
│   │   └── SKILL.md
│   └── review-change/
│       └── SKILL.md
├── commands/
│   └── prepare-review.md
├── hooks/
│   └── hooks.json
├── scripts/
│   └── verify-clean-tree.sh
└── README.md
```

Example `.claude-plugin/plugin.json`:

```json
{
  "name": "engineering-workflows",
  "description": "Reusable requirement clarification and change-review workflows.",
  "version": "1.0.0",
  "author": {
    "name": "Example Engineering Team"
  },
  "repository": "https://github.com/example/engineering-workflows-plugin",
  "license": "MIT"
}
```

Example `skills/clarify-requirements/SKILL.md`:

```markdown
---
name: clarify-requirements
description: Interview the user to resolve ambiguous product or engineering requirements before implementation. Use when scope, constraints, terminology, acceptance criteria, or tradeoffs remain unclear.
---

# Clarify requirements

1. Restate the current goal and known constraints.
2. Ask one high-impact question at a time.
3. Record decisions, rejected alternatives, and unresolved risks.
4. Stop when acceptance criteria and boundaries are explicit.
5. Present the resulting specification for approval before implementation.
```

Example command `commands/prepare-review.md`:

```markdown
Review the current change set against the accepted requirements and repository standards. Report blocking issues first. Do not modify files unless explicitly asked.
```

Example `hooks/hooks.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/verify-clean-tree.sh"
          }
        ]
      }
    ]
  }
}
```

Example `scripts/verify-clean-tree.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "Working tree contains unreviewed changes." >&2
  exit 2
fi
```

This hook is intentionally strict for demonstration. Real hooks must document when they run, what they block, and how users can diagnose failures.

## 8. Add MCP only when needed

A plugin may configure an MCP server, but the server remains a separate trust boundary.

Document:

- command or URL;
- transport;
- required environment variables;
- authentication scopes;
- tools, resources, and prompts exposed;
- write effects;
- startup and shutdown behavior;
- version pinning.

Do not embed production secrets in the plugin repository.

## 9. Hooks require the highest scrutiny

Hooks can execute without the user explicitly invoking a skill. For every hook define:

```text
Event:
Matcher:
Command or handler:
Inputs received:
Files or services accessed:
Failure result:
Timeout:
User-visible diagnostics:
Disable procedure:
```

Prefer read-only validation hooks. Require explicit approval before hooks can cause external writes or destructive actions.

## 10. Test locally

Test these layers independently:

### Package validation

- manifest parses;
- required files exist;
- identifiers and versions are valid;
- referenced paths stay inside the package;
- executable files have documented runtimes.

### Installation

- clean-profile installation succeeds;
- expected components appear;
- repeated installation is idempotent or fails clearly;
- unsupported host versions are rejected.

### Skills and commands

- positive and negative discovery tests pass;
- namespaces are correct;
- supporting references and scripts resolve;
- output and approval requirements are observable.

### Hooks and MCP

- each event matcher is tested;
- denied permissions fail safely;
- timeouts and unavailable dependencies are visible;
- startup and shutdown do not leave orphaned processes;
- no unexpected network or filesystem access occurs.

### Removal and rollback

- uninstall removes package registration;
- skills, commands, agents, hooks, and MCP entries disappear;
- external credentials are revoked separately when necessary;
- previous pinned version can be restored.

## 11. Build a marketplace repository

For a host that supports third-party marketplaces, publish a separate marketplace index or the host-required metadata around the plugin package.

A marketplace entry should include:

- plugin identifier and display name;
- current version;
- source and package location;
- description and categories;
- license;
- compatibility;
- publisher identity;
- changelog or release notes;
- security contact;
- installation and removal instructions.

A marketplace must not silently redirect an existing plugin identifier to an unrelated package.

## 12. Version behavior, not only files

Use semantic versioning as a communication tool:

- patch: clarification or compatible fix that does not expand permissions;
- minor: new compatible skill, command, or optional integration;
- major: changed activation behavior, removed capability, new mandatory dependency, expanded privilege, or incompatible manifest change.

Treat instruction changes as behavioral changes. A one-line `SKILL.md` update can materially change commands or approval requirements.

## 13. Multi-platform publication

Do not claim one package is universal because the bundled skills are portable.

For each host:

1. build a dedicated adapter;
2. validate against official schema;
3. test install and uninstall in a clean profile;
4. document unsupported components;
5. publish a host-specific package version;
6. keep the shared skills synchronized through generation or an explicit release process.

## 14. Common mistakes

### Copying one host manifest into another

Result: partial installation or ignored components. Fix: maintain thin, validated adapters.

### Putting essential workflow rules only in plugin metadata

Result: portable clients load incomplete skills. Fix: keep essential behavior in `SKILL.md`.

### Adding hooks before validating the basic package

Result: startup failures obscure packaging errors. Fix: add one component class at a time.

### Auto-updating privileged plugins without review

Result: permissions or behavior can change silently. Fix: pin versions and review diffs.

### Uninstalling without credential cleanup

Result: external tokens remain valid. Fix: document revocation separately.

## Publication checklist

- [ ] Plugin is necessary beyond a standalone skill.
- [ ] Target host and minimum version are explicit.
- [ ] Portable and host-specific layers are separated.
- [ ] Manifest validates against official schema.
- [ ] Skills, commands, hooks, MCP, connectors, code, and assets are inventoried.
- [ ] Permissions and approval gates are documented.
- [ ] Clean install, update, rollback, and uninstall tests pass.
- [ ] Version and changelog describe behavioral changes.
- [ ] Marketplace metadata identifies the real publisher and source.
- [ ] Security contact and reporting process are available.

## References

- Plugin concept: ../../
- Using Plugins: ../using/
- Creating Agent Skills: ../../../agent-skills/sub/creating/
- OpenAI plugin creation: https://developers.openai.com/codex/plugins/create-plugin
- Claude Code plugin creation: https://code.claude.com/docs/en/plugins
- Claude Code plugin marketplaces: https://code.claude.com/docs/en/plugin-marketplaces
- Cursor plugins: https://cursor.com/docs/plugins
- OpenCode plugins: https://opencode.ai/docs/plugins/
