# Supervisor-Specialist Architecture

A supervisor-specialist architecture uses one stateful supervising agent to retain the main interaction and repeatedly invoke bounded specialist agents as tools.

## Translations

- English

## Status

Established multi-agent pattern.

## Core idea

The supervisor owns the conversation, global state, routing, synthesis, and terminal decision. Specialists receive focused context, perform one domain task, and return a result to the supervisor rather than becoming the task owner.

```text
user <-> supervisor -> research specialist -> result
                   -> coding specialist   -> result
                   -> calendar specialist -> result
```

Specialists are often stateless between invocations. This supports context isolation, but durable specialist state may be added deliberately when the workload requires it.

## Distinguish related patterns

- **Supervisor-specialist:** one stateful agent retains ownership and calls specialists as tools over multiple turns.
- **Router-specialist:** a normally bounded classification step dispatches to one route and may not retain ongoing control.
- **Handoff or swarm:** ownership transfers to the receiving agent.
- **Orchestrator-worker:** a broader coordinator may create dynamic task graphs, manage many artifacts and workers, and synthesize a project; supervisor-specialist is the narrower conversational or tool-calling form.
- **Hierarchical orchestration:** supervisors may themselves be nested, but hierarchy is not required for this pattern.

## Supervisor contract

Record:

```text
Supervisor ID and model:
Authoritative goal and conversation state:
Specialist registry and versions:
Allowed calls and routing criteria:
Context policy by specialist:
Tool and permission boundaries:
Concurrency and merge policy:
Retry and escalation budget:
Human approval points:
Terminal criteria:
```

The registry should describe actual capabilities and limitations, not role names alone.

## Supervisor responsibilities

The supervisor should:

- preserve user intent and authoritative state;
- determine whether a specialist is needed;
- select an allowed specialist and construct a bounded request;
- minimize and label context passed to the specialist;
- prevent specialist access to unrelated tools, data, or secrets;
- validate and reconcile returned results;
- track repeated failures, cost, latency, and incomplete work;
- decide whether to retry, use another specialist, escalate, or answer;
- retain accountability for the final response or action.

A supervisor should not blindly forward specialist output to the user or to a consequential tool.

## Specialist contract

Each specialist should define:

- domain and supported task classes;
- input and output schema;
- required context and evidence;
- model, tools, permissions, and data class;
- side-effect policy;
- quality ceiling and common failures;
- timeout, retry, and abstention behavior;
- artifact and citation requirements.

Specialists should return a bounded result, evidence, limitations, and an explicit inability state when the request is unsupported.

## Context isolation

Pass only context required for the specialist task:

- the bounded question or operation;
- relevant source excerpts or artifact references;
- explicit constraints and output schema;
- quality tier and deadline;
- allowed tools and side effects.

The supervisor should distinguish:

- authoritative user content;
- supervisor interpretation;
- retrieved evidence;
- prior specialist claims;
- untrusted instructions embedded in data.

Do not copy the complete conversation to every specialist by default. Context isolation lowers cost and reduces cross-domain leakage, but omitted requirements can also cause failure; evaluate the policy per specialist.

## Specialist selection

Use deterministic rules where categories are stable and model judgment only where necessary. Consider:

- domain and modality;
- required tools;
- data and permission boundary;
- language and jurisdiction;
- quality and risk tier;
- expected latency and accepted-result cost;
- current availability and resource state;
- previous failure signatures.

Validate model-generated specialist names against the registry. A supervisor must not create undeclared capabilities or grant broader permissions through a tool argument.

## Parallel specialist calls

The supervisor may invoke independent specialists concurrently when:

- their inputs and mutable resources do not conflict;
- each result has an explicit schema;
- late, partial, failed, and duplicate results are handled;
- merge and contradiction rules are defined;
- concurrency remains within cost and service limits.

Do not parallelize specialists whose work depends on another specialist's validated result or whose side effects touch shared state.

## Result integration

The supervisor should:

- verify deterministic claims where possible;
- retain source and artifact references;
- detect contradictions between specialists;
- separate facts, inferences, recommendations, and unknowns;
- request targeted correction rather than restarting every specialist;
- use independent review or human approval for consequential output;
- avoid presenting a specialist's confidence as calibrated truth.

If specialists disagree materially, preserve the disagreement and use a declared decision process.

## Failure and escalation

Define:

- maximum calls per specialist and total workflow;
- repeated-failure detection;
- fallback specialist or stronger model;
- whether the supervisor may solve the task directly;
- timeout and partial-result treatment;
- human escalation and fail-closed conditions;
- specialist quarantine after malformed, unsafe, or stale behavior.

A supervisor that repeatedly calls the same unsuitable specialist is not recovering.

## Suitable uses

- assistants spanning calendar, email, research, coding, CRM, or data domains;
- systems requiring one consistent user-facing agent;
- specialist tools that should not see the entire conversation;
- workflows where centralized permissions and synthesis matter;
- workloads with repeated routing over several turns.

## Poor fits

Avoid or simplify this pattern when:

- a single agent with a few tools is sufficient;
- one deterministic router can dispatch the complete task;
- specialists need direct ongoing interaction with the user;
- no supervisor model can route and synthesize reliably;
- a fixed pipeline or graph is more predictable;
- centralized control becomes a throughput or failure bottleneck.

## Strengths

- centralizes user context, authority, and final synthesis;
- isolates specialist contexts and permissions;
- supports reuse of focused agents as tools;
- permits parallel specialist calls under one controller;
- simplifies human approval and audit at the supervisor boundary;
- avoids direct specialist-to-specialist context growth.

## Limitations

- the supervisor is a bottleneck and single control failure domain;
- weak routing or synthesis can waste strong specialists;
- repeated specialist calls increase latency and cost;
- context reduction can omit critical constraints;
- centralized history can become large;
- specialists may share correlated model errors despite different role names.

## Evaluation metrics

Record:

- specialist selection accuracy;
- unnecessary, missing, and repeated calls;
- context-token reduction and omitted-context defects;
- specialist schema and task success;
- integration and contradiction errors;
- supervisor direct-answer versus specialist-call quality;
- parallelism, queueing, latency, and cost;
- escalation and human-intervention rate;
- terminal acceptance and cost per accepted result.

## Evidence and established usage

LangChain documents a subagents architecture in which a central main agent or supervisor calls specialized agents as tools, maintains the conversation memory, and receives their results. Its documentation explicitly distinguishes a stateful supervisor from a one-step router.

Sources:

- [LangChain: Subagents](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)
- [LangGraph Supervisor reference](https://reference.langchain.com/python/langgraph-supervisor)

## Related concepts

- [Multi-Agent Systems](../..)
- [Orchestrator-Worker Architecture](../orchestrator-worker/)
- [Hierarchical Orchestration](../hierarchical-orchestration/)
- [Router-Specialist Architecture](../router-specialist/)
- [Handoff or Swarm Architecture](../handoff-swarm/)
- [Agent State](../../../agent-state/)
