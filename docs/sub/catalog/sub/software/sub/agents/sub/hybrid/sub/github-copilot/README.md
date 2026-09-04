# GitHub Copilot

GitHub Copilot is GitHub's AI development product spanning editor, terminal, GitHub, and agentic development workflows. Its agent surfaces include interactive IDE or terminal workflows as well as **GitHub Copilot cloud agent**, which performs delegated repository work in GitHub-managed ephemeral development environments backed by GitHub Actions.

## Cloud-agent and automation boundary

The cloud agent can take assigned repository tasks, inspect the codebase, change a branch, run checks, create commits, and return work through pull requests for review. Repository instructions, custom agents, Agent Skills, hooks, MCP servers/tools, and agent secrets or variables can customize that execution; scheduled and repository-event-triggered runs can extend it into unattended automation.

These capabilities remain subject to repository and organization policies, Actions-environment permissions, secret handling, branch protection, generated-diff review, and merge controls. IDE/local agent mode and cloud-agent execution should not be treated as the same runtime or permission boundary.

## Official resources

- [GitHub Copilot](https://github.com/features/copilot)
- [Copilot agents](https://docs.github.com/en/copilot/concepts/agents)
- [Copilot cloud agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent)
- [GitHub, Inc.](../../../../../../../producers/sub/g/sub/github-inc/)
