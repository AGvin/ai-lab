# Documentation Requirements

## Requirements

- Identify Pydantic AI as the canonical software profile for the provider-agnostic Python agent framework represented at this path.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Preserve its typed Python/Pydantic orientation and keep agent-loop, tool/toolset, structured-output, dependency-injection, model-provider, harness, and other mutable capabilities source-backed when expanded.
- Use the current official Pydantic documentation location and repository references rather than relying on a legacy docs URL.
- Distinguish Pydantic AI V2 stable (released 2026-06-23) from V1 security maintenance (fixes pledged for at least six months after V2, not a confirmed end date). Source-back the latest-V1/deprecation-first upgrade path and V2 behavior changes without creating a duplicate V2 product identity.
- Document V2's composable `capabilities` interface for tools, hooks, instructions and model settings, and direct V1 adopters to upgrade to the latest V1, resolve deprecation warnings and review the official V1-to-V2 migration map before switching.
- Keep Pydantic AI core distinct from the existing `catalog/software/agent-frameworks/pydantic-ai-harness` package: core supplies the typed agent loop and framework capabilities, while the separately versioned `pydantic-ai-harness` supplies assembled coding/research agents, workspaces, shell execution and higher-level capability bundles.
- When describing tool execution or Harness usage, make application-level workspace isolation, command permissions, credential separation and approval gates explicit. Harness helpers, guardrails and typed outputs do not themselves guarantee sandbox isolation or safe tool execution.

## Validation

- Official resource links match canonical entity metadata.
- The page remains a concrete framework profile and does not duplicate Pydantic library documentation generally.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
