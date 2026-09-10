# Documentation Requirements

## Requirements

- Teach blackboard architecture as a coordination choice for problems where several independent specialists should contribute opportunistically to one shared structured problem state and the next useful contribution depends on the evolving state rather than a fixed sequence or one manager explicitly assigning every subtask.
- Start from the canonical Blackboard Architecture concept for reusable blackboard/problem-state, knowledge-source, control/scheduling, version/conflict, provenance, authorization, termination, and evaluation semantics. Use this learning node for practical selection, schema/control design consequences, examples, and trade-offs.
- Teach pattern fit with examples such as multi-specialist diagnosis or interpretation, multimodal evidence fusion, research/hypothesis refinement, incident response with shared operational state, and design/planning where partial results change which specialist should act next.
- Prefer a fixed pipeline or graph/DAG when stages, dependencies, branches, and joins are already known and opportunistic shared-state scheduling adds no material value.
- Prefer manager-worker when one retained owner can decompose the task, assign bounded work, and integrate results more clearly than maintaining a shared opportunistic problem state.
- Prefer group chat when collaboration fundamentally depends on participants reacting through an evolving conversational transcript rather than structured shared state.
- Prefer one agent or deterministic logic when shared-state schemas, scheduling, conflict handling, and provenance overhead exceed the expected task value.
- Teach the three practical roles explicitly: the structured blackboard/problem state, independent knowledge sources/agents, and control/scheduling that decides which eligible contribution should be considered or committed next.
- Make the blackboard schema purposeful rather than generic. Where material, model problem entities/regions, hypotheses, partial solutions, constraints, evidence/provenance, confidence/uncertainty, dependencies, status, ownership/version, and terminal/acceptance markers needed by the domain.
- Preserve authority distinctions in shared state. Facts, hypotheses, proposals, derived values, conflicts, and accepted decisions should remain distinguishable; repeated or later writes do not automatically make a claim authoritative.
- Define knowledge-source preconditions and contribution contracts: what state patterns make a source eligible, what it reads, what it can propose, required evidence, expected cost, permissions/tools, side effects, and success/failure semantics.
- Separate proposal from authoritative commit when consequential shared-state updates or external effects require deterministic validation, conflict policy, authorization, or approval.
- Teach versioning and stale-state behavior explicitly. A contribution produced from an older blackboard version must be revalidated, recomputed, merged under declared policy, or rejected when intervening changes invalidate its assumptions.
- Preserve competing hypotheses/evidence when useful and define conflict/arbitration rules rather than resolving disagreement through last-write-wins or participant confidence alone.
- Teach scheduling as policy, not truth. Rules, heuristics, utility/cost, learned policies, or model judgment may prioritize eligible contributions, but the scheduler remains bounded by allowed participants/actions and validated transitions.
- Bound termination explicitly using acceptance state, quiescence/no eligible action, time/cost/resource limits, repeated-state/cycle detection, evaluator/human decision, or declared failure/unknown outcomes.
- Apply least privilege and data minimization across blackboard regions. Shared state does not imply every participant can read/write every field or invoke unrelated tools/side effects.
- Preserve provenance through derived entries and transformations so accepted outputs can be traced back to source state/evidence, participant identity, version, and intermediate decisions.
- Explain granularity trade-offs: coarse entries can hide evidence/conflict while overly fine-grained state increases scheduling, storage, context, and merge overhead.
- Teach LLM agents as possible knowledge sources/controllers without implying probabilistic generation replaces authoritative state, validation, permissions, versioning, conflict handling, or termination controls.
- Compare blackboard against simpler manager-worker, graph/pipeline, group-chat, and one-agent baselines. Adopt it only when opportunistic shared-state coordination materially improves accepted-result quality, evidence integration, or workflow control enough to justify added complexity.
- Evaluate useful/invalid/stale contributions, scheduler decisions, conflict rate, convergence/termination, provenance completeness, state growth, context/data leakage, latency/cost, side-effect safety, and accepted solution quality.
- Use the exact H. Penny Nii DOI preserved in entity metadata as historical evidence. Do not silently substitute the different related DOI present in canonical concept metadata; resolve historical source relationships explicitly if later consolidation requires it.

## Validation

- A blackboard implementation has structured shared problem state, independent contributors, and contribution control/scheduling; generic shared storage is not enough.
- Blackboard is distinguished from group chat, pipelines/DAGs, manager-worker, event transport, and generic memory.
- Facts, hypotheses, proposals, provenance, versions, and conflicts remain distinguishable.
- Stale contributions and consequential commits are validated rather than silently overwriting current state.
- Pattern selection compares against simpler alternatives and requires enough value to justify shared-state/control overhead.
- Historical provenance preserves the exact legacy DOI without claiming it is interchangeable with other Nii references.
