# Documentation Requirements

## Requirements

- Teach agent task decomposition as applying general decomposition to bounded agent/tool/worker work units while preserving agent runtime state, permissions, context boundaries, evidence, and recombination/terminal responsibility.
- Use general `planning-and-scheduling/task-decomposition/` as the prerequisite for implementation-independent decomposition boundaries, dependencies, context/recombination trade-offs, and decomposition cost rather than duplicating that theory here.
- Show practical applications such as multi-source research split into discovery/evidence/comparison/synthesis; repository changes split by component/responsibility; document processing split by independent files/sections; and specialized work assigned to tools, agents, deterministic workers, or humans.
- Before dispatch, define each agent subtask's bounded purpose, authoritative inputs/context/artifacts, dependencies/readiness, expected output/effect, acceptance criteria, permitted tools/data/side effects, resource/time budget, and owner for unresolved state where material.
- Pass enough global requirements and evidence for correct local decisions while minimizing unrelated context/secrets. A small subtask is not useful if its worker cannot observe the cross-cutting constraint that determines correctness.
- Assign a subtask only to an eligible capability/tool/agent/human role whose permissions and data boundary match the task; decomposition itself must not expand authority.
- Parallelize only units with satisfied dependencies and safe shared-state/resource relationships. Define artifact ownership, mutation boundaries, locking/reservation/version rules, duplicate-work handling, cancellation, and late-result policy when concurrent workers can conflict.
- When outputs recombine, define the integrator/decision owner, output schema/identity, evidence/provenance, merge/conflict policy, duplicate detection, consistency/global-constraint validation, and terminal acceptance before assuming independent partial results form a correct whole.
- Preserve stable subtask/artifact identities across retry, reassignment, replanning, or partial failure where duplicate work or stale late results could corrupt current state.
- Distinguish independent fan-out from manager-worker orchestration. If one retained manager dynamically decomposes, selects workers, tracks dependencies, and integrates results continuously, route readers to Manager-Worker Orchestration rather than treating all decomposition as a standalone pattern.
- Distinguish deterministic partition/map/reduce from arbitrary agent decomposition. When the workload has an explicit partition manifest/intermediate schema/reduction contract, use Workflow Fundamentals MapReduce teaching rather than informal decomposition labels.
- Handle missing/failed/abstained subtasks explicitly. Recombination must not silently treat only successful results as complete coverage when omitted work is material.
- Prefer a direct tool call, deterministic loop, fixed workflow, or one agent when decomposition adds more coordination, context loss, duplication, merge risk, latency, or cost than specialization/parallelism/failure isolation provides.
- Evaluate requirement and source coverage, dependency/readiness correctness, context sufficiency/leakage, worker eligibility/permission failures, safe parallelism, duplicated/omitted work, merge/conflict incidents, stale result rejection, recombination correctness, coordination latency/cost, and accepted terminal result quality.
- Keep general planning/decomposition theory with Reasoning and Decision Making, workflow topology with Workflows and Orchestration, and concrete project task graphs with project/evidence owners.

## Validation

- Agent decomposition preserves general decomposition semantics while adding explicit permissions, runtime state, dispatch, evidence, and recombination responsibilities.
- Worker assignment never expands authority beyond the bounded task contract.
- Parallelism has explicit dependency/shared-state safety and late-result handling where material.
- Recombination validates global constraints and missing work rather than concatenating successful outputs blindly.
- Simpler single-owner/deterministic alternatives are preferred when decomposition adds no material value.
