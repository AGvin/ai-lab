# Planner-Executor Architecture

A planner-executor architecture separates creation and maintenance of an execution plan from performance of the plan's bounded steps.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established agent workflow pattern.

## Core idea

The planner converts a goal into explicit steps, dependencies, acceptance criteria, and resource requirements. The executor performs only ready steps and returns artifacts and evidence. The planner or a separate controller updates the plan when observations invalidate assumptions.

```text
goal -> planner -> versioned plan -> executor -> observations and artifacts
                    ^                                  |
                    |------- bounded replanning -------|
```

The plan is an inspectable artifact. It should not exist only as hidden model reasoning or an unstructured promise to “think step by step.”

## Distinguish related patterns

- **Planner-executor:** planning and execution are separate roles or phases; the plan may be revised from execution evidence.
- **Orchestrator-worker:** a coordinator may dynamically decompose, delegate, schedule, verify, and synthesize several worker tasks; explicit planning is one responsibility among many.
- **Graph or DAG workflow:** control flow is encoded as nodes and edges; a planner may generate or update part of that graph.
- **Pipeline:** stages are fixed in advance and normally do not require dynamic planning.
- **ReAct-style agent:** planning and acting are interleaved within one agent loop rather than represented as a durable plan.

Use planner-executor only when a separate plan improves control, verification, or cost enough to justify another model call and state artifact.

## Plan contract

Record:

```text
Plan ID and version:
Goal and authoritative requirements:
Assumptions and missing information:
Tasks and stable task IDs:
Dependencies and ready conditions:
Inputs, outputs, and artifact locations:
Acceptance criteria by task:
Assigned capability, tool, model, or human role:
Permissions and data boundaries:
Estimated cost, latency, and resources:
Retry, escalation, and fallback rules:
Terminal conditions:
Replanning triggers and maximum revisions:
```

A plan should distinguish required work from optional optimization and identify which facts are verified, assumed, or unknown.

## Planner responsibilities

The planner should:

- preserve the complete goal and constraints;
- identify deliverables and terminal acceptance criteria;
- decompose work at a useful granularity;
- detect dependencies, shared state, and conflict risks;
- identify information that must be acquired before action;
- select sequential, parallel, or conditional execution;
- assign capability and permission requirements rather than relying only on role names;
- estimate budgets and resource lifecycles;
- define verification and human approval points;
- stop planning when the plan is executable enough.

The planner should not fabricate tool availability, file contents, resource state, or completed work.

## Executor responsibilities

The executor should:

- accept only tasks whose prerequisites and state version are valid;
- follow the bounded task and permissions;
- use deterministic tools where appropriate;
- preserve outputs and evidence durably;
- report actual changes, tests, failures, cost, and uncertainty;
- avoid silently modifying the plan or unrelated tasks;
- request replanning when assumptions fail or new dependencies appear;
- refrain from claiming plan completion when only one step completed.

A task result and the plan's terminal state are separate decisions.

## Plan validation

Before execution, check:

- requirement coverage;
- dependency consistency and absence of impossible cycles;
- input availability;
- task ownership and permissions;
- resource and budget feasibility;
- acceptance-criteria observability;
- side-effect and approval placement;
- fallback for unavailable tools, models, or people;
- whether a simpler deterministic workflow is sufficient.

For high-risk workflows, use an independent reviewer or human to validate the plan before consequential execution.

## Replanning

Replanning is justified when:

- an assumption is disproved;
- a prerequisite is unavailable;
- execution reveals a new dependency or conflict;
- a task repeatedly fails for the same reason;
- cost, latency, or resource state exceeds the envelope;
- the user changes an authoritative requirement;
- a reviewer finds incomplete coverage;
- a fallback or human decision changes the route.

Replanning should preserve completed valid work. Do not regenerate an entirely new plan after every minor observation.

Set:

- maximum plan versions;
- minimum state change required;
- issue and task identity across versions;
- invalidation rules for downstream work;
- comparison with the previous plan;
- escalation when plans oscillate or remain infeasible.

## Plan drift and stale execution

Bind every task to a plan version and authoritative state revision. When the plan changes:

- cancel or fence tasks whose assumptions no longer hold;
- preserve completed artifacts that remain valid;
- mark superseded tasks explicitly;
- prevent late results from overwriting newer state;
- revalidate pending approvals and resource reservations;
- record why the plan changed.

An executor should not continue a stale plan merely because it already started.

## Suitable uses

- repository-scale coding or migration work;
- research and evidence synthesis with several dependencies;
- long-form document, localization, or media production;
- infrastructure changes requiring preparation, execution, verification, and rollback;
- tasks where a cheaper planner can structure work for specialized executors;
- workflows that must resume after interruption.

## Poor fits

Avoid or simplify this pattern when:

- the task is one bounded action;
- a fixed pipeline fully describes the process;
- the environment changes faster than plans remain valid;
- planning cost exceeds execution cost;
- the planner cannot observe enough state to produce a feasible plan;
- execution requires continuous low-latency interaction rather than staged control.

## Strengths

- separates global reasoning from bounded action;
- creates an inspectable dependency and acceptance record;
- supports specialized or cheaper executors;
- permits plan review before side effects;
- enables selective replanning without discarding valid work;
- improves pause, resume, and progress reporting.

## Limitations

- plan generation adds latency and model cost;
- plans can be incomplete, over-detailed, or stale;
- executors can misinterpret tasks or return weak evidence;
- repeated replanning can become an unbounded loop;
- a strong planner does not guarantee capable execution;
- a rigid plan can suppress useful adaptation.

## Evaluation metrics

Record:

- requirement and acceptance-criteria coverage;
- valid dependency and ready-task decisions;
- plan revisions per completed workflow;
- stale or invalid task execution;
- completed work preserved across replans;
- execution failure caused by plan defects;
- unnecessary tasks and duplicate work;
- planner, executor, and total latency and cost;
- terminal acceptance and cost per accepted result;
- human correction and escalation rate.

Compare against one-agent and fixed-workflow baselines. A planner is useful only when it improves the complete workflow.

## Evidence and established usage

LangChain described plan-and-execute agents as separating long-term planning from execution, with a planner generating steps and an executor acting on them. The pattern is related to plan-and-solve approaches but requires workflow-level validation beyond prompting alone.

Source:

- [LangChain: Plan-and-Execute Agents](https://www.langchain.com/blog/plan-and-execute-agents)

## Related concepts

- [Multi-Agent Systems](../..)
- [Orchestrator-Worker Architecture](../orchestrator-worker/)
- [Graph or DAG Workflow](../graph-dag-workflow/)
- [Pipeline Architecture](../pipeline/)
- [Evaluator-Optimizer Architecture](../evaluator-optimizer/)
- [Task Decomposition](../../../task-decomposition/)
- [Agent State](../../../agent-state/)
