# Documentation Requirements

## Requirements

- Identify Cursor as Anysphere, Inc.'s AI-first code editor and development environment, not as a standalone agent identity.
- Preserve current multi-surface behavior at a stable level: desktop editor, editor Agent workflows, CLI, remote/background/cloud agent execution, rules/skills/plugins, MCP, and model-provider integration.
- Record Cursor's VS Code codebase foundation when discussing editor compatibility, but do not imply that VS Code Agent Customization is a 1:1 compatibility contract. Link the canonical VS Code profile as upstream context and distinguish Cursor's own customization surface for rules, skills, plugins, MCP, subagents, commands, and hooks.
- Distinguish local editor execution from hosted agent/runtime and inference paths. Do not imply that Privacy Mode makes AI requests fully local or bypasses Cursor infrastructure.
- Preserve useful legacy trust boundaries around repository access, codebase indexing, prompts/context sent for AI features, downstream model providers, background/cloud execution, skills/plugins/MCP, shell/tool permissions, secrets, approval policy, and generated changes.
- Keep exact plans, model/provider lists, pricing, retention periods, feature availability, platform versions, and other mutable service state source-backed and time-scoped when expanded.
- Keep editor extensions under the editor-owned extension subtree rather than duplicating them in the Cursor profile.
- Link the canonical Anysphere, Inc. producer profile.
- Include current official Cursor documentation, privacy/data-use, security, and Terms references.

## Validation

- Cursor remains canonically a code editor/development tool despite agent capabilities.
- VS Code is represented as Cursor's upstream codebase foundation without claiming 1:1 agent-customization compatibility.
- Hosted/background agent execution is not described as local execution.
- Privacy Mode is represented as a data-handling control, not a fully local inference guarantee.
- The producer relation resolves to Anysphere, Inc.
