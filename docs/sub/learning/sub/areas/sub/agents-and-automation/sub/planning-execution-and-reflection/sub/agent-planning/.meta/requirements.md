# Documentation Requirements

## Requirements

- Teach agent planning as application of general planning inside an agent execution loop: the agent or planner creates and maintains an explicit plan artifact, while execution components perform only currently valid bounded work and report observed state/results back into the loop.
- Use the general Reasoning and Decision Making `planning/` learning topic as the prerequisite for implementation-independent plan representation, dependencies, assumptions, feasibility, acceptance, and revision semantics rather than duplicating that theory here.
- Teach the planner/executor separation as an operational contract, not a requirement for two different models/processes. Planning and execution may be implemented by one or multiple components as long as the plan artifact, execution authority, state transitions, and acceptance responsibilities remain explicit.
- For non-trivial agent work, bind an executable plan to a plan ID/version and authoritative state revision. Preserve stable task identities, dependencies/ready conditions, required inputs/artifacts, acceptance criteria, assigned capability/tool/model/human role, permissions/data boundaries, resource/cost/latency envelopes, retry/escalation/fallback, and terminal/replanning conditions where material.
- Require the planner to preserve authoritative requirements and terminal acceptance, expose dependencies/shared-state/conflict risks, identify unknown/missing information, choose sequential/parallel/conditional structure deliberately, identify capability/permission/resource needs, place verification/approval points, and stop decomposing once the plan is executable enough for the next bounded actions.
- The planner must not fabricate tool availability, source contents, resource state, permissions, successful tests, completed tasks, or other execution facts. Unknown state remains unknown until observed or verified.
- Require executors to accept only tasks whose prerequisites, plan version, authoritative state revision, permissions, and resource conditions are currently valid. Execution must stay within the bounded task and must not silently broaden scope because the plan contains a high-level objective.
- Require executors to persist material outputs/evidence, actual tool/system changes, validation/test results, failures, cost/resource use, uncertainty, and unresolved state needed by later tasks or terminal acceptance.
- Do not let an executor silently rewrite unrelated plan state or mark the whole plan complete because one task finished. Task completion, plan progress, and terminal acceptance are separate states.
- Before executing consequential or expensive work, validate plan requirement coverage, dependency consistency, input/prerequisite availability, ownership/permissions, resource/budget feasibility, observable acceptance criteria, side-effect/approval placement, unavailable-capability fallbacks, and whether a simpler direct/fixed workflow remains sufficient.
- Treat material execution observations as possible replanning triggers: disproved assumptions, unavailable prerequisites, newly discovered dependencies/conflicts, repeated failures with the same root cause, resource/budget envelope violations, authoritative requirement changes, incomplete coverage, or a route-changing human/fallback decision.
- Preserve valid completed work across replans. Use stable task/issue identities where useful, mark superseded work explicitly, compare material plan changes, invalidate only downstream work whose assumptions no longer hold, and bound maximum revisions/time/cost before escalation when plans oscillate or remain infeasible.
- Bind in-flight and pending tasks to the plan/state version they were authorized against. After a material plan/state change, fence or cancel stale work, revalidate pending approvals/resource reservations, preserve still-valid artifacts, and prevent late results from overwriting newer authoritative state.
- An executor must not continue stale work solely because it has already started. Define cancellation, safe completion, detached-result handling, or reconciliation explicitly for tasks that cannot be stopped immediately.
- Keep external side effects under applicable idempotency/authorization/reconciliation controls. Plan revision or retry does not by itself make a duplicate external write safe.
- Teach fit for work where an explicit dependency/acceptance artifact improves control, such as repository-scale implementation/migration, multi-source research, long-form production, infrastructure changes, resumable workflows, or dispatch to specialized executors.
- Prefer one bounded action or a fixed pipeline when dynamic planning adds more state, latency, cost, or failure modes than value. Avoid plan-heavy control when the environment changes faster than plans remain useful or when the planner cannot observe enough authoritative state to make feasible decisions.
- Evaluate requirement/acceptance coverage, dependency/readiness correctness, plan revisions and causes, stale/invalid task execution, valid work preserved across replans, failures caused by planning defects versus execution defects, duplicate/unnecessary work, planner/executor/total latency and cost, terminal acceptance, and human correction/escalation rate against simpler baselines.
- Use the exact historical LangChain Plan-and-Execute Agents reference preserved in entity metadata as implementation/evidence provenance only. Do not freeze historical framework APIs or infer that one implementation defines the general planner/executor contract.
- Keep execution monitoring, verification/reflection, replanning/recovery, idempotency/retries, workflow orchestration topology, and agent state with their selected concept/learning/operations owners where deeper treatment is needed; link rather than duplicate.

## Validation

- Agent plans are explicit inspectable artifacts and do not require disclosure of private hidden chain-of-thought.
- Planner outputs never become authoritative execution facts without observation/verification.
- Executors operate only on currently valid plan/state versions and bounded permissions.
- Task completion, plan progress, and terminal acceptance remain distinct.
- Replanning preserves valid work, invalidates stale dependencies deliberately, and fences late/stale execution.
- Historical framework evidence remains provenance, not timeless API truth.
