# Documentation Requirements

## Requirements

- Use the reader-facing title `Group Chat`.
- Define group chat as a multi-agent coordination pattern in which multiple agents participate in a shared iterative conversation, each relevant turn is made available to the group according to the implementation's synchronization policy, and an explicit speaker/turn-selection mechanism determines who contributes next until a declared termination condition.
- Keep shared conversational context plus turn/speaker policy as the defining invariant. Several agents independently answering the same prompt and later aggregating results is parallel/advisory execution, not group chat unless the participants actually collaborate through the evolving shared conversation.
- Distinguish group chat from `handoffs/`. A handoff transfers active ownership to one participant; group chat keeps a multi-participant conversational space in which several agents can contribute across turns under a selection policy.
- Distinguish group chat from `manager-worker-orchestration/`. A manager can call specialists privately and synthesize returned results without exposing a shared conversation to all specialists; group chat exposes the evolving group exchange according to its synchronization rules.
- Distinguish group chat from `blackboard/`. Group chat coordinates through conversational turns/messages; blackboard coordination centers on a shared structured problem representation that participants inspect/update independently and need not be conversational.
- Distinguish group chat from generic chat UI. The concept concerns agent-to-agent collaboration semantics and turn/context policy, not a visual chat window, channel product, or human messaging service.
- Define participant membership where material: stable agent/role identity, declared expertise/capabilities, allowed tools/permissions/data scope, join/leave behavior, and whether membership is static or dynamic.
- Define the shared-conversation state explicitly. Preserve message identity/order, sender, content type, provenance/evidence references, task/round metadata, and any system-level control messages needed for deterministic orchestration rather than relying on an ambiguous concatenated transcript.
- Define context synchronization. Participants can receive complete history, a bounded window, summaries, selected messages, or role-specific views; the system must state what is shared and avoid implying all agents literally share one memory/session object when the implementation synchronizes separate sessions.
- Preserve authority/provenance distinctions in shared history. Repetition or broadcast does not turn one agent's claim into verified fact or higher-priority instruction.
- Apply context/data minimization. Do not broadcast secrets, tenant-private records, internal chain-of-thought, privileged tool outputs, or irrelevant sensitive context to all participants solely because they share a group conversation.
- Treat every participant message as untrusted input according to source and threat model. Messages can contain prompt injection, malformed data, incorrect claims, or attempts to alter permissions/speaker policy; group membership does not make content trusted.
- Define speaker selection as a first-class policy. Common mechanisms can include round-robin, deterministic rules, manager/selector decisions, model-based selection, self-selection, priority queues, or custom policies; no one mechanism is required by the concept.
- Keep speaker selection bounded to an allowed participant registry and policy. A model-based selector must not create arbitrary privileged speakers, expand permissions, or bypass required human/system gates by generating a name.
- Define fairness/starvation behavior where relevant. A selector can repeatedly choose the same persuasive/high-probability participant and suppress other views; systems requiring coverage/diversity should make participation constraints explicit rather than assume group chat naturally produces diversity.
- Define termination explicitly: maximum turns/rounds, objective/acceptance state, consensus threshold if used, evaluator/manager decision, human decision, timeout/cost limit, no-progress/repeated-state detection, or other terminal outcomes.
- Treat consensus/agreement as a decision rule, not proof of correctness. Agents sharing models, prompts, sources, or conversation history can have correlated errors and social/anchoring effects; preserve dissent and evidence where decision quality depends on them.
- Define contradiction and unresolved-disagreement handling. The group can request evidence, invoke verification/evaluation, escalate to a decision owner, retain multiple hypotheses, or stop with `unknown`; it should not erase dissent merely to create a clean transcript.
- Explain conversational-order effects. Early messages can anchor later participants, repeated claims can gain salience without gaining evidence, and speaker policy can shape outcomes; evaluate order/selector sensitivity when material.
- Define tool/side-effect ownership separately from conversational participation. Being selected to speak does not automatically authorize an agent to execute writes, transactions, deployments, communications, or other consequential actions.
- Prevent duplicate/conflicting side effects. If several participants can act, define resource ownership, idempotency, locking/reservation, approvals, and conflict resolution outside conversational agreement alone.
- Bound context growth. Long group conversations can exhaust context, increase latency/cost, and amplify stale or malicious text; use structured summaries/checkpoints/compaction with provenance and loss checks where needed.
- Define human participation explicitly when present. Humans can be ordinary conversational participants, selectors, approvers, arbitrators, or termination authorities; these roles should not be collapsed into one generic `human in the loop` label.
- Treat advisory-council/review-board patterns as compositions rather than separate group-chat synonyms. They may use group chat for deliberation while adding evaluation criteria, aggregation/decision authority, independent reviews, or human governance owned elsewhere.
- Evaluate group chat as a system: task success, unique/useful contributions, redundancy, disagreement handling, speaker-selection failures, starvation, context leakage, unsupported consensus, loop/termination behavior, latency/cost, side-effect errors, and accepted-result quality.
- Keep concrete speaker selectors, participant registries, framework session/message classes, prompts, conversation traces, summaries, thresholds, evaluation runs, and project-specific group rules with their applicable catalog/evidence/project owners.
- Use the canonical entity references as research inputs for shared-conversation synchronization and speaker-selection boundaries while keeping Microsoft/framework-specific implementation APIs outside concept ownership.

## Validation

- Group chat requires an evolving shared/broadcast conversation plus an explicit speaker/turn policy; independent parallel answers are not mislabeled as group chat.
- Group chat is distinguished from ownership-transferring handoffs, manager-private specialist calls, and structured blackboard coordination.
- Shared conversation does not imply shared permissions, trusted content, independent evidence, or factual consensus.
- Speaker selection and termination are bounded and auditable where material.
- Context growth, order/anchoring effects, disagreement, and side-effect conflicts are addressed rather than hidden by the conversational interface.
- Concrete framework APIs, selectors, participant registries, prompts, traces, and run results remain outside the reusable concept owner.
