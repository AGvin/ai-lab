# Documentation Requirements

## Requirements

- Use the reader-facing title `Handoffs`.
- Define a handoff as an explicit coordination transition in which one active agent/configuration transfers responsibility/control for a task, conversation, or declared sub-scope to another agent/configuration that becomes the active owner for that transferred scope.
- Keep active-ownership transfer as the defining invariant. A message, recommendation, tool call, consultation, or bounded specialist result is not a handoff if the original controller remains the authoritative task owner.
- Distinguish handoffs from `workflows-and-orchestration/manager-worker-orchestration/`. A manager delegates bounded work while retaining global ownership and integrates worker results; a handoff changes which participant owns the active interaction/task scope.
- Distinguish handoffs from `workflows-and-orchestration/agent-routing/`. Routing chooses a destination; a handoff performs/represents the ownership transfer. A router can initiate a handoff, call a specialist as a tool, or route into a workflow without transferring ownership depending on the surrounding control contract.
- Distinguish handoffs from ordinary sequential workflows. Sequential stages can pass artifacts while the workflow remains the owner; a handoff specifically changes the active agent/configuration responsible for the transferred scope.
- Treat handoffs as compatible with centralized or peer/decentralized topologies. The transfer mechanism does not require a swarm, mesh, triage agent, or one routing topology, even though those structures can use handoffs.
- Treat `swarm` as a possible decentralized topology/behavior built from local handoff rules rather than a synonym for handoff itself. Preserve swarm-specific organization/topology with `multiagent-systems/` or learning/project owners unless later selected separately.
- Define the handoff contract where material: source and target identity, transferred objective/scope, authoritative state, user/system constraints, relevant context/evidence/artifacts, unresolved issues, permissions/data boundary, deadline/budget, accepted next action, return/re-handoff policy, and terminal condition.
- Preserve explicit context-transfer semantics. A receiving agent may need full conversation history, a scoped state snapshot, selected messages, structured task data, artifact references, or a summary; the concept does not require one universal context shape.
- Minimize transferred context according to the target role and risk. Do not automatically expose secrets, unrelated tenant data, hidden instructions, privileged tool outputs, or complete prior context merely because an agent becomes active.
- Preserve provenance/authority labels across transfer. User/system requirements, retrieved evidence, prior-agent claims, tool results, generated hypotheses, accepted decisions, and unresolved uncertainty should not collapse into one indistinguishable conversation history.
- Preserve authorization independently of ownership. Becoming the active agent does not grant new filesystem/network/tool/account/data/side-effect permissions beyond the policy attached to the transferred scope.
- Treat target capability metadata as claims that must be resolved from a trusted registry/configuration. A source agent must not create arbitrary privileged handoff targets or infer permissions merely by generating an agent name.
- Validate the target and allowed handoff edge outside unconstrained model output where practical. Model selection can propose a transition, while deterministic policy/registry checks enforce which source->target transitions and scopes are permitted.
- Define rejection/unavailable behavior. If the target is missing, incompatible, unauthorized, overloaded, or unable to accept the task, the workflow needs an explicit fallback: keep current ownership, choose another allowed target, request clarification, escalate, or fail rather than silently dropping responsibility.
- Define return/re-handoff semantics. A handoff can be terminal, reversible, or permit further transfers; prevent ping-pong loops with hop/turn/time/cost limits, repeated-state detection, and escalation.
- Preserve user-facing continuity where relevant. The system should make ownership transitions comprehensible enough to avoid contradictory commitments, duplicated questions/actions, or hidden changes in permissions/scope, without requiring disclosure of internal implementation details that are unsafe or irrelevant.
- Keep side-effect ownership explicit during transition. Do not leave concurrent agents believing they both own the same transaction/resource unless the system intentionally supports shared authority with a conflict/locking protocol.
- Handle in-flight work explicitly. A transfer should define whether previous-agent tool calls/jobs are cancelled, awaited, detached, or transferred and who owns their eventual results/errors.
- Treat handoff messages/state as untrusted input according to source and threat model. An agent cannot escalate privilege, change policy, or overwrite higher-priority instructions by embedding such requests in transferred context.
- Record consequential handoffs with enough traceability to reconstruct source, target, reason/policy, state/version, transferred scope, approvals, and terminal outcome while respecting privacy/minimization constraints.
- Evaluate handoffs by more than successful tool/transition execution. Useful measures include correct target selection, context sufficiency/leakage, ownership ambiguity, repeated/looping transfers, unauthorized transitions, downstream task success, user continuity, latency/cost, and accepted-result quality.
- Keep concrete handoff tool schemas, target registries, prompt descriptions, platform APIs, transfer filters, speaker/UI behavior, traces, thresholds, and project-specific handoff graphs with their applicable catalog/evidence/project owners.
- Use the canonical entity references as research inputs for the ownership-transfer boundary while keeping framework-specific mechanisms and current API behavior outside concept ownership.

## Validation

- The receiving participant becomes the active owner for the declared transferred scope; otherwise the interaction is delegation, consultation, routing, or messaging rather than a handoff.
- Handoffs are not conflated with manager-worker delegation, routing decisions, sequential stages, or swarm topology.
- Context transfer and authorization transfer are treated separately; ownership does not grant undeclared permissions.
- Allowed targets/edges and consequential actions are not created from unconstrained model text alone.
- In-flight work, failed/unavailable targets, return/re-handoff, and loop/termination behavior are explicit where material.
- Concrete framework APIs, registries, prompts, traces, and project handoff graphs remain outside the reusable concept owner.
