# Documentation Requirements

## Requirements

- Use the reader-facing title `Coordination and Communication`.
- Define coordination as the policies/mechanisms by which multiple agents or agent-like participants align responsibilities, task ownership, turn-taking, shared problem state, dependencies, conflicts, and progress; define communication as the transfer or sharing of messages, context, state, claims, evidence, requests, or other information used by that coordination.
- Keep the domain distinct from `workflows-and-orchestration/`. Workflows own explicit execution paths, stages, transitions, routing, loops, and manager-controlled delegation; coordination owns how participants exchange ownership/information or collaborate through shared state while those workflows execute.
- Keep the domain distinct from `multiagent-systems/`. MAS owns system-level identity/topology for systems containing multiple interacting agents; coordination-and-communication owns reusable mechanisms those systems can use.
- Keep the domain distinct from `state-and-memory/`. State/memory owns representations and persistence; coordination owns how shared/private state is exposed, synchronized, updated, interpreted, and used to coordinate participants.
- Keep the domain distinct from `integration-and-interoperability/`. Formal protocols/transports can carry agent communication, but the coordination concept concerns semantic ownership/turn/state relationships rather than wire methods, schemas, transports, or vendor APIs.
- Keep `handoffs/`, `group-chat/`, and `blackboard/` as the currently selected child mechanisms whose durable semantics justify independent concept nodes.
- Define `handoffs/` by active-ownership transfer: one agent/configuration delegates or transfers the current task/conversation/control state so another participant becomes the active owner for the transferred scope.
- Define `group-chat/` by a shared iterative conversation: multiple agents receive the shared/broadcast conversation state and a speaker/turn-selection policy decides who contributes next until a declared terminal condition.
- Define `blackboard/` by shared structured problem state: multiple independent knowledge sources/agents inspect and contribute to a common blackboard/problem representation while a control/scheduling mechanism determines which contributions occur when.
- Treat communication topology as multidimensional rather than one hierarchy: centralized brokered exchange, peer-to-peer, broadcast, shared-state, environment-mediated, synchronous, asynchronous, directed, and many-to-many forms can all be valid depending on the mechanism.
- Separate task ownership from message visibility. An agent can see a message without owning the task, and an agent can own a task while receiving only a scoped context summary rather than all prior messages.
- Separate communication from authorization. Receiving a message, handoff, shared-state reference, or peer request does not automatically grant tool, data, credential, network, account, or side-effect authority.
- Treat participant identities/capabilities as declared claims whose trust depends on the registry/protocol/system. A role/name alone does not prove expertise, current availability, jurisdictional suitability, or permissions.
- Preserve context/data minimization. Share only the context/state/evidence required for the receiving participant's role where practical; avoid broadcasting secrets, unrelated tenant data, hidden system instructions, or unrestricted tool results merely for coordination convenience.
- Preserve provenance and authority distinctions across communication. Mark user/system requirements, retrieved evidence, participant claims, generated hypotheses, tool outputs, accepted decisions, and unresolved uncertainty distinctly enough that repeated forwarding does not make derived text authoritative.
- Treat received content as untrusted input according to source and threat model. Participant messages/shared-state entries can contain prompt injection, malformed data, stale assumptions, or adversarial claims and must not override higher-priority policy merely because they arrived through an internal agent channel.
- Define handoff/message/state schemas where consequences require it. Useful fields can include task/subtask ID, sender/receiver, objective, accepted inputs, evidence/artifacts, state/version, permissions, deadlines/budgets, unresolved blockers, requested next action, completion/return contract, and provenance references.
- Define conflict resolution explicitly. Multiple agents can write contradictory claims or compete for the same resource; systems need an owner/policy for reconciliation, versioning/locking, merge, arbitration, escalation, or preserving unresolved disagreement.
- Define termination/cycle behavior. Peer handoffs, group conversation, or repeated shared-state contributions can loop indefinitely; coordination needs hop/turn/iteration/time/cost limits, repeated-state detection, escalation, and terminal outcomes appropriate to the pattern.
- Define communication failure separately from task failure. Delivery, parsing, authorization, stale-version, duplicate, out-of-order, participant-unavailable, and semantic-misunderstanding failures can occur even when individual agents are functioning correctly.
- Explain synchronous/asynchronous trade-offs without prescribing one style. Synchronous coordination can simplify immediate consistency while increasing blocking; asynchronous coordination can improve concurrency/resilience while adding ordering, staleness, duplication, and reconciliation complexity.
- Keep consensus/voting/advisory review distinct from verification. Multiple agreeing agents do not prove correctness unless independence, aggregation, evidence, and evaluation are explicitly validated; advisory/review-board patterns can compose coordination with evaluation/decision ownership without becoming a selected coordination child by default.
- Keep swarm/decentralized topologies distinct from the handoff mechanism. Swarm behavior can be built from peer handoffs and local policies, but topology/organization remains `multiagent-systems/` or project/learning design rather than a separate handoff synonym.
- Keep concrete agent IDs, message schemas, protocol methods, broker/topic names, handoff tool definitions, speaker selectors, shared-state stores, framework APIs, traces, run results, and project-specific coordination policies with their applicable catalog/evidence/project owners.
- Render direct-child navigation from the validated materialized selected child set when reader-facing rendering is activated.
- Use the canonical entity references as research inputs for modern handoff/group-chat distinctions while preserving blackboard's established AI architecture lineage and keeping concrete implementations outside concept ownership.

## Validation

- Coordination/communication is not collapsed into workflow control flow, MAS identity, shared memory, or transport/protocol interoperability.
- Handoffs, group chat, and blackboard remain distinguishable by ownership, conversational-turn, and shared-problem-state invariants.
- Communication does not itself grant authorization or turn participant claims into authoritative truth.
- Shared/broadcast context is minimized and provenance/authority distinctions survive forwarding.
- Conflict, cycle/termination, and communication-failure semantics are explicit where material.
- Agreement among agents is not treated as verification by itself.
- Concrete protocols, framework APIs, schemas, registries, stores, traces, and project policies remain outside the reusable concept owner.
- Direct-child navigation contains only currently materialized selected descendants.
