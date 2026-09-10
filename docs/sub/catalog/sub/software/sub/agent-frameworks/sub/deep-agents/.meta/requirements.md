# Documentation Requirements

## Requirements

- Identify Deep Agents as LangChain's open-source batteries-included agent harness for long-horizon, multi-step agent work.
- Explain its architectural layering accurately: Deep Agents is an opinionated harness over LangChain's agent abstraction and LangGraph's runtime rather than a competing execution runtime.
- Cover its current bundled surfaces such as filesystem/workspace operations, sub-agents, context management, memory, shell/tool integration, human-in-the-loop controls, skills, and pluggable backends only when source-backed.
- Distinguish the reusable Deep Agents SDK/harness from Deep Agents Code, which is a separate ready-to-use coding-agent product surface.
- Preserve the upstream security boundary: agent authority is bounded by the tools and sandboxes made available; model behavior alone is not a security boundary.
- Keep current package languages, release/version policy, supported integrations, and deployment claims freshness-sensitive.

## Validation

- Deep Agents is not described as LangGraph itself or as a standalone hosted service.
- Deep Agents Code is not silently merged into the framework identity.
- Security guidance does not imply that prompts alone can sandbox side effects.
