# Documentation Requirements

## Requirements

- Identify OpenAI Agents SDK as the canonical software profile for OpenAI's lightweight agentic application SDK represented at this path.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Preserve its small-primitives design around agents, handoffs/agents-as-tools, and guardrails while keeping sessions, tracing, human-in-the-loop, sandbox, realtime, provider, and tool capabilities source-backed when expanded.
- Record its upstream relationship to the earlier Swarm experimentation as historical evolution, not as a current alias or separate active identity.
- Include the official SDK documentation reference.
- Cover OpenAI's Python (`openai/openai-agents-python`, `openai-agents`, Python 3.10+) and JavaScript/TypeScript (`openai/openai-agents-js`, `@openai/agents`, Node.js 22+ / Deno / Bun) SDK distributions within one canonical product family; language API compatibility and versions must be checked independently.
- Record current official Python and JavaScript/TypeScript documentation and upstream repositories and keep hosted OpenAI model endpoints distinct from the locally executed orchestration SDK; non-OpenAI model providers can be used subject to their actual compatibility.
- Treat sandbox agents, tool execution, provider credentials, session history, tracing and realtime audio as separate operational trust boundaries; enforce least privilege, isolation and explicit authorization for tool execution, and do not imply that SDK guardrails alone guarantee safe execution or data handling.

## Validation

- The official resource link matches canonical entity metadata.
- The page does not conflate the SDK with the lower-level OpenAI Responses API.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
