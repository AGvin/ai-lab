# Documentation Requirements

## Requirements

- Identify CrewAI as the open-source Python agent framework represented by the canonical software profile at this path.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Preserve the current upstream distinction between Crews, which coordinate autonomous role-based agent teams, and Flows, which provide structured event-driven control, state, branching, and integration with ordinary Python logic.
- Explain that the open-source CrewAI framework and CrewAI's managed/enterprise platform are related but distinct adoption surfaces; do not present hosted platform capabilities as intrinsic requirements of the open-source framework.
- Preserve relevant legacy adoption boundaries around tools, delegated task permissions, provider credentials, memory and knowledge-source data, observability, execution controls, and human approval when discussing operational use.
- Keep package versions, Python support, model-provider coverage, cloud deployment options, RBAC, platform pricing, and other mutable implementation/service facts source-backed when expanded.
- Include the official CrewAI website, documentation, and repository references.
- For current CrewAI 1.15.x, distinguish the JSONC-first `agents/*.jsonc` + `crew.jsonc` setup of newly created projects from the still-supported classic `config/agents.yaml` with `@CrewBase`; do not rewrite an existing classic project based on a new-project default.
- Document agent-level execution controls from official docs: `allow_code_execution` defaults to false; `code_execution_mode="safe"` uses Docker, whereas `"unsafe"` executes code directly. Do not interpret Docker mode as complete sandboxing; enforce least-privilege credentials, mount/network/resource limits and review generated code.
- Note that `allow_delegation` defaults to false and `max_iter`, `max_execution_time`, tool access and human-in-the-loop approvals need explicit policy for sensitive workflows. Do not equate HITL feedback with authorization for every action.

## Validation

- Official resource links match canonical entity metadata.
- The page does not present Crews and Flows as interchangeable concepts.
- The page does not imply that the open-source framework requires CrewAI's hosted platform.
- Hosted/enterprise capabilities are clearly distinguished from the framework identity.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
