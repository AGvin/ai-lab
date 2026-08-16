# Documentation Requirements

## Requirements

- Identify GitHub Copilot as GitHub's AI development product spanning editor, terminal, Copilot app, GitHub, and agentic development workflows.
- Treat the former legacy `GitHub Copilot Coding Agent` page as the cloud-agent surface of the broader GitHub Copilot product rather than as a separate canonical software identity.
- Distinguish IDE/local and Copilot-app execution surfaces from GitHub Copilot cloud agent, which performs delegated repository work in GitHub-managed ephemeral development environments backed by GitHub Actions.
- Preserve the cloud-agent task flow at a stable high level: assigned issues or tasks can produce branch changes, checks, commits, and pull requests for human review.
- Preserve current customization and automation surfaces at a high level, including repository instructions, custom agents, Agent Skills, hooks, MCP servers/tools, agent secrets/variables, scheduled runs, and repository-event-triggered automation.
- Preserve useful legacy operational boundaries around repository/organization policies and permissions, Actions environments, agent secrets and variables, generated branches/commits/pull requests, custom instructions, external tools, branch protection, and human review before merge.
- Preserve the broader product boundary without reducing GitHub Copilot to only code completion or only the cloud agent.
- Keep model availability, plan eligibility, billing, preview status, repository policy details, automation limits, and other mutable product/service-state claims source-backed and time-scoped when expanded.
- Include the official GitHub Copilot product page and current official agent/cloud-agent documentation.
- Preserve GitHub, Inc. as the canonical producer through the `produced-by` relation.

## Validation

- The page does not materialize GitHub Copilot cloud agent as a duplicate product identity.
- The page does not conflate IDE/local or Copilot-app execution with GitHub Copilot cloud agent.
- Hosted agent execution is described as a GitHub-managed surface rather than as local execution.
- Scheduled/event automation and custom tools do not remove repository policy, secret, branch-protection, or human-review boundaries.
- Official resource links match canonical entity metadata.
