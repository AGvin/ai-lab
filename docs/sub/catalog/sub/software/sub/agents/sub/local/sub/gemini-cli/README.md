# Gemini CLI

Gemini CLI is Google's open-source, terminal-first AI agent for code understanding, generation, task automation, and tool-driven workflows with Gemini models. The CLI runs against local project context and provides file, shell, web, and MCP tooling while normal current use authenticates to Google services for Gemini model access.

## Execution and security boundaries

Gemini CLI can also run through the official `google-github-actions/run-gemini-cli` GitHub Action on the configured GitHub Actions runner, for repository issue triage, PR reviews, and automation. This is not the separate Google-hosted Jules agent or a Gemini CLI vendor-managed cloud runtime. Review workflow permissions, Google/model credentials, untrusted issue or PR contents, and code execution in that runner.

Tool policies decide whether an action is permitted, denied, or requires confirmation. Optional process- or tool-level sandboxing is a separate isolation configuration and is not a universal security guarantee; Gemini model access still normally uses remote Google services.

## Related

- [Google](../../../../../../../producers/sub/g/sub/google/) — canonical producer organization.

## Official resources

- [Gemini CLI repository](https://github.com/google-gemini/gemini-cli)
- [Gemini CLI sandboxing](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/sandbox.md)
- [Gemini CLI tool policy engine](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/policy-engine.md)
- [Official Gemini CLI GitHub Action](https://github.com/google-github-actions/run-gemini-cli)
