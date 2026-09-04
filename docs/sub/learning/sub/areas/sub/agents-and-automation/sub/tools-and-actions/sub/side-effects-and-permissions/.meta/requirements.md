# Documentation Requirements

## Requirements

- Teach side effects and permissions as the control boundary for tool actions that create, modify, send, purchase, deploy, delete, publish, provision, move money/data, change access, or otherwise alter authoritative external state.
- Distinguish read-only/analysis capabilities from reversible writes, costly/long-lived effects, security/privacy-sensitive actions, and irreversible/high-consequence operations so authorization/approval/recovery requirements can scale with consequence.
- Apply least privilege independently from model prompts: expose only tools/data/environments/actions the current user/workflow is eligible to use and enforce target/resource/tenant/environment/amount/scope/time constraints at execution time.
- A model-selected tool or schema-valid arguments do not grant authorization. Authenticate the acting identity, authorize the specific operation/target, validate current authoritative state/business rules, and enforce required approvals before execution.
- Do not place reusable credentials/secrets in model-visible context when the host can retain them behind a bounded tool interface. Tool identity and execution authority remain host-controlled.
- For consequential operations, use stable operation/idempotency identities and define what can be retried safely. A network timeout or lost acknowledgement can leave an ambiguous effect; reconcile authoritative external state before repeating the write.
- Separate proposed/requested, authorized, submitted, externally confirmed, partially completed, failed, cancelled, and ambiguous states when those distinctions affect safety/recovery. The model must not mark an effect complete based on intent or request acceptance alone.
- Use human approval gates when policy requires accountable authorization for a specific reviewed consequential action/state; use deterministic policy directly when a human adds no necessary authority or information.
- Revalidate material state immediately before effect execution when approvals/plans can become stale. Changes in target, artifact/version, permissions, amount, deadline, resource state, or business constraints can invalidate prior authorization.
- Treat untrusted tool inputs/content as data, not instructions that can expand permissions or change system policy. Validate retrieved/user/generated paths, URLs, commands, queries, recipients, identifiers, and payloads according to the capability boundary.
- Define rollback/compensation only when actually supported. Do not label destructive/financial/publication/security actions reversible merely because a conceptual opposite action exists.
- Record auditable evidence for material effects: operation identity, acting/requesting identity, target/scope, validated arguments/artifact version, authorization/approval, external identifiers/status, timestamps as appropriate, actual effect, residual risk, and rollback/compensation result when used.
- Bound side effects in parallel/multi-agent systems with ownership/reservation/locking/fencing/conflict rules so several agents do not mutate the same resource merely because each request is locally valid.
- Keep generic authentication/authorization, sandboxing, secrets, idempotency/retries, recovery, and governance concepts with their canonical security/engineering owners; this node teaches how those controls apply around agent tool actions.
- Evaluate unauthorized/blocked attempts, stale-approval/state invalidations, duplicate/ambiguous effects, successful reconciliation, rollback/compensation outcomes, cross-agent conflicts, credential/data exposure, approval burden, and safely completed consequential operations.
- Keep concrete credentials/scopes/provider permissions, business approval policies, and environment-specific runbooks source-backed with catalog/project owners.

## Validation

- Model tool selection and schema conformance never constitute authorization.
- Consequential effects use least privilege, current-state validation, and explicit approval where policy requires it.
- Ambiguous external writes are reconciled before retry.
- Credentials remain behind bounded host interfaces where possible.
- Reversibility/compensation claims reflect actual operational capability.
- Parallel agents cannot mutate shared authoritative state without declared ownership/conflict controls.
