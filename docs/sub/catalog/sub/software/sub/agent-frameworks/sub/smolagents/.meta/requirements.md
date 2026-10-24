# Documentation Requirements

## Requirements

- Identify smolagents as the canonical software profile for Hugging Face's lightweight Python agent library represented at this path.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Describe its code-agent and tool-calling orientation while keeping model/provider support, execution security, multi-agent behavior, and other mutable capabilities source-backed when expanded.
- Preserve the current upstream warning that the agent API is experimental only while official documentation still states that status.
- Distinguish `CodeAgent`, which emits executable Python, from `ToolCallingAgent`, which emits structured JSON tool calls, without assuming their security properties or execution privileges are identical.
- Document that the local Python interpreter is not a complete security boundary: for untrusted/code-generating agents use appropriately configured isolated Docker, E2B, Modal, or another maintained executor; validate import/tool allowlists, command capabilities, filesystem/network access, credentials, resource limits and cleanup before deployment.
- Explain the sandbox placement tradeoff: isolating only generated code does not isolate the agent orchestrator, while isolating the whole agent also moves tools and potentially secrets across trust boundaries; external providers can receive prompts, execution state and code under their own handling policies.
- Track Hub-downloaded tools, MCP tools and any remote-code execution as explicit supply-chain and permission risks, with trust decisions and review before use.
- Include the official Hugging Face documentation reference.

## Validation

- The official resource link matches canonical entity metadata.
- Experimental/stability claims are source-backed and treated as mutable.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
