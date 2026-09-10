# Claude Code

Claude Code is Anthropic's agentic coding tool for development work across terminal, IDE, desktop, and web surfaces. It can read codebases, edit files, run commands, use development tools, and carry multi-step coding tasks through implementation and verification.

## Execution and automation boundaries

Claude Code spans both user-controlled and Anthropic-managed execution. Terminal, IDE, and local Desktop workflows can operate against the user's project environment, while web/cloud sessions and remote routines execute on Anthropic-managed infrastructure. CI/CD integrations add another execution boundary through repository automation. These surfaces differ in filesystem access, runtime availability, permissions, and credential exposure, so they should not be treated as one uniform environment.

Claude Code can be customized through project instructions and memory, Agent Skills, hooks, MCP servers/connectors, and CI/CD integrations. The Agent SDK is a related but distinct developer surface rather than the Claude Code product identity itself. Treat repository write access, shell commands, generated diffs, instruction/memory trust, MCP/tool scopes, secrets, remote sessions, and unattended scheduled/background work as explicit review and permission boundaries.

## Related

- [Anthropic](../../../../../../../producers/sub/a/sub/anthropic/) — canonical producer organization.

## Official resources

- [Claude Code](https://www.anthropic.com/claude-code)
- [Claude Code documentation](https://code.claude.com/docs/en/overview)
