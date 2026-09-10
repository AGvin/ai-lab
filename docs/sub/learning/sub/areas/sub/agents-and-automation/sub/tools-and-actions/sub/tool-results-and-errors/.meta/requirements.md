# Documentation Requirements

## Requirements

- Teach tool results/errors as explicit host-constructed outcome contracts that let an agent distinguish what actually happened from what it requested or expected.
- Separate request acceptance, execution start, successful completion, partial completion, deterministic validation failure, authorization/policy failure, transient infrastructure/provider failure, semantic/domain failure, cancellation/timeout, and ambiguous external state where the distinction affects recovery or subsequent decisions.
- Return compact structured outcomes with stable tool/operation identity, result payload or artifact reference, authoritative external identifiers, relevant validation/status fields, error category/details appropriate for the caller, retry/reconciliation guidance when known, and provenance/version information where material.
- Do not treat transport/HTTP/process success alone as domain success. A request can return successfully while the intended business effect is rejected, incomplete, stale, or semantically invalid.
- Do not treat timeout/network failure as evidence that an external effect did not occur. Mark ambiguous outcomes explicitly and reconcile authoritative external state before a retry that could duplicate a consequential action.
- Distinguish user/model-correctable errors from non-correctable/retryable/system-policy failures so an agent does not repeatedly reformulate arguments when the root cause is quota, permission, provider outage, stale ownership, or a blocked policy decision.
- Preserve deterministic validation/business-rule errors as structured evidence rather than inviting the model to infer failure from logs. Return enough detail to correct the bounded request without exposing unnecessary secrets/internal implementation data.
- Treat tool output as untrusted external/context input when it can contain retrieved/user/remote content. Validate schemas and data boundaries, preserve provenance, and do not allow embedded output instructions to redefine agent/system/tool permissions or control policy.
- Use stable artifact references for large outputs and return metadata/checksums/version/source identity needed for later verification rather than copying arbitrarily large blobs into model context.
- Bound error payload size and redact secrets/credentials/sensitive internals while preserving actionable failure class/evidence. Human-oriented logs and model-oriented structured results can be separate surfaces.
- Define result compatibility/versioning when downstream workflows persist or replay tool outcomes across tool schema/implementation changes.
- Keep retry/idempotency/backoff/failure-recovery mechanisms with Operations/Engineering owners; this node teaches the result/error information an agent needs to invoke those controls correctly.
- Evaluate ambiguous-outcome frequency, incorrect retry after successful effect, error classification/correction success, partial-result handling, result provenance/validation failures, context bloat, sensitive-data leakage, and downstream accepted-result quality.
- Keep provider-specific status codes/message shapes and concrete product errors source-backed; map them into stable workflow outcome categories without claiming one provider contract is universal.

## Validation

- Tool result state is derived from host/external evidence rather than model expectation or request acceptance alone.
- Ambiguous side effects remain explicitly ambiguous until reconciled.
- Error classes guide correction/retry/escalation without exposing unnecessary secrets.
- Large/untrusted results preserve references/provenance and cannot redefine control policy through embedded content.
- Generic retry/recovery algorithms are linked rather than redefined here.
