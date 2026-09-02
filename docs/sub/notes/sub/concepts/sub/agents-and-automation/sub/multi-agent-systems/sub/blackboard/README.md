# Blackboard Architecture

Legacy residual retained for practical pattern-selection guidance and exact legacy evidence provenance that are intentionally outside the canonical Blackboard Architecture concept owner.

> **Migration note:** Blackboard identity, shared structured problem state, knowledge-source/contributor contracts, control/scheduling, distinctions from group chat/pipelines/DAGs/manager-worker/event transport, proposal-versus-commit, version/concurrency/stale-read handling, conflict resolution, termination, least privilege, provenance, LLM-agent adaptation, trade-offs, and evaluation dimensions are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/coordination-and-communication/sub/blackboard/`. The remaining material below stays here until its exact learning/decision owner and legacy evidence provenance are verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Pattern-selection residual

A blackboard can be a useful fit when several specialists should contribute incrementally to a shared structured problem state and the next useful contribution depends on the current state rather than on a fixed stage sequence or one manager explicitly assigning every subtask. Example workloads include:

- complex diagnosis or interpretation with several specialist perspectives;
- multimodal evidence fusion;
- research and hypothesis refinement;
- incident response with shared operational state; and
- design/planning problems where partial results change which specialist should act next.

Prefer a simpler design when a fixed pipeline/graph already describes the workflow, one agent or deterministic operation is sufficient, shared state cannot be modeled reliably, every participant truly requires unrestricted full context, contribution scheduling costs more than the task value, or strict low latency favors a direct route.

Compare the design against a simpler manager-worker, graph, or pipeline baseline. Use a blackboard only when opportunistic shared-state coordination materially improves accepted-result quality, evidence handling, or workflow control enough to justify schema, scheduling, conflict, context, and state-maintenance overhead.

## Legacy evidence-provenance residual

The legacy source cited H. Penny Nii's 1986 overview as historical evidence for the blackboard model and its evolution from systems including HEARSAY-II:

- [The Blackboard Model of Problem Solving and the Evolution of Blackboard Architectures](https://doi.org/10.1609/aimag.v7i2.537)

The canonical Blackboard entity currently carries related but not identical historical references, including a different Nii 1986 AI Magazine DOI. Preserve this exact legacy citation until the source relationship/correct provenance is verified rather than silently treating the references as interchangeable.

These pattern-selection and evidence-provenance fragments remain migration source material until their exact learning/decision/research owners are verified.
