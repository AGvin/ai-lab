# Documentation Requirements

## Requirements

- Present Planning, Execution, and Reflection as the Agents and Automation learning group for applying general planning/reasoning methods inside an agent execution loop: decomposing work, generating/revising plans, monitoring actual execution, verifying outcomes, and recovering/replanning when state changes.
- Keep generic planning, task decomposition, search, scheduling, and replanning theory with Reasoning and Decision Making; teach agent-specific application here and link those generic prerequisites rather than duplicating their full theory.
- Keep workflow topology/orchestration patterns with `workflows-and-orchestration/`; this group owns the agent's plan/execution/check/recovery loop rather than every multi-agent coordination pattern.
- Keep explicit agent runtime state/memory with `context-state-and-memory/`; planning/execution may consume/update that state but does not become its second canonical owner.
- Keep runtime idempotency/retry/failure recovery operational controls with `operations-and-control/` where they extend beyond planning semantics.
- Explain that the current materialized subset focuses on `agent-planning/` because planner/executor legacy material has source-backed procedural teaching and historical evidence ready for migration.
- Do not imply that unmaterialized selected siblings `agent-task-decomposition/`, `execution-monitoring/`, `verification-and-reflection/`, or `replanning-and-recovery/` are absent from the logical architecture; standard navigation reflects only physical children.
- Teach plans, execution observations, verification results, and replan decisions as explicit inspectable artifacts/state where practical rather than requiring disclosure of private hidden model reasoning.
- Separate intended state from observed authoritative state. Execution can invalidate a plan; plans and self-reports must not override actual tool/system state merely because the agent expected a different outcome.
- Keep concrete framework planner/executor APIs, prompts, traces, project task graphs, and mutable product behavior with catalog/evidence/project owners.

## Validation

- General planning theory is linked from Reasoning and Decision Making rather than duplicated as agent-only truth.
- Planning, execution monitoring, verification/reflection, and replanning/recovery remain distinct selected learning outcomes.
- Agent plans and observations are inspectable without exposing private hidden chain-of-thought.
- Current navigation exposes only materialized selected children.
