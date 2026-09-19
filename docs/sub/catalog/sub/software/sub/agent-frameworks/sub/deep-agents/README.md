# Deep Agents

Deep Agents is LangChain's open-source batteries-included agent harness for long-horizon, multi-step agent work.

## Scope and boundaries

- The profile explains its architectural layering accurately: Deep Agents is an opinionated harness over LangChain's agent abstraction and LangGraph's runtime rather than a competing execution runtime.
- The profile covers its current bundled surfaces such as filesystem/workspace operations, sub-agents, context management, memory, shell/tool integration, human-in-the-loop controls, skills, and pluggable backends only when source-backed.
- The reusable Deep Agents SDK/harness remains distinct from Deep Agents Code, which is a separate ready-to-use coding-agent product surface.
- The profile preserves the upstream security boundary: agent authority is bounded by the tools and sandboxes made available; model behavior alone is not a security boundary.

## Relations

- Produced by: [`catalog/producers/l/langchain-inc`](../../../../../producers/sub/l/sub/langchain-inc/)

## Official resources

- <https://docs.langchain.com/deepagents>
- <https://github.com/langchain-ai/deepagents>
