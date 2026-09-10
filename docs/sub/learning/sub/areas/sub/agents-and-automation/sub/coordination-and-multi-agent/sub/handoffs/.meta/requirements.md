# Documentation Requirements

## Requirements

- Teach handoffs as a practical coordination choice for workflows where the receiving participant should genuinely become the active owner of a conversation, task phase, or declared sub-scope rather than merely return a bounded result to a retained manager.
- Start from the canonical Handoffs concept for reusable ownership-transfer semantics. Use this learning node to teach selection, topology, context/authority implications, implementation consequences, failure handling, and evaluation without redefining the stable concept contract.
- Teach pattern fit with examples such as service triage, multilingual or jurisdiction-specific workflows, incident escalation between operational roles, and specialist-user interaction where active tools/permissions/context differ by role.
- Prefer manager-worker delegation when specialists should return bounded subresults while one controller retains global dependencies, budget/resource ownership, conversation state, approval boundaries, and terminal responsibility.
- Prefer routing without handoff when the system only needs to classify/dispatch into a bounded handler or workflow and no participant-level ownership transfer is required.
- Prefer a single agent or deterministic workflow when changing active ownership does not materially improve specialization, context isolation, policy separation, user interaction, or operational control.
- Teach swarm-like coordination as a topology that may be built from local handoff rules rather than as a synonym for handoff. A decentralized swarm can reduce reliance on one central orchestrator but increases the need for explicit allowed transitions, ownership fencing, context minimization, termination, loop detection, and global policy enforcement.
- Explain that local handoff autonomy does not eliminate global authorization, safety policy, budget, resource, or terminal-state constraints. Every locally valid transition still operates inside system-level boundaries.
- Make allowed handoff edges inspectable and constrain them through trusted configuration/policy rather than letting model-generated target names implicitly create privileged transitions.
- Teach context transfer as a deliberate design choice: pass enough authoritative state, evidence, user/system constraints, artifacts, unresolved issues, and continuity information for the target to act safely while minimizing unrelated sensitive or privileged context.
- Keep ownership transfer separate from permission transfer. The receiving agent becomes active for the declared scope but receives only the tools/data/side-effect authority explicitly allowed for that role and transition.
- Define what happens to in-flight work when ownership changes: cancel, await, detach, or transfer responsibility explicitly, and assign ownership for eventual results, costs, side effects, and errors.
- Teach unavailable/rejected-target behavior explicitly: retain current ownership, select another allowed target, clarify, escalate, or fail rather than dropping responsibility silently.
- Teach return and re-handoff paths as deliberate policy. Use hop/turn/time/cost bounds, repeated-state detection, terminal conditions, or escalation to prevent ping-pong/looping transfers.
- For swarm-like topologies, teach stale-owner fencing and duplicate-side-effect prevention so two participants do not continue acting as authoritative owners of the same consequential scope after a transfer.
- Preserve user-facing continuity where relevant: ownership changes should not produce contradictory commitments, duplicated questions/actions, hidden scope/permission changes, or unexplained loss of prior accepted constraints.
- Evaluate handoff systems using correct target/transition choice, context sufficiency and leakage, ownership ambiguity, unauthorized edges, repeated/looping transfers, stale-owner/duplicate-action incidents, downstream task success, user continuity, latency/cost, and accepted-result quality.
- Compare a handoff/swarm design against a simpler manager-worker, routing, or deterministic workflow baseline. Use the more decentralized form only when ownership transfer or topology produces enough value to justify additional state, policy, context-transfer, termination, and recovery complexity.
- Use the exact AutoGen Swarm, handoff, and termination references preserved in entity metadata as implementation/evidence examples only. Mutable framework APIs and behavior remain source-backed; stable semantics remain concept-owned.

## Validation

- The receiving participant becomes the active owner for the declared scope; bounded consultation/delegation is not mislabeled as handoff.
- Swarm is taught as a topology built from handoff rules, not as a synonym for handoff.
- Context and authorization are minimized independently; ownership transfer never implies unrestricted permission transfer.
- Unavailable targets, in-flight work, re-handoffs, loops, stale owners, and terminal conditions are explicit where material.
- Pattern selection compares against simpler retained-owner and deterministic alternatives.
- Framework examples remain evidence, not canonical timeless API behavior.
