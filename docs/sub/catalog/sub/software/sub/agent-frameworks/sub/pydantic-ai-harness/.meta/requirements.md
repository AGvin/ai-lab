# Documentation Requirements

## Requirements

- Identify Pydantic AI Harness as the official separate capability and harness library built on Pydantic AI and distributed as `pydantic-ai-harness`.
- Explain the package boundary from Pydantic AI core: the core owns the lean typed agent loop and framework-level capabilities, while the Harness packages higher-level capabilities for complex, long-running work.
- Cover current workspace, planning, memory, sub-agent, context-management, execution, control/safety, and packaged-agent capabilities only when supported by current official documentation.
- Preserve the current version-policy nuance: the Harness is intended for production use while remaining on 0.x API versioning with possible minor-version API changes.
- Keep optional dependencies, model-provider extras, complete packaged agents, and supported interfaces freshness-sensitive.
- Explain upstream history precisely: the historical `pydantic/pydantic-ai-harness` repository is archived at v0.36.0; actively maintained `pydantic-ai-harness` source now lives under `pydantic/pydantic-ai/src/pydantic_ai_harness` and is still released as a separately versioned 0.x package alongside Pydantic AI 2.x. Do not describe the framework package as abandoned or merge its canonical identity into Pydantic AI core.
- Record the current Python 3.11+ Harness runtime requirement and separately selectable provider/sandbox extras; do not imply the main Pydantic AI distribution or every extra is automatically required.
- Explicitly warn that `LocalWorkspace` performs file operations and shell commands on the user's host without isolation. A `FileSystem(root_dir=...)` restriction contains only filesystem tools, not Shell commands or SSH executions; configure E2B, Modal, Bubblewrap or an appropriate microVM sandbox for untrusted code and scope commands, credentials, network and human approvals separately.
- Warn that selected capability persistent files, step/media stores or code-mode paths may live on the application host even when a run's workspace is sandboxed. Check trace content/retention and shared workspace access before processing sensitive data.

## Validation

- Pydantic AI Harness is not collapsed into the Pydantic AI core profile.
- The 0.x version policy is not misrepresented as project immaturity or API stability.
