# Pydantic AI Harness

Pydantic AI Harness is the official separate capability and harness library built on Pydantic AI and distributed as `pydantic-ai-harness`.

## Scope and boundaries

- The profile explains the package boundary from Pydantic AI core: the core owns the lean typed agent loop and framework-level capabilities, while the Harness packages higher-level capabilities for complex, long-running work.
- The profile covers current workspace, planning, memory, sub-agent, context-management, execution, control/safety, and packaged-agent capabilities only when supported by current official documentation.
- The profile preserves the current version-policy nuance: the Harness is intended for production use while remaining on 0.x API versioning with possible minor-version API changes.
- The profile keeps optional dependencies, model-provider extras, complete packaged agents, and supported interfaces freshness-sensitive.

## Relations

- Produced by: [`catalog/producers/p/pydantic`](../../../../../producers/sub/p/sub/pydantic/)

## Official resources

- <https://pydantic.dev/docs/ai/harness/>
- <https://github.com/pydantic/pydantic-ai>
