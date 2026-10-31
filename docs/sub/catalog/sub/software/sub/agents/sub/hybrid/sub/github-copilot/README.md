# GitHub Copilot

GitHub Copilot is GitHub's AI development product spanning editor, terminal, GitHub, and agentic development workflows. Its agent surfaces include interactive IDE or terminal workflows as well as **GitHub Copilot cloud agent**, which performs delegated repository work in GitHub-managed ephemeral development environments backed by GitHub Actions.

## Cloud-agent and automation boundary

The cloud agent can take assigned repository tasks, inspect code, change a branch, run checks, create commits, and return work through pull requests for human review. Its ephemeral development environment is powered by GitHub Actions: GitHub-hosted runners are standard, while configured self-hosted runners run in an organization's own infrastructure. Repository instructions, custom agents, Agent Skills, hooks, MCP tools, secrets and scheduled/event-triggered automation can customize these workflows.

These capabilities remain subject to repository and organization policies, Actions-environment permissions, secret handling, branch protection, generated-diff review, and merge controls. Local Copilot CLI/IDE sandbox controls protect a different filesystem/network/credential boundary from a cloud agent running on an Actions runner; the environments are not interchangeable.

## Official resources

- [GitHub Copilot](https://github.com/features/copilot)
- [Copilot agents](https://docs.github.com/en/copilot/concepts/agents)
- [Copilot cloud agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent)
- [Cloud agent environment and runner options](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment)
- [Cloud and local sandbox options](https://docs.github.com/en/copilot/how-tos/cloud-and-local-sandboxes)
- [GitHub, Inc.](../../../../../../../producers/sub/g/sub/github-inc/)
