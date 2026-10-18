# OpenAI Codex Agent Skills

Codex discovers skill descriptions first and loads the full `SKILL.md` when a skill is selected. Skills supply instructions and resources; plugins, MCP servers, and `AGENTS.md` remain separate mechanisms.

## Discovery and controls

Repository skills use `.agents/skills` from the current directory up to the repository root. User skills use `~/.agents/skills`; administrator skills use `/etc/codex/skills`, alongside bundled system skills. Symlinked skill folders are supported. Same-name skills are not merged and can both appear.

Place or install a skill into the intended scope. In the CLI and IDE, `/skills` or `$` supports explicit selection; Codex can also choose skills by their descriptions. A skill's optional `agents/openai.yaml` can set `allow_implicit_invocation: false` while retaining explicit use.

Individual skills can be disabled through `[[skills.config]]` entries in `~/.codex/config.toml`, using their path and `enabled = false`; restart after configuration changes. Scope, metadata, and client behavior should be checked against the current documentation. Loading a skill does not bypass the host's tool approvals or sandbox.

## Related

- [Agent Skills concept](../../../../../../../../../../../../../concepts/sub/ai-engineering/sub/extensibility-and-packaging/sub/agent-skills/)
- [Skill portability](../../../../../../../../../../../../../learning/sub/areas/sub/agents-and-automation/sub/integration-and-extensibility/sub/agent-skills/sub/platform-support-and-portability/)

## Official resources

- [Codex skill documentation](https://developers.openai.com/codex/skills)
