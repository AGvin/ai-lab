# Documentation Requirements

## Requirements

- Teach group chat as a coordination choice for multi-agent work that genuinely benefits from an evolving shared conversation in which participants react to one another across turns under an explicit speaker/turn policy.
- Start from the canonical Group Chat concept for reusable shared-conversation, speaker-selection, authority, disagreement, termination, side-effect, and context-growth semantics. Use this learning node for practical selection, configuration, operational consequences, examples, and evaluation.
- Teach pattern fit with examples where visible iterative exchange is useful: a writer/critic/domain-expert/editor refining one artifact; roles negotiating responsibility or resolving ambiguity; review/debugging where contributions should remain inspectable; or tasks where the next useful participant cannot always be predetermined.
- Prefer manager-worker when specialists can work privately and return bounded results to one retained owner without needing the evolving group transcript.
- Prefer routing or parallel/advisory execution when specialists should remain independent, a single dispatch decision is sufficient, or independent reviews are more valuable than conversational influence.
- Prefer handoffs when active ownership should transfer to one participant instead of maintaining a shared multi-participant conversational space.
- Prefer blackboard coordination when participants mainly need to inspect/update a structured shared problem state rather than converse through ordered turns.
- Prefer a deterministic workflow or one agent when shared deliberation adds no material value and only increases latency, cost, or context exposure.
- Teach explicit participant membership and role boundaries: who may join/leave, what expertise/capabilities each participant claims, what context each receives, and what tools/permissions/data scopes each role is allowed to use.
- Explain that a shared conversation need not mean identical full history for every participant. Full history, bounded windows, summaries, selected messages, or role-specific views are design choices that must preserve enough provenance and constraints for safe collaboration.
- Apply context minimization. Do not broadcast secrets, unrelated tenant/private data, privileged tool results, or unnecessary context merely because all participants can contribute to the same conversation.
- Teach speaker selection as an explicit policy choice: round-robin, deterministic rules, a selector/manager, model-based selection, self-selection, priority, or another bounded mechanism. Selection must stay within an allowed participant registry and must not mint new privileges.
- Address starvation and order effects. When coverage/diversity matters, define participation constraints and evaluate sensitivity to early messages, repeated claims, selector bias, and anchoring rather than assuming conversation naturally produces independent perspectives.
- Teach disagreement handling: request evidence, run deterministic verification, invoke an evaluator/reviewer, escalate to a decision owner, retain competing hypotheses, or terminate with `unknown` instead of manufacturing consensus.
- Treat consensus or repeated agreement as a decision signal rather than proof of correctness. Shared models, prompts, sources, and conversation history can produce correlated error.
- Keep tool/side-effect authority separate from conversational participation. Being selected to speak does not authorize external writes; when multiple participants can act, define resource ownership, idempotency, approvals, locking/reservation, and conflict resolution outside conversational agreement.
- Bound conversation growth with turn/time/cost limits, termination conditions, structured checkpoints/summaries, and provenance/loss checks where needed. Conversational activity alone is not progress.
- Teach human roles explicitly when present: participant, selector, reviewer, approver, arbitrator, or termination authority rather than a single undifferentiated human-in-the-loop label.
- Compare group chat against simpler manager-worker, routing, advisory/parallel, blackboard, or deterministic alternatives and justify the shared conversation by accepted-result value rather than framework convenience.
- Evaluate task success, useful unique contributions, redundancy, disagreement quality, speaker-selection failures/starvation, context leakage, unsupported consensus, loops/termination, side-effect conflicts, latency/cost, and accepted-result quality.
- Use the exact AutoGen Group Chat and Teams references preserved in entity metadata as historical/framework evidence only. Mutable framework APIs and behavior remain source-backed; stable group-chat semantics remain concept-owned.

## Validation

- The pattern requires an evolving shared conversation and explicit turn/speaker policy; independent parallel answers are not mislabeled as group chat.
- Group chat is distinguished from retained-manager delegation, routing, handoffs, blackboard coordination, and advisory/parallel review.
- Shared context never implies shared permissions, trusted claims, or factual consensus.
- Speaker selection, disagreement, termination, context growth, and side-effect ownership are explicit where material.
- Pattern selection compares against simpler alternatives and evaluates accepted-result value.
- Framework references remain evidence rather than timeless API contracts.
