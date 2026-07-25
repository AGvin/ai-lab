# Handoff or Swarm Architecture

A handoff or swarm architecture lets the currently active agent transfer control of a conversation or task to another specialist agent according to the current state and responsibility boundary.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established multi-agent pattern.

## Core idea

Unlike a central orchestrator that delegates every worker call and retains control, a handoff system changes which agent owns the next turn or task phase.

```text
user or event -> triage agent -> specialist A -> specialist B -> completion or escalation
                         \-> specialist C
```

The handoff should be an explicit state transition, not an informal suggestion embedded in prose. At any point, the system should know which agent owns the task, what authority it has, and how control returns or terminates.

## Distinguish related patterns

- **Handoff:** the active agent transfers ownership and the receiving agent becomes responsible for subsequent decisions.
- **Agent as tool:** a parent agent calls a specialist for a bounded result but retains ownership.
- **Router-specialist:** a router chooses a destination, usually from a central control point.
- **Group chat:** several agents participate under a speaking or selection policy.
- **Swarm:** a network of specialists can transfer control among themselves through declared handoffs.

Do not use the names interchangeably when their ownership, context, and termination semantics differ.

## Handoff contract

Every handoff should contain structured data such as:

```text
Handoff ID:
From agent:
To agent:
Reason and triggering criterion:
Current goal and bounded assignment:
Authoritative requirements:
State summary and state version:
Input and artifact references:
Completed work and evidence:
Open issues and uncertainty:
Permissions and prohibited actions:
Quality tier, budget, and deadline:
Expected return, next owner, or terminal condition:
```

Pass references to durable state and artifacts rather than copying an ever-growing transcript when possible. The receiver should verify that the handoff is current and within its capability and permission boundary.

## Ownership and admission

Use one authoritative ownership record with a version or generation. A receiving agent should accept work only when:

- it is an allowed handoff target;
- the handoff predicate is satisfied;
- required context and artifacts are available;
- permissions and data class are compatible;
- the state version is current;
- budget and deadline remain valid;
- no newer owner has already accepted the task.

A handoff request and a handoff acceptance are separate events. If acceptance fails, ownership should remain with the sender or move to a defined fallback rather than becoming ambiguous.

## Context transfer

Transfer the minimum context needed for the receiving role:

- user goal and constraints;
- relevant facts and evidence;
- artifact identifiers and checksums;
- previous decisions and unresolved issues;
- allowed tools and side effects;
- completion and return criteria.

Avoid forwarding hidden chain-of-thought, unrelated private data, stale summaries, or unrestricted conversation history. The receiver should distinguish authoritative inputs from prior-agent inferences.

## Handoff predicates

Prefer explicit predicates such as:

- domain or intent classification;
- required modality or tool;
- permission boundary;
- language or jurisdiction;
- risk or quality tier;
- repeated failure signature;
- escalation threshold;
- user request for a human or named specialist;
- task phase completion.

A model may recommend a handoff, but workflow code should validate the target and predicate. Do not allow arbitrary agent names, tools, or permissions from model-generated text.

## Return and termination

Define whether the receiving agent may:

- complete the task directly;
- return a bounded result to the sender;
- hand off to another approved specialist;
- escalate to a supervisor or human;
- reject the handoff with a reason;
- request missing information;
- fail closed.

Every route requires a terminal condition. A swarm should not depend on agents eventually deciding to stop without an explicit rule.

## Prevent ping-pong and drift

Set:

- maximum total handoffs;
- maximum visits to one agent or edge;
- repeated-state and repeated-reason detection;
- minimum new evidence required for another handoff;
- cost and time budgets;
- supervisor or human escalation threshold;
- terminal fallback when no agent accepts ownership.

Record the handoff path. Detect loops such as `A -> B -> A` with unchanged state or specialists repeatedly disclaiming responsibility.

## Concurrency and side effects

A simple handoff normally has one active owner. If the system permits concurrent specialists:

- create separate child tasks rather than ambiguous shared ownership;
- isolate mutable state and side effects;
- define merge and conflict-resolution ownership;
- fence stale agents after transfer;
- require idempotency for external operations.

An agent that lost ownership must not continue issuing consequential side effects from stale context.

## Suitable uses

- customer-support or service triage across specialist domains;
- multilingual or jurisdiction-specific workflows;
- incident response that escalates between operational roles;
- assistants where specialists have different tools or permissions;
- conversational workflows where a specialist should interact directly with the user;
- systems that need decentralized routing without one large central orchestrator.

## Poor fits

Avoid or simplify this pattern when:

- one agent can complete the task reliably;
- specialists only need to return bounded subresults;
- global dependency, budget, and resource coordination requires a central orchestrator;
- state cannot be transferred safely or consistently;
- responsibilities overlap so heavily that ownership remains ambiguous;
- irreversible actions can occur before a central approval boundary.

## Strengths

- lets the most relevant specialist own the interaction;
- reduces central-orchestrator context and routing load;
- supports different permissions, prompts, tools, and policies;
- permits natural escalation and direct specialist-user interaction;
- can extend by adding approved handoff targets without redesigning one monolithic agent.

## Limitations

- control and context can drift across several transfers;
- agents can create loops, ownership gaps, or contradictory decisions;
- repeated context transfer increases cost and privacy exposure;
- decentralized agents may optimize their local objective rather than the complete workload;
- stale agents can issue duplicate actions without fencing;
- debugging requires a complete transition and state history.

## Evaluation metrics

Record:

- correct destination and handoff acceptance rate;
- rejected, invalid, or unauthorized handoffs;
- task success by route and specialist;
- handoffs per completed task;
- ping-pong, repeated-state, and no-owner incidents;
- context loss, stale-state, and duplicated-action incidents;
- escalation and human-transfer rate;
- latency and cost added by transfer;
- user repetition or correction required after handoff;
- cost per accepted result.

## Evidence and established usage

AutoGen documents a Swarm team in which agents use handoff messages to transfer control to another agent. Its documentation distinguishes handoffs from other team selection strategies and requires explicit termination conditions.

Sources:

- [AutoGen Swarm](https://microsoft.github.io/autogen/stable/reference/python/autogen_agentchat.teams.html#autogen_agentchat.teams.Swarm)
- [AutoGen handoffs](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html)
- [AutoGen termination conditions](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/termination.html)

## Related concepts

- [Multi-Agent Systems](../..)
- [Orchestrator-Worker Architecture](../orchestrator-worker/)
- [Multi-Agent Group Chat](../group-chat/)
- [Graph or DAG Workflow](../graph-dag-workflow/)
- [Human Approval Gates](../human-approval-gates/)
- [Agent State](../../../agent-state/)
