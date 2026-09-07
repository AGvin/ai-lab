# Documentation Requirements

## Requirements

- Identify Pydantic AI Harness as the official separate capability and harness library built on Pydantic AI and distributed as `pydantic-ai-harness`.
- Explain the package boundary from Pydantic AI core: the core owns the lean typed agent loop and framework-level capabilities, while the Harness packages higher-level capabilities for complex, long-running work.
- Cover current workspace, planning, memory, sub-agent, context-management, execution, control/safety, and packaged-agent capabilities only when supported by current official documentation.
- Preserve the current version-policy nuance: the Harness is intended for production use while remaining on 0.x API versioning with possible minor-version API changes.
- Keep optional dependencies, model-provider extras, complete packaged agents, and supported interfaces freshness-sensitive.

## Validation

- Pydantic AI Harness is not collapsed into the Pydantic AI core profile.
- The 0.x version policy is not misrepresented as project immaturity or API stability.
