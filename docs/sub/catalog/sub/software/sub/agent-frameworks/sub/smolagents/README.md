# smolagents

smolagents is Hugging Face's lightweight Python library for building multi-step agents that can act through Python code or structured tool calls.

> **Current API status:** Hugging Face documents the smolagents agent API as experimental and subject to change.

## Agent and execution boundaries

- `CodeAgent` produces Python code actions; `ToolCallingAgent` uses structured tool calls. The official agent API is still labeled experimental, so check compatibility before upgrades.
- The local Python interpreter is not a full sandbox. For untrusted agent-generated code, use an explicitly configured isolated executor (such as Docker, E2B or Modal) with appropriate access restrictions, resource limits and cleanup. Separately control tool permissions, Hub/MCP imports, host filesystem, network access and secrets.
- A sandbox that runs only generated code leaves the orchestrator outside the sandbox. Running the whole agent in isolation improves separation but requires deliberate handling of credentials and provider-visible state.

## Official resources

- [Official documentation](https://huggingface.co/docs/smolagents/)
- [Official repository](https://github.com/huggingface/smolagents)
- [Agent API reference](https://huggingface.co/docs/smolagents/reference/agents)
- [Secure code execution](https://huggingface.co/docs/smolagents/tutorials/secure_code_execution)
