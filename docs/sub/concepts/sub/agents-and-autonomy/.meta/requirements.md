# Documentation Requirements

## Requirements

- Use the reader-facing title `Agents and Autonomy`.
- Present an AI agent as a system in which one or more AI models participate in selecting, revising, or sequencing actions toward an objective using observations, state/context, tools or environment interactions, and feedback from prior steps.
- Make clear that the agent is the surrounding system, not the model alone. Models, tools, state stores, policies, execution environments, permissions, stopping conditions, and deterministic controls can all be separate components.
- Acknowledge that `agent` terminology varies across research and industry. For this documentation, distinguish more model-directed/dynamic control from workflows whose principal control paths are explicitly orchestrated; treat hybrid systems as possible rather than forcing every implementation into a binary category.
- Distinguish autonomy from mere multi-step execution. Repeated model calls, a fixed pipeline, or a chat interface do not by themselves establish that the model controls meaningful action selection or task progression.
- Explain the observe/decide/act feedback pattern as common but not universal; agents can use planning, tools, memory, verification, human intervention, multi-agent coordination, or other selected mechanisms in different combinations.
- Treat model-generated plans, tool requests, and conclusions as untrusted decision inputs when they can cause external effects; authorization, validation, least privilege, and consequential-action controls remain separate system responsibilities.
- Keep workflows/orchestration, tool use, state/memory, autonomy/control, coordination, multi-agent systems, and verification/reflection as distinct selected descendants rather than collapsing them into one universal agent architecture.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep concrete agent products/frameworks, provider-specific APIs, mutable capability claims, benchmark results, deployment recipes, and task-specific recommendations with their applicable catalog, evidence, engineering, learning, or decision owners.
- Use the canonical entity references as research inputs for agent/control-loop terminology and the workflow-versus-agent boundary when reader-facing rendering is activated.

## Validation

- The page does not equate an agent with a single model, any multi-step LLM pipeline, or tool calling alone.
- The documentation-local workflow/agent distinction is stated without claiming one universally standardized industry definition.
- Autonomy is not presented as an authorization or security boundary.
- Agent components are not assumed to require one fixed loop, memory architecture, planning method, or tool protocol.
- Direct-child navigation contains only currently materialized selected descendants.
- Legacy implementation and safety guidance is preserved as system-boundary semantics rather than copied as a universal agent recipe.
