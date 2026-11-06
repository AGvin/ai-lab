# Pydantic AI Harness

Pydantic AI Harness is the official separate capability and harness library built on Pydantic AI and distributed as `pydantic-ai-harness`.

## Scope and boundaries

- The profile explains the package boundary from Pydantic AI core: the core owns the lean typed agent loop and framework-level capabilities, while the Harness packages higher-level capabilities for complex, long-running work.
- The profile covers current workspace, planning, memory, sub-agent, context-management, execution, control/safety, and packaged-agent capabilities only when supported by current official documentation.
- The profile preserves the current version-policy nuance: the Harness is intended for production use while remaining on 0.x API versioning with possible minor-version API changes.
- The profile keeps optional dependencies, model-provider extras, complete packaged agents, and supported interfaces freshness-sensitive.

## Active upstream and execution safety

The original [Pydantic AI Harness repository](https://github.com/pydantic/pydantic-ai-harness) is archived at v0.36.0. Active development moved into the [Pydantic AI monorepo](https://github.com/pydantic/pydantic-ai/tree/main/src/pydantic_ai_harness); the `pydantic-ai-harness` Python 3.11+ package is still separately versioned with 0.x API stability, not discontinued. Choose provider and sandbox extras individually.

`LocalWorkspace` is **not a sandbox**: the agent's commands run with the application's host permissions. A `FileSystem(root_dir=...)` constraint covers its file tools but does **not** constrain Shell commands. For untrusted tool/code execution, configure a restricted cloud sandbox or Bubblewrap/microVM isolation and enforce tool permissions, secrets, network limits and approvals. Some persistent stores or capability state may remain on the application host outside a remote run workspace.

## Relations

- Produced by: [`catalog/producers/p/pydantic`](../../../../../producers/sub/p/sub/pydantic/)

## Official resources

- <https://pydantic.dev/docs/ai/harness/>
- [Current monorepo](https://github.com/pydantic/pydantic-ai/tree/main/src/pydantic_ai_harness)
- [Archived historical repository](https://github.com/pydantic/pydantic-ai-harness)
- [Filesystem tool restrictions](https://pydantic.dev/docs/ai/harness/filesystem/)
