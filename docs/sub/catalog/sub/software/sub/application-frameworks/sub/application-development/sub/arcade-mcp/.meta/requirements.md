# Documentation Requirements

## Requirements

- Identify Arcade MCP as the published MIT-licensed Python framework/library for building MCP servers and tools, including decorators for MCP tools/resources/prompts and optional typed auth declarations. It is an installable library, not the full Arcade platform or a hosted AI agent.
- Keep portable standalone stdio/HTTP tool server execution distinct from integration with vendor-hosted Arcade Cloud deployments; hosted Arcade token brokerage/policy/orchestration are separate platform capabilities and may not be present in standalone installations.
- Distinguish MCP specification semantics, SDK decorator API, OAuth bearer-token handling and resource-server authentication. Declaring `requires_auth` does not obviate safe token custody and per-user authorization in an untrusted deployment.
- Pin Python package version, MCP protocol compatibility, runtime, toolkits/plugins, server transport, credential model and auth-provider behavior. Do not assume every first-party managed Arcade toolkit is maintained or distributed by this single framework repository.
- Preserve producer Arcade AI Inc., and prevent a second producer identity based solely on the software's `ArcadeAI` GitHub organization.

## Validation

- First-party published documentation and/or repository demonstrates an existing usable product, with install/deployment boundary correctly distinguished.
- Exact reciprocal producer relation resolves to one canonical organization rather than any evaluated integration/tool provider.
- Source-available/managed feature and licensing claims are versioned, never silently generalized.
