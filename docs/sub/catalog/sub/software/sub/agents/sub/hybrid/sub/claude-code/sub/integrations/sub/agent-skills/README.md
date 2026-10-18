# Claude Code Agent Skills

Claude Code loads reusable instructions from `SKILL.md` files and can invoke them automatically or through `/name`. Its skill support extends the Agent Skills standard with host-specific invocation and execution controls.

## Discovery and invocation

Personal skills live under `~/.claude/skills/`; repository skills use `.claude/skills/`. Managed settings and plugins supply additional scopes. Enterprise skills take precedence over personal and project skills with the same name; plugin skills use `/plugin:skill` namespacing.

`disable-model-invocation: true` reserves a skill for explicit invocation. `user-invocable: false` hides its user command while allowing model invocation. Legacy `.claude/commands/` files remain supported within the merged skill system.

## Permissions and lifecycle

`allowed-tools` pre-approves listed tools for the invoking turn; it is not a tool allowlist. Other tools remain governed by normal permissions. Managed policy can suppress these grants. Review executable content and declared tool access before enabling repository skills.

Remove a personal or project skill by deleting its directory; remove plugin-provided skills through plugin management and account-synced skills through account settings. Already-loaded instructions remain in the conversation. Local personal skills do not automatically appear in cloud sessions.

See [Agent Skills](../../../../../../../../../../../../../concepts/sub/ai-engineering/sub/extensibility-and-packaging/sub/agent-skills/) for the concept and [Platform Support and Portability](../../../../../../../../../../../../../learning/sub/areas/sub/agents-and-automation/sub/integration-and-extensibility/sub/agent-skills/sub/platform-support-and-portability/) for cross-host guidance.

## Official resources

- [Claude Code skills](https://code.claude.com/docs/en/skills)
