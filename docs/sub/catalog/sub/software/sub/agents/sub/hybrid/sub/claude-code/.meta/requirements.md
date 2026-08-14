# Documentation Requirements

## Requirements

- Identify Claude Code as Anthropic's agentic coding tool represented by the current Claude Code product across terminal, IDE, desktop, and web surfaces.
- Preserve the core agent behavior documented by Anthropic: reading codebases, editing files, running commands, using development tools, and completing multi-step development work.
- Distinguish user-machine execution surfaces from Anthropic-managed web/cloud execution and model-backed processing; do not describe Claude Code as a fully offline or purely local agent.
- Preserve the current split between local and managed automation surfaces at a high level: CI/CD integrations, local Desktop scheduled tasks, and Anthropic-managed routines/cloud execution have different runtime, file-access, and permission boundaries.
- Preserve the product's extensibility surfaces at a stable high level: project instructions and memory, Agent Skills, hooks, MCP servers/connectors, CI/CD integrations, and the separate Agent SDK.
- Preserve useful legacy operational boundaries around repository read/write access, shell execution, command approvals, generated diff review, repository instructions and memory, secrets, MCP/tool scopes, remote sessions, background or scheduled execution, and human review gates.
- Keep authentication, subscriptions, model-provider options, availability, scheduling limits, integration availability, and other mutable product-state claims source-backed when expanded.
- Link the canonical Anthropic producer profile.
- Include current official Claude Code documentation and product references.

## Validation

- The page does not conflate Claude Code with the Claude model family itself or with the Claude Agent SDK.
- The producer link resolves to the canonical Anthropic organization node.
- The page does not imply that local/desktop sessions and Anthropic-managed cloud routines have the same filesystem or permission model.
- MCP, skills, hooks, instructions, and related extension mechanisms are described as configurable product surfaces rather than inherently trusted capabilities.
- Reader-facing capability and execution-boundary claims remain supported by current official Claude Code documentation.
