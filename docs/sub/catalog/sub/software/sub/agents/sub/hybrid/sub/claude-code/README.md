# Claude Code

Claude Code is Anthropic's agentic coding tool for development work across terminal, IDE, desktop, and web surfaces. It can read codebases, edit files, run commands, use development tools, and carry multi-step coding tasks through implementation and verification.

## Execution and automation boundaries

Claude Code spans user-controlled and managed execution. Terminal, IDE and Local Desktop sessions run in the user's project environment; Desktop SSH sessions execute on a remote host operated by the user. Web/Remote sessions run in Anthropic-managed cloud infrastructure. Cloud routines can execute there or in an organization's configured self-hosted environment, while local Desktop schedules and CI/CD runners are separate automation surfaces. Scheduled/API/GitHub-triggered cloud routines may execute commands and connector actions without interactive approval; repository, connector, network and credential permissions must therefore be narrowly scoped. These environments do not share one universal file-access or consent boundary.

Claude Code can be customized through project instructions and memory, Agent Skills, hooks, MCP servers/connectors, and CI/CD integrations. The Agent SDK is a related but distinct developer surface rather than the Claude Code product identity itself. Treat repository write access, shell commands, generated diffs, instruction/memory trust, MCP/tool scopes, secrets, remote sessions, and unattended scheduled/background work as explicit review and permission boundaries.

## Related

- [Anthropic](../../../../../../../producers/sub/a/sub/anthropic/) — canonical producer organization.

## Official resources

- [Claude Code](https://www.anthropic.com/claude-code)
- [Claude Code documentation](https://code.claude.com/docs/en/overview)
- [Claude Code Desktop environments](https://code.claude.com/docs/en/desktop)
- [Claude Code cloud sessions](https://code.claude.com/docs/en/claude-code-on-the-web)
- [Claude Code routines and triggers](https://code.claude.com/docs/en/routines)
