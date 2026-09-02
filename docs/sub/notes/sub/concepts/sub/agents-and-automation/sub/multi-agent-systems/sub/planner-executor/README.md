# Planner-Executor Architecture

Legacy residual retained for planner/executor-specific workflow pedagogy, executable-plan contracts, and exact legacy framework evidence because the selected planning learning owners are not yet materialized on the active branch.

> **Migration note:** Generic planning, decomposition, plan representations, planning-versus-execution boundaries, and replanning semantics are already preserved in `docs/sub/concepts/sub/reasoning-and-decision-making/sub/planning-and-scheduling/`; generic execution/orchestration state and recovery semantics are preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/workflows-and-orchestration/`. The readiness design routes deeper teaching to generic planning learning and `learning/areas/agents-and-automation/planning-execution-and-reflection/agent-planning/`, but those selected learning nodes are currently absent on the active AI Lab ref. Preserve the procedural material below until those exact owners are materialized and verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Executable-plan residual

A planner-executor workflow separates creation/maintenance of an explicit plan from performance of bounded ready steps. The plan should be an inspectable versioned artifact rather than hidden model reasoning or an unstructured promise to think step by step.

For a non-trivial workflow, a plan may record:

- plan ID/version, goal, authoritative requirements, assumptions, and unknowns;
- stable task IDs, dependencies, ready conditions, inputs/outputs/artifact locations;
- acceptance criteria and assigned capability/tool/model/human role;
- permissions/data boundaries and resource/cost/latency envelopes;
- retry/escalation/fallback and terminal conditions;
- replanning triggers and bounded revision policy.

Distinguish required work from optional optimization and verified facts from assumptions/unknowns.

## Planner and executor contract residual

The planner should preserve complete constraints, identify deliverables and terminal acceptance, decompose work at useful granularity, expose dependencies/shared-state/conflict risks, identify missing information, choose sequential/parallel/conditional structure, assign capability and permission needs, place verification/approval points, and stop planning once the plan is executable enough.

The planner should not fabricate tool availability, source contents, resource state, or completed work.

The executor should accept only tasks whose prerequisites and plan/state versions are valid, stay within the bounded task/permissions, preserve outputs/evidence durably, report actual changes/tests/failures/cost/uncertainty, avoid silently rewriting unrelated plan state, and request replanning when assumptions fail or dependencies change.

Completion of one task is not the same as terminal acceptance of the whole plan.

## Validation and bounded-replanning residual

Before execution, validate requirement coverage, dependency consistency, input availability, ownership/permissions, resource/budget feasibility, observable acceptance criteria, side-effect/approval placement, fallbacks for unavailable capabilities, and whether a simpler deterministic workflow would suffice.

Replanning is justified by material state change: disproved assumptions, unavailable prerequisites, newly discovered dependencies/conflicts, repeated root-cause-identical failure, budget/resource envelope violations, authoritative requirement changes, incomplete coverage, or a route-changing human/fallback decision.

Preserve valid completed work across revisions. Define maximum plan versions, minimum state change sufficient to justify a revision, stable issue/task identity, downstream invalidation rules, comparison with the previous plan, and escalation when plans oscillate or remain infeasible.

## Plan-version and stale-execution residual

Bind executable tasks to a plan version and authoritative state revision. After a plan change, fence/cancel work whose assumptions no longer hold, preserve still-valid artifacts, mark superseded tasks explicitly, prevent late results from overwriting newer state, revalidate pending approvals/resource reservations, and record why the revision occurred.

An executor should not continue stale work merely because it already started.

## Pattern-fit and evaluation residual

Planner-executor fits work where an explicit dependency/acceptance artifact improves control: repository-scale implementation/migration, multi-source research, long-form production, infrastructure changes, resumable workflows, or specialized executor dispatch.

Prefer one bounded action or a fixed pipeline when dynamic planning adds more latency/state/cost than value. Avoid the pattern when the environment changes faster than plans remain valid or when the planner cannot observe enough state to produce feasible work.

Evaluate requirement/acceptance coverage, dependency/readiness correctness, plan revisions, stale/invalid task execution, valid work preserved across replans, execution failures caused by plan defects, duplicate/unnecessary work, planner/executor/total latency and cost, terminal acceptance, and human correction/escalation rate against simpler baselines.

## Legacy evidence-provenance residual

The legacy source cited:

- [LangChain: Plan-and-Execute Agents](https://www.langchain.com/blog/plan-and-execute-agents)

Preserve this exact historical framework reference until the selected planning learning/evidence owners are materialized and its current/historical evidence disposition is verified.

These planner/executor-specific pedagogical and evidence fragments remain migration source material until their exact owners are ready.
