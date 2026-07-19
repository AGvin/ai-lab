# Using AI Plugins

This guide explains how to evaluate, install, verify, update, disable, and remove an AI plugin without assuming that all platforms use the same plugin format.

## 1. Identify the plugin ecosystem

Before following any command, identify the target host:

- OpenAI ChatGPT or Codex;
- Claude Code;
- Cursor;
- OpenCode;
- another explicitly documented platform.

A plugin built for one host may contain useful portable skills, but its manifest, hooks, connector declarations, and marketplace metadata usually cannot be installed unchanged in another host.

## 2. Inspect before installation

Record:

```text
Plugin name:
Publisher:
Source repository:
Version or commit:
Target host:
Marketplace:
Bundled skills:
Bundled agents or commands:
Hooks:
MCP servers:
Connectors and OAuth scopes:
Executable code:
Network destinations:
Writable paths:
Update policy:
Uninstall behavior:
```

Review the complete package rather than only its marketplace description. In particular, inspect startup hooks, shell commands, install scripts, MCP configuration, external asset loading, telemetry, and credential requirements.

## 3. Choose an installation model

### Marketplace installation

Use a marketplace when you want managed discovery and updates:

```text
/plugin install package-name@marketplace-name
```

The exact command is host-specific. A marketplace entry is a distribution channel, not an independent security review.

### Direct repository installation

Some hosts accept a Git repository or URL. Pin a tag or commit when the host supports it. Avoid executing installation instructions copied from an unreviewed branch.

### Local development installation

Use a local plugin directory when authoring or auditing a plugin. Keep it outside production projects until its hooks, permissions, and cleanup behavior are understood.

## 4. Install with least privilege

Before enabling the plugin:

1. disable unnecessary connectors;
2. use read-only credentials where possible;
3. restrict filesystem scope;
4. require approval for shell commands and writes;
5. prefer a disposable repository or test workspace;
6. keep secrets outside the plugin directory;
7. deny optional telemetry until reviewed.

A plugin that contains only Markdown skills may still change agent behavior. A plugin containing hooks or code additionally expands the execution boundary.

## 5. Platform examples

### Claude Code

Register a marketplace and install a package:

```text
/plugin marketplace add owner/repository
/plugin install plugin-name@marketplace-name
```

Equivalent shell commands use `claude plugin`. Plugin skills are normally namespaced, for example:

```text
/plugin-name:release-notes
```

### OpenAI Codex

Use the Plugins browser in supported ChatGPT/Codex surfaces or `/plugins` in Codex CLI where available. Inspect connector and MCP dependencies before enabling the plugin, then start a new session when required so bundled skills are discovered.

### Cursor

Install from Cursor Marketplace or use the supported chat command:

```text
/add-plugin plugin-name
```

Check whether the package includes rules, skills, agents, commands, hooks, or MCP configuration. Do not assume desktop, CLI, SSH, and background-agent surfaces expose identical plugin behavior.

### OpenCode

OpenCode plugins are JavaScript or TypeScript extensions loaded from configuration or plugin directories. Treat their executable code as application extensions, not as portable Agent Skills. Use neutral skill directories when no OpenCode-specific runtime behavior is required.

## 6. Verify after installation

Do not stop at a successful installation message. Verify observable state:

- the expected plugin version is shown;
- only the expected skills, commands, agents, hooks, connectors, and MCP servers appear;
- a positive test invokes the intended capability;
- a nearby negative test does not trigger it;
- denied tools remain denied;
- consequential actions request approval;
- no unexpected process, network call, or file modification occurs;
- a fresh session loads the same package state.

For a plugin containing several skills, test each skill independently before testing their composition.

## 7. Update safely

An update can change instructions, code, permissions, dependencies, network access, or marketplace metadata.

Before updating:

1. record the currently installed version;
2. read the release notes and source diff;
3. check for new hooks, connectors, MCP servers, and secrets;
4. reproduce the update in a test environment;
5. rerun activation and permission tests;
6. keep a rollback path to the previous version.

Prefer pinned or explicitly approved updates for workflows with repository write access, production credentials, messaging, payments, or deployment capabilities.

## 8. Disable versus remove

Use **disable** when investigating behavior or temporarily removing capabilities while preserving configuration. Use **remove** when the package is no longer trusted or needed.

After removal, verify that the host no longer exposes:

- bundled skills and commands;
- custom agents;
- lifecycle hooks;
- MCP server entries;
- connector authorizations;
- cached executables or generated files;
- environment variables and secrets created only for the plugin.

Revoke external tokens separately when uninstall does not revoke them automatically.

## 9. Troubleshooting

### Installed but not visible

- restart the host or begin a new session;
- verify the package targets the current host and version;
- check marketplace and organization policy;
- inspect manifest parsing errors;
- confirm the plugin is enabled rather than merely downloaded.

### Skills appear but do not activate

- inspect the bundled `SKILL.md` descriptions;
- test explicit invocation;
- check namespace syntax;
- confirm the host loaded the plugin version you reviewed.

### Hook or MCP startup fails

- inspect runtime and dependency versions;
- validate command paths and working directories;
- check environment variables and secret availability;
- run the component directly in a restricted test environment;
- do not disable approval or sandbox controls merely to hide the error.

### Removal leaves behavior behind

Search the host configuration for generated MCP entries, copied skills, hook registrations, cached packages, and connector authorizations. Compare a clean profile when necessary.

## Operational checklist

- [ ] Correct host and plugin ecosystem identified.
- [ ] Publisher, source, version, and license recorded.
- [ ] Manifest, skills, code, hooks, MCP, connectors, and telemetry reviewed.
- [ ] Permissions minimized.
- [ ] Installation performed in a test environment first.
- [ ] Positive, negative, permission, and failure tests pass.
- [ ] Update and rollback policy defined.
- [ ] Disable, uninstall, and credential-revocation procedures verified.

## References

- Plugin concept: ../../
- Creating Plugins: ../creating/
- Agent Skills platform support: ../../../agent-skills/sub/platform-support/
- OpenAI plugins: https://developers.openai.com/codex/plugins
- Claude Code plugins: https://code.claude.com/docs/en/plugins
- Cursor plugins: https://cursor.com/docs/plugins
- OpenCode plugins: https://opencode.ai/docs/plugins/
