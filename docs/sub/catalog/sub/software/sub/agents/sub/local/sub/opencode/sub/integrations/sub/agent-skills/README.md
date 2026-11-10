# OpenCode Agent Skills

OpenCode discovers `SKILL.md` packages and loads their full content on demand through the native `skill` tool. Each skill supplies a name and description; skills are separate from executable plugins, commands, agent definitions, and MCP servers.

## Discovery and access

Place project skills in `.opencode/skills/<name>/SKILL.md` or user skills in `~/.config/opencode/skills/<name>/SKILL.md`. Compatibility roots include project `.claude/skills`, `.agents/skills`, and user `~/.claude/skills`, `~/.agents/skills`. Project discovery walks from the current directory to the Git worktree root.

The optional `opencode/slash` metadata value `"true"` exposes a skill as a slash command. `opencode/autoinvoke: "false"` hides it from model discovery while allowing manual loading.

The `permission.skill` configuration controls access with `allow`, `ask`, or `deny` rules, including pattern matching. Agent-specific permissions can override access, and disabling `tools.skill` removes the tool for that agent. These govern skill loading; tool execution and external services retain their own controls. Consult the current documentation for exact roots, metadata, and permission syntax.

## Related

- [Agent Skills concept](../../../../../../../../../../../../../concepts/sub/ai-engineering/sub/extensibility-and-packaging/sub/agent-skills/)
- [Skill portability](../../../../../../../../../../../../../learning/sub/areas/sub/agents-and-automation/sub/integration-and-extensibility/sub/agent-skills/sub/platform-support-and-portability/)

## Official resources

- [OpenCode skills](https://opencode.ai/docs/skills/)
