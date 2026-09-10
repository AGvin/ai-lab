# Documentation Requirements

## Requirements

- Teach agent state as the explicit authoritative execution/task/workflow data needed to decide what is currently true, what work is complete/pending/blocked, what artifacts/evidence exist, and how execution can continue or recover independently from conversational prose.
- Use the canonical State and Memory concept for reusable state-versus-memory/context semantics. This learning node focuses on practical schema, transition, artifact, concurrency, and recovery design for agent systems.
- Distinguish state from model-visible working context, conversation history, and long-term memory. Only the projection needed for a model decision must enter context; the complete authoritative state can remain in structured storage.
- For a non-trivial workflow, teach a state schema that can include execution/task identity, current stage/status, validated inputs/outputs, stable artifact/tool-result references, completed/pending/blocked actions, retry/error/escalation state, approvals/rejections, ownership/lease/version fields, and model/prompt/tool/schema/configuration versions when they affect continuation or auditability.
- Treat these fields as implementation examples rather than one universal schema. Add only state required by the workflow's correctness, recovery, auditability, concurrency, privacy, or operational needs.
- Prefer typed, schema-validated, or otherwise deterministic transitions over free-form model prose as the workflow ledger. Model output can propose a transition; application/control logic decides whether the transition is valid and commits authoritative state.
- Define transition preconditions, allowed from/to states, required evidence/artifacts, side-effect ownership, acceptance/validation, and version/concurrency behavior where material. Reject or reconcile stale transitions rather than silently applying them to newer state.
- Keep large artifacts in their authoritative stores when practical and place stable identities/URIs/checksums/version references in state. Do not repeatedly copy large source/output blobs into workflow state or model context when a stable reference preserves identity more safely and efficiently.
- Preserve enough provenance to reproduce/interpret important state: source artifact/version, producer/tool/model/prompt/configuration versions, validation status, timestamps where useful, and the authoritative external identifiers related to side effects.
- Separate intended/planned state from observed external state. A worker or model must not mark a consequential action complete merely because it proposed/sent the request, expected success, or lost the acknowledgement.
- Reconcile ambiguous external effects against authoritative external systems before committing success/failure states or retrying consequential operations. Persist the reconciliation result and operation identity where later recovery depends on it.
- Teach persistence as necessary but not sufficient for recovery. A durable state snapshot can still be unusable if schema versions are incompatible, referenced artifacts are missing, credentials/permissions expired, external side effects diverged, or the workflow cannot determine which step is safe to resume.
- Teach schema/version evolution for durable state: identify state/schema versions, define compatibility/migration or fail-safe behavior, and do not silently resume old state under code/prompt/tool semantics that invalidate its assumptions.
- When several workers/controllers can update related state, define ownership, optimistic/version checks, locking/reservation, fencing, merge/conflict policy, idempotency/reconciliation, or another explicit concurrency contract appropriate to the system. Conversational coordination is not a concurrency-control mechanism.
- Apply privacy/data-minimization/retention rules to persisted state and referenced artifacts. Do not persist secrets, personal/sensitive data, or full model/tool payloads merely because they were present in working context; preserve only what the workflow requires under the applicable policy.
- Define cleanup/retention for terminal/cancelled/expired workflows and generated artifacts, including what audit/provenance state remains, what is deleted, and how deletion propagates to external stores where required.
- Evaluate invalid/stale transition rate, state-conflict incidents, ambiguous-effect reconciliation, recovery/resume success, missing/broken artifact references, schema-migration failures, duplicate side effects, state/context size, retention/privacy incidents, and time/cost to restore accepted execution.
- Keep generic database transactions, distributed consistency algorithms, privacy law/policy, and concrete storage product behavior with their Engineering/Trustworthy AI/Catalog/Project owners; link those mechanisms when agent-state implementation needs deeper detail.

## Validation

- Authoritative agent state is not equated with conversation history, working context, or model memory.
- Model/tool output can propose but cannot directly authoritatively commit invalid state transitions.
- Consequential completion follows verified/reconciled external effects rather than expected or unacknowledged requests.
- Persisted state has explicit schema/version, artifact, privacy, concurrency, and recovery boundaries where material.
- Large artifacts use stable references when appropriate instead of becoming duplicated state/context blobs.
- Generic storage/consistency/privacy mechanisms remain linked rather than redefined as agent-only truth.
