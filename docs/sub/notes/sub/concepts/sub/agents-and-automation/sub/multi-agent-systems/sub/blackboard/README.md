# Blackboard Architecture

A blackboard architecture coordinates specialized knowledge sources through a shared structured problem state. Specialists inspect eligible state, contribute partial results, and a controller selects which contribution or action should occur next.

## Translations

- English

## Status

Established problem-solving architecture adapted for agent systems.

## Core idea

```text
                    controller or scheduler
                            |
                            v
knowledge source A <-> shared blackboard <-> knowledge source B
knowledge source C <-> facts, hypotheses, goals, evidence, tasks, artifacts
```

Agents do not need to send every message directly to every other agent. They communicate by reading and writing declared blackboard objects under access, validation, provenance, and scheduling rules.

## Distinguish related patterns

- **Blackboard:** specialists contribute to shared structured state; a controller schedules eligible contributions.
- **Group chat:** agents exchange conversational messages in one shared transcript.
- **Event-driven:** agents react to events or topics; an event may update a blackboard, but the event stream is not itself the complete problem state.
- **Graph or DAG:** nodes and edges define execution flow; a blackboard controller may select dynamically from currently applicable knowledge sources.
- **Orchestrator-worker:** a central manager explicitly assigns bounded tasks; blackboard knowledge sources may volunteer or become eligible from state changes.

Do not call an unbounded shared chat history a blackboard. The architecture requires an explicit state model and contribution semantics.

## Blackboard contract

Record:

```text
Blackboard ID and schema version:
Problem, goals, and terminal criteria:
Object types and lifecycle:
Authoritative versus proposed fields:
Provenance and evidence requirements:
Knowledge-source registry:
Eligibility and trigger rules:
Controller and scheduling policy:
Conflict and merge policy:
Access and data boundaries:
Retention, compaction, and archival:
Retry, cycle, escalation, and human approval rules:
```

The blackboard should preserve which agent, tool, human, or source produced every material entry.

## State layers

A blackboard may separate levels such as:

- raw observations and source references;
- normalized entities, facts, and measurements;
- hypotheses and competing interpretations;
- partial solutions and artifacts;
- goals, subgoals, tasks, and dependencies;
- critiques, confidence, uncertainty, and rejected alternatives;
- decisions, approvals, and terminal status.

Do not mix verified facts and model hypotheses in one unlabeled field. Preserve source evidence and validation status.

## Knowledge-source contract

Each specialist or knowledge source should define:

- supported object types and problem states;
- preconditions or trigger predicates;
- fields it may read and write;
- model, tools, permissions, and data boundary;
- output schema and evidence;
- expected cost, latency, and resource requirements;
- side-effect policy;
- confidence or abstention behavior;
- duplicate, stale, and conflicting-contribution handling.

A role name is not enough. The controller needs machine-checkable eligibility and authority.

## Controller responsibilities

The controller or scheduler should:

- detect state changes and eligible knowledge sources;
- prioritize by dependency, expected information gain, risk, cost, and deadline;
- reserve shared resources and prevent conflicting writes;
- validate contributions before promotion to authoritative state;
- detect repeated states, duplicate work, and non-improving cycles;
- trigger review, escalation, or human approval;
- determine terminal success, failure, or insufficient evidence.

The controller may be deterministic, model-assisted, or hybrid. Deterministic code should enforce schemas, permissions, budgets, and terminal conditions where practical.

## Contribution lifecycle

Use explicit states such as:

```text
PROPOSED -> VALIDATED -> ACCEPTED | REJECTED | SUPERSEDED
```

A contribution should include:

- stable object and contribution IDs;
- input state version;
- content or artifact reference;
- producer and method;
- source evidence;
- assumptions and uncertainty;
- validation results;
- affected objects and dependencies.

Late contributions based on stale state should not overwrite newer accepted objects without reconciliation.

## Conflict resolution

Conflicts may involve:

- contradictory facts or hypotheses;
- competing artifact revisions;
- incompatible plans or resource requests;
- duplicate entities;
- different confidence or source quality;
- write-write races.

Define whether to:

- preserve alternatives;
- select by deterministic evidence or authority;
- request targeted verification;
- merge non-conflicting fields;
- ask an independent reviewer;
- escalate to a human decision owner.

Do not force consensus when the evidence remains contradictory.

## Scheduling and termination

Possible scheduling criteria include:

- prerequisite satisfaction;
- expected reduction in uncertainty;
- blocking severity;
- task priority and deadline;
- resource availability;
- marginal value versus cost;
- fairness or starvation prevention.

Set:

- maximum contributions or rounds;
- maximum repeated source activation;
- unchanged-state and oscillation detection;
- budget and elapsed-time limits;
- minimum evidence or improvement;
- terminal acceptance, failure, and escalation rules.

A blackboard should not run until every specialist becomes silent by chance.

## Context and scale

Do not serialize the complete blackboard into every model prompt. Retrieve a bounded view based on:

- object type and task;
- dependency neighborhood;
- state version;
- evidence relevance;
- permissions and data class;
- token or media budget.

Maintain canonical objects outside model context. Summaries are derived views and should not replace authoritative state.

## Suitable uses

- complex diagnosis or interpretation with several specialist perspectives;
- multimodal evidence fusion;
- research and hypothesis refinement;
- incident response and shared operational state;
- design or planning problems whose next useful step depends on partial results;
- systems where specialists can contribute opportunistically without one manager knowing every capability in advance.

## Poor fits

Avoid or simplify this pattern when:

- a fixed pipeline or graph fully describes the workflow;
- one agent or deterministic operation is sufficient;
- shared state cannot be modeled reliably;
- every specialist needs the complete unrestricted context;
- contribution scheduling cost exceeds the task value;
- strict low latency requires a direct route.

## Strengths

- supports incremental and opportunistic problem solving;
- decouples specialists through shared state;
- preserves competing hypotheses and evidence;
- permits new knowledge sources without rewriting every peer interaction;
- centralizes provenance, validation, and progress state;
- can combine deterministic and model-based specialists.

## Limitations

- blackboard schema and controller design are substantial work;
- shared state can become large, stale, or inconsistent;
- contribution selection may be harder than direct orchestration;
- unrestricted shared access creates privacy and prompt-injection risk;
- specialists can duplicate work or reinforce popular hypotheses;
- termination and information-value estimation can be difficult.

## Evaluation metrics

Record:

- terminal task acceptance;
- useful, duplicate, rejected, and stale contributions;
- contribution precision and evidence-grounding;
- conflicts, merges, and unresolved alternatives;
- controller selection quality and starvation;
- state growth, retrieval size, and compaction loss;
- repeated states, cycles, and escalations;
- latency, model calls, resource use, and cost per accepted result;
- human interventions and post-acceptance defects.

Compare against a simpler supervisor, graph, or pipeline baseline. Use a blackboard only when shared incremental state materially improves the workflow.

## Evidence and established usage

The blackboard model was developed in classical AI as a problem-solving organization with a shared global data structure, independent knowledge sources, and a control component that selects applicable actions. H. Penny Nii's 1986 overview defines the model and traces its evolution from systems including HEARSAY-II.

Source:

- [The Blackboard Model of Problem Solving and the Evolution of Blackboard Architectures](https://doi.org/10.1609/aimag.v7i2.537)

## Related concepts

- [Multi-Agent Systems](../..)
- [Multi-Agent Group Chat](../group-chat/)
- [Event-Driven Architecture](../event-driven/)
- [Graph or DAG Workflow](../graph-dag-workflow/)
- [Supervisor-Specialist Architecture](../supervisor-specialist/)
- [Agent State](../../../agent-state/)
