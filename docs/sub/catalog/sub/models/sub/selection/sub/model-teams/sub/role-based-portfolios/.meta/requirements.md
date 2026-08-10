# Documentation Requirements

## Requirements

- Treat each role as an explicit behavioral contract before selecting a model.
- Preserve the useful legacy role vocabulary: orchestrator, planner, router, worker, reviewer, verifier, evaluator/judge, advisor, memory manager, and context manager.
- Require role-specific responsibilities, capabilities, tools/data, failure boundaries, verification, retries/escalation, and completion criteria.
- Permit role consolidation only when independence is unnecessary and measured workflow quality remains acceptable.
- Flag self-approval combinations such as worker/verifier and worker/final-reviewer as reduced-independence designs requiring explicit evidence or compensating controls.
- Require role-specific evaluation rather than one aggregate benchmark or popularity ranking.
- Require exact model/version/artifact and evidence boundaries for role assignments.
- Link canonical model facts from `../../../../../reference/`.
- Materialize specific portfolio shapes only when they have distinct selection evidence or reader value.

## Validation

- Role names are not mapped to models without evidence.
- Independence requirements are explicit where material.
- The page does not duplicate generic orchestration mechanics unrelated to choosing models for roles.
