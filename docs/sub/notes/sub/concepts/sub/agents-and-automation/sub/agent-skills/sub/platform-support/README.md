# Agent Skills Platform Support

Legacy residual for current host-specific Agent Skills support facts that have not yet been reconciled into their catalog/platform/evidence owners.

> **Migration note:** This page is intentionally fragmentary during the active consolidation. Transferable multi-platform layout, maintenance, synchronization, and verification guidance moved to the canonical `learning/.../agent-skills/platform-support-and-portability/` owner. The remaining material is kept here because exact host paths, commands, availability, invocation, permissions, plugin behavior, and support matrices are mutable product facts and do not belong in timeless learning content.

Last verified: 2026-07-19.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Support matrix

| Platform | Native Agent Skills | Project-local skills | User-global skills | Explicit invocation | Automatic invocation | Plugin distribution |
|---|---:|---:|---:|---|---|---:|
| ChatGPT | Yes, on eligible plans and surfaces | Upload or create in the product rather than a repository scan | Personal and workspace-managed skills | Skill picker or direct request | Yes | Yes, on supported Work/Codex surfaces |
| OpenAI Codex | Yes | `.agents/skills/<name>/SKILL.md` | `~/.agents/skills/<name>/SKILL.md` | `$skill-name`, skill mention, or `/skills` selector | Yes | Yes |
| Claude Code | Yes | `.claude/skills/<name>/SKILL.md` | `~/.claude/skills/<name>/SKILL.md` | `/skill-name` | Yes | Yes, Claude Code-specific plugins |
| Cursor | Yes, editor and CLI | `.cursor/skills/` or compatible `.agents/skills/` roots | `~/.cursor/skills/` and supported compatible roots | Slash-command menu | Yes | Yes, Cursor Marketplace |
| OpenCode | Yes | `.opencode/skills/`, `.claude/skills/`, or `.agents/skills/` | Corresponding user configuration roots | Ask for the skill or let the agent call the native `skill` tool | Yes | OpenCode plugins exist, but are not the same format as OpenAI or Claude Code plugins |

Support is not identical across surfaces of the same product. Verify the current product documentation before standardizing an organization-wide installation.

## ChatGPT

### Availability

ChatGPT supports reusable personal and workspace skills on eligible plans. Exact availability depends on plan, workspace settings, admin permissions, region, and product surface.

Skills in ChatGPT follow the open Agent Skills standard, but personal skills may need to be added separately across desktop and web/mobile surfaces when synchronization is unavailable.

### Create or install

Open the Skills area from the ChatGPT interface. Depending on the current surface, this may appear under the Plugin Directory or the profile/workspace menu.

Supported creation paths include:

- ask ChatGPT to create a skill in conversation;
- use the Skills editor;
- upload an existing skill directory or archive;
- install a skill shared by another user or the workspace;
- install a plugin containing skills on a supported surface.

Before uploading a third-party skill, review its complete contents, scripts, required connectors, and network behavior. Product scanning is an additional control, not a replacement for source review.

### Invoke

A skill can activate automatically when the request matches its description. To make the choice explicit, select or mention the skill where the interface supports it, or state the skill name directly in the prompt.

Example:

```text
Use the repository-link-checker skill to validate this documentation export.
```

### Manage

Use the Skills interface to inspect, share, download, disable, or remove a skill. Workspace admins may separately control:

- who can create or use skills;
- uploading;
- workspace sharing and publication;
- installation for other members;
- access to apps or connectors required by a skill or plugin.

### Limitations

- availability differs by plan and workspace policy;
- skills and plugins are not available on every ChatGPT mode or surface;
- skills do not automatically gain connector or filesystem access;
- an installed skill may behave differently between conversational and tool-enabled chats.

## OpenAI Codex

### Discovery paths

Codex reads repository skills from `.agents/skills` directories between the current working directory and repository root:

```text
$CWD/.agents/skills/<name>/SKILL.md
$REPO_ROOT/.agents/skills/<name>/SKILL.md
```

User skills:

```text
$HOME/.agents/skills/<name>/SKILL.md
```

Shared machine or container skills:

```text
/etc/codex/skills/<name>/SKILL.md
```

Codex also includes system skills bundled by OpenAI.

### Install manually

Copy the complete skill directory, not only `SKILL.md`:

```bash
mkdir -p .agents/skills
cp -R /path/to/release-notes .agents/skills/
```

For a personal installation:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R /path/to/release-notes "$HOME/.agents/skills/"
```

Codex follows symlinked skill directories. Use symlinks only when their update and trust model is understood.

### Install with Codex

Codex provides built-in skill creation and installation workflows:

```text
$skill-creator
$skill-installer linear
```

The installer can also retrieve skills from other repositories. Record the source revision for consequential workflows.

### Invoke

In the CLI or IDE:

- run `/skills` to inspect available skills;
- type `$` to mention a skill;
- explicitly write `$skill-name` in the request;
- describe the task and allow implicit activation.

Example:

```text
$repository-link-checker validate docs/ before I commit.
```

### Enable or disable

A skill can be disabled without deleting it through `~/.codex/config.toml`:

```toml
[[skills.config]]
path = "/absolute/path/to/skill/SKILL.md"
enabled = false
```

Restart Codex after changing this configuration.

### OpenAI-specific metadata

An optional `agents/openai.yaml` can declare presentation metadata, invocation policy, and dependencies:

```yaml
interface:
  display_name: "Repository Link Checker"
  short_description: "Validate relative Markdown links"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI documentation access"
```

Keep essential workflow instructions in `SKILL.md`; other clients may ignore this file.

### Plugins

Codex plugins can package skills with connectors, MCP configuration, hooks, and presentation resources. Use the ChatGPT desktop plugin browser or `/plugins` in Codex CLI where supported. Start a new session after installation so bundled skills become available.

## Claude Code

### Discovery paths

Project skill:

```text
.claude/skills/<name>/SKILL.md
```

Personal skill:

```text
~/.claude/skills/<name>/SKILL.md
```

Plugin skill:

```text
<plugin-root>/skills/<name>/SKILL.md
```

Claude Code scans project skills from the working directory through parent directories up to the repository root and can discover nested package skills as relevant files are accessed.

### Install manually

Project-local:

```bash
mkdir -p .claude/skills
cp -R /path/to/release-notes .claude/skills/
```

Personal:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R /path/to/release-notes "$HOME/.claude/skills/"
```

Claude Code watches existing skill roots for changes. If a top-level skill directory is created after the session starts and is not detected, restart the session.

### Invoke

Use either automatic selection or the slash command created from the directory name:

```text
/release-notes
```

Plugin skills are namespaced:

```text
/plugin-name:release-notes
```

### Plugins

Add a marketplace, then install a plugin:

```text
/plugin marketplace add owner/repository
/plugin install plugin-name@marketplace-name
```

Equivalent non-interactive commands are available through `claude plugin ...`.

Use standalone skills for personal, repository-local, or experimental workflows. Use Claude Code plugins for managed distribution, namespacing, versioning, and bundles containing agents, hooks, MCP servers, or other Claude-specific components.

## Cursor

### Discovery and invocation

Cursor supports Agent Skills in the editor and CLI. Agents discover relevant `SKILL.md` workflows and can apply them automatically. Skills can also be selected from the slash-command menu.

Use a client-native project root:

```text
.cursor/skills/<name>/SKILL.md
```

For portable project skills, Cursor also supports Agent Skills-compatible roots such as:

```text
.agents/skills/<name>/SKILL.md
```

A typical personal root is:

```text
~/.cursor/skills/<name>/SKILL.md
```

Exact compatible roots and parity between desktop, SSH, CLI, and SDK surfaces may change. Test the actual execution surface rather than assuming desktop behavior applies everywhere.

### Install manually

Copy the entire skill directory into the selected project or personal root. Open Cursor settings for Rules, Commands, or Skills to confirm discovery where the UI exposes it.

### Plugins

Cursor plugins can package skills, rules, agents, commands, hooks, and MCP configuration for Marketplace installation. Installation can be initiated from the Marketplace or, where supported, from Agent chat:

```text
/add-plugin plugin-name
```

Cursor plugin format and behavior are platform-specific. Do not assume a Claude Code or OpenAI plugin directory will install unchanged.

## OpenCode

### Discovery paths

OpenCode recognizes several project roots:

```text
.opencode/skills/<name>/SKILL.md
.claude/skills/<name>/SKILL.md
.agents/skills/<name>/SKILL.md
```

And corresponding global roots:

```text
~/.config/opencode/skills/<name>/SKILL.md
~/.claude/skills/<name>/SKILL.md
~/.agents/skills/<name>/SKILL.md
```

For project-local paths, OpenCode walks from the current working directory toward the Git worktree root.

### Invoke

OpenCode lists discovered metadata through its native `skill` tool. The agent calls:

```text
skill({ name: "release-notes" })
```

Users normally describe the task or ask OpenCode to use the named skill. The full instructions are loaded only when the tool is called.

### Permissions

Control skill visibility and approval in `opencode.json`:

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

The values are:

- `allow` — load immediately;
- `ask` — request approval;
- `deny` — hide and reject access.

Skills can also be disabled per agent by disabling the `skill` tool.

### Plugins

OpenCode supports plugins, but its plugin API and package model are OpenCode-specific. Prefer the neutral Agent Skills directory for portable instructions. Use an OpenCode plugin only when the workflow requires OpenCode lifecycle hooks, JavaScript/TypeScript extension code, or another host-specific capability.

## References

- Agent Skills standard: https://agentskills.io/
- ChatGPT Skills: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- Codex skills: https://developers.openai.com/codex/skills
- OpenAI plugins: https://developers.openai.com/codex/plugins
- Claude Code skills: https://code.claude.com/docs/en/skills
- Claude Code plugins: https://code.claude.com/docs/en/plugins
- Cursor Agent Skills: https://cursor.com/docs/skills
- OpenCode Agent Skills: https://opencode.ai/docs/skills/
